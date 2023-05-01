from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow, QDialog, QMessageBox
from PyQt5.uic import loadUi
import sys

import mysql.connector as con


class Loginapp(QDialog):
    def __init__(self):
        super(Loginapp, self).__init__()
        loadUi("login.ui", self)
        self.b3.clicked.connect(self.login)
        self.b1.clicked.connect(self.show_reg)

    def login(self):
        username = self.tb1.text()
        password = self.tb2.text()
        db = con.connect(host="localhost", user="root", password="", db="antidepbot")
        cursor = db.cursor()
        self.tb1.setText("")
        self.tb2.setText("")

        cursor.execute(
            "select *from details where Username='"
            + username
            + "'and Password='"
            + password
            + "'"
        )
        results = cursor.fetchone()
        if results:
            QMessageBox.information(
                self, "Login Output", "You have successfully logged in!"
            )
            self.showform()
        else:
            QMessageBox.information(self, "Login Output", "Invalid credentials!")

    def show_reg(self):
        widget.setCurrentIndex(1)

    def showform(self):
        widget.setCurrentIndex(2)


class register(QDialog):
    def __init__(self):
        super(register, self).__init__()
        loadUi("register.ui", self)
        self.b4.clicked.connect(self.show_login)
        self.b4.clicked.connect(self.reg)

    def show_login(self):
        widget.setCurrentIndex(0)

    def reg(self):
        username = self.tb3.text()
        password = self.tb4.text()
        age = self.tb5.text()
        address = self.tb6.text()
        ph = self.tb7.text()
        id1 = "1"
        db = con.connect(host="localhost", user="root", password="", db="antidepbot")
        cursor = db.cursor()
        cursor.execute(
            "select *from details where Username='"
            + username
            + "'and Password='"
            + password
            + "'"
        )
        results = cursor.fetchone()

        if results:
            QMessageBox.information(
                self,
                "Registration Status",
                "User Already exists! please change your username",
            )
        else:
            cursor.execute(
                "insert into details values('"
                + id1
                + '","'
                + username
                + "','"
                + password
                + "','"
                + age
                + "','"
                + address
                + "','"
                + ph
                + "')"
            )
            db.commit()
            QMessageBox.information(
                self, "Registration status", "Registered Sucessfully"
            )


class form(QDialog):
    def __init__(self):
        super(form, self).__init__()
        loadUi("form.ui", self)
        self.b1.clicked.connect(self.nextpage)
        self.counter = 0

    def show_results(self):
        widget.setCurrentIndex(3)

    def nextpage(self):
        if self.counter == 0:
            self.bg2.setExclusive(False)
            self.bg3.setExclusive(False)
            self.bg4.setExclusive(False)
            self.bg5.setExclusive(False)
            self.bg6.setExclusive(False)

            self.r1.setChecked(False)
            self.r2.setChecked(False)
            self.r3.setChecked(False)
            self.r4.setChecked(False)
            self.r5.setChecked(False)
            self.r6.setChecked(False)
            self.r7.setChecked(False)
            self.r8.setChecked(False)
            self.r9.setChecked(False)
            self.r10.setChecked(False)
            self.r11.setChecked(False)
            self.r12.setChecked(False)
            self.r13.setChecked(False)
            self.r14.setChecked(False)
            self.r15.setChecked(False)
            self.r16.setChecked(False)
            self.r17.setChecked(False)
            self.r18.setChecked(False)
            self.r19.setChecked(False)
            self.r20.setChecked(False)

            self.bg2.setExclusive(True)
            self.bg3.setExclusive(True)
            self.bg4.setExclusive(True)
            self.bg5.setExclusive(True)
            self.bg6.setExclusive(True)

            self.l1.setText(
                "6. Feeling bad about yourself - or that you are a failure or have let yourself or your family down"
            )
            self.l2.setText(
                "7. Trouble concentrating on things, such as reading the newspaper or watching television"
            )
            self.l3.setText(
                "8. Moving or speaking so slowly that other people could have noticed"
            )
            self.l4.setText(
                "9. Thoughts that you would be better off dead, or of hurting yourself"
            )
            self.l5.setText(
                "10. how difficult have these problems made it for you at work, home, school, or with other people? "
            )
            self.l6.setText("Click to see your Results")
            self.b1.setText("Click here for Results")
            self.counter = self.counter + 1

        elif self.counter == 1:
            self.show_results()


class result(QDialog):
    def __init__(self):
        super(result, self).__init__()
        loadUi("result.ui", self)
        self.counter = 0


app = QApplication(sys.argv)
widget = QtWidgets.QStackedWidget()
loginform = Loginapp()
registerform = register()
form = form()
result = result()
widget.addWidget(loginform)
widget.addWidget(registerform)
widget.addWidget(form)
widget.addWidget(result)
widget.setCurrentIndex(0)
widget.setFixedHeight(700)
widget.setFixedWidth(980)
widget.show()

app.exec_()
