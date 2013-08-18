"""
fungui is a software to help measuring the shell of a fungi.
"""
from __future__ import division
from PyQt4 import QtGui, QtCore
from matplotlib.figure import Figure
from matplotlib.backends.backend_qt4agg import FigureCanvasQTAgg as FigureCanvas


class MainWindow(QtGui.QMainWindow):

    width = 1000
    height = 600
    appname = 'FunGUI'

    def __init__(self):
        super(MainWindow, self).__init__()
        self.populate()
        self.zoom_level = 1

    def populate(self):
        "Initializes the GUI and populates with widgets."
        self.image_widget = QtGui.QLabel()
        self.image_widget.setSizePolicy(QtGui.QSizePolicy.Ignored,
            QtGui.QSizePolicy.Ignored)
        self.image_widget.setScaledContents(True)
        self.image_pane = QtGui.QScrollArea()
        self.image_pane.setWidget(self.image_widget)
        self.setCentralWidget(self.image_pane)
        self.create_actions()
        self.create_menus()
        self.resize(self.width, self.height)
        self.center()
        self.setWindowTitle(self.appname)

    def center(self):
        "Center the window on the screen"
        qr = self.frameGeometry()
        cp = QtGui.QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())

    def about(self):
        QtGui.QMessageBox.about(self, self.tr("About fungui"),
            self.tr("fungui..."))

    def create_actions(self):
        "Create actions and connect them to the proper functions/methods"
        self.exit_act = QtGui.QAction(self.tr("E&xit"), self,
            shortcut="Ctrl+Q", triggered=self.close)
        self.about_act = QtGui.QAction(self.tr("&About"), self,
            triggered=self.about)
        self.open_img_act = QtGui.QAction(self.tr("&Open"), self,
            shortcut="Ctrl+O", triggered=self.open_img)
        self.zoom_in_act = QtGui.QAction(self.tr("Zoom &In"), self,
            shortcut="+", triggered=self.zoom_in)
        self.zoom_out_act = QtGui.QAction(self.tr("Zoom &Out"), self,
            shortcut="-", triggered=self.zoom_out)

    def create_menus(self):
        "Connect menu items with actions"
        self.file_menu = self.menuBar().addMenu(self.tr("&File"))
        self.file_menu.addAction(self.open_img_act)
        self.file_menu.addAction(self.exit_act)
        self.image_menu = self.menuBar().addMenu(self.tr("&Image"))
        self.image_menu.addAction(self.zoom_in_act)
        self.image_menu.addAction(self.zoom_out_act)
        self.help_menu = self.menuBar().addMenu(self.tr("&Help"))
        self.help_menu.addAction(self.about_act)

    def open_img(self):
        "Starts a file browser to select an image to open."
        fname = QtGui.QFileDialog.getOpenFileName(self, "Open File",
                QtCore.QDir.currentPath())
        if fname:
            image = QtGui.QImage(fname)
            if image.isNull():
                QtGui.QMessageBox.information(self, "Oops",
                        "Cannot load %s." % fname)
                return
            self.image_widget.setPixmap(QtGui.QPixmap.fromImage(image))
            # Make the image fit one of the dimensions of the window
            size = self.image_widget.pixmap().size()
            ih, iw = size.height(), size.width()
            h, w = self.size().height(), self.size().width()
            factor = min(h/ih, w/iw)
            self.scale_img(0.99*factor)
            self.zoom_level = 1.0
            # Makes the image be the exact size of the window
            #self.image_pane.setWidgetResizable(True)
            self.setWindowTitle(self.appname + ' - ' + fname)

    def zoom_in(self):
        self.zoom_level *= 1.25
        self.scale_img(self.zoom_level)
        self.zoom_in_act.setEnabled(self.zoom_level < 3.0)

    def zoom_out(self):
        self.zoom_level *= 0.8
        self.scale_img(self.zoom_level)
        self.zoom_out_act.setEnabled(self.zoom_level > 0.333)

    def scale_img(self, factor):
        "Scaled the image by a factor"
        self.image_widget.resize(
                factor*self.image_widget.pixmap().size())
        self.adjust_scrollbar(self.image_pane.horizontalScrollBar(), factor)
        self.adjust_scrollbar(self.image_pane.verticalScrollBar(), factor)

    def adjust_scrollbar(self, scrollbar, factor):
        scrollbar.setValue(int(
            factor*scrollbar.value() + ((factor - 1)*scrollbar.pageStep()/2)))

