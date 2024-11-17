# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'DuoStep1.ui'
##
## Created by: Qt User Interface Compiler version 6.8.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QAction, QBrush, QColor, QConicalGradient,
    QCursor, QFont, QFontDatabase, QGradient,
    QIcon, QImage, QKeySequence, QLinearGradient,
    QPainter, QPalette, QPixmap, QRadialGradient,
    QTransform)
from PySide6.QtWidgets import (QApplication, QCheckBox, QComboBox, QGridLayout,
    QHBoxLayout, QLabel, QMainWindow, QMenu,
    QMenuBar, QPushButton, QScrollArea, QSizePolicy,
    QSlider, QStatusBar, QTabWidget, QTextBrowser,
    QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.setEnabled(True)
        MainWindow.resize(887, 618)
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setCursor(QCursor(Qt.CursorShape.ArrowCursor))
        MainWindow.setMouseTracking(False)
        icon = QIcon()
        iconThemeName = u"stuff"
        if QIcon.hasThemeIcon(iconThemeName):
            icon = QIcon.fromTheme(iconThemeName)
        else:
            icon.addFile(u"C:/Users/hefan-zhang/.designer/backup", QSize(), QIcon.Mode.Normal, QIcon.State.Off)

        MainWindow.setWindowIcon(icon)
        MainWindow.setAutoFillBackground(True)
        MainWindow.setTabShape(QTabWidget.Rounded)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        font = QFont()
        font.setFamilies([u"Bahnschrift SemiBold"])
        font.setPointSize(12)
        font.setBold(True)
        self.centralwidget.setFont(font)
        self.Tabs = QTabWidget(self.centralwidget)
        self.Tabs.setObjectName(u"Tabs")
        self.Tabs.setGeometry(QRect(10, 9, 861, 231))
        self.Tabs.setAutoFillBackground(False)
        self.Master = QWidget()
        self.Master.setObjectName(u"Master")
        self.label_18 = QLabel(self.Master)
        self.label_18.setObjectName(u"label_18")
        self.label_18.setGeometry(QRect(50, 50, 191, 16))
        self.layoutWidget = QWidget(self.Master)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.layoutWidget.setGeometry(QRect(50, 70, 361, 88))
        self.gridLayout = QGridLayout(self.layoutWidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.L3d = QCheckBox(self.layoutWidget)
        self.L3d.setObjectName(u"L3d")

        self.gridLayout.addWidget(self.L3d, 2, 2, 1, 1)

        self.L2d = QCheckBox(self.layoutWidget)
        self.L2d.setObjectName(u"L2d")

        self.gridLayout.addWidget(self.L2d, 2, 3, 1, 1)

        self.L3u = QCheckBox(self.layoutWidget)
        self.L3u.setObjectName(u"L3u")

        self.gridLayout.addWidget(self.L3u, 1, 2, 1, 1)

        self.L4u = QCheckBox(self.layoutWidget)
        self.L4u.setObjectName(u"L4u")

        self.gridLayout.addWidget(self.L4u, 1, 1, 1, 1)

        self.L5d = QCheckBox(self.layoutWidget)
        self.L5d.setObjectName(u"L5d")

        self.gridLayout.addWidget(self.L5d, 2, 0, 1, 1)

        self.L4d = QCheckBox(self.layoutWidget)
        self.L4d.setObjectName(u"L4d")

        self.gridLayout.addWidget(self.L4d, 2, 1, 1, 1)

        self.L5u = QCheckBox(self.layoutWidget)
        self.L5u.setObjectName(u"L5u")

        self.gridLayout.addWidget(self.L5u, 1, 0, 1, 1)

        self.L2u = QCheckBox(self.layoutWidget)
        self.L2u.setObjectName(u"L2u")

        self.gridLayout.addWidget(self.L2u, 1, 3, 1, 1)

        self.L1u = QCheckBox(self.layoutWidget)
        self.L1u.setObjectName(u"L1u")

        self.gridLayout.addWidget(self.L1u, 1, 4, 1, 1)

        self.L1d = QCheckBox(self.layoutWidget)
        self.L1d.setObjectName(u"L1d")

        self.gridLayout.addWidget(self.L1d, 2, 4, 1, 1)

        self.label_2 = QLabel(self.layoutWidget)
        self.label_2.setObjectName(u"label_2")

        self.gridLayout.addWidget(self.label_2, 0, 0, 1, 2)

        self.layoutWidget1 = QWidget(self.Master)
        self.layoutWidget1.setObjectName(u"layoutWidget1")
        self.layoutWidget1.setGeometry(QRect(50, 10, 267, 25))
        self.horizontalLayout = QHBoxLayout(self.layoutWidget1)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.label_selectSdLib = QLabel(self.layoutWidget1)
        self.label_selectSdLib.setObjectName(u"label_selectSdLib")

        self.horizontalLayout.addWidget(self.label_selectSdLib)

        self.masterLibraryComboBox = QComboBox(self.layoutWidget1)
        self.masterLibraryComboBox.addItem("")
        self.masterLibraryComboBox.addItem("")
        self.masterLibraryComboBox.addItem("")
        self.masterLibraryComboBox.setObjectName(u"masterLibraryComboBox")
        self.masterLibraryComboBox.setEnabled(True)

        self.horizontalLayout.addWidget(self.masterLibraryComboBox)

        self.layoutWidget_11 = QWidget(self.Master)
        self.layoutWidget_11.setObjectName(u"layoutWidget_11")
        self.layoutWidget_11.setGeometry(QRect(450, 70, 366, 88))
        self.gridLayout_11 = QGridLayout(self.layoutWidget_11)
        self.gridLayout_11.setObjectName(u"gridLayout_11")
        self.gridLayout_11.setContentsMargins(0, 0, 0, 0)
        self.R4u = QCheckBox(self.layoutWidget_11)
        self.R4u.setObjectName(u"R4u")

        self.gridLayout_11.addWidget(self.R4u, 1, 3, 1, 1)

        self.R2d = QCheckBox(self.layoutWidget_11)
        self.R2d.setObjectName(u"R2d")

        self.gridLayout_11.addWidget(self.R2d, 2, 1, 1, 1)

        self.R3d = QCheckBox(self.layoutWidget_11)
        self.R3d.setObjectName(u"R3d")

        self.gridLayout_11.addWidget(self.R3d, 2, 2, 1, 1)

        self.R5u = QCheckBox(self.layoutWidget_11)
        self.R5u.setObjectName(u"R5u")

        self.gridLayout_11.addWidget(self.R5u, 1, 4, 1, 1)

        self.R3u = QCheckBox(self.layoutWidget_11)
        self.R3u.setObjectName(u"R3u")

        self.gridLayout_11.addWidget(self.R3u, 1, 2, 1, 1)

        self.R5d = QCheckBox(self.layoutWidget_11)
        self.R5d.setObjectName(u"R5d")

        self.gridLayout_11.addWidget(self.R5d, 2, 4, 1, 1)

        self.R1u = QCheckBox(self.layoutWidget_11)
        self.R1u.setObjectName(u"R1u")
        self.R1u.setEnabled(True)
        self.R1u.setTristate(False)

        self.gridLayout_11.addWidget(self.R1u, 1, 0, 1, 1)

        self.R2u = QCheckBox(self.layoutWidget_11)
        self.R2u.setObjectName(u"R2u")

        self.gridLayout_11.addWidget(self.R2u, 1, 1, 1, 1)

        self.R1d = QCheckBox(self.layoutWidget_11)
        self.R1d.setObjectName(u"R1d")

        self.gridLayout_11.addWidget(self.R1d, 2, 0, 1, 1)

        self.R4d = QCheckBox(self.layoutWidget_11)
        self.R4d.setObjectName(u"R4d")

        self.gridLayout_11.addWidget(self.R4d, 2, 3, 1, 1)

        self.label_13 = QLabel(self.layoutWidget_11)
        self.label_13.setObjectName(u"label_13")

        self.gridLayout_11.addWidget(self.label_13, 0, 0, 1, 2)

        self.startingNote = QComboBox(self.Master)
        self.startingNote.addItem("")
        self.startingNote.addItem("")
        self.startingNote.addItem("")
        self.startingNote.addItem("")
        self.startingNote.addItem("")
        self.startingNote.addItem("")
        self.startingNote.addItem("")
        self.startingNote.addItem("")
        self.startingNote.addItem("")
        self.startingNote.addItem("")
        self.startingNote.addItem("")
        self.startingNote.addItem("")
        self.startingNote.setObjectName(u"startingNote")
        self.startingNote.setGeometry(QRect(451, 11, 61, 21))
        self.startingOct = QComboBox(self.Master)
        self.startingOct.addItem("")
        self.startingOct.addItem("")
        self.startingOct.addItem("")
        self.startingOct.addItem("")
        self.startingOct.addItem("")
        self.startingOct.addItem("")
        self.startingOct.addItem("")
        self.startingOct.addItem("")
        self.startingOct.addItem("")
        self.startingOct.setObjectName(u"startingOct")
        self.startingOct.setGeometry(QRect(520, 10, 33, 21))
        self.Tabs.addTab(self.Master, "")
        self.tab_2 = QWidget()
        self.tab_2.setObjectName(u"tab_2")
        self.layoutWidget2 = QWidget(self.tab_2)
        self.layoutWidget2.setObjectName(u"layoutWidget2")
        self.layoutWidget2.setGeometry(QRect(50, 70, 361, 88))
        self.gridLayout_3 = QGridLayout(self.layoutWidget2)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.gridLayout_3.setContentsMargins(0, 0, 0, 0)
        self.L3d_2 = QCheckBox(self.layoutWidget2)
        self.L3d_2.setObjectName(u"L3d_2")

        self.gridLayout_3.addWidget(self.L3d_2, 2, 2, 1, 1)

        self.L2d_2 = QCheckBox(self.layoutWidget2)
        self.L2d_2.setObjectName(u"L2d_2")

        self.gridLayout_3.addWidget(self.L2d_2, 2, 3, 1, 1)

        self.L3u_2 = QCheckBox(self.layoutWidget2)
        self.L3u_2.setObjectName(u"L3u_2")

        self.gridLayout_3.addWidget(self.L3u_2, 1, 2, 1, 1)

        self.L4u_2 = QCheckBox(self.layoutWidget2)
        self.L4u_2.setObjectName(u"L4u_2")

        self.gridLayout_3.addWidget(self.L4u_2, 1, 1, 1, 1)

        self.L5d_2 = QCheckBox(self.layoutWidget2)
        self.L5d_2.setObjectName(u"L5d_2")

        self.gridLayout_3.addWidget(self.L5d_2, 2, 0, 1, 1)

        self.L4d_2 = QCheckBox(self.layoutWidget2)
        self.L4d_2.setObjectName(u"L4d_2")

        self.gridLayout_3.addWidget(self.L4d_2, 2, 1, 1, 1)

        self.L5u_2 = QCheckBox(self.layoutWidget2)
        self.L5u_2.setObjectName(u"L5u_2")

        self.gridLayout_3.addWidget(self.L5u_2, 1, 0, 1, 1)

        self.L2u_2 = QCheckBox(self.layoutWidget2)
        self.L2u_2.setObjectName(u"L2u_2")

        self.gridLayout_3.addWidget(self.L2u_2, 1, 3, 1, 1)

        self.L1u_2 = QCheckBox(self.layoutWidget2)
        self.L1u_2.setObjectName(u"L1u_2")

        self.gridLayout_3.addWidget(self.L1u_2, 1, 4, 1, 1)

        self.L1d_2 = QCheckBox(self.layoutWidget2)
        self.L1d_2.setObjectName(u"L1d_2")

        self.gridLayout_3.addWidget(self.L1d_2, 2, 4, 1, 1)

        self.label_4 = QLabel(self.layoutWidget2)
        self.label_4.setObjectName(u"label_4")

        self.gridLayout_3.addWidget(self.label_4, 0, 0, 1, 2)

        self.layoutWidget_2 = QWidget(self.tab_2)
        self.layoutWidget_2.setObjectName(u"layoutWidget_2")
        self.layoutWidget_2.setGeometry(QRect(450, 70, 366, 88))
        self.gridLayout_4 = QGridLayout(self.layoutWidget_2)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.gridLayout_4.setContentsMargins(0, 0, 0, 0)
        self.R4u_2 = QCheckBox(self.layoutWidget_2)
        self.R4u_2.setObjectName(u"R4u_2")

        self.gridLayout_4.addWidget(self.R4u_2, 1, 3, 1, 1)

        self.R2d_2 = QCheckBox(self.layoutWidget_2)
        self.R2d_2.setObjectName(u"R2d_2")

        self.gridLayout_4.addWidget(self.R2d_2, 2, 1, 1, 1)

        self.R3d_2 = QCheckBox(self.layoutWidget_2)
        self.R3d_2.setObjectName(u"R3d_2")

        self.gridLayout_4.addWidget(self.R3d_2, 2, 2, 1, 1)

        self.R5u_2 = QCheckBox(self.layoutWidget_2)
        self.R5u_2.setObjectName(u"R5u_2")

        self.gridLayout_4.addWidget(self.R5u_2, 1, 4, 1, 1)

        self.R3u_2 = QCheckBox(self.layoutWidget_2)
        self.R3u_2.setObjectName(u"R3u_2")

        self.gridLayout_4.addWidget(self.R3u_2, 1, 2, 1, 1)

        self.R5d_2 = QCheckBox(self.layoutWidget_2)
        self.R5d_2.setObjectName(u"R5d_2")

        self.gridLayout_4.addWidget(self.R5d_2, 2, 4, 1, 1)

        self.R1u_2 = QCheckBox(self.layoutWidget_2)
        self.R1u_2.setObjectName(u"R1u_2")
        self.R1u_2.setEnabled(True)
        self.R1u_2.setTristate(False)

        self.gridLayout_4.addWidget(self.R1u_2, 1, 0, 1, 1)

        self.R2u_2 = QCheckBox(self.layoutWidget_2)
        self.R2u_2.setObjectName(u"R2u_2")

        self.gridLayout_4.addWidget(self.R2u_2, 1, 1, 1, 1)

        self.R1d_2 = QCheckBox(self.layoutWidget_2)
        self.R1d_2.setObjectName(u"R1d_2")

        self.gridLayout_4.addWidget(self.R1d_2, 2, 0, 1, 1)

        self.R4d_2 = QCheckBox(self.layoutWidget_2)
        self.R4d_2.setObjectName(u"R4d_2")

        self.gridLayout_4.addWidget(self.R4d_2, 2, 3, 1, 1)

        self.label_5 = QLabel(self.layoutWidget_2)
        self.label_5.setObjectName(u"label_5")

        self.gridLayout_4.addWidget(self.label_5, 0, 0, 1, 2)

        self.label_17 = QLabel(self.tab_2)
        self.label_17.setObjectName(u"label_17")
        self.label_17.setGeometry(QRect(50, 30, 211, 16))
        self.layoutWidget_5 = QWidget(self.tab_2)
        self.layoutWidget_5.setObjectName(u"layoutWidget_5")
        self.layoutWidget_5.setGeometry(QRect(450, 30, 76, 23))
        self.horizontalLayout_3 = QHBoxLayout(self.layoutWidget_5)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.startingNote_2 = QComboBox(self.layoutWidget_5)
        self.startingNote_2.addItem("")
        self.startingNote_2.addItem("")
        self.startingNote_2.addItem("")
        self.startingNote_2.addItem("")
        self.startingNote_2.addItem("")
        self.startingNote_2.addItem("")
        self.startingNote_2.addItem("")
        self.startingNote_2.setObjectName(u"startingNote_2")

        self.horizontalLayout_3.addWidget(self.startingNote_2)

        self.startingOct_2 = QComboBox(self.layoutWidget_5)
        self.startingOct_2.addItem("")
        self.startingOct_2.addItem("")
        self.startingOct_2.addItem("")
        self.startingOct_2.addItem("")
        self.startingOct_2.addItem("")
        self.startingOct_2.addItem("")
        self.startingOct_2.addItem("")
        self.startingOct_2.addItem("")
        self.startingOct_2.addItem("")
        self.startingOct_2.setObjectName(u"startingOct_2")

        self.horizontalLayout_3.addWidget(self.startingOct_2)

        self.Tabs.addTab(self.tab_2, "")
        self.tab_3 = QWidget()
        self.tab_3.setObjectName(u"tab_3")
        self.layoutWidget_3 = QWidget(self.tab_3)
        self.layoutWidget_3.setObjectName(u"layoutWidget_3")
        self.layoutWidget_3.setGeometry(QRect(50, 70, 361, 88))
        self.gridLayout_5 = QGridLayout(self.layoutWidget_3)
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.gridLayout_5.setContentsMargins(0, 0, 0, 0)
        self.L3d_3 = QCheckBox(self.layoutWidget_3)
        self.L3d_3.setObjectName(u"L3d_3")

        self.gridLayout_5.addWidget(self.L3d_3, 2, 2, 1, 1)

        self.L2d_3 = QCheckBox(self.layoutWidget_3)
        self.L2d_3.setObjectName(u"L2d_3")

        self.gridLayout_5.addWidget(self.L2d_3, 2, 3, 1, 1)

        self.L3u_3 = QCheckBox(self.layoutWidget_3)
        self.L3u_3.setObjectName(u"L3u_3")

        self.gridLayout_5.addWidget(self.L3u_3, 1, 2, 1, 1)

        self.L4u_3 = QCheckBox(self.layoutWidget_3)
        self.L4u_3.setObjectName(u"L4u_3")

        self.gridLayout_5.addWidget(self.L4u_3, 1, 1, 1, 1)

        self.L5d_3 = QCheckBox(self.layoutWidget_3)
        self.L5d_3.setObjectName(u"L5d_3")

        self.gridLayout_5.addWidget(self.L5d_3, 2, 0, 1, 1)

        self.L4d_3 = QCheckBox(self.layoutWidget_3)
        self.L4d_3.setObjectName(u"L4d_3")

        self.gridLayout_5.addWidget(self.L4d_3, 2, 1, 1, 1)

        self.L5u_3 = QCheckBox(self.layoutWidget_3)
        self.L5u_3.setObjectName(u"L5u_3")

        self.gridLayout_5.addWidget(self.L5u_3, 1, 0, 1, 1)

        self.L2u_3 = QCheckBox(self.layoutWidget_3)
        self.L2u_3.setObjectName(u"L2u_3")

        self.gridLayout_5.addWidget(self.L2u_3, 1, 3, 1, 1)

        self.L1u_3 = QCheckBox(self.layoutWidget_3)
        self.L1u_3.setObjectName(u"L1u_3")

        self.gridLayout_5.addWidget(self.L1u_3, 1, 4, 1, 1)

        self.L1d_3 = QCheckBox(self.layoutWidget_3)
        self.L1d_3.setObjectName(u"L1d_3")

        self.gridLayout_5.addWidget(self.L1d_3, 2, 4, 1, 1)

        self.label_6 = QLabel(self.layoutWidget_3)
        self.label_6.setObjectName(u"label_6")

        self.gridLayout_5.addWidget(self.label_6, 0, 0, 1, 2)

        self.layoutWidget_4 = QWidget(self.tab_3)
        self.layoutWidget_4.setObjectName(u"layoutWidget_4")
        self.layoutWidget_4.setGeometry(QRect(450, 70, 366, 88))
        self.gridLayout_6 = QGridLayout(self.layoutWidget_4)
        self.gridLayout_6.setObjectName(u"gridLayout_6")
        self.gridLayout_6.setContentsMargins(0, 0, 0, 0)
        self.R2u_3 = QCheckBox(self.layoutWidget_4)
        self.R2u_3.setObjectName(u"R2u_3")

        self.gridLayout_6.addWidget(self.R2u_3, 1, 1, 1, 1)

        self.R1d_3 = QCheckBox(self.layoutWidget_4)
        self.R1d_3.setObjectName(u"R1d_3")

        self.gridLayout_6.addWidget(self.R1d_3, 2, 0, 1, 1)

        self.R4u_3 = QCheckBox(self.layoutWidget_4)
        self.R4u_3.setObjectName(u"R4u_3")

        self.gridLayout_6.addWidget(self.R4u_3, 1, 3, 1, 1)

        self.R5d_3 = QCheckBox(self.layoutWidget_4)
        self.R5d_3.setObjectName(u"R5d_3")

        self.gridLayout_6.addWidget(self.R5d_3, 2, 4, 1, 1)

        self.R5u_3 = QCheckBox(self.layoutWidget_4)
        self.R5u_3.setObjectName(u"R5u_3")

        self.gridLayout_6.addWidget(self.R5u_3, 1, 4, 1, 1)

        self.R3u_3 = QCheckBox(self.layoutWidget_4)
        self.R3u_3.setObjectName(u"R3u_3")

        self.gridLayout_6.addWidget(self.R3u_3, 1, 2, 1, 1)

        self.R3d_3 = QCheckBox(self.layoutWidget_4)
        self.R3d_3.setObjectName(u"R3d_3")

        self.gridLayout_6.addWidget(self.R3d_3, 2, 2, 1, 1)

        self.R1u_3 = QCheckBox(self.layoutWidget_4)
        self.R1u_3.setObjectName(u"R1u_3")
        self.R1u_3.setEnabled(True)
        self.R1u_3.setTristate(False)

        self.gridLayout_6.addWidget(self.R1u_3, 1, 0, 1, 1)

        self.R2d_3 = QCheckBox(self.layoutWidget_4)
        self.R2d_3.setObjectName(u"R2d_3")

        self.gridLayout_6.addWidget(self.R2d_3, 2, 1, 1, 1)

        self.R4d_3 = QCheckBox(self.layoutWidget_4)
        self.R4d_3.setObjectName(u"R4d_3")

        self.gridLayout_6.addWidget(self.R4d_3, 2, 3, 1, 1)

        self.label_7 = QLabel(self.layoutWidget_4)
        self.label_7.setObjectName(u"label_7")

        self.gridLayout_6.addWidget(self.label_7, 0, 0, 1, 2)

        self.label = QLabel(self.tab_3)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(50, 30, 211, 16))
        self.layoutWidget_6 = QWidget(self.tab_3)
        self.layoutWidget_6.setObjectName(u"layoutWidget_6")
        self.layoutWidget_6.setGeometry(QRect(450, 30, 76, 23))
        self.horizontalLayout_4 = QHBoxLayout(self.layoutWidget_6)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.startingNote_3 = QComboBox(self.layoutWidget_6)
        self.startingNote_3.addItem("")
        self.startingNote_3.addItem("")
        self.startingNote_3.addItem("")
        self.startingNote_3.addItem("")
        self.startingNote_3.addItem("")
        self.startingNote_3.addItem("")
        self.startingNote_3.addItem("")
        self.startingNote_3.setObjectName(u"startingNote_3")

        self.horizontalLayout_4.addWidget(self.startingNote_3)

        self.startingOct_3 = QComboBox(self.layoutWidget_6)
        self.startingOct_3.addItem("")
        self.startingOct_3.addItem("")
        self.startingOct_3.addItem("")
        self.startingOct_3.addItem("")
        self.startingOct_3.addItem("")
        self.startingOct_3.addItem("")
        self.startingOct_3.addItem("")
        self.startingOct_3.addItem("")
        self.startingOct_3.addItem("")
        self.startingOct_3.setObjectName(u"startingOct_3")

        self.horizontalLayout_4.addWidget(self.startingOct_3)

        self.Tabs.addTab(self.tab_3, "")
        self.tab = QWidget()
        self.tab.setObjectName(u"tab")
        self.scrollArea = QScrollArea(self.tab)
        self.scrollArea.setObjectName(u"scrollArea")
        self.scrollArea.setGeometry(QRect(0, 0, 851, 201))
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.scrollArea.sizePolicy().hasHeightForWidth())
        self.scrollArea.setSizePolicy(sizePolicy1)
        self.scrollArea.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOn)
        self.scrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 832, 336))
        self.verticalLayout = QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.gridLayout_10 = QGridLayout()
        self.gridLayout_10.setObjectName(u"gridLayout_10")
        self.uploadButtonL_8 = QPushButton(self.scrollAreaWidgetContents)
        self.uploadButtonL_8.setObjectName(u"uploadButtonL_8")

        self.gridLayout_10.addWidget(self.uploadButtonL_8, 8, 1, 1, 1)

        self.uploadButtonR_5 = QPushButton(self.scrollAreaWidgetContents)
        self.uploadButtonR_5.setObjectName(u"uploadButtonR_5")

        self.gridLayout_10.addWidget(self.uploadButtonR_5, 5, 5, 1, 1)

        self.uploadButtonR_4 = QPushButton(self.scrollAreaWidgetContents)
        self.uploadButtonR_4.setObjectName(u"uploadButtonR_4")

        self.gridLayout_10.addWidget(self.uploadButtonR_4, 4, 5, 1, 1)

        self.L3d_5 = QCheckBox(self.scrollAreaWidgetContents)
        self.L3d_5.setObjectName(u"L3d_5")

        self.gridLayout_10.addWidget(self.L3d_5, 6, 0, 1, 1)

        self.L5d_5 = QCheckBox(self.scrollAreaWidgetContents)
        self.L5d_5.setObjectName(u"L5d_5")

        self.gridLayout_10.addWidget(self.L5d_5, 2, 0, 1, 1)

        self.uploadButtonL_7 = QPushButton(self.scrollAreaWidgetContents)
        self.uploadButtonL_7.setObjectName(u"uploadButtonL_7")

        self.gridLayout_10.addWidget(self.uploadButtonL_7, 7, 1, 1, 1)

        self.R1u_5 = QCheckBox(self.scrollAreaWidgetContents)
        self.R1u_5.setObjectName(u"R1u_5")
        self.R1u_5.setEnabled(True)
        self.R1u_5.setTristate(False)

        self.gridLayout_10.addWidget(self.R1u_5, 1, 4, 1, 1)

        self.R1d_5 = QCheckBox(self.scrollAreaWidgetContents)
        self.R1d_5.setObjectName(u"R1d_5")

        self.gridLayout_10.addWidget(self.R1d_5, 2, 4, 1, 1)

        self.R4u_5 = QCheckBox(self.scrollAreaWidgetContents)
        self.R4u_5.setObjectName(u"R4u_5")

        self.gridLayout_10.addWidget(self.R4u_5, 7, 4, 1, 1)

        self.uploadButtonR_2 = QPushButton(self.scrollAreaWidgetContents)
        self.uploadButtonR_2.setObjectName(u"uploadButtonR_2")

        self.gridLayout_10.addWidget(self.uploadButtonR_2, 2, 5, 1, 1)

        self.uploadButtonR_6 = QPushButton(self.scrollAreaWidgetContents)
        self.uploadButtonR_6.setObjectName(u"uploadButtonR_6")

        self.gridLayout_10.addWidget(self.uploadButtonR_6, 6, 5, 1, 1)

        self.R4d_5 = QCheckBox(self.scrollAreaWidgetContents)
        self.R4d_5.setObjectName(u"R4d_5")

        self.gridLayout_10.addWidget(self.R4d_5, 8, 4, 1, 1)

        self.uploadButtonL_9 = QPushButton(self.scrollAreaWidgetContents)
        self.uploadButtonL_9.setObjectName(u"uploadButtonL_9")

        self.gridLayout_10.addWidget(self.uploadButtonL_9, 9, 1, 1, 1)

        self.L2u_5 = QCheckBox(self.scrollAreaWidgetContents)
        self.L2u_5.setObjectName(u"L2u_5")

        self.gridLayout_10.addWidget(self.L2u_5, 7, 0, 1, 1)

        self.L4d_5 = QCheckBox(self.scrollAreaWidgetContents)
        self.L4d_5.setObjectName(u"L4d_5")

        self.gridLayout_10.addWidget(self.L4d_5, 4, 0, 1, 1)

        self.R5u_5 = QCheckBox(self.scrollAreaWidgetContents)
        self.R5u_5.setObjectName(u"R5u_5")

        self.gridLayout_10.addWidget(self.R5u_5, 9, 4, 1, 1)

        self.uploadButtonL = QPushButton(self.scrollAreaWidgetContents)
        self.uploadButtonL.setObjectName(u"uploadButtonL")

        self.gridLayout_10.addWidget(self.uploadButtonL, 1, 1, 1, 1)

        self.uploadButtonL_6 = QPushButton(self.scrollAreaWidgetContents)
        self.uploadButtonL_6.setObjectName(u"uploadButtonL_6")

        self.gridLayout_10.addWidget(self.uploadButtonL_6, 6, 1, 1, 1)

        self.uploadButtonL_10 = QPushButton(self.scrollAreaWidgetContents)
        self.uploadButtonL_10.setObjectName(u"uploadButtonL_10")

        self.gridLayout_10.addWidget(self.uploadButtonL_10, 10, 1, 1, 1)

        self.uploadButtonR_1 = QPushButton(self.scrollAreaWidgetContents)
        self.uploadButtonR_1.setObjectName(u"uploadButtonR_1")

        self.gridLayout_10.addWidget(self.uploadButtonR_1, 1, 5, 1, 1)

        self.uploadButtonR_9 = QPushButton(self.scrollAreaWidgetContents)
        self.uploadButtonR_9.setObjectName(u"uploadButtonR_9")

        self.gridLayout_10.addWidget(self.uploadButtonR_9, 9, 5, 1, 1)

        self.R2u_5 = QCheckBox(self.scrollAreaWidgetContents)
        self.R2u_5.setObjectName(u"R2u_5")

        self.gridLayout_10.addWidget(self.R2u_5, 3, 4, 1, 1)

        self.label_11 = QLabel(self.scrollAreaWidgetContents)
        self.label_11.setObjectName(u"label_11")

        self.gridLayout_10.addWidget(self.label_11, 0, 0, 1, 4)

        self.uploadButtonL_5 = QPushButton(self.scrollAreaWidgetContents)
        self.uploadButtonL_5.setObjectName(u"uploadButtonL_5")

        self.gridLayout_10.addWidget(self.uploadButtonL_5, 5, 1, 1, 1)

        self.R2d_5 = QCheckBox(self.scrollAreaWidgetContents)
        self.R2d_5.setObjectName(u"R2d_5")

        self.gridLayout_10.addWidget(self.R2d_5, 4, 4, 1, 1)

        self.uploadButtonL_2 = QPushButton(self.scrollAreaWidgetContents)
        self.uploadButtonL_2.setObjectName(u"uploadButtonL_2")

        self.gridLayout_10.addWidget(self.uploadButtonL_2, 2, 1, 1, 1)

        self.R3d_5 = QCheckBox(self.scrollAreaWidgetContents)
        self.R3d_5.setObjectName(u"R3d_5")

        self.gridLayout_10.addWidget(self.R3d_5, 6, 4, 1, 1)

        self.L4u_5 = QCheckBox(self.scrollAreaWidgetContents)
        self.L4u_5.setObjectName(u"L4u_5")

        self.gridLayout_10.addWidget(self.L4u_5, 3, 0, 1, 1)

        self.L3u_5 = QCheckBox(self.scrollAreaWidgetContents)
        self.L3u_5.setObjectName(u"L3u_5")

        self.gridLayout_10.addWidget(self.L3u_5, 5, 0, 1, 1)

        self.L1u_5 = QCheckBox(self.scrollAreaWidgetContents)
        self.L1u_5.setObjectName(u"L1u_5")

        self.gridLayout_10.addWidget(self.L1u_5, 9, 0, 1, 1)

        self.uploadButtonR_7 = QPushButton(self.scrollAreaWidgetContents)
        self.uploadButtonR_7.setObjectName(u"uploadButtonR_7")

        self.gridLayout_10.addWidget(self.uploadButtonR_7, 7, 5, 1, 1)

        self.L2d_5 = QCheckBox(self.scrollAreaWidgetContents)
        self.L2d_5.setObjectName(u"L2d_5")

        self.gridLayout_10.addWidget(self.L2d_5, 8, 0, 1, 1)

        self.R5d_5 = QCheckBox(self.scrollAreaWidgetContents)
        self.R5d_5.setObjectName(u"R5d_5")

        self.gridLayout_10.addWidget(self.R5d_5, 10, 4, 1, 1)

        self.L1d_5 = QCheckBox(self.scrollAreaWidgetContents)
        self.L1d_5.setObjectName(u"L1d_5")

        self.gridLayout_10.addWidget(self.L1d_5, 10, 0, 1, 1)

        self.uploadButtonL_3 = QPushButton(self.scrollAreaWidgetContents)
        self.uploadButtonL_3.setObjectName(u"uploadButtonL_3")

        self.gridLayout_10.addWidget(self.uploadButtonL_3, 3, 1, 1, 1)

        self.R3u_5 = QCheckBox(self.scrollAreaWidgetContents)
        self.R3u_5.setObjectName(u"R3u_5")

        self.gridLayout_10.addWidget(self.R3u_5, 5, 4, 1, 1)

        self.uploadButtonL_4 = QPushButton(self.scrollAreaWidgetContents)
        self.uploadButtonL_4.setObjectName(u"uploadButtonL_4")

        self.gridLayout_10.addWidget(self.uploadButtonL_4, 4, 1, 1, 1)

        self.uploadButtonR_10 = QPushButton(self.scrollAreaWidgetContents)
        self.uploadButtonR_10.setObjectName(u"uploadButtonR_10")

        self.gridLayout_10.addWidget(self.uploadButtonR_10, 10, 5, 1, 1)

        self.uploadButtonR_3 = QPushButton(self.scrollAreaWidgetContents)
        self.uploadButtonR_3.setObjectName(u"uploadButtonR_3")

        self.gridLayout_10.addWidget(self.uploadButtonR_3, 3, 5, 1, 1)

        self.uploadButtonR_8 = QPushButton(self.scrollAreaWidgetContents)
        self.uploadButtonR_8.setObjectName(u"uploadButtonR_8")

        self.gridLayout_10.addWidget(self.uploadButtonR_8, 8, 5, 1, 1)

        self.L5u_5 = QCheckBox(self.scrollAreaWidgetContents)
        self.L5u_5.setObjectName(u"L5u_5")

        self.gridLayout_10.addWidget(self.L5u_5, 1, 0, 1, 1)

        self.upload_label_R_2 = QLabel(self.scrollAreaWidgetContents)
        self.upload_label_R_2.setObjectName(u"upload_label_R_2")

        self.gridLayout_10.addWidget(self.upload_label_R_2, 2, 6, 1, 2)

        self.upload_label_R_1 = QLabel(self.scrollAreaWidgetContents)
        self.upload_label_R_1.setObjectName(u"upload_label_R_1")

        self.gridLayout_10.addWidget(self.upload_label_R_1, 1, 6, 1, 2)

        self.upload_label_R_3 = QLabel(self.scrollAreaWidgetContents)
        self.upload_label_R_3.setObjectName(u"upload_label_R_3")

        self.gridLayout_10.addWidget(self.upload_label_R_3, 3, 6, 1, 2)

        self.upload_label_R_4 = QLabel(self.scrollAreaWidgetContents)
        self.upload_label_R_4.setObjectName(u"upload_label_R_4")

        self.gridLayout_10.addWidget(self.upload_label_R_4, 4, 6, 1, 2)

        self.upload_label_R_5 = QLabel(self.scrollAreaWidgetContents)
        self.upload_label_R_5.setObjectName(u"upload_label_R_5")

        self.gridLayout_10.addWidget(self.upload_label_R_5, 5, 6, 1, 2)

        self.upload_label_R_6 = QLabel(self.scrollAreaWidgetContents)
        self.upload_label_R_6.setObjectName(u"upload_label_R_6")

        self.gridLayout_10.addWidget(self.upload_label_R_6, 6, 6, 1, 2)

        self.upload_label_R_7 = QLabel(self.scrollAreaWidgetContents)
        self.upload_label_R_7.setObjectName(u"upload_label_R_7")

        self.gridLayout_10.addWidget(self.upload_label_R_7, 7, 6, 1, 2)

        self.upload_label_R_8 = QLabel(self.scrollAreaWidgetContents)
        self.upload_label_R_8.setObjectName(u"upload_label_R_8")

        self.gridLayout_10.addWidget(self.upload_label_R_8, 8, 6, 1, 2)

        self.upload_label_R_9 = QLabel(self.scrollAreaWidgetContents)
        self.upload_label_R_9.setObjectName(u"upload_label_R_9")

        self.gridLayout_10.addWidget(self.upload_label_R_9, 9, 6, 1, 2)

        self.upload_label_R_10 = QLabel(self.scrollAreaWidgetContents)
        self.upload_label_R_10.setObjectName(u"upload_label_R_10")

        self.gridLayout_10.addWidget(self.upload_label_R_10, 10, 6, 1, 2)

        self.upload_label_L_1 = QLabel(self.scrollAreaWidgetContents)
        self.upload_label_L_1.setObjectName(u"upload_label_L_1")

        self.gridLayout_10.addWidget(self.upload_label_L_1, 1, 2, 1, 2)

        self.upload_label_L_2 = QLabel(self.scrollAreaWidgetContents)
        self.upload_label_L_2.setObjectName(u"upload_label_L_2")

        self.gridLayout_10.addWidget(self.upload_label_L_2, 2, 2, 1, 2)

        self.upload_label_L_3 = QLabel(self.scrollAreaWidgetContents)
        self.upload_label_L_3.setObjectName(u"upload_label_L_3")

        self.gridLayout_10.addWidget(self.upload_label_L_3, 3, 2, 1, 2)

        self.upload_label_L_4 = QLabel(self.scrollAreaWidgetContents)
        self.upload_label_L_4.setObjectName(u"upload_label_L_4")

        self.gridLayout_10.addWidget(self.upload_label_L_4, 4, 2, 1, 2)

        self.upload_label_L_5 = QLabel(self.scrollAreaWidgetContents)
        self.upload_label_L_5.setObjectName(u"upload_label_L_5")

        self.gridLayout_10.addWidget(self.upload_label_L_5, 5, 2, 1, 2)

        self.upload_label_L_6 = QLabel(self.scrollAreaWidgetContents)
        self.upload_label_L_6.setObjectName(u"upload_label_L_6")

        self.gridLayout_10.addWidget(self.upload_label_L_6, 6, 2, 1, 2)

        self.upload_label_L_7 = QLabel(self.scrollAreaWidgetContents)
        self.upload_label_L_7.setObjectName(u"upload_label_L_7")

        self.gridLayout_10.addWidget(self.upload_label_L_7, 7, 2, 1, 2)

        self.upload_label_L_8 = QLabel(self.scrollAreaWidgetContents)
        self.upload_label_L_8.setObjectName(u"upload_label_L_8")

        self.gridLayout_10.addWidget(self.upload_label_L_8, 8, 2, 1, 2)

        self.upload_label_L_9 = QLabel(self.scrollAreaWidgetContents)
        self.upload_label_L_9.setObjectName(u"upload_label_L_9")

        self.gridLayout_10.addWidget(self.upload_label_L_9, 9, 2, 1, 2)

        self.upload_label_L_10 = QLabel(self.scrollAreaWidgetContents)
        self.upload_label_L_10.setObjectName(u"upload_label_L_10")

        self.gridLayout_10.addWidget(self.upload_label_L_10, 10, 2, 1, 2)

        self.label_10 = QLabel(self.scrollAreaWidgetContents)
        self.label_10.setObjectName(u"label_10")

        self.gridLayout_10.addWidget(self.label_10, 0, 4, 1, 4)


        self.verticalLayout.addLayout(self.gridLayout_10)

        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.Tabs.addTab(self.tab, "")
        self.masterVol = QSlider(self.centralwidget)
        self.masterVol.setObjectName(u"masterVol")
        self.masterVol.setGeometry(QRect(200, 270, 160, 16))
        self.masterVol.setMaximum(100)
        self.masterVol.setOrientation(Qt.Horizontal)
        self.masterVol.setTickPosition(QSlider.TicksBelow)
        self.pianoVol = QSlider(self.centralwidget)
        self.pianoVol.setObjectName(u"pianoVol")
        self.pianoVol.setGeometry(QRect(200, 310, 160, 16))
        self.pianoVol.setMaximum(100)
        self.pianoVol.setOrientation(Qt.Horizontal)
        self.pianoVol.setTickPosition(QSlider.TicksBelow)
        self.clarinetVol = QSlider(self.centralwidget)
        self.clarinetVol.setObjectName(u"clarinetVol")
        self.clarinetVol.setGeometry(QRect(200, 350, 160, 16))
        self.clarinetVol.setMaximum(100)
        self.clarinetVol.setValue(0)
        self.clarinetVol.setOrientation(Qt.Horizontal)
        self.clarinetVol.setInvertedControls(False)
        self.clarinetVol.setTickPosition(QSlider.TicksBelow)
        self.label_MasterVol = QLabel(self.centralwidget)
        self.label_MasterVol.setObjectName(u"label_MasterVol")
        self.label_MasterVol.setGeometry(QRect(60, 270, 121, 16))
        self.label_PianoVol = QLabel(self.centralwidget)
        self.label_PianoVol.setObjectName(u"label_PianoVol")
        self.label_PianoVol.setGeometry(QRect(60, 310, 111, 16))
        self.label_TrumpetVol = QLabel(self.centralwidget)
        self.label_TrumpetVol.setObjectName(u"label_TrumpetVol")
        self.label_TrumpetVol.setGeometry(QRect(60, 350, 131, 16))
        self.label_19 = QLabel(self.centralwidget)
        self.label_19.setObjectName(u"label_19")
        self.label_19.setGeometry(QRect(370, 270, 31, 16))
        self.label_20 = QLabel(self.centralwidget)
        self.label_20.setObjectName(u"label_20")
        self.label_20.setGeometry(QRect(370, 310, 31, 16))
        self.label_21 = QLabel(self.centralwidget)
        self.label_21.setObjectName(u"label_21")
        self.label_21.setGeometry(QRect(370, 350, 31, 16))
        self.recordButton = QPushButton(self.centralwidget)
        self.recordButton.setObjectName(u"recordButton")
        self.recordButton.setGeometry(QRect(60, 400, 141, 25))
        self.stopButton = QPushButton(self.centralwidget)
        self.stopButton.setObjectName(u"stopButton")
        self.stopButton.setGeometry(QRect(60, 440, 141, 25))
        self.textBrowser = QTextBrowser(self.centralwidget)
        self.textBrowser.setObjectName(u"textBrowser")
        self.textBrowser.setGeometry(QRect(430, 270, 411, 191))
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 887, 22))
        self.menubar.setNativeMenuBar(True)
        self.menumain = QMenu(self.menubar)
        self.menumain.setObjectName(u"menumain")
        MainWindow.setMenuBar(self.menubar)

        self.menubar.addAction(self.menumain.menuAction())
        self.menumain.addSeparator()

        self.retranslateUi(MainWindow)

        self.Tabs.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"DuoStep", None))
        self.label_18.setText(QCoreApplication.translate("MainWindow", u"Enable/Disable Button", None))
        self.L3d.setText(QCoreApplication.translate("MainWindow", u"L3_d", None))
        self.L2d.setText(QCoreApplication.translate("MainWindow", u"L2_d", None))
        self.L3u.setText(QCoreApplication.translate("MainWindow", u"L3_u", None))
        self.L4u.setText(QCoreApplication.translate("MainWindow", u"L4_u", None))
        self.L5d.setText(QCoreApplication.translate("MainWindow", u"L5_d", None))
        self.L4d.setText(QCoreApplication.translate("MainWindow", u"L4_d", None))
        self.L5u.setText(QCoreApplication.translate("MainWindow", u"L5_u", None))
        self.L2u.setText(QCoreApplication.translate("MainWindow", u"L2_u", None))
        self.L1u.setText(QCoreApplication.translate("MainWindow", u"L1_u", None))
        self.L1d.setText(QCoreApplication.translate("MainWindow", u"L1_d", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Left Hand", None))
        self.label_selectSdLib.setText(QCoreApplication.translate("MainWindow", u"Select Sound Library", None))
        self.masterLibraryComboBox.setItemText(0, QCoreApplication.translate("MainWindow", u"Piano", None))
        self.masterLibraryComboBox.setItemText(1, QCoreApplication.translate("MainWindow", u"Trumpet", None))
        self.masterLibraryComboBox.setItemText(2, QCoreApplication.translate("MainWindow", u"Custom", None))

        self.R4u.setText(QCoreApplication.translate("MainWindow", u"R4_u", None))
        self.R2d.setText(QCoreApplication.translate("MainWindow", u"R2_d", None))
        self.R3d.setText(QCoreApplication.translate("MainWindow", u"R3_d", None))
        self.R5u.setText(QCoreApplication.translate("MainWindow", u"R5_u", None))
        self.R3u.setText(QCoreApplication.translate("MainWindow", u"R3_u", None))
        self.R5d.setText(QCoreApplication.translate("MainWindow", u"R5_d", None))
        self.R1u.setText(QCoreApplication.translate("MainWindow", u"R1_u", None))
        self.R2u.setText(QCoreApplication.translate("MainWindow", u"R2_u", None))
        self.R1d.setText(QCoreApplication.translate("MainWindow", u"R2_d", None))
        self.R4d.setText(QCoreApplication.translate("MainWindow", u"R4_d", None))
        self.label_13.setText(QCoreApplication.translate("MainWindow", u"Right Hand", None))
        self.startingNote.setItemText(0, QCoreApplication.translate("MainWindow", u"A", None))
        self.startingNote.setItemText(1, QCoreApplication.translate("MainWindow", u"A#", None))
        self.startingNote.setItemText(2, QCoreApplication.translate("MainWindow", u"B", None))
        self.startingNote.setItemText(3, QCoreApplication.translate("MainWindow", u"C", None))
        self.startingNote.setItemText(4, QCoreApplication.translate("MainWindow", u"C#", None))
        self.startingNote.setItemText(5, QCoreApplication.translate("MainWindow", u"D", None))
        self.startingNote.setItemText(6, QCoreApplication.translate("MainWindow", u"D#", None))
        self.startingNote.setItemText(7, QCoreApplication.translate("MainWindow", u"E", None))
        self.startingNote.setItemText(8, QCoreApplication.translate("MainWindow", u"F", None))
        self.startingNote.setItemText(9, QCoreApplication.translate("MainWindow", u"F#", None))
        self.startingNote.setItemText(10, QCoreApplication.translate("MainWindow", u"G", None))
        self.startingNote.setItemText(11, QCoreApplication.translate("MainWindow", u"G#", None))

        self.startingOct.setItemText(0, QCoreApplication.translate("MainWindow", u"0", None))
        self.startingOct.setItemText(1, QCoreApplication.translate("MainWindow", u"1", None))
        self.startingOct.setItemText(2, QCoreApplication.translate("MainWindow", u"2", None))
        self.startingOct.setItemText(3, QCoreApplication.translate("MainWindow", u"3", None))
        self.startingOct.setItemText(4, QCoreApplication.translate("MainWindow", u"4", None))
        self.startingOct.setItemText(5, QCoreApplication.translate("MainWindow", u"5", None))
        self.startingOct.setItemText(6, QCoreApplication.translate("MainWindow", u"6", None))
        self.startingOct.setItemText(7, QCoreApplication.translate("MainWindow", u"7", None))
        self.startingOct.setItemText(8, QCoreApplication.translate("MainWindow", u"8", None))

        self.Tabs.setTabText(self.Tabs.indexOf(self.Master), QCoreApplication.translate("MainWindow", u"Master", None))
        self.L3d_2.setText(QCoreApplication.translate("MainWindow", u"L3_d", None))
        self.L2d_2.setText(QCoreApplication.translate("MainWindow", u"L2_d", None))
        self.L3u_2.setText(QCoreApplication.translate("MainWindow", u"L3_u", None))
        self.L4u_2.setText(QCoreApplication.translate("MainWindow", u"L4_u", None))
        self.L5d_2.setText(QCoreApplication.translate("MainWindow", u"L5_d", None))
        self.L4d_2.setText(QCoreApplication.translate("MainWindow", u"L4_d", None))
        self.L5u_2.setText(QCoreApplication.translate("MainWindow", u"L5_u", None))
        self.L2u_2.setText(QCoreApplication.translate("MainWindow", u"L2_u", None))
        self.L1u_2.setText(QCoreApplication.translate("MainWindow", u"L1_u", None))
        self.L1d_2.setText(QCoreApplication.translate("MainWindow", u"L1_d", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"Left Hand", None))
        self.R4u_2.setText(QCoreApplication.translate("MainWindow", u"R4_u", None))
        self.R2d_2.setText(QCoreApplication.translate("MainWindow", u"R2_d", None))
        self.R3d_2.setText(QCoreApplication.translate("MainWindow", u"R3_d", None))
        self.R5u_2.setText(QCoreApplication.translate("MainWindow", u"R5_u", None))
        self.R3u_2.setText(QCoreApplication.translate("MainWindow", u"R3_u", None))
        self.R5d_2.setText(QCoreApplication.translate("MainWindow", u"R5_d", None))
        self.R1u_2.setText(QCoreApplication.translate("MainWindow", u"R1_u", None))
        self.R2u_2.setText(QCoreApplication.translate("MainWindow", u"R2_u", None))
        self.R1d_2.setText(QCoreApplication.translate("MainWindow", u"R2_d", None))
        self.R4d_2.setText(QCoreApplication.translate("MainWindow", u"R4_d", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"Right Hand", None))
        self.label_17.setText(QCoreApplication.translate("MainWindow", u"Select Button for Piano", None))
        self.startingNote_2.setItemText(0, QCoreApplication.translate("MainWindow", u"A", None))
        self.startingNote_2.setItemText(1, QCoreApplication.translate("MainWindow", u"B", None))
        self.startingNote_2.setItemText(2, QCoreApplication.translate("MainWindow", u"C", None))
        self.startingNote_2.setItemText(3, QCoreApplication.translate("MainWindow", u"D", None))
        self.startingNote_2.setItemText(4, QCoreApplication.translate("MainWindow", u"E", None))
        self.startingNote_2.setItemText(5, QCoreApplication.translate("MainWindow", u"F", None))
        self.startingNote_2.setItemText(6, QCoreApplication.translate("MainWindow", u"G", None))

        self.startingOct_2.setItemText(0, QCoreApplication.translate("MainWindow", u"0", None))
        self.startingOct_2.setItemText(1, QCoreApplication.translate("MainWindow", u"1", None))
        self.startingOct_2.setItemText(2, QCoreApplication.translate("MainWindow", u"2", None))
        self.startingOct_2.setItemText(3, QCoreApplication.translate("MainWindow", u"3", None))
        self.startingOct_2.setItemText(4, QCoreApplication.translate("MainWindow", u"4", None))
        self.startingOct_2.setItemText(5, QCoreApplication.translate("MainWindow", u"5", None))
        self.startingOct_2.setItemText(6, QCoreApplication.translate("MainWindow", u"6", None))
        self.startingOct_2.setItemText(7, QCoreApplication.translate("MainWindow", u"7", None))
        self.startingOct_2.setItemText(8, QCoreApplication.translate("MainWindow", u"8", None))

        self.Tabs.setTabText(self.Tabs.indexOf(self.tab_2), QCoreApplication.translate("MainWindow", u"Piano", None))
        self.L3d_3.setText(QCoreApplication.translate("MainWindow", u"L3_d", None))
        self.L2d_3.setText(QCoreApplication.translate("MainWindow", u"L2_d", None))
        self.L3u_3.setText(QCoreApplication.translate("MainWindow", u"L3_u", None))
        self.L4u_3.setText(QCoreApplication.translate("MainWindow", u"L4_u", None))
        self.L5d_3.setText(QCoreApplication.translate("MainWindow", u"L5_d", None))
        self.L4d_3.setText(QCoreApplication.translate("MainWindow", u"L4_d", None))
        self.L5u_3.setText(QCoreApplication.translate("MainWindow", u"L5_u", None))
        self.L2u_3.setText(QCoreApplication.translate("MainWindow", u"L2_u", None))
        self.L1u_3.setText(QCoreApplication.translate("MainWindow", u"L1_u", None))
        self.L1d_3.setText(QCoreApplication.translate("MainWindow", u"L1_d", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"Left Hand", None))
        self.R2u_3.setText(QCoreApplication.translate("MainWindow", u"R2_u", None))
        self.R1d_3.setText(QCoreApplication.translate("MainWindow", u"R2_d", None))
        self.R4u_3.setText(QCoreApplication.translate("MainWindow", u"R4_u", None))
        self.R5d_3.setText(QCoreApplication.translate("MainWindow", u"R5_d", None))
        self.R5u_3.setText(QCoreApplication.translate("MainWindow", u"R5_u", None))
        self.R3u_3.setText(QCoreApplication.translate("MainWindow", u"R3_u", None))
        self.R3d_3.setText(QCoreApplication.translate("MainWindow", u"R3_d", None))
        self.R1u_3.setText(QCoreApplication.translate("MainWindow", u"R1_u", None))
        self.R2d_3.setText(QCoreApplication.translate("MainWindow", u"R2_d", None))
        self.R4d_3.setText(QCoreApplication.translate("MainWindow", u"R4_d", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"Right Hand", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Select Button for Trumpet", None))
        self.startingNote_3.setItemText(0, QCoreApplication.translate("MainWindow", u"A", None))
        self.startingNote_3.setItemText(1, QCoreApplication.translate("MainWindow", u"B", None))
        self.startingNote_3.setItemText(2, QCoreApplication.translate("MainWindow", u"C", None))
        self.startingNote_3.setItemText(3, QCoreApplication.translate("MainWindow", u"D", None))
        self.startingNote_3.setItemText(4, QCoreApplication.translate("MainWindow", u"E", None))
        self.startingNote_3.setItemText(5, QCoreApplication.translate("MainWindow", u"F", None))
        self.startingNote_3.setItemText(6, QCoreApplication.translate("MainWindow", u"G", None))

        self.startingOct_3.setItemText(0, QCoreApplication.translate("MainWindow", u"0", None))
        self.startingOct_3.setItemText(1, QCoreApplication.translate("MainWindow", u"1", None))
        self.startingOct_3.setItemText(2, QCoreApplication.translate("MainWindow", u"2", None))
        self.startingOct_3.setItemText(3, QCoreApplication.translate("MainWindow", u"3", None))
        self.startingOct_3.setItemText(4, QCoreApplication.translate("MainWindow", u"4", None))
        self.startingOct_3.setItemText(5, QCoreApplication.translate("MainWindow", u"5", None))
        self.startingOct_3.setItemText(6, QCoreApplication.translate("MainWindow", u"6", None))
        self.startingOct_3.setItemText(7, QCoreApplication.translate("MainWindow", u"7", None))
        self.startingOct_3.setItemText(8, QCoreApplication.translate("MainWindow", u"8", None))

        self.Tabs.setTabText(self.Tabs.indexOf(self.tab_3), QCoreApplication.translate("MainWindow", u"Trumpet", None))
        self.uploadButtonL_8.setText(QCoreApplication.translate("MainWindow", u"upload", None))
        self.uploadButtonR_5.setText(QCoreApplication.translate("MainWindow", u"upload", None))
        self.uploadButtonR_4.setText(QCoreApplication.translate("MainWindow", u"upload", None))
        self.L3d_5.setText(QCoreApplication.translate("MainWindow", u"L3_d", None))
        self.L5d_5.setText(QCoreApplication.translate("MainWindow", u"L5_d", None))
        self.uploadButtonL_7.setText(QCoreApplication.translate("MainWindow", u"upload", None))
        self.R1u_5.setText(QCoreApplication.translate("MainWindow", u"R1_u", None))
        self.R1d_5.setText(QCoreApplication.translate("MainWindow", u"R2_d", None))
        self.R4u_5.setText(QCoreApplication.translate("MainWindow", u"R4_u", None))
        self.uploadButtonR_2.setText(QCoreApplication.translate("MainWindow", u"upload", None))
        self.uploadButtonR_6.setText(QCoreApplication.translate("MainWindow", u"upload", None))
        self.R4d_5.setText(QCoreApplication.translate("MainWindow", u"R4_d", None))
        self.uploadButtonL_9.setText(QCoreApplication.translate("MainWindow", u"upload", None))
        self.L2u_5.setText(QCoreApplication.translate("MainWindow", u"L2_u", None))
        self.L4d_5.setText(QCoreApplication.translate("MainWindow", u"L4_d", None))
        self.R5u_5.setText(QCoreApplication.translate("MainWindow", u"R5_u", None))
        self.uploadButtonL.setText(QCoreApplication.translate("MainWindow", u"upload", None))
        self.uploadButtonL_6.setText(QCoreApplication.translate("MainWindow", u"upload", None))
        self.uploadButtonL_10.setText(QCoreApplication.translate("MainWindow", u"upload", None))
        self.uploadButtonR_1.setText(QCoreApplication.translate("MainWindow", u"upload", None))
        self.uploadButtonR_9.setText(QCoreApplication.translate("MainWindow", u"upload", None))
        self.R2u_5.setText(QCoreApplication.translate("MainWindow", u"R2_u", None))
        self.label_11.setText(QCoreApplication.translate("MainWindow", u"Left Hand", None))
        self.uploadButtonL_5.setText(QCoreApplication.translate("MainWindow", u"upload", None))
        self.R2d_5.setText(QCoreApplication.translate("MainWindow", u"R2_d", None))
        self.uploadButtonL_2.setText(QCoreApplication.translate("MainWindow", u"upload", None))
        self.R3d_5.setText(QCoreApplication.translate("MainWindow", u"R3_d", None))
        self.L4u_5.setText(QCoreApplication.translate("MainWindow", u"L4_u", None))
        self.L3u_5.setText(QCoreApplication.translate("MainWindow", u"L3_u", None))
        self.L1u_5.setText(QCoreApplication.translate("MainWindow", u"L1_u", None))
        self.uploadButtonR_7.setText(QCoreApplication.translate("MainWindow", u"upload", None))
        self.L2d_5.setText(QCoreApplication.translate("MainWindow", u"L2_d", None))
        self.R5d_5.setText(QCoreApplication.translate("MainWindow", u"R5_d", None))
        self.L1d_5.setText(QCoreApplication.translate("MainWindow", u"L1_d", None))
        self.uploadButtonL_3.setText(QCoreApplication.translate("MainWindow", u"upload", None))
        self.R3u_5.setText(QCoreApplication.translate("MainWindow", u"R3_u", None))
        self.uploadButtonL_4.setText(QCoreApplication.translate("MainWindow", u"upload", None))
        self.uploadButtonR_10.setText(QCoreApplication.translate("MainWindow", u"upload", None))
        self.uploadButtonR_3.setText(QCoreApplication.translate("MainWindow", u"upload", None))
        self.uploadButtonR_8.setText(QCoreApplication.translate("MainWindow", u"upload", None))
        self.L5u_5.setText(QCoreApplication.translate("MainWindow", u"L5_u", None))
        self.upload_label_R_2.setText(QCoreApplication.translate("MainWindow", u"No File Uploaded", None))
        self.upload_label_R_1.setText(QCoreApplication.translate("MainWindow", u"No File Uploaded", None))
        self.upload_label_R_3.setText(QCoreApplication.translate("MainWindow", u"No File Uploaded", None))
        self.upload_label_R_4.setText(QCoreApplication.translate("MainWindow", u"No File Uploaded", None))
        self.upload_label_R_5.setText(QCoreApplication.translate("MainWindow", u"No File Uploaded", None))
        self.upload_label_R_6.setText(QCoreApplication.translate("MainWindow", u"No File Uploaded", None))
        self.upload_label_R_7.setText(QCoreApplication.translate("MainWindow", u"No File Uploaded", None))
        self.upload_label_R_8.setText(QCoreApplication.translate("MainWindow", u"No File Uploaded", None))
        self.upload_label_R_9.setText(QCoreApplication.translate("MainWindow", u"No File Uploaded", None))
        self.upload_label_R_10.setText(QCoreApplication.translate("MainWindow", u"No File Uploaded", None))
        self.upload_label_L_1.setText(QCoreApplication.translate("MainWindow", u"No File Uploaded", None))
        self.upload_label_L_2.setText(QCoreApplication.translate("MainWindow", u"No File Uploaded", None))
        self.upload_label_L_3.setText(QCoreApplication.translate("MainWindow", u"No File Uploaded", None))
        self.upload_label_L_4.setText(QCoreApplication.translate("MainWindow", u"No File Uploaded", None))
        self.upload_label_L_5.setText(QCoreApplication.translate("MainWindow", u"No File Uploaded", None))
        self.upload_label_L_6.setText(QCoreApplication.translate("MainWindow", u"No File Uploaded", None))
        self.upload_label_L_7.setText(QCoreApplication.translate("MainWindow", u"No File Uploaded", None))
        self.upload_label_L_8.setText(QCoreApplication.translate("MainWindow", u"No File Uploaded", None))
        self.upload_label_L_9.setText(QCoreApplication.translate("MainWindow", u"No File Uploaded", None))
        self.upload_label_L_10.setText(QCoreApplication.translate("MainWindow", u"No File Uploaded", None))
        self.label_10.setText(QCoreApplication.translate("MainWindow", u"Right Hand", None))
        self.Tabs.setTabText(self.Tabs.indexOf(self.tab), QCoreApplication.translate("MainWindow", u"Upload", None))
        self.label_MasterVol.setText(QCoreApplication.translate("MainWindow", u"Master Volume", None))
        self.label_PianoVol.setText(QCoreApplication.translate("MainWindow", u"Piano Volume", None))
        self.label_TrumpetVol.setText(QCoreApplication.translate("MainWindow", u"Trumpet Volume", None))
        self.label_19.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.label_20.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.label_21.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.recordButton.setText(QCoreApplication.translate("MainWindow", u"Start Recording", None))
        self.stopButton.setText(QCoreApplication.translate("MainWindow", u"Stop Recording", None))
        self.menumain.setTitle(QCoreApplication.translate("MainWindow", u"main", None))
    # retranslateUi

