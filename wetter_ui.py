from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form, temp):
        Form.setObjectName("Wetter-App")
        Form.resize(979, 127)
        Form.setStyleSheet("background-color: rgb(78, 125, 255);")
        Form.setFixedSize(979, 127)
        self.frame = QtWidgets.QFrame(Form)
        self.frame.setGeometry(QtCore.QRect(0, 0, 981, 131))
        self.frame.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:2, stop:0 " + self.getColor(temp) + ", stop:1 rgba(255, 255, 255, 255));")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.shortdesc = QtWidgets.QLabel(self.frame)
        self.shortdesc.setGeometry(QtCore.QRect(170, 30, 181, 71))
        self.shortdesc.setStyleSheet("background-color: rgba(255, 255, 255, 0);\n"
"font: 20pt \"Arial\";")
        self.shortdesc.setScaledContents(True)
        self.shortdesc.setAlignment(QtCore.Qt.AlignCenter)
        self.shortdesc.setWordWrap(True)
        self.shortdesc.setObjectName("shortdesc")
        self.mintemp = QtWidgets.QLabel(self.frame)
        self.mintemp.setGeometry(QtCore.QRect(10, 30, 131, 41))
        self.mintemp.setMaximumSize(131, 41)
        self.mintemp.setStyleSheet("font: 36pt \"Arial\";\n"
"background-color: rgba(255, 255, 255, 0);")
        self.mintemp.setScaledContents(True)
        self.mintemp.setAlignment(QtCore.Qt.AlignCenter)
        self.mintemp.setWordWrap(True)
        self.mintemp.setObjectName("mintemp")
        self.weatherdesc = QtWidgets.QLabel(self.frame)
        self.weatherdesc.setGeometry(QtCore.QRect(450, 30, 531, 71))
        self.weatherdesc.setStyleSheet("background-color: rgba(255, 255, 255, 0);")
        self.weatherdesc.setScaledContents(True)
        self.weatherdesc.setAlignment(QtCore.Qt.AlignCenter)
        self.weatherdesc.setWordWrap(True)
        self.weatherdesc.setObjectName("weatherdesc")
        self.divider1 = QtWidgets.QLabel(self.frame)
        self.divider1.setGeometry(QtCore.QRect(145, 10, 2, 101))
        self.divider1.setStyleSheet("background-color: rgb(0, 0, 0);")
        self.divider1.setObjectName("divider1")
        self.divider2 = QtWidgets.QLabel(self.frame)
        self.divider2.setGeometry(QtCore.QRect(380, 10, 2, 101))
        self.divider2.setStyleSheet("background-color: rgb(0, 0, 0);")
        self.divider2.setObjectName("divider2")

        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("sun_icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Form.setWindowIcon(icon)
        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Wetter-App", "Wetter-App"))
        self.shortdesc.setText(_translate("Form", "TextLabel"))
        self.mintemp.setText(_translate("Form", "TextLabel"))
        self.weatherdesc.setText(_translate("Form", "TextLabel"))
        self.divider1.setText(_translate("Form", "TextLabel"))
        self.divider2.setText(_translate("Form", "TextLabel"))


    def setText(self, temp, long, short):
        self.weatherdesc.setText(long)
        self.mintemp.setText(temp)
        self.shortdesc.setText(short)
        self.weatherdesc.adjustSize()
        self.shortdesc.adjustSize()
        self.mintemp.adjustSize()

    @staticmethod
    def getColor(temp):
        if temp < 0:
            return "rgba(0, 0, 102 ,255)"
        elif temp < 5:
            return "rgba( ,255)"
        elif temp < 10:
            return "rgba(0, 128, 255 ,255)"
        elif temp < 15:
            return "rgba(153, 255, 255 ,255)"
        elif temp < 20:
            return "rgba(0, 179, 119 ,255)"
        elif temp < 25:
            return "rgba(204, 204, 0 ,255)"
        elif temp < 30:
            return "rgba(204, 163, 0 ,255)"
        else:
            return "rgba(153, 51, 0 ,255)"



