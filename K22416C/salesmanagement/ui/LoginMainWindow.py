# Form implementation generated from reading ui file 'C:\Tiêu Đăng Vinh\Học máy trong kinh doanh\K22416C\salesmanagement\ui\LoginMainWindow.ui'
#
# Created by: PyQt6 UI code generator 6.8.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(parent=MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(parent=self.centralwidget)
        self.label.setGeometry(QtCore.QRect(330, 50, 411, 141))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(330, 180, 171, 41))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(330, 270, 121, 41))
        self.label_3.setObjectName("label_3")
        self.lineEditUsername = QtWidgets.QLineEdit(parent=self.centralwidget)
        self.lineEditUsername.setGeometry(QtCore.QRect(330, 230, 441, 31))
        self.lineEditUsername.setText("")
        self.lineEditUsername.setObjectName("lineEditUsername")
        self.lineEditPassword = QtWidgets.QLineEdit(parent=self.centralwidget)
        self.lineEditPassword.setGeometry(QtCore.QRect(330, 320, 441, 31))
        self.lineEditPassword.setText("")
        self.lineEditPassword.setEchoMode(QtWidgets.QLineEdit.EchoMode.Password)
        self.lineEditPassword.setObjectName("lineEditPassword")
        self.checkBoxLuuthongtin = QtWidgets.QCheckBox(parent=self.centralwidget)
        self.checkBoxLuuthongtin.setGeometry(QtCore.QRect(120, 400, 211, 41))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.checkBoxLuuthongtin.setFont(font)
        self.checkBoxLuuthongtin.setObjectName("checkBoxLuuthongtin")
        self.pushButtonDangNhap = QtWidgets.QPushButton(parent=self.centralwidget)
        self.pushButtonDangNhap.setGeometry(QtCore.QRect(120, 460, 231, 51))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.pushButtonDangNhap.setFont(font)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("C:\\Tiêu Đăng Vinh\\Học máy trong kinh doanh\\K22416C\\salesmanagement\\ui\\../images/Login.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.pushButtonDangNhap.setIcon(icon)
        self.pushButtonDangNhap.setIconSize(QtCore.QSize(32, 32))
        self.pushButtonDangNhap.setObjectName("pushButtonDangNhap")
        self.pushButtonThoat = QtWidgets.QPushButton(parent=self.centralwidget)
        self.pushButtonThoat.setGeometry(QtCore.QRect(420, 460, 231, 51))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.pushButtonThoat.setFont(font)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("C:\\Tiêu Đăng Vinh\\Học máy trong kinh doanh\\K22416C\\salesmanagement\\ui\\../images/Logout.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.pushButtonThoat.setIcon(icon1)
        self.pushButtonThoat.setIconSize(QtCore.QSize(32, 32))
        self.pushButtonThoat.setObjectName("pushButtonThoat")
        self.label_4 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(200, 170, 41, 51))
        self.label_4.setText("")
        self.label_4.setPixmap(QtGui.QPixmap("C:\\Tiêu Đăng Vinh\\Học máy trong kinh doanh\\K22416C\\salesmanagement\\ui\\../../../../../Users/Lenovo/.designer/images/11230326_user_admin_icon.png"))
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(200, 260, 41, 51))
        self.label_5.setText("")
        self.label_5.setPixmap(QtGui.QPixmap("C:\\Tiêu Đăng Vinh\\Học máy trong kinh doanh\\K22416C\\salesmanagement\\ui\\../../../../../Users/Lenovo/.designer/images/11230326_user_admin_icon.png"))
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(50, 150, 311, 231))
        self.label_6.setText("")
        self.label_6.setPixmap(QtGui.QPixmap("C:\\Tiêu Đăng Vinh\\Học máy trong kinh doanh\\K22416C\\salesmanagement\\ui\\../images/11230326_user_admin_icon.png"))
        self.label_6.setObjectName("label_6")
        self.label_7 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(40, 120, 271, 261))
        self.label_7.setText("")
        self.label_7.setPixmap(QtGui.QPixmap("C:\\Tiêu Đăng Vinh\\Học máy trong kinh doanh\\K22416C\\salesmanagement\\ui\\../images/Admin.png"))
        self.label_7.setObjectName("label_7")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(parent=MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(parent=MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.pushButtonThoat.clicked.connect(MainWindow.close) # type: ignore
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:24pt; font-weight:600;\">Đăng nhập hệ thống</span></p></body></html>"))
        self.label_2.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:14pt;\">Username:</span></p></body></html>"))
        self.label_3.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:14pt;\">Password: </span></p></body></html>"))
        self.checkBoxLuuthongtin.setText(_translate("MainWindow", "Lưu thông tin đăng nhập"))
        self.pushButtonDangNhap.setText(_translate("MainWindow", "Đăng nhập"))
        self.pushButtonThoat.setText(_translate("MainWindow", "Thoát"))
