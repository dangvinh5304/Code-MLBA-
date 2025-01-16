from PyQt6.QtWidgets import QMessageBox, QMainWindow

from salesmanagement.ui.LoginMainWindow import Ui_MainWindow
from salesmanagement.ui.MainProgramMainWindowExt import MainProgramMainWindowExt


class LoginMainWindowExt(Ui_MainWindow):
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
        #giả lập đăng nhập (hôm sau truy vấn thật trong CSDL)
        if username == 'admin' and password =='123':
            self.MainWindow.hide()
            self.MainWindow = QMainWindow()
            self.myui = MainProgramMainWindowExt()
            self.myui.setupUi(self.MainWindow)
            self.myui.showWindow()
        else:
            self.msg=QMessageBox()
            self.msg.setWindowTitle("Login thất bại")
            self.msg.setText("Bạn đăng nhập thát bại.\n Kiểm tra lại thông tin đăng nhập.")
            self.msg.setIcon(QMessageBox.Icon.Critical)
            self.msg.show()
