#!/usr/bin/env python

"""
fungui is a software to help measuring the shell of a fungi.
"""

# Import modules
from PyQt4 import QtGui, QtCore
import sys


# Global variables
FRAME_WIDTH = 1020
FRAME_HEIGHT = 480

class MainWindow(QtGui.QMainWindow):
    def __init__(self):
        QtGui.QMainWindow.__init__(self)

        # create stuff
        self.wdg = Widget()
        self.setCentralWidget(self.wdg)
        self.createActions()
        self.createMenus()
        #self.createStatusBar()

         # format the main window
        self.resize(FRAME_WIDTH, FRAME_HEIGHT)
        self.center()
        self.setWindowTitle('Fungui')

        # show windows
        self.show()
        self.wdg.show()
        
    def center(self):
        qr = self.frameGeometry()
        cp = QtGui.QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())        

    def about(self):
        QtGui.QMessageBox.about(self, self.tr("About fungui"),
            self.tr("fungui..."))

    def createActions(self):
        self.exitAct = QtGui.QAction(self.tr("E&xit"), self)
        self.exitAct.setShortcut(self.tr("Ctrl+Q"))
        self.exitAct.setStatusTip(self.tr("Exit the application"))
        self.exitAct.triggered.connect(self.close)

        self.aboutAct = QtGui.QAction(self.tr("&About"), self)
        self.aboutAct.setStatusTip(self.tr("Show the application's About box"))
        self.aboutAct.triggered.connect(self.about)

        self.aboutQtAct = QtGui.QAction(self.tr("About &Qt"), self)
        self.aboutQtAct.setStatusTip(self.tr("Show the Qt library's About box"))
        self.aboutQtAct.triggered.connect(QtGui.qApp.aboutQt)

    def createMenus(self):
        self.fileMenu = self.menuBar().addMenu(self.tr("&File"))
        self.fileMenu.addAction(self.exitAct)

        self.helpMenu = self.menuBar().addMenu(self.tr("&Help"))
        self.helpMenu.addAction(self.aboutAct)
        self.helpMenu.addAction(self.aboutQtAct)

class Widget(QtGui.QWidget):
    
    def __init__(self):
        super(Widget, self).__init__()

        # set font for tips
        QtGui.QToolTip.setFont(QtGui.QFont('SansSerif', 10))

        self.create_frame()
        

    def create_frame(self):
        """The frame"""
        self.main_frame = QtGui.QWidget()        
       

        
def main():
    app = QtGui.QApplication(sys.argv)
    mw = MainWindow()
    sys.exit(app.exec_()) 
 
if __name__ == '__main__':
    main()        