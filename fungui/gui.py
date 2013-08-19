"""
fungui is a software to help measuring the shell of a fungi.
"""
from __future__ import division
from PyQt4 import QtGui, QtCore


class ImageWindow(QtGui.QMainWindow):

    width = 1000
    height = 600

    def __init__(self):
        super(ImageWindow, self).__init__()
        self.populate()
        self.zoom_level = 1

    def populate(self):
        "Initializes the GUI and populates with widgets."
        self.image_pane = QtGui.QScrollArea()
        self.setCentralWidget(self.image_pane)
        self.image_widget = QtGui.QLabel()
        self.image_widget.setSizePolicy(QtGui.QSizePolicy.Ignored,
            QtGui.QSizePolicy.Ignored)
        self.image_widget.setScaledContents(True)
        self.image_pane.setWidget(self.image_widget)
        self.resize(self.width, self.height)
        self.center()

    def connect(self):
        self.create_actions()
        self.create_menus()

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

    def zoom_in(self):
        self.zoom_level *= 1.25
        self.scale_img(self.zoom_level)

    def zoom_out(self):
        self.zoom_level *= 0.8
        self.scale_img(self.zoom_level)

    def scale_img(self, factor):
        "Scaled the image by a factor"
        self.image_widget.resize(factor*self.image_widget.pixmap().size())

