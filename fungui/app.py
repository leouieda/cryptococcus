"""
fungui is a software to help measuring the shell of a fungi.
"""
from __future__ import division
import os
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
        self.imgsize = None
        self.image_path = QtCore.QDir.currentPath()

    def open_img(self):
        "Starts a file browser to select an image to open."
        fname = QtGui.QFileDialog.getOpenFileName(self.image_window,
            "Open File", self.image_path)
        self.image_path = os.path.dirname(str(fname))
        if fname:
            image = QtGui.QImage(fname)
            if image.isNull():
                QtGui.QMessageBox.information(self.image_window, "Oops",
                        "Cannot load %s." % fname)
                return
            self.image_window.image_widget.setPixmap(
                QtGui.QPixmap.fromImage(image))
            self.imgsize = self.image_window.image_widget.pixmap().size()
            w = self.image_window.size().width()
            h = w*self.imgsize.height()/self.imgsize.width()
            self.image_window.resize(w, h)
            self.image_window.image_widget.resize(w, h)
            self.image_window.setWindowTitle(
                ' - '.join([self.appname, str(fname)]))

    def run(self):
        self.image_window.show()
