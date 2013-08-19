"""
fungui is a software to help measuring the shell of a fungi.
"""
from __future__ import division
from PyQt4 import QtGui, QtCore


class SelectionRectangle(QtGui.QRubberBand):
    """
    The selection rectagle.

    Modified from:
    http://www.qtcentre.org/threads/26140-Change-the-color-of-QRubberBand
    """

    color = QtGui.QColor(200, 0, 0)

    def __init__(self, parent):
        super(SelectionRectangle, self).__init__(QtGui.QRubberBand.Rectangle,
            parent)
        palette = QtGui.QPalette()
        palette.setBrush(QtGui.QPalette.WindowText,
            QtGui.QBrush(self.color))
        self.setPalette(palette)

    def paintEvent(self, e):
        painter = QtGui.QStylePainter(self)
        option = QtGui.QStyleOptionFocusRect()
        option.initFrom(self)
        painter.drawControl(QtGui.QStyle.CE_FocusFrame, option)

class ImageWindow(QtGui.QMainWindow):

    starting_width = 600

    def __init__(self):
        super(ImageWindow, self).__init__()
        self.image_widget = QtGui.QLabel()
        self.image_widget.setSizePolicy(QtGui.QSizePolicy.Ignored,
            QtGui.QSizePolicy.Ignored)
        self.image_widget.setScaledContents(True)
        self.image_widget.setMouseTracking(True)
        self.setCentralWidget(self.image_widget)
        self.selection_rect = SelectionRectangle(self.image_widget)

    def initial_size(self):
        self.resize(self.starting_width, self.starting_width)

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
        self.select_act = QtGui.QAction(self.tr("&Select"), self,
            shortcut="Ctrl+L", enabled=True, triggered=self.select)

    def create_menus(self):
        "Connect menu items with actions"
        self.file_menu = self.menuBar().addMenu(self.tr("&File"))
        self.file_menu.addAction(self.open_img_act)
        self.file_menu.addAction(self.exit_act)
        self.image_menu = self.menuBar().addMenu(self.tr("&Image"))
        self.image_menu.addAction(self.select_act)
        self.help_menu = self.menuBar().addMenu(self.tr("&Help"))
        self.help_menu.addAction(self.about_act)

    def mousePressEvent(self, event):
        if not self.select_act.isEnabled():
            self.select_origin = event.pos()
            self.selection_rect.setGeometry(
                QtCore.QRect(self.select_origin, QtCore.QSize()))
            self.selection_rect.show()
        QtGui.QWidget.mousePressEvent(self, event)

    def mouseMoveEvent(self, event):
        if not self.select_act.isEnabled():
            self.selection_rect.setGeometry(
                QtCore.QRect(self.select_origin, event.pos()).normalized())
        QtGui.QWidget.mouseMoveEvent(self, event)

    def mouseReleaseEvent(self, event):
        if not self.select_act.isEnabled():
            #self.selection_rect.hide()
            self.show_selection(self.selection_rect.geometry())
            self.select_act.setEnabled(True)
        QtGui.QWidget.mouseReleaseEvent(self, event)

class SelectionWindow(ImageWindow):

    starting_width = 500

    def __init__(self):
        super(SelectionWindow, self).__init__()

    def create_actions(self):
        "Create actions and connect them to the proper functions/methods"
        self.close_act = QtGui.QAction(self.tr("Close"), self,
            shortcut="Ctrl+Q", triggered=self.close)

    def create_menus(self):
        "Connect menu items with actions"
        self.selection_menu = self.menuBar().addMenu(self.tr("Selection"))
        self.selection_menu.addAction(self.close_act)

    def mousePressEvent(self, event):
        QtGui.QWidget.mousePressEvent(self, event)

    def mouseMoveEvent(self, event):
        QtGui.QWidget.mouseMoveEvent(self, event)

    def mouseReleaseEvent(self, event):
        QtGui.QWidget.mouseReleaseEvent(self, event)
