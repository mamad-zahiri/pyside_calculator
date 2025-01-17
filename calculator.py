from PyQt5 import QtCore, QtGui, QtWidgets
import numpy as np


class custom_QTextEdit(QtWidgets.QTextEdit):
    clicked = QtCore.pyqtSignal()

    def mouseReleaseEvent(self, event):
        self.clicked.emit()


class Ui_Calculator(object):
    def setupUi(self, Calculator: QtWidgets.QWidget):
        Calculator.setObjectName("Calculator")
        Calculator.setWindowTitle("Calculator")
        Calculator.resize(311, 378)
        Calculator.setStyleSheet("background: white;")

        # stores last number and operator
        self.curr_number = ''
        self.last_number = ''
        self.last_operator = ''

        self.output = QtWidgets.QLabel(Calculator, text="0")
        self.output.setGeometry(QtCore.QRect(11, 11, 290, 44))
        font = QtGui.QFont()
        font.setFamily("Noto Sans")
        font.setPointSize(14)
        font.setBold(False)
        font.setWeight(50)
        self.output.setFont(font)
        self.output.setStyleSheet("border: 1px solid #eee;\n"
                                  "border-radius: 5px;\n"
                                  "background: #fefefe;\n"
                                  "")
        self.output.setFrameShadow(QtWidgets.QFrame.Raised)
        self.output.setAlignment(
            QtCore.Qt.AlignRight | QtCore.Qt.AlignTrailing | QtCore.Qt.AlignVCenter)
        self.output.setObjectName("output")

        font = QtGui.QFont()
        font.setFamily("Ubuntu")

        change_mode_stylesheet = """ ::indicator { image: none; width: 0px; height: 0px; } ::unchecked { color: gray; } ::checked { color: #454545; } """

        self.change_mode_buttonGroup = QtWidgets.QButtonGroup(Calculator)
        self.change_mode_buttonGroup.setObjectName("change_mode_buttonGroup")
        self.change_mode_buttonGroup.buttonClicked.connect(
            self._change_mode)

        self.programing_mode = QtWidgets.QRadioButton(
            Calculator, text="Programing")
        self.programing_mode.setGeometry(QtCore.QRect(20, 63, 81, 22))
        self.programing_mode.setFont(font)
        self.programing_mode.setStyleSheet(change_mode_stylesheet)
        self.programing_mode.setChecked(False)
        self.programing_mode.setObjectName("programing_mode")
        self.change_mode_buttonGroup.addButton(self.programing_mode)

        self.simple_mode = QtWidgets.QRadioButton(Calculator, text="Simple")
        self.simple_mode.setGeometry(QtCore.QRect(100, 63, 51, 22))
        self.simple_mode.setFont(font)
        self.simple_mode.setStyleSheet(change_mode_stylesheet)
        self.simple_mode.setChecked(True)
        self.simple_mode.setObjectName("simple_mode")
        self.change_mode_buttonGroup.addButton(self.simple_mode)

        self.number_base_buttonGroup = QtWidgets.QButtonGroup(Calculator)
        self.number_base_buttonGroup.setObjectName("number_base_buttonGroup")
        self.number_base_buttonGroup.buttonClicked.connect(
            self._change_base)

        self.Binary = QtWidgets.QRadioButton(Calculator, text="Bin")
        self.Binary.setEnabled(True)
        self.Binary.setGeometry(QtCore.QRect(160, 63, 30, 25))
        self.Binary.setFont(font)
        self.Binary.setAutoFillBackground(False)
        self.Binary.setStyleSheet(change_mode_stylesheet)
        self.Binary.setCheckable(True)
        self.Binary.setChecked(False)
        self.Binary.setObjectName("Binary")
        self.number_base_buttonGroup.addButton(self.Binary)

        self.Octal = QtWidgets.QRadioButton(Calculator, text="Oct")
        self.Octal.setEnabled(True)
        self.Octal.setGeometry(QtCore.QRect(190, 63, 30, 25))
        self.Octal.setFont(font)
        self.Octal.setAutoFillBackground(False)
        self.Octal.setStyleSheet(change_mode_stylesheet)
        self.Octal.setCheckable(True)
        self.Octal.setChecked(False)
        self.Octal.setObjectName("Octal")
        self.number_base_buttonGroup.addButton(self.Octal)

        self.Decimal = QtWidgets.QRadioButton(Calculator, text="Dec")
        self.Decimal.setEnabled(True)
        self.Decimal.setGeometry(QtCore.QRect(220, 63, 30, 25))
        self.Decimal.setFont(font)
        self.Decimal.setAutoFillBackground(False)
        self.Decimal.setStyleSheet(change_mode_stylesheet)
        self.Decimal.setCheckable(True)
        self.Decimal.setChecked(True)
        self.Decimal.setObjectName("Decimal")
        self.number_base_buttonGroup.addButton(self.Decimal)

        self.current_number_base = 10

        self.Hexadecimal = QtWidgets.QRadioButton(Calculator, text="Hex")
        self.Hexadecimal.setEnabled(True)
        self.Hexadecimal.setGeometry(QtCore.QRect(260, 63, 30, 25))
        self.Hexadecimal.setFont(font)
        self.Hexadecimal.setAutoFillBackground(False)
        self.Hexadecimal.setStyleSheet(change_mode_stylesheet)
        self.Hexadecimal.setCheckable(True)
        self.Hexadecimal.setChecked(False)
        self.Hexadecimal.setObjectName("Hexadecimal")
        self.number_base_buttonGroup.addButton(self.Hexadecimal)

        self.btn_d = QtWidgets.QPushButton(
            Calculator,
            text="d",
            clicked=lambda: self._btn_digit('D'))
        self.btn_d.setGeometry(QtCore.QRect(160, 94, 41, 34))
        self.btn_d.setObjectName("btn_d")

        self.btn_e = QtWidgets.QPushButton(
            Calculator,
            text="e",
            clicked=lambda: self._btn_digit('E'))
        self.btn_e.setGeometry(QtCore.QRect(210, 94, 41, 34))
        self.btn_e.setObjectName("btn_e")

        self.btn_f = QtWidgets.QPushButton(
            Calculator,
            text="f",
            clicked=lambda: self._btn_digit('F'))
        self.btn_f.setGeometry(QtCore.QRect(260, 94, 41, 34))
        self.btn_f.setObjectName("btn_f")

        self.btn_a = QtWidgets.QPushButton(
            Calculator,
            text="a",
            clicked=lambda: self._btn_digit('A'))
        self.btn_a.setGeometry(QtCore.QRect(160, 134, 41, 34))
        self.btn_a.setObjectName("btn_a")

        self.btn_b = QtWidgets.QPushButton(
            Calculator,
            text="b",
            clicked=lambda: self._btn_digit('B'))
        self.btn_b.setGeometry(QtCore.QRect(210, 134, 41, 34))
        self.btn_b.setObjectName("btn_b")

        self.btn_c = QtWidgets.QPushButton(
            Calculator,
            text="c",
            clicked=lambda: self._btn_digit('C'))
        self.btn_c.setGeometry(QtCore.QRect(260, 134, 41, 34))
        self.btn_c.setObjectName("btn_c")

        self.btn_7 = QtWidgets.QPushButton(
            Calculator,
            text="7",
            clicked=lambda: self._btn_digit('7'))
        self.btn_7.setGeometry(QtCore.QRect(160, 174, 41, 34))
        self.btn_7.setObjectName("btn_7")

        self.btn_8 = QtWidgets.QPushButton(
            Calculator,
            text="8",
            clicked=lambda: self._btn_digit('8'))
        self.btn_8.setGeometry(QtCore.QRect(210, 174, 41, 34))
        self.btn_8.setObjectName("btn_8")

        self.btn_9 = QtWidgets.QPushButton(
            Calculator,
            text="9",
            clicked=lambda: self._btn_digit('9'))
        self.btn_9.setGeometry(QtCore.QRect(260, 174, 41, 34))
        self.btn_9.setObjectName("btn_9")

        self.btn_4 = QtWidgets.QPushButton(
            Calculator,
            text="4",
            clicked=lambda: self._btn_digit('4'))
        self.btn_4.setGeometry(QtCore.QRect(160, 214, 41, 34))
        self.btn_4.setObjectName("btn_4")

        self.btn_5 = QtWidgets.QPushButton(
            Calculator,
            text="5",
            clicked=lambda: self._btn_digit('5'))
        self.btn_5.setGeometry(QtCore.QRect(210, 214, 41, 34))
        self.btn_5.setObjectName("btn_5")

        self.btn_6 = QtWidgets.QPushButton(
            Calculator,
            text="6",
            clicked=lambda: self._btn_digit('6'))
        self.btn_6.setGeometry(QtCore.QRect(260, 214, 41, 34))
        self.btn_6.setObjectName("btn_6")

        self.btn_1 = QtWidgets.QPushButton(
            Calculator,
            text="1",
            clicked=lambda: self._btn_digit('1'))
        self.btn_1.setGeometry(QtCore.QRect(160, 254, 41, 34))
        self.btn_1.setObjectName("btn_1")

        self.btn_2 = QtWidgets.QPushButton(
            Calculator,
            text="2",
            clicked=lambda: self._btn_digit('2'))
        self.btn_2.setGeometry(QtCore.QRect(210, 254, 41, 34))
        self.btn_2.setObjectName("btn_2")

        self.btn_3 = QtWidgets.QPushButton(
            Calculator,
            text="3",
            clicked=lambda: self._btn_digit('3'))
        self.btn_3.setGeometry(QtCore.QRect(260, 254, 41, 34))
        self.btn_3.setObjectName("btn_3")

        self.btn_0 = QtWidgets.QPushButton(
            Calculator,
            text="0",
            clicked=lambda: self._btn_digit('0'))
        self.btn_0.setGeometry(QtCore.QRect(160, 294, 40, 34))
        self.btn_0.setObjectName("btn_0")

        self.btn_dot = QtWidgets.QPushButton(
            Calculator,
            text=".",
            clicked=lambda: self._btn_digit('.'))
        self.btn_dot.setGeometry(QtCore.QRect(210, 294, 41, 34))
        self.btn_dot.setObjectName("btn_dot")

        self.line = QtWidgets.QFrame(Calculator)
        self.line.setGeometry(QtCore.QRect(154, 65, 3, 19))
        self.line.setFrameShadow(QtWidgets.QFrame.Plain)
        self.line.setFrameShape(QtWidgets.QFrame.VLine)
        self.line.setObjectName("line")

        self.btn_clear = QtWidgets.QPushButton(
            Calculator,
            text="×",
            clicked=self._btn_clear)
        self.btn_clear.setGeometry(QtCore.QRect(20, 23, 20, 20))
        self.btn_clear.setStyleSheet("QPushButton {\n"
                                     "background-color: #ccc;\n"
                                     "border-radius: 10px;\n"
                                     "}\n"
                                     "::pressed {\n"
                                     "background-color: #eee;\n"
                                     "}")
        self.btn_clear.setObjectName("btn_clear")

        self.btn_remove_last = QtWidgets.QPushButton(
            Calculator,
            text="←",
            clicked=lambda: self._btn_remove_last())
        self.btn_remove_last.setGeometry(QtCore.QRect(260, 334, 41, 34))
        self.btn_remove_last.setObjectName("btn_remove_last")

        self.btn_and = QtWidgets.QPushButton(
            Calculator,
            text="&&",
            clicked=lambda: self._btn_operator('&'))
        self.btn_and.setGeometry(QtCore.QRect(10, 334, 41, 34))
        self.btn_and.setObjectName("btn_and")

        self.btn_or = QtWidgets.QPushButton(
            Calculator,
            text="|",
            clicked=lambda: self._btn_operator('|'))
        self.btn_or.setGeometry(QtCore.QRect(60, 334, 41, 34))
        self.btn_or.setObjectName("btn_or")

        self.btn_right_shift = QtWidgets.QPushButton(
            Calculator,
            text=">>",
            clicked=lambda: self._btn_operator('>>'))
        self.btn_right_shift.setGeometry(QtCore.QRect(160, 334, 41, 34))
        self.btn_right_shift.setObjectName("btn_right_shift")

        self.btn_xor = QtWidgets.QPushButton(
            Calculator,
            text="^",
            clicked=lambda: self._btn_operator('^'))
        self.btn_xor.setGeometry(QtCore.QRect(110, 334, 41, 34))
        self.btn_xor.setObjectName("btn_xor")

        self.btn_left_shift = QtWidgets.QPushButton(
            Calculator,
            text="<<",
            clicked=lambda: self._btn_operator('<<'))
        self.btn_left_shift.setGeometry(QtCore.QRect(210, 334, 41, 34))
        self.btn_left_shift.setObjectName("btn_left_shift")

        self.btn_tan = QtWidgets.QPushButton(
            Calculator,
            text="tan",
            clicked=lambda: self._btn_trigonometry('tan'))
        self.btn_tan.setGeometry(QtCore.QRect(110, 254, 41, 34))
        self.btn_tan.setObjectName("btn_tan")

        self.btn_cosh = QtWidgets.QPushButton(
            Calculator,
            text="cosh",
            clicked=lambda: self._btn_trigonometry('cosh'))
        self.btn_cosh.setGeometry(QtCore.QRect(60, 294, 41, 34))
        self.btn_cosh.setObjectName("btn_cosh")

        self.btn_factorial = QtWidgets.QPushButton(
            Calculator,
            text="x!",
            clicked=lambda: self._btn_factorial())
        self.btn_factorial.setGeometry(QtCore.QRect(110, 134, 41, 34))
        self.btn_factorial.setObjectName("btn_factorial")

        self.btn_minus = QtWidgets.QPushButton(
            Calculator,
            text="-",
            clicked=lambda: self._btn_operator('-'))
        self.btn_minus.setGeometry(QtCore.QRect(60, 94, 41, 34))
        self.btn_minus.setObjectName("btn_minus")

        self.btn_pi_number = QtWidgets.QPushButton(
            Calculator,
            text="π",
            clicked=lambda: self._btn_digit(f'{round(np.pi, 10)}'))
        self.btn_pi_number.setGeometry(QtCore.QRect(60, 174, 41, 34))
        self.btn_pi_number.setObjectName("btn_pi_number")

        self.btn_mod = QtWidgets.QPushButton(
            Calculator,
            text="mod",
            clicked=lambda: self._btn_operator('%'))
        self.btn_mod.setGeometry(QtCore.QRect(110, 214, 41, 34))
        self.btn_mod.setObjectName("btn_mod")

        self.btn_power = QtWidgets.QPushButton(
            Calculator,
            clicked=lambda: self._btn_operator('**'))
        self.btn_power.setGeometry(QtCore.QRect(10, 214, 42, 34))
        self.btn_power.setObjectName("btn_power")

        self.power_label = custom_QTextEdit(Calculator)
        self.power_label.setEnabled(True)
        self.power_label.setGeometry(QtCore.QRect(16, 218, 30, 26))
        font = QtGui.QFont()
        font.setFamily("Ubuntu")
        self.power_label.setFont(font)
        self.power_label.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.power_label.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.power_label.setTextInteractionFlags(QtCore.Qt.NoTextInteraction, )
        self.power_label.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        self.power_label.setObjectName("power_label")
        self.power_label.setCursor(QtCore.Qt.ArrowCursor)
        self.power_label.viewport().setCursor(QtCore.Qt.ArrowCursor)
        self.power_label.clicked.connect(lambda: self.btn_power.animateClick())
        self.power_label.setHtml(QtCore.QCoreApplication.translate("Calculator", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
                                                                   "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
                                                                   "p, li { white-space: pre-wrap; }\n"
                                                                   "</style></head><body style=\" font-family:\'Ubuntu\'; font-size:10pt; font-weight:400; font-style:normal;\">\n"
                                                                   "<p align=\"center\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Noto Sans\';\">x</span><span style=\" font-family:\'Noto Sans\'; vertical-align:super;\">n</span></p></body></html>"))

        self.btn_cos = QtWidgets.QPushButton(
            Calculator,
            text="cos",
            clicked=lambda: self._btn_trigonometry('cos'))
        self.btn_cos.setGeometry(QtCore.QRect(60, 254, 41, 34))
        self.btn_cos.setObjectName("btn_cos")

        self.btn_euler_number = QtWidgets.QPushButton(
            Calculator,
            text="e",
            clicked=lambda: self._btn_digit(f'{round(np.e, 10)}'))
        self.btn_euler_number.setGeometry(QtCore.QRect(10, 174, 41, 34))
        self.btn_euler_number.setObjectName("btn_euler_number")

        self.btn_plus = QtWidgets.QPushButton(
            Calculator,
            text="+",
            clicked=lambda: self._btn_operator('+'))
        self.btn_plus.setGeometry(QtCore.QRect(10, 94, 41, 34))
        self.btn_plus.setObjectName("btn_plus")

        self.btn_sin = QtWidgets.QPushButton(
            Calculator,
            text="sin",
            clicked=lambda: self._btn_trigonometry('sin'))
        self.btn_sin.setGeometry(QtCore.QRect(10, 254, 41, 34))
        self.btn_sin.setObjectName("btn_sin")

        self.btn_devision = QtWidgets.QPushButton(
            Calculator,
            text="÷",
            clicked=lambda: self._btn_operator('/'))
        self.btn_devision.setGeometry(QtCore.QRect(60, 134, 41, 34))
        self.btn_devision.setObjectName("btn_devision")

        self.btn_multiply = QtWidgets.QPushButton(
            Calculator,
            text="×",
            clicked=lambda: self._btn_operator('*'))
        self.btn_multiply.setGeometry(QtCore.QRect(10, 134, 41, 34))
        self.btn_multiply.setObjectName("btn_multiply")

        self.btn_precent = QtWidgets.QPushButton(
            Calculator,
            text="%",
            clicked=lambda: self._btn_operator('/100*'))
        self.btn_precent.setGeometry(QtCore.QRect(110, 174, 41, 34))
        self.btn_precent.setObjectName("btn_precent")

        self.btn_log = QtWidgets.QPushButton(
            Calculator,
            text="log",
            clicked=lambda: self._btn_log())
        self.btn_log.setGeometry(QtCore.QRect(60, 214, 41, 34))
        self.btn_log.setObjectName("btn_log")

        self.btn_sinh = QtWidgets.QPushButton(
            Calculator,
            text="sinh",
            clicked=lambda: self._btn_trigonometry('sinh'))
        self.btn_sinh.setGeometry(QtCore.QRect(10, 294, 41, 34))
        self.btn_sinh.setObjectName("btn_sinh")

        self.btn_tanh = QtWidgets.QPushButton(
            Calculator,
            text="tanh",
            clicked=lambda: self._btn_trigonometry('tanh'))
        self.btn_tanh.setGeometry(QtCore.QRect(110, 294, 41, 34))
        self.btn_tanh.setObjectName("btn_tanh")

        self.btn_equal = QtWidgets.QPushButton(
            Calculator,
            text="=",
            clicked=lambda: self._btn_equal())
        self.btn_equal.setGeometry(QtCore.QRect(260, 294, 41, 34))
        self.btn_equal.setObjectName("btn_equal")

        self.btn_change_sign = QtWidgets.QPushButton(
            Calculator,
            text="-/+",
            clicked=lambda: self._btn_change_sign())
        self.btn_change_sign.setGeometry(QtCore.QRect(110, 94, 41, 34))
        self.btn_change_sign.setObjectName("btn_change_sign")

        QtCore.QMetaObject.connectSlotsByName(Calculator)
        self._change_mode()

    def _btn_clear(self):
        self.curr_number = self.last_number = self.last_operator = ''
        self.output.setText("0")

    def _btn_remove_last(self):
        # move the result of last operation to self.curr_number
        # if remove_last pressed just after an operation
        if self.last_operator == self.curr_number == '':
            self.curr_number = self.last_number
            self.last_number = ''

        self.curr_number = self.curr_number[:-1]  # remove last number
        self.output.setText(self.curr_number)

        if self.curr_number == '-' or len(self.curr_number) == 0:
            self._btn_clear()

    def _btn_digit(self, digit):
        # check for Euler and PI constants
        if digit in (f'{round(np.pi, 10)}', f'{round(np.e, 10)}'):
            self.curr_number = digit

        # check for decimal point
        elif digit == '.':
            if '.' not in self.curr_number:
                if self.curr_number in ('', '-'):
                    self.curr_number += '0.'
                else:
                    self.curr_number += '.'

        else:
            # handle zero at the begining of numbers
            if self.curr_number in ('0', '-0'):
                self.curr_number = f'{self.curr_number[:-1]+digit}'
            else:
                self.curr_number += digit

        # clear result of last operation if user try to insert number just after that
        if self.last_operator == '':
            self.last_number = ''

        self.output.setText(self.curr_number)

    def _btn_operator(self, operator):
        if self.curr_number != '':
            if self.last_number != '':
                # if calculator has two saved number and an operator,
                # on press new operator it gives the result of the
                # operatoron. like every calculators do.
                self._btn_equal()

            else:
                # move curr to last for new number
                self.last_number = self.curr_number

        else:
            if self.last_number == '':
                operator = ''

        self.curr_number = ''  # clear curr_number for input new number
        self.last_operator = operator  # set the operator

        self.output.setText(self.last_number)

    def _btn_trigonometry(self, func):
        self._btn_equal()
        self.last_number = f"{eval(f'round(np.{func}((np.pi/180) * {self.last_number}), 3)')}"
        self._btn_equal()

    def _btn_log(self):
        self._btn_equal()
        self.last_number = f"{eval(f'np.log({self.last_number})')}"
        self._btn_equal()

    def _btn_factorial(self):
        self._btn_equal()
        self.last_number = f"{eval(f'np.math.gamma({self.last_number}+1)')}"
        self._btn_equal()

    def _btn_change_sign(self):
        # move the result of last operation to self.curr_number
        # if change_sign pressed just after an operation
        if self.last_operator == self.curr_number == '':
            self.curr_number = self.last_number
            self.last_number = ''

        # set curr_number to '0' if empty
        if self.curr_number == '':
            self.curr_number = '0'

        # change the curr_number sign
        self.curr_number = self.curr_number[1:] \
            if '-' in self.curr_number \
            else f'-{self.curr_number}'

        self.output.setText(self.curr_number)

    def _btn_equal(self):
        # convert current base to 10 if not 10
        if self.current_number_base != 10:
            if self.curr_number != '':
                self.curr_number = f'{int(self.curr_number, self.current_number_base)}'
            if self.last_number != '':
                self.last_number = f'{int(self.last_number, self.current_number_base)}'

        # ignore last_operator if curr_number is empty
        if self.last_number != '' and self.curr_number == '':
            self.last_operator = ''

        string = f'{eval(self.last_number + self.last_operator + self.curr_number + "+0")}'

        self._btn_clear()
        # convert output to current base if base isn't 10
        self.last_number = self.base_convert(string, 10, self.current_number_base) \
            if self.current_number_base != 10 \
            else string

        self.output.setText(self.last_number)

    def base_convert(self, number, _from, _to):
        number = int(number, _from)  # convert number to base 10
        sign = '-' if number < 0 else ''  # detect sign
        number = abs(number)  # unsigning number

        output = ''
        alph = '0123456789ABCDEF'
        while number > 0:
            output = f'{alph[number % _to]}' + output
            number //= _to

        self.current_number_base = _to

        return sign + output if output != '' else '0'

    def enable_digits_for_base(self, _to):
        digits = [self.btn_0, self.btn_1, self.btn_2, self.btn_3, self.btn_4, self.btn_5, self.btn_6, self.btn_7,
                  self.btn_8, self.btn_9, self.btn_a, self.btn_b, self.btn_c, self.btn_d, self.btn_e, self.btn_f, ]

        for x in digits[0:_to]:  # Enable related digits
            x.setEnabled(True)

        for x in digits[_to:]:  # Disable other digits
            x.setDisabled(True)

    def _change_base(self):
        self._btn_equal()

        if self.Binary.isChecked():
            self.last_number = f'{self.base_convert(self.last_number, self.current_number_base, 2)}'
            self.enable_digits_for_base(2)

        elif self.Octal.isChecked():
            self.last_number = f'{self.base_convert(self.last_number, self.current_number_base, 8)}'
            self.enable_digits_for_base(8)

        elif self.Decimal.isChecked():
            self.last_number = f'{self.base_convert(self.last_number, self.current_number_base, 10)}'
            self.enable_digits_for_base(10)

        else:
            self.last_number = f'{self.base_convert(self.last_number, self.current_number_base, 16)}'
            self.enable_digits_for_base(16)

        self._btn_equal()

    def _change_mode(self):
        if self.simple_mode.isChecked():
            self._btn_clear()
            # change current number to base_10
            self.Decimal.click()
            # Disable base changer
            self.Binary.setDisabled(True)
            self.Octal.setDisabled(True)
            self.Hexadecimal.setDisabled(True)
            # toggle to Decimal numbers
            self.Decimal.click()
            # Disable bitwise operarors
            self.btn_and.setDisabled(True)
            self.btn_or.setDisabled(True)
            self.btn_xor.setDisabled(True)
            self.btn_right_shift.setDisabled(True)
            self.btn_left_shift.setDisabled(True)
            self.btn_a.setDisabled(True)
            self.btn_b.setDisabled(True)
            self.btn_c.setDisabled(True)
            self.btn_d.setDisabled(True)
            self.btn_e.setDisabled(True)
            self.btn_f.setDisabled(True)
            # Enable aritاmetic operarors
            self.btn_plus.setEnabled(True)
            self.btn_minus.setEnabled(True)
            self.btn_devision.setEnabled(True)
            self.btn_multiply.setEnabled(True)
            self.btn_factorial.setEnabled(True)
            self.btn_euler_number.setEnabled(True)
            self.btn_pi_number.setEnabled(True)
            self.btn_precent.setEnabled(True)
            self.btn_power.setEnabled(True)
            self.power_label.setEnabled(True)
            self.btn_log.setEnabled(True)
            self.btn_mod.setEnabled(True)
            self.btn_sin.setEnabled(True)
            self.btn_cos.setEnabled(True)
            self.btn_tan.setEnabled(True)
            self.btn_sinh.setEnabled(True)
            self.btn_cosh.setEnabled(True)
            self.btn_tanh.setEnabled(True)
            self.btn_dot.setEnabled(True)
        else:
            self.btn_clear.click()
            # Enable base changer
            self.Binary.setEnabled(True)
            self.Octal.setEnabled(True)
            self.Hexadecimal.setEnabled(True)
            # Enable bitwise operators
            self.btn_and.setEnabled(True)
            self.btn_or.setEnabled(True)
            self.btn_xor.setEnabled(True)
            self.btn_right_shift.setEnabled(True)
            self.btn_left_shift.setEnabled(True)
            # Disable arithmetic operators
            self.btn_plus.setDisabled(True)
            self.btn_minus.setDisabled(True)
            self.btn_devision.setDisabled(True)
            self.btn_multiply.setDisabled(True)
            self.btn_factorial.setDisabled(True)
            self.btn_euler_number.setDisabled(True)
            self.btn_pi_number.setDisabled(True)
            self.btn_precent.setDisabled(True)
            self.btn_power.setDisabled(True)
            self.power_label.setDisabled(True)
            self.btn_log.setDisabled(True)
            self.btn_mod.setDisabled(True)
            self.btn_sin.setDisabled(True)
            self.btn_cos.setDisabled(True)
            self.btn_tan.setDisabled(True)
            self.btn_sinh.setDisabled(True)
            self.btn_cosh.setDisabled(True)
            self.btn_tanh.setDisabled(True)
            self.btn_dot.setDisabled(True)


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    app.setStyle("Fusion")

    Calculator = QtWidgets.QWidget()

    ui = Ui_Calculator()
    ui.setupUi(Calculator)

    Calculator.show()

    sys.exit(app.exec_())
