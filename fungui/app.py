"""
fungui is a software to help measuring the shell of a fungi.
"""
from __future__ import division
from PyQt4 import QtGui, QtCore
from .gui import ImageWindow


class App(object):

    appname = 'FunGUI'

    def __init__(self):
        super(App, self).__init__()
        self.image_window = ImageWindow()
        self.image_window.open_img = self.open_img
        self.image_window.connect()
        self.image_window.setWindowTitle(self.appname)

    def open_img(self):
        "Starts a file browser to select an image to open."
        fname = QtGui.QFileDialog.getOpenFileName(self.image_window, "Open File",
                QtCore.QDir.currentPath())
        if fname:
            image = QtGui.QImage(fname)
            if image.isNull():
                QtGui.QMessageBox.information(self, "Oops",
                        "Cannot load %s." % fname)
                return
            self.image_window.image_widget.setPixmap(QtGui.QPixmap.fromImage(image))
            # Make the image fit one of the dimensions of the window
            size = self.image_window.image_widget.pixmap().size()
            ih, iw = size.height(), size.width()
            h, w = self.image_window.size().height(), self.image_window.size().width()
            factor = min(h/ih, w/iw)
            self.image_window.scale_img(0.99*factor)
            self.image_window.zoom_level = 1.0
            # Makes the image be the exact size of the window
            self.image_window.image_pane.setWidgetResizable(True)
            self.image_window.setWindowTitle(self.appname + ' - ' + fname)

    def run(self):
        self.image_window.show()
