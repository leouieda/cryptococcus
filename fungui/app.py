"""
fungui is a software to help measuring the shell of a fungi.
"""
from __future__ import division
import os
from PyQt4 import QtGui, QtCore
from .gui import ImageWindow, SelectionWindow


class App(object):

    appname = 'FunGUI'

    def __init__(self):
        super(App, self).__init__()
        self.img_size = None
        self.image_path = QtCore.QDir.currentPath()
        self.image_window = ImageWindow()
        self.image_window.open_img = self.open_img
        self.image_window.select = self.select
        self.image_window.show_selection = self.show_selection
        self.image_window.connect()
        self.image_window.setWindowTitle(self.appname)
        self.image_window.center()
        self.image_window.initial_size()
        self.selection_window = SelectionWindow()
        self.selection_window.connect()
        self.selection_window.initial_size()

    def open_img(self):
        "Starts a file browser to select an image to open."
        fname = QtGui.QFileDialog.getOpenFileName(self.image_window,
            "Open File", self.image_path)
        if fname:
            image = QtGui.QImage(fname)
            if image.isNull():
                QtGui.QMessageBox.information(self.image_window, "Oops",
                        "Cannot load %s." % fname)
                return
            self.image_path = os.path.dirname(str(fname))
            self.image_window.image_widget.setPixmap(
                QtGui.QPixmap.fromImage(image))
            self.resize_with_ratio(self.image_window, image)
            self.image_window.setWindowTitle(
                ' - '.join([self.appname, str(fname)]))
            self.selection_window.image_widget.clear()
            self.selection_window.initial_size()

    def resize_with_ratio(self, window, image):
        w = window.size().width()
        h = w*image.height()/image.width()
        window.resize(w, h)
        window.image_widget.resize(w, h)

    def select(self):
        self.image_window.select_act.setEnabled(False)

    def show_selection(self, rectangle):
        image = self.image_window.image_widget.pixmap()
        i, j, w, h = rectangle.getRect()
        # Need to scale the selection to image coordinates. The rect is in
        # window coordinates
        wfactor = image.width()/self.image_window.size().width()
        hfactor = image.height()/self.image_window.size().height()
        i *= wfactor
        w *= wfactor
        j *= hfactor
        h *= hfactor
        selection = image.copy(i, j, w, h)
        self.selection_window.image_widget.setPixmap(selection)
        self.resize_with_ratio(self.selection_window, selection)
        self.selection_window.setWindowTitle(
                ' - '.join([self.appname, 'Selection']))
        self.selection_window.show()

    def run(self):
        self.image_window.show()
