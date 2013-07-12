#!/usr/bin/env python

"""
fungui is a software to help measuring the shell of a fungi.
"""

# Import modules
from PyQt4 import QtGui, QtCore
from matplotlib.figure import Figure
from matplotlib.backends.backend_qt4agg import FigureCanvasQTAgg as FigureCanvas
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
        
        # Create the mpl Figure and FigCanvas objects. 
        # 5x4 inches, 100 dots-per-inch
        #
        self.dpi = 100
        self.fig = Figure((5.0, 4.0), dpi = self.dpi)
        self.canvas = FigureCanvas(self.fig)
        self.canvas.setParent(self.main_frame)  
        
        # Since we have only one plot, we can use add_axes 
        # instead of add_subplot, but then the subplot
        # configuration tool in the navigation toolbar wouldn't
        # work.
        #
        self.axes = self.fig.add_subplot(111) 
            
        self.on_draw()
        
        
        # button to open image through file dialog
        self.open_button = QtGui.QPushButton('Open', self)
        self.open_button.clicked.connect(self.file_dialog)
        self.open_button.setToolTip('Open image')
        #self.obs_button.resize(self.open_button.sizeHint())
        self.open_button.setMaximumWidth(60)        
        
        
        #
        # Layout with box sizers
        #
        # define grid
        grid = QtGui.QGridLayout()
        #grid.setSpacing(10)
        
        #set matplotlib canvas
        grid.addWidget(self.canvas, 0, 1, 6, 1)
        #open image button
        grid.addWidget(self.open_button, 0, 0)

        self.setLayout(grid) 
        
        self.show()  
      
        
    # Draw canvas        
    def on_draw(self):
        """ draws the figure"""
        # clear the axes and redraw the plot anew
        #
        self.axes.clear()        
        
        self.axes.plot(range(10), [i**2 for i in range(10)])
        
        self.axes.set_title('Image name', fontsize= 'small') 
        
        self.canvas.draw()  


    # Support Modules              
    def file_dialog(self):
        """Open a file dialog"""
        #self.fileDialog = QtGui.QFileDialog(self)
        #self.fileDialog.show()
        fname = str(QtGui.QFileDialog.getOpenFileName(self,"Open File"))
        if fname != '':
            # here we should set a variable to passname
            pass

        
def main():
    app = QtGui.QApplication(sys.argv)
    mw = MainWindow()
    sys.exit(app.exec_()) 
 
if __name__ == '__main__':
    main()        