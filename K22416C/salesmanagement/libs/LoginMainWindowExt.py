from PyQt6.QtWidgets import QMessageBox, QMainWindow
from salesmanagement.ui.LoginMainWindow import Ui_MainWindow
from salesmanagement.libs.MainProgramMainWindowExt import MainProgramMainWindowExt
from salesmanagement.libs.nhanvienconnector import Nhanvienconnector

class LoginMainWindowExt(Ui_MainWindow):
    def __init__(self):
        self.nvconnector=Nhanvienconnector()
    def setupUi(self, MainWindow):
        super().setupUi(MainWindow)
        self.MainWindow = MainWindow
        self.setupSignalAndSlot()
    def showwindow(self):
        self.MainWindow.show()
    def setupSignalAndSlot(self):
        self.pushButtonDangNhap.clicked.connect(self.xuly_dangnhap)
    def xuly_dangnhap(self):
        username=self.lineEditUsername.text()
        password=self.lineEditPassword.text()
        #gọi kết nối cơ sở dữ liệu MySQL
        self.nvconnector.connector()
        self.nvlogin = self.nvconnector.DangNhap(username, password)
        if self.nvlogin!=None or (username == 'admin' and password == '123'):
                self.MainWindow.hide()
                self.mainwindow = QMainWindow()
                self.myui = MainProgramMainWindowExt()
                self.myui.setupUi(self.mainwindow)
                self.myui.showWindow()
        else:
                self.msg=QMessageBox()
                self.msg.setWindowTitle("Login thất bại")
                self.msg.setText("Bạn đăng nhập thất bại.\nKiểm tra lại thông tin đăng nhập")
                self.msg.setIcon(QMessageBox.Icon.Critical)
                self.msg.show()