from PyQt6.QtWidgets import QApplication, QMainWindow

from salesmanagement.ui.LoginMainWindowExt import LoginMainWindowExt

app = QApplication([])
mainWindow = QMainWindow()
myui = LoginMainWindowExt()
myui.setupUi(mainWindow)
myui.showwindow()
app.exec()