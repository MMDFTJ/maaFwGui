# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'untitled.ui'
##
## Created by: Qt User Interface Compiler version 6.4.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QFrame, QGridLayout, QSizePolicy,
    QSpacerItem, QWidget)

from qfluentwidgets import (BodyLabel, PushButton, ScrollArea)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(1118, 744)
        self.frame = QFrame(Form)
        self.frame.setObjectName(u"frame")
        self.frame.setGeometry(QRect(50, 70, 311, 52))
        self.frame.setStyleSheet(u"background-color: white;\n"
"border: 1px solid #d3d3d3;")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.gridLayout_2 = QGridLayout(self.frame)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.BodyLabel = BodyLabel(self.frame)
        self.BodyLabel.setObjectName(u"BodyLabel")
        self.BodyLabel.setStyleSheet(u"border: none;")
        self.BodyLabel.setProperty("pixelFontSize", 18)

        self.gridLayout.addWidget(self.BodyLabel, 0, 0, 1, 1)

        self.PushButton = PushButton(self.frame)
        self.PushButton.setObjectName(u"PushButton")

        self.gridLayout.addWidget(self.PushButton, 0, 2, 1, 1)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer, 0, 1, 1, 1)


        self.gridLayout_2.addLayout(self.gridLayout, 0, 0, 1, 1)

        self.frame_2 = QFrame(Form)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setGeometry(QRect(420, 80, 671, 54))
        self.frame_2.setStyleSheet(u"background-color: white;\n"
"border: 1px solid #d3d3d3;")
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.gridLayout_4 = QGridLayout(self.frame_2)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.gridLayout_3 = QGridLayout()
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.PushButton_2 = PushButton(self.frame_2)
        self.PushButton_2.setObjectName(u"PushButton_2")

        self.gridLayout_3.addWidget(self.PushButton_2, 0, 2, 1, 1)

        self.BodyLabel_2 = BodyLabel(self.frame_2)
        self.BodyLabel_2.setObjectName(u"BodyLabel_2")
        self.BodyLabel_2.setStyleSheet(u"border: none;")
        self.BodyLabel_2.setProperty("pixelFontSize", 18)

        self.gridLayout_3.addWidget(self.BodyLabel_2, 0, 0, 1, 1)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_3.addItem(self.horizontalSpacer_2, 0, 1, 1, 1)


        self.gridLayout_4.addLayout(self.gridLayout_3, 0, 0, 1, 1)

        self.PushButton_3 = PushButton(Form)
        self.PushButton_3.setObjectName(u"PushButton_3")
        self.PushButton_3.setGeometry(QRect(500, 240, 102, 32))
        self.frame_3 = QFrame(Form)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setGeometry(QRect(40, 140, 331, 521))
        self.frame_3.setStyleSheet(u".QFrame{\n"
"background-color: white;\n"
"border: 1px solid #d3d3d3;\n"
"}")
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.gridLayout_6 = QGridLayout(self.frame_3)
        self.gridLayout_6.setObjectName(u"gridLayout_6")
        self.gridLayout_5 = QGridLayout()
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.BodyLabel_3 = BodyLabel(self.frame_3)
        self.BodyLabel_3.setObjectName(u"BodyLabel_3")
        self.BodyLabel_3.setMaximumSize(QSize(16777215, 30))
        self.BodyLabel_3.setStyleSheet(u"border:none;")
        self.BodyLabel_3.setProperty("pixelFontSize", 18)

        self.gridLayout_5.addWidget(self.BodyLabel_3, 0, 0, 1, 1)

        self.line_2 = QFrame(self.frame_3)
        self.line_2.setObjectName(u"line_2")
        self.line_2.setFrameShape(QFrame.HLine)
        self.line_2.setFrameShadow(QFrame.Sunken)

        self.gridLayout_5.addWidget(self.line_2, 1, 0, 1, 1)

        self.widget = QWidget(self.frame_3)
        self.widget.setObjectName(u"widget")
        self.widget.setStyleSheet(u".QWidget{\n"
"background-color: white;\n"
"border: 1px solid #d3d3d3;\n"
"}")
        self.ScrollArea = ScrollArea(self.widget)
        self.ScrollArea.setObjectName(u"ScrollArea")
        self.ScrollArea.setGeometry(QRect(0, 0, 311, 461))
        self.ScrollArea.setStyleSheet(u"border:none;")
        self.ScrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 311, 461))
        self.gridLayout_s = QGridLayout(self.scrollAreaWidgetContents)
        self.gridLayout_s.setObjectName(u"gridLayout_s")
        self.ScrollArea.setWidget(self.scrollAreaWidgetContents)

        self.gridLayout_5.addWidget(self.widget, 2, 0, 1, 1)


        self.gridLayout_6.addLayout(self.gridLayout_5, 0, 0, 1, 1)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.BodyLabel.setText(QCoreApplication.translate("Form", u"\u8c03\u5ea6\u5668", None))
        self.PushButton.setText(QCoreApplication.translate("Form", u"\u542f\u52a8", None))
        self.PushButton_2.setText(QCoreApplication.translate("Form", u"\u81ea\u52a8\u6eda\u52a8", None))
        self.BodyLabel_2.setText(QCoreApplication.translate("Form", u"\u65e5\u5fd7", None))
        self.PushButton_3.setText(QCoreApplication.translate("Form", u"Push button", None))
        self.BodyLabel_3.setText(QCoreApplication.translate("Form", u"\u4efb\u52a1\u5217\u8868", None))
    # retranslateUi

