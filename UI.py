# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'untitledQVrhGp.ui'
##
## Created by: Qt User Interface Compiler version 5.14.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################
from PySide2.QtCharts import QtCharts
from PySide2.QtCore import (QCoreApplication, QMetaObject, QObject, QPoint,
    QRect, QSize, QUrl, Qt, QTimer, QDate)
from PySide2.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont,
    QFontDatabase, QIcon, QLinearGradient, QPalette, QPainter, QPixmap,
    QRadialGradient, QPainter, QPen)
from PySide2.QtWidgets import *

import Resources

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        series = QtCharts.QPieSeries()

        QFontDatabase.addApplicationFont(":/fonts/Roboto-Medium.ttf")
        if MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1070, 600)
        MainWindow.setMaximumSize(QSize(1070, 600))
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(10, 10, 10, 10)
        self.frame = QFrame(self.centralwidget)
        self.frame.setObjectName(u"frame")
        self.frame.setMinimumSize(QSize(1050, 580))
        self.frame.setMaximumSize(QSize(1050, 580))
        self.frame.setStyleSheet(u"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 	rgb(185, 43, 39), stop:1 rgb(66, 134, 244));\n"
"border-radius: 10px")
        self.frame.setFrameShape(QFrame.NoFrame)
        self.frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.frame)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.TitleFrame = QFrame(self.frame)
        self.TitleFrame.setObjectName(u"TitleFrame")
        self.TitleFrame.setMinimumSize(QSize(0, 0))
        self.TitleFrame.setMaximumSize(QSize(16777215, 35))
        self.TitleFrame.setStyleSheet(u"background-color: none;")
        self.TitleFrame.setFrameShape(QFrame.StyledPanel)
        self.TitleFrame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.TitleFrame)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.topTitle = QFrame(self.TitleFrame)
        self.topTitle.setObjectName(u"topTitle")
        self.topTitle.setFrameShape(QFrame.StyledPanel)
        self.topTitle.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.topTitle)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(15, 0, 0, 0)
        self.title = QLabel(self.topTitle)
        self.title.setObjectName(u"title")
        font = QFont()
        font.setFamily(u"Roboto")
        font.setPointSize(14)
        self.title.setFont(font)
        self.title.setStyleSheet(u"color: rgb(220, 220, 220);")

        self.verticalLayout_3.addWidget(self.title)


        self.horizontalLayout.addWidget(self.topTitle)

        self.topButtons = QFrame(self.TitleFrame)
        self.topButtons.setObjectName(u"topButtons")
        self.topButtons.setMaximumSize(QSize(100, 16777215))
        self.topButtons.setLayoutDirection(Qt.LeftToRight)
        self.topButtons.setFrameShape(QFrame.StyledPanel)
        self.topButtons.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.topButtons)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.btnMinimize = QPushButton(self.topButtons)
        self.btnMinimize.setObjectName(u"btnMinimize")
        self.btnMinimize.setMinimumSize(QSize(17, 17))
        self.btnMinimize.setMaximumSize(QSize(17, 17))
        self.btnMinimize.setLayoutDirection(Qt.LeftToRight)
        self.btnMinimize.setStyleSheet(u"QPushButton{\n"
"	border: none;\n"
"	border-radius: 8px;\n"
"	background-color: rgb(255, 170, 0);\n"
"}\n"
"QPushButton:hover{	\n"
"	background-color: rgba(255, 170, 0, 150);\n"
"}")

        self.horizontalLayout_2.addWidget(self.btnMinimize)

        self.buttonMinimize = QPushButton(self.topButtons)
        self.buttonMinimize.setObjectName(u"buttonMinimize")
        self.buttonMinimize.setMinimumSize(QSize(17, 17))
        self.buttonMinimize.setMaximumSize(QSize(17, 17))
        self.buttonMinimize.setLayoutDirection(Qt.RightToLeft)
        self.buttonMinimize.setStyleSheet(u"QPushButton{\n"
"	border: none;\n"
"	border-radius: 8px;\n"
"	background-color: rgb(255, 0, 0);\n"
"}\n"
"QPushButton:hover{	\n"
"	background-color: rgba(255, 0, 0, 150);\n"
"}")

        self.horizontalLayout_2.addWidget(self.buttonMinimize)


        self.horizontalLayout.addWidget(self.topButtons)


        self.verticalLayout_2.addWidget(self.TitleFrame)

        self.OptionFrame = QFrame(self.frame)
        self.OptionFrame.setObjectName(u"OptionFrame")
        self.OptionFrame.setMaximumSize(QSize(16777215, 16777215))
        self.OptionFrame.setStyleSheet(u"background-color: none;")
        self.OptionFrame.setFrameShape(QFrame.StyledPanel)
        self.OptionFrame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_4 = QVBoxLayout(self.OptionFrame)
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.frame_2 = QFrame(self.OptionFrame)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setMaximumSize(QSize(16777215, 100))
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.frame_2)
        self.horizontalLayout_3.setSpacing(9)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.pushButton_7 = QPushButton(self.frame_2)
        self.pushButton_7.setObjectName(u"pushButton_7")
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_7.sizePolicy().hasHeightForWidth())
        self.pushButton_7.setSizePolicy(sizePolicy)
        self.pushButton_7.setMinimumSize(QSize(120, 31))
        self.pushButton_7.setMaximumSize(QSize(120, 31))
        font1 = QFont()
        font1.setFamily(u"Roboto")
        font1.setPointSize(10)
        self.pushButton_7.setFont(font1)
        self.pushButton_7.setStyleSheet(u"QPushButton{\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:0, x1:1, y2:0, stop:0 	rgb(43, 192, 228), stop:1 rgb(234, 236, 198));\n"
"\n"
"}\n"
"\n"
"QPushButton:hover{	\n"
"	background-color: qlineargradient(spread:pad, x1:0, y1:0, x1:1, y2:0, stop:0 	rgba(43, 192, 228, 150), stop:1 rgba(234, 236, 198, 150));\n"
"}\n"
"\n"
"")

        self.horizontalLayout_3.addWidget(self.pushButton_7)

        self.pushButton_10 = QPushButton(self.frame_2)
        self.pushButton_10.setObjectName(u"pushButton_10")
        sizePolicy.setHeightForWidth(self.pushButton_10.sizePolicy().hasHeightForWidth())
        self.pushButton_10.setSizePolicy(sizePolicy)
        self.pushButton_10.setMinimumSize(QSize(120, 31))
        self.pushButton_10.setMaximumSize(QSize(120, 31))
        self.pushButton_10.setFont(font1)
        self.pushButton_10.setStyleSheet(u"QPushButton{\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:0, x1:1, y2:0, stop:0 	rgb(43, 192, 228), stop:1 rgb(234, 236, 198));\n"
"\n"
"}\n"
"\n"
"QPushButton:hover{	\n"
"	background-color: qlineargradient(spread:pad, x1:0, y1:0, x1:1, y2:0, stop:0 	rgba(43, 192, 228, 150), stop:1 rgba(234, 236, 198, 150));\n"
"}")

        self.horizontalLayout_3.addWidget(self.pushButton_10)

        self.pushButton_11 = QPushButton(self.frame_2)
        self.pushButton_11.setObjectName(u"pushButton_11")
        sizePolicy.setHeightForWidth(self.pushButton_11.sizePolicy().hasHeightForWidth())
        self.pushButton_11.setSizePolicy(sizePolicy)
        self.pushButton_11.setMinimumSize(QSize(120, 31))
        self.pushButton_11.setMaximumSize(QSize(120, 31))
        self.pushButton_11.setFont(font1)
        self.pushButton_11.setStyleSheet(u"QPushButton{\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:0, x1:1, y2:0, stop:0 	rgb(43, 192, 228), stop:1 rgb(234, 236, 198));\n"
"\n"
"}\n"
"\n"
"QPushButton:hover{	\n"
"	background-color: qlineargradient(spread:pad, x1:0, y1:0, x1:1, y2:0, stop:0 	rgba(43, 192, 228, 150), stop:1 rgba(234, 236, 198, 150));\n"
"}")

        self.horizontalLayout_3.addWidget(self.pushButton_11)

        self.pushButton_9 = QPushButton(self.frame_2)
        self.pushButton_9.setObjectName(u"pushButton_9")
        sizePolicy.setHeightForWidth(self.pushButton_9.sizePolicy().hasHeightForWidth())
        self.pushButton_9.setSizePolicy(sizePolicy)
        self.pushButton_9.setMinimumSize(QSize(120, 31))
        self.pushButton_9.setMaximumSize(QSize(120, 31))
        self.pushButton_9.setFont(font1)
        self.pushButton_9.setStyleSheet(u"QPushButton{\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:0, x1:1, y2:0, stop:0 	rgb(43, 192, 228), stop:1 rgb(234, 236, 198));\n"
"\n"
"}\n"
"\n"
"QPushButton:hover{	\n"
"	background-color: qlineargradient(spread:pad, x1:0, y1:0, x1:1, y2:0, stop:0 	rgba(43, 192, 228, 150), stop:1 rgba(234, 236, 198, 150));\n"
"}")

        self.horizontalLayout_3.addWidget(self.pushButton_9)

        self.pushButton_8 = QPushButton(self.frame_2)
        self.pushButton_8.setObjectName(u"pushButton_8")
        sizePolicy.setHeightForWidth(self.pushButton_8.sizePolicy().hasHeightForWidth())
        self.pushButton_8.setSizePolicy(sizePolicy)
        self.pushButton_8.setMinimumSize(QSize(120, 31))
        self.pushButton_8.setMaximumSize(QSize(120, 31))
        self.pushButton_8.setFont(font1)
        self.pushButton_8.setStyleSheet(u"QPushButton{\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:0, x1:1, y2:0, stop:0 	rgb(43, 192, 228), stop:1 rgb(234, 236, 198));\n"
"\n"
"}\n"
"\n"
"QPushButton:hover{	\n"
"	background-color: qlineargradient(spread:pad, x1:0, y1:0, x1:1, y2:0, stop:0 	rgba(43, 192, 228, 150), stop:1 rgba(234, 236, 198, 150));\n"
"}")

        self.horizontalLayout_3.addWidget(self.pushButton_8)


        self.verticalLayout_4.addWidget(self.frame_2)

        self.frame_3 = QFrame(self.OptionFrame)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setMinimumSize(QSize(0, 450))
        self.frame_3.setMaximumSize(QSize(16777215, 16777215))
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_4 = QHBoxLayout(self.frame_3)
        self.horizontalLayout_4.setSpacing(0)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(10, 0, 10, 0)
        self.frame_4 = QFrame(self.frame_3)
        self.frame_4.setMaximumSize(QSize(300, 16777215))
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setFrameShape(QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Raised)
        self.label_4 = QLabel(self.frame_4)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(130, 0, 60, 30))
        self.label_4.setMaximumSize(QSize(60, 30))
        font2 = QFont()
        font2.setFamily(u"Roboto")
        font2.setPointSize(12)
        font2.setBold(False)
        font2.setWeight(50)
        self.label_4.setFont(font2)
        self.label_4.setStyleSheet(u"background-color: rgb(253, 255, 255, 0);\n"
"color: rgb(220, 220, 220);")
        self.label_4.setTextFormat(Qt.AutoText)
        self.label_4.setScaledContents(False)
        self.label_4.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.pushButton_14 = QPushButton(self.frame_4)
        self.pushButton_14.setObjectName(u"pushButton_14")
        self.pushButton_14.setGeometry(QRect(10, 80, 75, 23))
        self.pushButton_14.setFont(font1)
        self.pushButton_14.setStyleSheet(u"QPushButton{\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:0, x1:1, y2:0, stop:0 	rgb(43, 192, 228), stop:1 rgb(234, 236, 198));\n"
"\n"
"}\n"
"\n"
"QPushButton:hover{	\n"
"	background-color: qlineargradient(spread:pad, x1:0, y1:0, x1:1, y2:0, stop:0 	rgba(43, 192, 228, 150), stop:1 rgba(234, 236, 198, 150));\n"
"}\n"
"")
        self.scrollBar1 = QScrollBar()
        self.scrollBar1.setStyleSheet(u"QScrollBar:vertical{\n"
                                      "	border:none;\n"
                                      "	background-color: rgb(253, 255, 255, 20);\n"
                                      "	border-radius:0px;\n"
                                      "	width:15px;\n"
                                      "	margin: 15px 0 15px 0;\n"
                                      "}\n"
                                      "\n"
                                      "QScrollBar::handle:vertical{\n"
                                      "	background-color: rgb(59,59,90);\n"
                                      "	min-height:10px;\n"
                                      "	border-radius:7px;\n"
                                      "}\n"
                                      "\n"
                                      "QScrollBar::sub-line:vertical{\n"
                                      "      border: none;\n"
                                      "      background: none;\n"
                                      "}\n"
                                      "\n"
                                      "QScrollBar::add-line:vertical{\n"
                                      "      border: none;\n"
                                      "      background: none;\n"
                                      "}\n"
                                      "\n"
                                      "")

        self.textBrowser_4 = QTextBrowser(self.frame_4)
        self.textBrowser_4.setObjectName(u"textBrowser_4")
        self.textBrowser_4.setGeometry(QRect(10, 110, 280, 320))
        self.textBrowser_4.setFont(font1)
        self.textBrowser_4.setVerticalScrollBar(self.scrollBar1)
        self.textBrowser_4.setStyleSheet(u"QWidget{\n"
                                         "	background-color: rgb(253, 255, 255, 99);\n"
                                         "}\n"
                                         "\n"
                                         "\n"
                                         "\n"
                                         "\n"
                                         "")
        self.textBrowser_4.setVerticalScrollBarPolicy(Qt.ScrollBarAsNeeded)
        self.btnMinimize_2 = QPushButton(self.frame_4)
        self.btnMinimize_2.setObjectName(u"btnMinimize_2")
        self.btnMinimize_2.setGeometry(QRect(201, 7, 17, 17))
        self.btnMinimize_2.setMinimumSize(QSize(17, 17))
        self.btnMinimize_2.setMaximumSize(QSize(17, 17))
        self.btnMinimize_2.setLayoutDirection(Qt.LeftToRight)
        self.btnMinimize_2.setStyleSheet(u"QPushButton{\n"
"	border: none;\n"
"	border-radius: 8px;\n"
"	background-color: rgb(253, 255, 255, 99);\n"
"}\n"
"QPushButton:hover{	\n"
"	background-color: rgba(253, 255, 255, 50);\n"
"}\n"
"QPushButton:pressed{\n"
"	background-color: rgb(59,59,90);\n"
"}")

        self.horizontalLayout_4.addWidget(self.frame_4)

        self.frame_5 = QFrame(self.frame_3)
        self.frame_5.setObjectName(u"frame_5")
        self.frame_5.setFrameShape(QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QFrame.Raised)
        self.dateEdit_3 = QDateEdit(self.frame_5)
        self.dateEdit_3.setObjectName(u"dateEdit_3")
        self.dateEdit_3.setGeometry(QRect(70, 0, 103, 30))
        self.dateEdit_3.setMaximumSize(QSize(120, 30))
        self.dateEdit_3.setFont(font1)
        self.dateEdit_3.setStyleSheet(u"QDateEdit{\n"
"	background-color: qlineargradient(spread:pad, x1:0, y1:0, x1:1, y2:0, stop:0 	rgb(43, 192, 228), stop:1 rgb(234, 236, 198));\n"
"	border-width:5px;\n"
"}\n"
"\n"
"QDateEdit:hover{	\n"
"	background-color: qlineargradient(spread:pad, x1:0, y1:0, x1:1, y2:0, stop:0 	rgba(43, 192, 228, 150), stop:1 rgba(234, 236, 198, 150));\n"
"}\n"
"\n"
"QDateEdit::drop-down {\n"
"}")
        self.dateEdit_3.setAlignment(Qt.AlignCenter)
        self.dateEdit_3.setButtonSymbols(QAbstractSpinBox.NoButtons)
        self.dateEdit_3.setCalendarPopup(True)
        self.label_3 = QLabel(self.frame_5)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(0, 0, 56, 30))
        self.label_3.setMaximumSize(QSize(56, 30))
        self.label_3.setFont(font2)
        self.label_3.setLayoutDirection(Qt.LeftToRight)
        self.label_3.setStyleSheet(u"background-color: rgb(253, 255, 255, 0);\n"
"color: rgb(220, 220, 220);")
        self.label_3.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.pushButton_15 = QPushButton(self.frame_5)
        self.pushButton_15.setObjectName(u"pushButton_15")
        self.pushButton_15.setGeometry(QRect(10, 80, 75, 23))
        self.pushButton_15.setFont(font1)
        self.pushButton_15.setStyleSheet(u"QPushButton{\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:0, x1:1, y2:0, stop:0 	rgb(43, 192, 228), stop:1 rgb(234, 236, 198));\n"
"\n"
"}\n"
"\n"
"QPushButton:hover{	\n"
"	background-color: qlineargradient(spread:pad, x1:0, y1:0, x1:1, y2:0, stop:0 	rgba(43, 192, 228, 150), stop:1 rgba(234, 236, 198, 150));\n"
"}")

        self.graphicsView = QtCharts.QChartView(self.frame_5)
        self.graphicsView.setObjectName(u"graphicsView")
        self.graphicsView.setGeometry(QRect(10, 110, 350, 320))
        self.graphicsView.setFont(font1)
        self.graphicsView.setStyleSheet(u"QChartView{\n"
"	background-color: rgb(253, 255, 255, 99);\n"
"}\n"
"")

        self.horizontalLayout_4.addWidget(self.frame_5)

        self.frame_6 = QFrame(self.frame_3)
        self.frame_6.setObjectName(u"frame_6")
        self.frame_6.setFrameShape(QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QFrame.Raised)
        self.label_5 = QLabel(self.frame_6)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(0, 0, 56, 30))
        self.label_5.setMaximumSize(QSize(56, 30))
        self.label_5.setFont(font2)
        self.label_5.setStyleSheet(u"color: rgb(220, 220, 220);")
        self.label_5.setTextFormat(Qt.AutoText)
        self.label_5.setScaledContents(False)
        self.label_5.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.dateEdit_4 = QDateEdit(self.frame_6)
        self.dateEdit_4.setObjectName(u"dateEdit_4")
        self.dateEdit_4.setGeometry(QRect(70, 0, 103, 30))
        self.dateEdit_4.setMaximumSize(QSize(120, 30))
        self.dateEdit_4.setFont(font1)
        self.dateEdit_4.setStyleSheet(u"QDateEdit{\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:0, x1:1, y2:0, stop:0 	rgb(43, 192, 228), stop:1 rgb(234, 236, 198));\n"
"\n"
"}\n"
"\n"
"QDateEdit:hover{	\n"
"	background-color: qlineargradient(spread:pad, x1:0, y1:0, x1:1, y2:0, stop:0 	rgba(43, 192, 228, 150), stop:1 rgba(234, 236, 198, 150));\n"
"}")
        self.dateEdit_4.setAlignment(Qt.AlignCenter)
        self.dateEdit_4.setButtonSymbols(QAbstractSpinBox.NoButtons)
        self.dateEdit_4.setCalendarPopup(True)
        self.pushButton_16 = QPushButton(self.frame_6)
        self.pushButton_16.setObjectName(u"pushButton_16")
        self.pushButton_16.setGeometry(QRect(10, 80, 75, 23))
        self.pushButton_16.setFont(font1)
        self.pushButton_16.setStyleSheet(u"QPushButton{\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:0, x1:1, y2:0, stop:0 	rgb(43, 192, 228), stop:1 rgb(234, 236, 198));\n"
"\n"
"}\n"
"\n"
"QPushButton:hover{	\n"
"	background-color: qlineargradient(spread:pad, x1:0, y1:0, x1:1, y2:0, stop:0 	rgba(43, 192, 228, 150), stop:1 rgba(234, 236, 198, 150));\n"
"}")


        self.graphicsView_2 = QtCharts.QChartView(self.frame_6)
        self.graphicsView_2.setObjectName(u"graphicsView_2")
        self.graphicsView_2.setGeometry(QRect(10, 110, 350, 320))
        self.graphicsView_2.setFont(font1)
        self.graphicsView_2.setStyleSheet(u"QChartView{\n"
                                          "	background-color: rgb(253, 255, 255, 99);\n"
                                          "}\n"
                                          "")

        self.horizontalLayout_4.addWidget(self.frame_6)


        self.verticalLayout_4.addWidget(self.frame_3)


        self.verticalLayout_2.addWidget(self.OptionFrame)

        self.frame_7 = QFrame(self.frame)
        self.frame_7.setObjectName(u"frame_7")
        self.frame_7.setFrameShape(QFrame.StyledPanel)
        self.frame_7.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_5 = QHBoxLayout(self.frame_7)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(-1, 0, -1, 0)
        self.frame_8 = QFrame(self.frame_7)
        self.frame_8.setObjectName(u"frame_8")
        self.frame_8.setStyleSheet(u"background-color: none;")
        self.frame_8.setFrameShape(QFrame.StyledPanel)
        self.frame_8.setFrameShadow(QFrame.Raised)
        self.verticalLayout_5 = QVBoxLayout(self.frame_8)
        self.verticalLayout_5.setSpacing(2)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.label = QLabel(self.frame_8)
        self.label.setObjectName(u"label")
        self.label.setMaximumSize(QSize(16777215, 20))
        font3 = QFont()
        font3.setFamily(u"Roboto")
        font3.setPointSize(13)
        font3.setItalic(True)
        self.label.setFont(font3)
        self.label.setStyleSheet(u"color: rgb(220, 220, 220);\n"
"background-color: none;\n"
"border-radius: 10px\n"
"")
        self.label.setTextFormat(Qt.AutoText)
        self.label.setAlignment(Qt.AlignCenter)

        self.verticalLayout_5.addWidget(self.label)

        self.label_2 = QLabel(self.frame_8)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setMaximumSize(QSize(16777215, 20))
        font4 = QFont()
        font4.setFamily(u"Roboto")
        font4.setPointSize(11)
        self.label_2.setFont(font4)
        self.label_2.setStyleSheet(u"color: rgb(220, 220, 220);\n"
"background-color: none;\n"
"border-radius: 10px\n"
"")
        self.label_2.setTextFormat(Qt.AutoText)
        self.label_2.setAlignment(Qt.AlignCenter)

        self.verticalLayout_5.addWidget(self.label_2)


        self.horizontalLayout_5.addWidget(self.frame_8)


        self.verticalLayout_2.addWidget(self.frame_7)


        self.verticalLayout.addWidget(self.frame)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.title.setText(QCoreApplication.translate("MainWindow", u"Welcome to TimeManager", None))
#if QT_CONFIG(tooltip)
        self.btnMinimize.setToolTip(QCoreApplication.translate("MainWindow", u"Minimize", None))
#endif // QT_CONFIG(tooltip)
        self.btnMinimize.setText("")
#if QT_CONFIG(tooltip)
        self.buttonMinimize.setToolTip(QCoreApplication.translate("MainWindow", u"Close", None))
#endif // QT_CONFIG(tooltip)
        self.buttonMinimize.setText("")
        self.pushButton_7.setText(QCoreApplication.translate("MainWindow", u"1 Day", None))
        self.pushButton_10.setText(QCoreApplication.translate("MainWindow", u"3 Day", None))
        self.pushButton_11.setText(QCoreApplication.translate("MainWindow", u"7 Day", None))
        self.pushButton_9.setText(QCoreApplication.translate("MainWindow", u"1 Month", None))
        self.pushButton_8.setText(QCoreApplication.translate("MainWindow", u"1 Year", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"Custom:", None))
        self.pushButton_14.setText(QCoreApplication.translate("MainWindow", u"Hide", None))
        self.btnMinimize_2.setText("")
        self.dateEdit_3.setDisplayFormat(QCoreApplication.translate("MainWindow", u"yyyy/MM/dd", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"From:", None))
        self.pushButton_15.setText(QCoreApplication.translate("MainWindow", u"Hide", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"Untill:", None))
        self.dateEdit_4.setDisplayFormat(QCoreApplication.translate("MainWindow", u"yyyy/MM/dd", None))
        self.pushButton_16.setText(QCoreApplication.translate("MainWindow", u"Hide", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"\u201cTime flies like an arrow; fruit flies like a banana.\u201d", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"\u2015 Anthony G. Oettinger ", None))
    # retranslateUi


