from salesmanagement.ui.MainProgramMainWindow import Ui_MainWindow
import sys

class MainProgramMainWindowExt(Ui_MainWindow):
    def setupUi(self, MainWindow):
        super().setupUi(MainWindow)
        self.MainWindow=MainWindow
        self.setupSignalandSlot()
    def showWindow(self):
        self.MainWindow.show()
    def setupSignalandSlot(self):
        self.actionthoatphanmem.triggered.connect(self.xuly_thoat)
    def xuly_thoat(self):
        sys.exit(0)
