import sys
import os
import shutil
import time
import numpy as np
import pandas as pd
import json
import mysql.connector as mysql
import cv2
import PySide6
import numpy as np
import pandas as pd
from PySide6 import *
from kalori import *
from PySide6.QtWidgets import *
from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtGui import QFont,QIcon,QRegularExpressionValidator

class MyWidget(QWidget):
    def __init__(self,parent=None):
        super(MyWidget,self).__init__(parent)
      
        self.horizontalLayout = QtWidgets.QHBoxLayout(self)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.frame = QtWidgets.QFrame(self)
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.frame)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.label_11 = QtWidgets.QLabel(self.frame)
        self.label_11.setMinimumSize(QtCore.QSize(150, 150))
        self.label_11.setMaximumSize(QtCore.QSize(150, 150))
        self.label_11.setText("")
        self.label_11.setPixmap(QtGui.QPixmap("images/Anne Yoğurdu.jpg"))
        self.label_11.setScaledContents(True)
        self.label_11.setObjectName("label_11")
        self.horizontalLayout_4.addWidget(self.label_11)
        self.horizontalLayout.addWidget(self.frame, 0, QtCore.Qt.AlignLeft)
        self.frame_2 = QtWidgets.QFrame(self)
        self.frame_2.setMinimumSize(QtCore.QSize(150, 150))
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.karb = QtWidgets.QFrame(self.frame_2)
        self.karb.setGeometry(QtCore.QRect(35, 20, 110, 110))
        self.karb.setStyleSheet("QFrame{\n"
"    \n"
"    background-color: qconicalgradient(cx:0.5, cy:0.5, angle:90, stop:0.711 rgba(0, 0, 0, 0), stop:0.712 rgba(85, 170, 255, 255));\n"
"    border-radius:55px;\n"
"}")
        self.karb.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.karb.setFrameShadow(QtWidgets.QFrame.Raised)
        self.karb.setObjectName("karb")
        self.protein = QtWidgets.QFrame(self.frame_2)
        self.protein.setGeometry(QtCore.QRect(30, 15, 110, 110))
        self.protein.setStyleSheet("QFrame{\n"
"    \n"
"    background-color: qconicalgradient(cx:0.5, cy:0.5, angle:90, stop:0.174692 rgba(0, 0, 0, 0), stop:0.781635 rgba(0, 170, 0, 255));\n"
"    border-radius:55px;\n"
"}")
        self.protein.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.protein.setFrameShadow(QtWidgets.QFrame.Raised)
        self.protein.setObjectName("protein")
        self.yag = QtWidgets.QFrame(self.frame_2)
        self.yag.setGeometry(QtCore.QRect(30, 17, 110, 110))
        self.yag.setStyleSheet("QFrame{\n"
"    \n"
"    background-color: qconicalgradient(cx:0.5, cy:0.5, angle:90, stop:0.246835 rgba(0, 0, 0, 0), stop:0.724684 rgba(255, 85, 255, 255));\n"
"    border-radius:55px;\n"
"}")
        self.yag.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.yag.setFrameShadow(QtWidgets.QFrame.Raised)
        self.yag.setObjectName("yag")
        self.front = QtWidgets.QFrame(self.frame_2)
        self.front.setGeometry(QtCore.QRect(40, 25, 90, 90))
        self.front.setStyleSheet("QFrame{\n"
"    \n"
"    background-color: rgb(255,255,255);\n"
"    border-radius:45px;\n"
"}")
        self.front.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.front.setFrameShadow(QtWidgets.QFrame.Raised)
        self.front.setObjectName("front")
        self.label_12 = QtWidgets.QLabel(self.front)
        self.label_12.setGeometry(QtCore.QRect(0, 20, 91, 20))
        self.label_12.setText("")
        self.label_12.setObjectName("label_12")
        self.label_13 = QtWidgets.QLabel(self.front)
        self.label_13.setGeometry(QtCore.QRect(60, 50, 47, 13))
        self.label_13.setObjectName("label_13")
        self.horizontalLayout.addWidget(self.frame_2)
        self.frame_3 = QtWidgets.QFrame(self)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_3.sizePolicy().hasHeightForWidth())
        self.frame_3.setSizePolicy(sizePolicy)
        self.frame_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_3.setObjectName("frame_3")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.frame_3)
        self.verticalLayout.setObjectName("verticalLayout")
        self.frame_4 = QtWidgets.QFrame(self.frame_3)
        font = QtGui.QFont()
        font.setBold(True)
        font.setLegacyWeight(75)
        self.frame_4.setFont(font)
        self.frame_4.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_4.setObjectName("frame_4")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.frame_4)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label_10 = QtWidgets.QLabel(self.frame_4)
        font = QtGui.QFont()
        font.setPointSize(9)
        self.label_10.setFont(font)
        self.label_10.setStyleSheet("")
        self.label_10.setObjectName("label_10")
        self.horizontalLayout_3.addWidget(self.label_10, 0, QtCore.Qt.AlignHCenter|QtCore.Qt.AlignTop)
        self.verticalLayout.addWidget(self.frame_4)
        self.frame_5 = QtWidgets.QFrame(self.frame_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_5.sizePolicy().hasHeightForWidth())
        self.frame_5.setSizePolicy(sizePolicy)
        self.frame_5.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_5.setObjectName("frame_5")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.frame_5)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.frame_6 = QtWidgets.QFrame(self.frame_5)
        self.frame_6.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_6.setObjectName("frame_6")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.frame_6)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label = QtWidgets.QLabel(self.frame_6)
        self.label.setStyleSheet("QLabel{\n"
"    color:rgba(85,170,255,255);\n"
"    font-size:10px;\n"
"    font-weight:600;\n"
"}")
        self.label.setObjectName("label")
        self.label.setText("Karbonhidrat")
        self.verticalLayout_2.addWidget(self.label)
        self.label_2 = QtWidgets.QLabel(self.frame_6)
        font = QtGui.QFont()
        font.setBold(True)
        font.setLegacyWeight(75)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.verticalLayout_2.addWidget(self.label_2)
        self.label_3 = QtWidgets.QLabel(self.frame_6)
        font = QtGui.QFont()
        font.setBold(True)
        font.setLegacyWeight(75)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.verticalLayout_2.addWidget(self.label_3)
        self.horizontalLayout_2.addWidget(self.frame_6)
        self.frame_8 = QtWidgets.QFrame(self.frame_5)
        self.frame_8.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_8.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_8.setObjectName("frame_8")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.frame_8)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.label_4 = QtWidgets.QLabel(self.frame_8)
        font = QtGui.QFont()
        font.setPointSize(0)
        font.setBold(True)
        font.setLegacyWeight(75)
        self.label_4.setFont(font)
        self.label_4.setStyleSheet("QLabel{\n"
"    color:rgba(0,170,0,255);\n"
"    font-size:10px;\n"
"    font-weight:600;\n"
"}")
        self.label_4.setObjectName("label_4")
        self.label_4.setText("Protein")
        self.verticalLayout_3.addWidget(self.label_4)
        self.label_5 = QtWidgets.QLabel(self.frame_8)
        font = QtGui.QFont()
        font.setBold(True)
        font.setLegacyWeight(75)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.verticalLayout_3.addWidget(self.label_5)
        self.label_6 = QtWidgets.QLabel(self.frame_8)
        font = QtGui.QFont()
        font.setBold(True)
        font.setLegacyWeight(75)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.verticalLayout_3.addWidget(self.label_6)
        self.horizontalLayout_2.addWidget(self.frame_8)
        self.frame_7 = QtWidgets.QFrame(self.frame_5)
        self.frame_7.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_7.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_7.setObjectName("frame_7")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.frame_7)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.label_7 = QtWidgets.QLabel(self.frame_7)
        self.label_7.setStyleSheet("QLabel{\n"
"    color:rgba(255,85,255,255);\n"
"    font-size:10px;\n"
"    font-weight:600;\n"
"}")
        self.label_7.setObjectName("label_7")
        self.label_7.setText("Yağ")
        self.verticalLayout_4.addWidget(self.label_7)
        self.label_8 = QtWidgets.QLabel(self.frame_7)
        font = QtGui.QFont()
        font.setBold(True)
        font.setLegacyWeight(75)
        self.label_8.setFont(font)
        self.label_8.setObjectName("label_8")
        self.verticalLayout_4.addWidget(self.label_8)
        self.label_9 = QtWidgets.QLabel(self.frame_7)
        font = QtGui.QFont()
        font.setBold(True)
        font.setLegacyWeight(75)
        self.label_9.setFont(font)
        self.label_9.setObjectName("label_9")
        self.verticalLayout_4.addWidget(self.label_9)
        self.horizontalLayout_2.addWidget(self.frame_7)
        self.verticalLayout.addWidget(self.frame_5)
        self.horizontalLayout.addWidget(self.frame_3)
    
    def __init__(self, color="white", parent= None):
        super(MyWidget, self).__init__(parent)

        self.image_path = "" 
        self.color = color

        self.horizontalLayout = QtWidgets.QHBoxLayout(self)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.frame = QtWidgets.QFrame(self)
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.frame)
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_4.setSpacing(0)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.label_11 = QtWidgets.QLabel(self.frame)
        self.label_11.setMinimumSize(QtCore.QSize(150, 150))
        self.label_11.setMaximumSize(QtCore.QSize(150, 150))
        self.label_11.setText("")
        self.label_11.setPixmap(QtGui.QPixmap("images/Anne Yoğurdu.jpg"))
        self.label_11.setScaledContents(True)
        self.label_11.setObjectName("label_11")
        self.horizontalLayout_4.addWidget(self.label_11)
        self.horizontalLayout.addWidget(self.frame, 0, QtCore.Qt.AlignLeft)
        self.frame_2 = QtWidgets.QFrame(self)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_2.sizePolicy().hasHeightForWidth())
        self.frame_2.setSizePolicy(sizePolicy)
        self.frame_2.setMinimumSize(QtCore.QSize(150, 0))
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.karb = QtWidgets.QFrame(self.frame_2)
        self.karb.setGeometry(QtCore.QRect(40, 20, 110, 110))
        self.karb.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.karb.setFrameShadow(QtWidgets.QFrame.Raised)
        self.karb.setObjectName("karb")
        self.protein = QtWidgets.QFrame(self.frame_2)
        self.protein.setGeometry(QtCore.QRect(40, 20, 110, 110))
        self.protein.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.protein.setFrameShadow(QtWidgets.QFrame.Raised)
        self.protein.setObjectName("protein")
        self.yag = QtWidgets.QFrame(self.frame_2)
        self.yag.setGeometry(QtCore.QRect(40, 20, 110, 110))
        self.yag.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.yag.setFrameShadow(QtWidgets.QFrame.Raised)
        self.yag.setObjectName("yag")
        self.front = QtWidgets.QFrame(self.frame_2)
        self.front.setGeometry(QtCore.QRect(50, 30, 90, 90))
        self.front.setStyleSheet("#front{\n"
"border-radius: 45px;\n"
"    background-color: rgb(255,255,255);\n"
"}")
        self.front.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.front.setFrameShadow(QtWidgets.QFrame.Raised)
        self.front.setObjectName("front")
        self.label_12 = QtWidgets.QLabel(self.front)
        self.label_12.setGeometry(QtCore.QRect(10, 30, 71, 16))
        self.label_12.setText("")
        self.label_12.setObjectName("label_12")
        self.label_12.setAlignment(QtCore.Qt.AlignHCenter)
        self.label_12.setGeometry(10, 25, 70, 30)
        self.label_12.setStyleSheet("""
            QLabel{
                color:black;
                font-size: 15pt;
                font-weight:600;        
        }""")
        self.label_13 = QtWidgets.QLabel(self.front)
        self.label_13.setGeometry(QtCore.QRect(50, 50, 31, 16))
        self.label_13.setObjectName("label_13")
        self.label_13.setGeometry(50,50,20,20)
        self.label_13.setStyleSheet("""
            QLabel{
                color:black;      
        }""")
        self.protein.raise_()
        self.yag.raise_()
        self.karb.raise_()
        self.front.raise_()
        self.horizontalLayout.addWidget(self.frame_2)
        self.frame_3 = QtWidgets.QFrame(self)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_3.sizePolicy().hasHeightForWidth())
        self.frame_3.setSizePolicy(sizePolicy)
        self.frame_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_3.setObjectName("frame_3")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.frame_3)
        self.verticalLayout.setObjectName("verticalLayout")
        self.frame_4 = QtWidgets.QFrame(self.frame_3)
        self.frame_4.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_4.setObjectName("frame_4")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.frame_4)
        self.horizontalLayout_3.setContentsMargins(0, 7, 0, 7)
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label_10 = QtWidgets.QLabel(self.frame_4)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setLegacyWeight(75)
        self.label_10.setFont(font)
        self.label_10.setStyleSheet(f"QLabel{{color: {self.color};font-size: 12pt; font-weight: 600;}}")
        self.label_10.setObjectName("label_10")
        self.horizontalLayout_3.addWidget(self.label_10, 0, QtCore.Qt.AlignHCenter|QtCore.Qt.AlignTop)
        self.verticalLayout.addWidget(self.frame_4)
        self.frame_5 = QtWidgets.QFrame(self.frame_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_5.sizePolicy().hasHeightForWidth())
        self.frame_5.setSizePolicy(sizePolicy)
        self.frame_5.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_5.setObjectName("frame_5")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.frame_5)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.frame_6 = QtWidgets.QFrame(self.frame_5)
        self.frame_6.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_6.setObjectName("frame_6")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.frame_6)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label = QtWidgets.QLabel(self.frame_6)
        self.label.setMinimumSize(QtCore.QSize(0, 20))
        self.label.setStyleSheet("QLabel{\n"
"    color: rgba(85, 170, 255, 255);\n"
"    font-size: 10pt;\n"
"    font-weight: 600;\n"
"}")
        self.label.setObjectName("label")
        self.label.setText("Karbonhidrat")
        self.verticalLayout_2.addWidget(self.label, 0, QtCore.Qt.AlignHCenter)
        self.label_2 = QtWidgets.QLabel(self.frame_6)
        font = QtGui.QFont()
        font.setBold(True)
        font.setLegacyWeight(75)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.label_2.setStyleSheet(f"QLabel{{color: {self.color};}}")
        self.verticalLayout_2.addWidget(self.label_2, 0, QtCore.Qt.AlignHCenter)
        self.label_3 = QtWidgets.QLabel(self.frame_6)
        font = QtGui.QFont()
        font.setBold(True)
        font.setLegacyWeight(75)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.label_3.setStyleSheet(f"QLabel{{color: {self.color};}}")
        self.verticalLayout_2.addWidget(self.label_3, 0, QtCore.Qt.AlignHCenter)
        self.horizontalLayout_2.addWidget(self.frame_6)
        self.frame_8 = QtWidgets.QFrame(self.frame_5)
        self.frame_8.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_8.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_8.setObjectName("frame_8")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.frame_8)
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.label_4 = QtWidgets.QLabel(self.frame_8)
        self.label_4.setMinimumSize(QtCore.QSize(0, 20))
        self.label_4.setStyleSheet("QLabel{\n"
"    color: rgba(0, 170, 0, 255);\n"
"    font-size: 10pt;\n"
"    font-weight: 600;\n"
"}")
        self.label_4.setObjectName("label_4")
        self.label_4.setText("Protein")
        self.verticalLayout_3.addWidget(self.label_4, 0, QtCore.Qt.AlignHCenter)
        self.label_5 = QtWidgets.QLabel(self.frame_8)
        font = QtGui.QFont()
        font.setBold(True)
        font.setLegacyWeight(75)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.label_5.setStyleSheet(f"QLabel{{color: {self.color};}}")
        self.verticalLayout_3.addWidget(self.label_5, 0, QtCore.Qt.AlignHCenter)
        self.label_6 = QtWidgets.QLabel(self.frame_8)
        font = QtGui.QFont()
        font.setBold(True)
        font.setLegacyWeight(75)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.label_6.setStyleSheet(f"QLabel{{color: {self.color};}}")
        self.verticalLayout_3.addWidget(self.label_6, 0, QtCore.Qt.AlignHCenter)
        self.horizontalLayout_2.addWidget(self.frame_8)
        self.frame_7 = QtWidgets.QFrame(self.frame_5)
        self.frame_7.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_7.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_7.setObjectName("frame_7")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.frame_7)
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.label_7 = QtWidgets.QLabel(self.frame_7)
        self.label_7.setMinimumSize(QtCore.QSize(0, 20))
        self.label_7.setStyleSheet("QLabel{\n"
"    color: rgba(255, 85, 255, 255);\n"
"    font-size: 10pt;\n"
"    font-weight: 600;\n"
"}")
        self.label_7.setObjectName("label_7")
        self.label_7.setText("Yağ")
        self.verticalLayout_4.addWidget(self.label_7, 0, QtCore.Qt.AlignHCenter)
        self.label_8 = QtWidgets.QLabel(self.frame_7)
        font = QtGui.QFont()
        font.setBold(True)
        font.setLegacyWeight(75)
        self.label_8.setFont(font)
        self.label_8.setObjectName("label_8")
        self.label_8.setStyleSheet(f"QLabel{{color: {self.color};}}")
        self.verticalLayout_4.addWidget(self.label_8, 0, QtCore.Qt.AlignHCenter)
        self.label_9 = QtWidgets.QLabel(self.frame_7)
        font = QtGui.QFont()
        font.setBold(True)
        font.setLegacyWeight(75)
        self.label_9.setFont(font)
        self.label_9.setObjectName("label_9")
        self.label_9.setStyleSheet(f"QLabel{{color: {self.color};}}")
        self.verticalLayout_4.addWidget(self.label_9, 0, QtCore.Qt.AlignHCenter)
        self.horizontalLayout_2.addWidget(self.frame_7)
        self.verticalLayout.addWidget(self.frame_5)
        self.horizontalLayout.addWidget(self.frame_3)

    def barvalues(self, valuelist): # Valuelist bir liste. 1. karbonhidrat yüzdesi, 2. protein yüzdesi, 3. yağ yüzdesi
        StyleKarb = ("QFrame{\n"
"    border-radius:55px;\n"
"    background-color: qconicalgradient(cx:0.5, cy:0.5, angle:90, stop:{STOP_1_K} rgba(0, 0, 0, 0), stop:{STOP_2_K} rgba(85, 170, 255, 255));\n"
"}")
        StyleProtein = ("QFrame{\n"
"    border-radius:55px;\n"
"    background-color: qconicalgradient(cx:0.5, cy:0.5, angle:90, stop:{STOP_1_P} rgba(0, 0, 0, 0), stop:{STOP_2_P} rgba(0, 170, 0, 255));\n"
"}")
        StyleYag = ("QFrame{\n"
"    border-radius: 55px;\n"
"    background-color: qconicalgradient(cx:0.5, cy:0.5, angle:90, stop:{STOP_1_Y} rgba(0, 0, 0, 0), stop:{STOP_2_Y} rgba(255, 85, 255, 255));\n"
"}")
        
        valuelist = np.array(valuelist)
        sorted_valuelist = np.argsort(valuelist)

        if sorted_valuelist[0] == 2:
            if sorted_valuelist[1] == 1: # [2,1,0], en büyük değerler karb --> protein --> yağ
                self.yag.raise_()
                self.protein.raise_()
                self.karb.raise_()
                self.front.raise_()

                karbValue = valuelist[0]
                proteinValue = valuelist[1] + karbValue
                yagValue = valuelist[2] + proteinValue

                progressKarb = (100 - karbValue)/100.0
                stop_1_k = str(progressKarb - 0.001)
                stop_2_k = str(progressKarb)

                if float(stop_1_k) < 0: stop_1_k = "0"

                progressProtein = (100 - proteinValue)/100.0
                stop_1_p = str(progressProtein - 0.001)
                stop_2_p = str(progressProtein)

                if float(stop_1_p) < 0: stop_1_p = "0"

                progressYag = (100 - yagValue)/100.0
                stop_1_y = str(progressYag - 0.001)
                stop_2_y = str(progressYag)

                if float(stop_1_y) < 0: stop_1_y = "0"

                nexStyleKarb = StyleKarb.replace("{STOP_1_K}", stop_1_k).replace("{STOP_2_K}", stop_2_k) 
                self.karb.setStyleSheet(nexStyleKarb)

                nexStyleProtein = StyleProtein.replace("{STOP_1_P}", stop_1_p).replace("{STOP_2_P}", stop_2_p) 
                self.protein.setStyleSheet(nexStyleProtein)

                nexStyleYag = StyleYag.replace("{STOP_1_Y}", stop_1_y).replace("{STOP_2_Y}", stop_2_y) 
                self.yag.setStyleSheet(nexStyleYag)

            if sorted_valuelist[1] == 0: # [2,0,1], en büyük değerler karb --> yağ --> protein 
                self.protein.raise_()
                self.yag.raise_()
                self.karb.raise_()
                self.front.raise_()

                karbValue = valuelist[0]
                yagValue = valuelist[2] + karbValue
                proteinValue = valuelist[1] + yagValue

                progressKarb = (100 - karbValue)/100.0
                stop_1_k = str(progressKarb - 0.001)
                stop_2_k = str(progressKarb)

                if float(stop_1_k) < 0: stop_1_k = "0"

                progressProtein = (100 - proteinValue)/100.0
                stop_1_p = str(progressProtein - 0.001)
                stop_2_p = str(progressProtein)

                if float(stop_1_p) < 0: stop_1_p = "0"

                progressYag = (100 - yagValue)/100.0
                stop_1_y = str(progressYag - 0.001)
                stop_2_y = str(progressYag)

                if float(stop_1_y) < 0: stop_1_y = "0"

                nexStyleKarb = StyleKarb.replace("{STOP_1_K}", stop_1_k).replace("{STOP_2_K}", stop_2_k) 
                self.karb.setStyleSheet(nexStyleKarb)

                nexStyleProtein = StyleProtein.replace("{STOP_1_P}", stop_1_p).replace("{STOP_2_P}", stop_2_p) 
                self.protein.setStyleSheet(nexStyleProtein)

                nexStyleYag = StyleYag.replace("{STOP_1_Y}", stop_1_y).replace("{STOP_2_Y}", stop_2_y) 
                self.yag.setStyleSheet(nexStyleYag)
        if sorted_valuelist[0] == 1:
            if sorted_valuelist[1] == 2: # [1,2,0], en büyük değerler protein --> karb --> yağ
                self.yag.raise_()
                self.karb.raise_()
                self.protein.raise_()
                self.front.raise_()

                proteinValue = valuelist[1]
                karbValue = valuelist[0] + proteinValue
                yagValue = valuelist[2] + karbValue

                progressKarb = (100 - karbValue)/100.0
                stop_1_k = str(progressKarb - 0.001)
                stop_2_k = str(progressKarb)

                if float(stop_1_k) < 0: stop_1_k = "0"

                progressProtein = (100 - proteinValue)/100.0
                stop_1_p = str(progressProtein - 0.001)
                stop_2_p = str(progressProtein)

                if float(stop_1_p) < 0: stop_1_p = "0"

                progressYag = (100 - yagValue)/100.0
                stop_1_y = str(progressYag - 0.001)
                stop_2_y = str(progressYag)

                if float(stop_1_y) < 0: stop_1_y = "0"

                nexStyleKarb = StyleKarb.replace("{STOP_1_K}", stop_1_k).replace("{STOP_2_K}", stop_2_k) 
                self.karb.setStyleSheet(nexStyleKarb)

                nexStyleProtein = StyleProtein.replace("{STOP_1_P}", stop_1_p).replace("{STOP_2_P}", stop_2_p) 
                self.protein.setStyleSheet(nexStyleProtein)

                nexStyleYag = StyleYag.replace("{STOP_1_Y}", stop_1_y).replace("{STOP_2_Y}", stop_2_y) 
                self.yag.setStyleSheet(nexStyleYag)
            if sorted_valuelist[1] == 0: # [1,0,2], en büyük değerler yağ --> karb --> protein
                self.protein.raise_()
                self.karb.raise_()
                self.yag.raise_()
                self.front.raise_()

                yagValue = valuelist[2]
                karbValue = valuelist[0] + yagValue
                proteinValue = valuelist[1] + karbValue

                progressKarb = (100 - karbValue)/100.0
                stop_1_k = str(progressKarb - 0.001)
                stop_2_k = str(progressKarb)

                if float(stop_1_k) < 0: stop_1_k = "0"

                progressProtein = (100 - proteinValue)/100.0
                stop_1_p = str(progressProtein - 0.001)
                stop_2_p = str(progressProtein)

                if float(stop_1_p) < 0: stop_1_p = "0"

                progressYag = (100 - yagValue)/100.0
                stop_1_y = str(progressYag - 0.001)
                stop_2_y = str(progressYag)

                if float(stop_1_y) < 0: stop_1_y = "0"

                nexStyleKarb = StyleKarb.replace("{STOP_1_K}", stop_1_k).replace("{STOP_2_K}", stop_2_k) 
                self.karb.setStyleSheet(nexStyleKarb)

                nexStyleProtein = StyleProtein.replace("{STOP_1_P}", stop_1_p).replace("{STOP_2_P}", stop_2_p) 
                self.protein.setStyleSheet(nexStyleProtein)

                nexStyleYag = StyleYag.replace("{STOP_1_Y}", stop_1_y).replace("{STOP_2_Y}", stop_2_y) 
                self.yag.setStyleSheet(nexStyleYag)
        if sorted_valuelist[0] == 0:
            if sorted_valuelist[1] == 1: # [0,1,2], en büyük değerler yağ --> protein --> karb
                self.karb.raise_()
                self.protein.raise_()
                self.yag.raise_()
                self.front.raise_()

                yagValue = valuelist[2]
                proteinValue = valuelist[1] + yagValue
                karbValue = valuelist[0] + proteinValue

                progressKarb = (100 - karbValue)/100.0
                stop_1_k = str(progressKarb - 0.001)
                stop_2_k = str(progressKarb)

                if float(stop_1_k) < 0: stop_1_k = "0"

                progressProtein = (100 - proteinValue)/100.0
                stop_1_p = str(progressProtein - 0.001)
                stop_2_p = str(progressProtein)

                if float(stop_1_p) < 0: stop_1_p = "0"

                progressYag = (100 - yagValue)/100.0
                stop_1_y = str(progressYag - 0.001)
                stop_2_y = str(progressYag)

                if float(stop_1_y) < 0: stop_1_y = "0"

                nexStyleKarb = StyleKarb.replace("{STOP_1_K}", stop_1_k).replace("{STOP_2_K}", stop_2_k) 
                self.karb.setStyleSheet(nexStyleKarb)

                nexStyleProtein = StyleProtein.replace("{STOP_1_P}", stop_1_p).replace("{STOP_2_P}", stop_2_p) 
                self.protein.setStyleSheet(nexStyleProtein)

                nexStyleYag = StyleYag.replace("{STOP_1_Y}", stop_1_y).replace("{STOP_2_Y}", stop_2_y) 
                self.yag.setStyleSheet(nexStyleYag)
            if sorted_valuelist[1] == 2: # [0,2,1], en büyük değerler protein --> yağ --> karb
                self.karb.raise_()
                self.yag.raise_()
                self.protein.raise_()
                self.front.raise_()

                proteinValue = valuelist[1]
                yagValue = valuelist[2] + proteinValue
                karbValue = valuelist[0] + yagValue

                progressKarb = (100 - karbValue)/100.0
                stop_1_k = str(progressKarb - 0.001)
                stop_2_k = str(progressKarb)

                if float(stop_1_k) < 0: stop_1_k = "0"

                progressProtein = (100 - proteinValue)/100.0
                stop_1_p = str(progressProtein - 0.001)
                stop_2_p = str(progressProtein)

                if float(stop_1_p) < 0: stop_1_p = "0"

                progressYag = (100 - yagValue)/100.0
                stop_1_y = str(progressYag - 0.001)
                stop_2_y = str(progressYag)

                if float(stop_1_y) < 0: stop_1_y = "0"

                nexStyleKarb = StyleKarb.replace("{STOP_1_K}", stop_1_k).replace("{STOP_2_K}", stop_2_k) 
                self.karb.setStyleSheet(nexStyleKarb)

                nexStyleProtein = StyleProtein.replace("{STOP_1_P}", stop_1_p).replace("{STOP_2_P}", stop_2_p) 
                self.protein.setStyleSheet(nexStyleProtein)

                nexStyleYag = StyleYag.replace("{STOP_1_Y}", stop_1_y).replace("{STOP_2_Y}", stop_2_y) 
                self.yag.setStyleSheet(nexStyleYag)
    
    
    
    def set_image(self,image_path):
        
        if os.path.exists(image_path):
            self.label_11.setPixmap(QPixmap(image_path).scaled(150,150))
        else:
            self.label_11.setPixmap(QPixmap("images/No image.jpg").scaled(150,150))
    
    def set_Text(self,yemek_ismi,kalori,karb,protein,yag):
        
        #yemek ismini ekrana yazdrıma
        self.label_10.setText(yemek_ismi)
        
        #kalori değeri ekleme
        kalori=str(round(kalori))
        self.label_12.setAlignment(QtCore.Qt.AlignHCenter)
        self.label_12.setGeometry(10,30,70,30)
        self.label_12.setStyleSheet("""
                                    QLabel{
                                        color:black;
                                        font-size:15pt;
                                        font-weight:600;
                                        border-radius:2px solid black;
            
            
            }""")
        self.label_12.setText(kalori)
        self.label_13.setGeometry(50,55,30,20)
        self.label_13.setStyleSheet("""
                                    QLabel{
                                        color:black;
                                        
            
            
            }""")
        self.label_13.setText("kcal")
        
        #Besinlerin gramlarını ekleyelim
        
        self.label_2.setText("{}g".format(str(round(karb,2))))
        self.label_5.setText("{}g".format(str(round(protein,2))))
        self.label_8.setText("{}g".format(str(round(yag,2))))
        
        #Yüzdelik değerlerini ekleyelim
        toplam=karb+protein+yag
        self.label_3.setText("%{}".format(str(round(karb/toplam*100))))
        self.label_6.setText("%{}".format(str(round(protein/toplam*100))))
        self.label_9.setText("%{}".format(str(100-(round(karb/toplam*100)-round(protein/toplam*100)))))
        
        
        
        
class Toggle(QCheckBox):
    def __init__(
            self,
            width = 60,
            bg_color = "#777",
            circle_color = "#DDD",
            active_color = "#00BCff"):
        QCheckBox.__init__(self)
        self.setFixedSize(width, 28)

        # Renkleri belirtelim
        self._bg_color = bg_color   
        self._circle_color = circle_color
        self._active_color = active_color

    def hitButton(self, pos:QPoint):
        return self.contentsRect().contains(pos)
    
    def paintEvent(self, e):
        p = QPainter(self)
        p.setRenderHint(QPainter.Antialiasing)
        p.setPen(Qt.NoPen)

        # Dikdörtgen çizelim
        rect = QRect(0,0, self.width(), self.height())

        if not self.isChecked(): #gece modunun tasarımı
            # Arkaplanı oluşturalım
            p.setBrush(QColor("#242424"))
            p.drawRoundedRect(0,0,rect.width(), self.height(), self.height()/2, self.height()/2)
            # Çemberi oluşturalım
            p.setBrush(QColor(self._circle_color))
            p.drawEllipse(self.width() - 26, 3, 22, 22)
            # Çemberin içine ikon ekleyelim
            p.drawPixmap(self.width() - 21, 6, 15, 15, QPixmap(r"C:\Users\kasap\Desktop\kalori_sayaci\icons\moon.png"))

        else: # gündüz modunun tasarımı
            p.setBrush(QColor(self._bg_color))
            p.drawRoundedRect(0,0,rect.width(), self.height(), self.height()/2, self.height()/2)
            p.setBrush(QColor("#f9c77f"))
            p.drawEllipse(3, 3, 22, 22)
            p.drawPixmap(6, 6, 15, 15, QPixmap(r"C:\Users\kasap\Desktop\kalori_sayaci\icons\sun.png"))

        p.end()   


class FoodList(QWidget):
    def __init__(self, color = "white", parent= None):
        super(FoodList, self).__init__(parent)

        self.color = color

        self.horizontalLayout = QtWidgets.QHBoxLayout(self)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.frame = QtWidgets.QFrame(self)
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.frame.setStyleSheet("QFrame{background-color: transparent;}")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.frame)
        self.horizontalLayout_2.setContentsMargins(11, 0, 0, 0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label = QtWidgets.QLabel(self.frame)
        self.label.setStyleSheet(f"QLabel{{color: {self.color}; font-size: 20px;}}")
        self.label.setText("")
        self.label.setObjectName("label")
        self.horizontalLayout_2.addWidget(self.label)
        self.frame_2 = QtWidgets.QFrame(self.frame)
        self.frame_2.setMinimumSize(QtCore.QSize(150, 0))
        self.frame_2.setStyleSheet("QFrame{\n"
"    background-color: red;\n"
"}")
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.frame_2.setMaximumWidth(0)
        self.frame_2.setMinimumWidth(0)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.frame_2)
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.pushButton = QtWidgets.QPushButton(self.frame_2)
        self.pushButton.setStyleSheet("QPushButton{\n"
"    background-color: red;\n"
"    border: none;\n"
"}")
        self.pushButton.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("icons/recycle-bin.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton.setIcon(icon)
        self.pushButton.setIconSize(QtCore.QSize(25, 25))
        self.pushButton.setObjectName("pushButton")
        self.horizontalLayout_3.addWidget(self.pushButton)
        self.horizontalLayout_2.addWidget(self.frame_2, 0, QtCore.Qt.AlignRight)
        self.horizontalLayout.addWidget(self.frame)

    def set_text(self, text):
        self.label.setText(text)



class CircularProgress(QWidget):
    def __init__(self, karb_yuzde, protein_yuzde, yag_yuzde):
        QWidget.__init__(self)

        # Parametreler
        self.value_karb = karb_yuzde #yüzde
        self.value_protein = protein_yuzde #yüzde
        self.value_yag = yag_yuzde #yüzde
        self.progress_width = 8
        # renk seçme
        self.karb = 0x0000ff
        self.bg_karb = 0x021b22
        self.protein = 0x00aa00
        self.bg_protein = 0x082101
        self.yag = 0xff00ff
        self.bg_yag = 0x230004

        self.max_value = 100
        self.enable_shadow = True

        self.setStyleSheet("background-color: transparent;")

    def paintEvent(self, event):
        value_karb = self.value_karb * 360 / self.max_value
        value_protein = self.value_protein * 360 / self.max_value
        value_yag = self.value_yag * 360 / self.max_value

        paint = QPainter()
        paint.begin(self)
        paint.setRenderHint(QPainter.Antialiasing) # pikselleşmiş köşeleri yok eder

        # Karb Arkaplanı
        bg_karb = QPen()
        bg_karb.setColor(QColor(self.bg_karb))
        bg_karb.setWidth(self.progress_width)
        bg_karb.setCapStyle(Qt.RoundCap)

        # Karb
        pen_karb = QPen()
        pen_karb.setColor(QColor(self.karb))
        pen_karb.setWidth(self.progress_width)
        pen_karb.setCapStyle(Qt.RoundCap)

        # Protein Arkaplanı
        bg_protein = QPen()
        bg_protein.setColor(QColor(self.bg_protein))
        bg_protein.setWidth(self.progress_width)
        bg_protein.setCapStyle(Qt.RoundCap)

        # Protein 
        pen_protein = QPen()
        pen_protein.setColor(QColor(self.protein))
        pen_protein.setWidth(self.progress_width)
        pen_protein.setCapStyle(Qt.RoundCap)

        # Protein Arkaplanı
        bg_yag = QPen()
        bg_yag.setColor(QColor(self.bg_yag))
        bg_yag.setWidth(self.progress_width)
        bg_yag.setCapStyle(Qt.RoundCap)

        # Protein Arkaplanı
        pen_yag = QPen()
        pen_yag.setColor(QColor(self.yag))
        pen_yag.setWidth(self.progress_width)
        pen_yag.setCapStyle(Qt.RoundCap)

        # Arkaplan karb barını çizelim
        paint.setPen(bg_karb)
        paint.drawArc(QRect(24,24,16,16), 90*16, -360*16)

        # Karb barını çizelim
        paint.setPen(pen_karb)
        paint.drawArc(QRect(24,24,16,16), 90*16, -value_karb*16)

        # Arkaplan protein barını çizelim
        paint.setPen(bg_protein)
        paint.drawArc(QRect(16,16,32,32), 90*16, -360*16)

        # Protein barını çizelim
        paint.setPen(pen_protein)
        paint.drawArc(QRect(16,16,32,32), 90*16, -value_protein*16)

        # Arkaplan yağ barını çizelim
        paint.setPen(bg_yag)
        paint.drawArc(QRect(8,8,48,48), 90*16, -360*16)

        # Yağ barını çizelim
        paint.setPen(pen_yag)
        paint.drawArc(QRect(8,8,48,48), 90*16, -value_yag*16)

        paint.end()


class MainWindow(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        
        # Minimum pencere boyutu
        self.setMinimumSize(1250,800)

        # Kaydırma çubuğunu gizleyelim
        self.ui.listWidget.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.ui.listWidget.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.ui.listWidget_2.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.ui.listWidget_2.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.ui.listWidget_3.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.ui.listWidget_3.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.ui.listWidget_4.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.ui.listWidget_4.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.ui.listWidget_5.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.ui.listWidget_5.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.ui.listWidget_6.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.ui.listWidget_6.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)

        # Default sayfa ayarları
        self.ui.stackedWidget.setCurrentWidget(self.ui.log_in)
        self.ui.label_3.setText("")
        self.ui.pushButton_20.clicked.connect(lambda: self.clear_lines_for_sign_up())
        self.ui.pushButton_21.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.log_in))
        self.ui.lineEdit_11.returnPressed.connect(lambda: self.log_in())
        self.ui.pushButton_18.clicked.connect(lambda: self.log_in())
        self.ui.pushButton_23.clicked.connect(lambda: self.sign_up())
        self.ui.pushButton_19.toggled.connect(self.show_password)
        self.ui.pushButton_22.clicked.connect(self.photo)

        # Kısıtlamalar
        input_validator = QRegularExpressionValidator(QRegularExpression(r"[0-9]{2,3}"))
        self.ui.lineEdit_13.setValidator(input_validator)
        self.ui.lineEdit_14.setValidator(input_validator)
        self.ui.lineEdit_15.setValidator(input_validator)
        self.ui.lineEdit_18.setValidator(input_validator)
        self.ui.lineEdit_19.setValidator(input_validator)
        self.ui.lineEdit_20.setValidator(input_validator)


        # Kullanıcı hatası mesajını gizleyelim
        self.ui.label_67.setVisible(False)
        self.ui.label_68.setVisible(False)
        self.ui.frame_96.setVisible(False)
        self.ui.buttons.setVisible(False)

        # Menu buton ayarlamaları
        self.ui.pushButton_3.clicked.connect(lambda: self.slideLeftMenu())
        self.ui.pushButton.clicked.connect(lambda: self.page_1())
        self.ui.pushButton_2.clicked.connect(lambda: self.page_2())
        self.ui.pushButton_4.clicked.connect(lambda: self.add_food())
        self.ui.pushButton_24.clicked.connect(lambda: self.settings())

        # Filtreleme fonksiyonları
        self.ui.lineEdit.textEdited.connect(lambda: self.filter())

        # Değişkenler
        self.image_path = ""
        self.lastButtonPressed = None

        # Toggle
        self.toggle = Toggle()
        layout_ = QVBoxLayout(self.ui.frame_116)
        layout_.addWidget(self.toggle)
        self.toggle.stateChanged.connect(self.night_light_mode)

        # Günlük ihtiyaç değerleri
        self.daily_kalori = 0.0
        self.daily_karb = 0.0
        self.daily_protein = 0.0
        self.daily_yag = 0.0
        self.kahvalti_kalori = 0.0
        self.kahvalti_karb = 0.0
        self.kahvalti_protein = 0.0
        self.kahvalti_yag = 0.0
        self.ogle_kalori = 0.0
        self.ogle_karb = 0.0
        self.ogle_protein = 0.0
        self.ogle_yag = 0.0
        self.aksam_kalori = 0.0
        self.aksam_karb = 0.0
        self.aksam_protein = 0.0
        self.aksam_yag = 0.0
        self.ara_kalori = 0.0
        self.ara_karb = 0.0
        self.ara_protein = 0.0
        self.ara_yag = 0.0
        self.kahvalti = {"Yemekler": list(), "Miktar": list()}
        self.ogle = {"Yemekler": list(), "Miktar": list()}
        self.aksam = {"Yemekler": list(), "Miktar": list()}
        self.ara = {"Yemekler": list(), "Miktar": list()}
        # Eski verileri yükleyelim
        data = self.userData(readMode=True)
        self.kahvalti = {"Yemekler": data["Kahvalti"]["Yemekler"], "Miktar": data["Kahvalti"]["Miktar"]}
        self.kahvalti_kalori = data["Kahvalti"]["Kalori"]
        self.kahvalti_karb = data["Kahvalti"]["Karbonhidrat"]
        self.kahvalti_protein = data["Kahvalti"]["Protein"]
        self.kahvalti_yag = data["Kahvalti"]["Yag"]
        self.ogle = {"Yemekler": data["Ogle"]["Yemekler"], "Miktar": data["Ogle"]["Miktar"]}
        self.ogle_kalori = data["Ogle"]["Kalori"]
        self.ogle_karb = data["Ogle"]["Karbonhidrat"]
        self.ogle_protein = data["Ogle"]["Protein"]
        self.ogle_yag = data["Ogle"]["Yag"]
        self.aksam = {"Yemekler": data["Aksam"]["Yemekler"], "Miktar": data["Aksam"]["Miktar"]}
        self.aksam_kalori = data["Aksam"]["Kalori"]
        self.aksam_karb = data["Aksam"]["Karbonhidrat"]
        self.aksam_protein = data["Aksam"]["Protein"]
        self.aksam_yag = data["Aksam"]["Yag"]
        self.ara = {"Yemekler": data["Ara"]["Yemekler"], "Miktar": data["Ara"]["Miktar"]}
        self.ara_kalori = data["Ara"]["Kalori"]
        self.ara_karb = data["Ara"]["Karbonhidrat"]
        self.ara_protein = data["Ara"]["Protein"]
        self.ara_yag = data["Ara"]["Yag"]

        # Kullanıcın ihtiyaç değeleri
        self.ihtiyac_kalori = 0
        self.ihtiyac_karb = 0
        self.ihtiyac_protein = 0
        self.ihtiyac_yag = 0

        # Eklenmiş yemekleri gösterelim
        for yemek_ismi in self.kahvalti["Yemekler"]:
            self.ui.frame_33.setMaximumHeight(16777215)
            self.ui.pushButton_13.toggled.connect(self.food_menu)
            self.ui.listWidget_2.itemDoubleClicked.connect(self.delete, Qt.UniqueConnection)
            #self.ui.listWidget_2.addItem(QListWidgetItem(yemek_ismi))
            if self.toggle.isChecked():
                self.widget = FoodList(color="black")
            else:
                self.widget = FoodList()
            self.widget.set_text(yemek_ismi)
            item = QListWidgetItem()
            item.setSizeHint(QSize(0, 50))
            self.ui.listWidget_2.addItem(item)
            self.ui.listWidget_2.setItemWidget(item, self.widget)
            self.ui.label_24.setText(str(round(self.kahvalti_kalori,2)))
            self.ui.label_32.setText(str(round(self.kahvalti_karb,2)))
            self.ui.label_34.setText(str(round(self.kahvalti_protein,2)))
            self.ui.label_36.setText(str(round(self.kahvalti_yag,2)))

        for yemek_ismi in self.ogle["Yemekler"]:
            self.ui.frame_35.setMaximumHeight(16777215)
            self.ui.pushButton_14.toggled.connect(self.food_menu)
            self.ui.listWidget_3.itemDoubleClicked.connect(self.delete, Qt.UniqueConnection)
            #self.ui.listWidget_3.addItem(QListWidgetItem(yemek_ismi))
            if self.toggle.isChecked():
                self.widget = FoodList(color="black")
            else:
                self.widget = FoodList()
            self.widget.set_text(yemek_ismi)
            item = QListWidgetItem()
            item.setSizeHint(QSize(0, 50))
            self.ui.listWidget_3.addItem(item)
            self.ui.listWidget_3.setItemWidget(item, self.widget)
            self.ui.label_25.setText(str(round(self.ogle_kalori,2)))
            self.ui.label_37.setText(str(round(self.ogle_karb,2)))
            self.ui.label_39.setText(str(round(self.ogle_protein,2)))
            self.ui.label_41.setText(str(round(self.ogle_yag,2)))

        for yemek_ismi in self.aksam["Yemekler"]:
            self.ui.frame_37.setMaximumHeight(16777215)
            self.ui.pushButton_15.toggled.connect(self.food_menu)
            self.ui.listWidget_4.itemDoubleClicked.connect(self.delete, Qt.UniqueConnection)
            #self.ui.listWidget_4.addItem(QListWidgetItem(yemek_ismi))
            if self.toggle.isChecked():
                self.widget = FoodList(color="black")
            else:
                self.widget = FoodList()
            self.widget.set_text(yemek_ismi)
            item = QListWidgetItem()
            item.setSizeHint(QSize(0, 50))
            self.ui.listWidget_4.addItem(item)
            self.ui.listWidget_4.setItemWidget(item, self.widget)
            self.ui.label_27.setText(str(round(self.aksam_kalori,2)))
            self.ui.label_44.setText(str(round(self.aksam_karb,2)))
            self.ui.label_45.setText(str(round(self.aksam_protein,2)))
            self.ui.label_48.setText(str(round(self.aksam_yag,2)))

        for yemek_ismi in self.ara["Yemekler"]:
            self.ui.frame_39.setMaximumHeight(16777215)
            self.ui.pushButton_16.toggled.connect(self.food_menu)
            self.ui.listWidget_5.itemDoubleClicked.connect(self.delete, Qt.UniqueConnection)
            #self.ui.listWidget_5.addItem(QListWidgetItem(yemek_ismi))
            if self.toggle.isChecked():
                self.widget = FoodList(color="black")
            else:
                self.widget = FoodList()
            self.widget.set_text(yemek_ismi)
            item = QListWidgetItem()
            item.setSizeHint(QSize(0, 50))
            self.ui.listWidget_5.addItem(item)
            self.ui.listWidget_5.setItemWidget(item, self.widget)
            self.ui.label_29.setText(str(round(self.ara_kalori,2)))
            self.ui.label_50.setText(str(round(self.ara_karb,2)))
            self.ui.label_52.setText(str(round(self.ara_protein,2)))
            self.ui.label_54.setText(str(round(self.ara_yag,2)))

        self.daily_kalori = data["Toplam"]["Kalori"]
        self.daily_karb = data["Toplam"]["Karbonhidrat"]
        self.daily_protein = data["Toplam"]["Protein"]
        self.daily_yag = data["Toplam"]["Yag"]

        self.ui.label_58.setText(str(self.daily_kalori))
        self.ui.label_60.setText(str(self.daily_karb))
        self.ui.label_62.setText(str(self.daily_protein))
        self.ui.label_64.setText(str(self.daily_yag))

        # Animasyon ayarları
        self.initial_movie = QMovie(r"C:\Users\kasap\Desktop\kalori_sayaci\gifs\Initial.gif")
        self.ui.initial.setMovie(self.initial_movie)

        self.match_movie = QMovie(r"C:\Users\kasap\Desktop\kalori_sayaci\gifs\Success.gif")
        self.ui.success.setMovie(self.match_movie)

        self.fail_movie = QMovie(r"C:\Users\kasap\Desktop\kalori_sayaci\gifs\Fail.gif")
        self.ui.fail.setMovie(self.fail_movie)

        self.match_movie.frameChanged.connect(self.check_frame)
        self.fail_movie.frameChanged.connect(self.check_frame)

        self.initial_movie.start()

        # self.face_recognition = FaceRecognition()
        # self.face_recognition.match_found.connect(self.show_match_animation)
        # self.face_recognition.timeout.connect(self.show_fail_animation)
        # self.face_recognition.update_face_names.connect(self.print_face_names)

        # self.face_recognition.start()

        self.food_list()

        self.ui.listWidget.installEventFilter(self)

        # Bildirim Ayarları
        self.tray_icon = QSystemTrayIcon(self)
        self.tray_icon.setIcon(QIcon(r"C:\Users\kasap\Desktop\kalori_sayaci\icons\fruit.png"))
        self.tray_icon.setToolTip("Kalori Sayacı")

        # Tray için bir menü oluşturalım.
        menu = QMenu()

        # Tarih ve saati güncelleyelim
        self.timer = QTimer()
        self.timer.timeout.connect(self.updateDateTime)
        self.timer.start(1000) # 1000 ms = 1 s

        # Bildirime tıkladığımızda uygulama açılsın.
        self.tray_icon.messageClicked.connect(self.on_message_clicked)

        # Çıkma fonksiyonu ekleyelim.
        action_exit = QAction("Çıkış", self)
        action_exit.triggered.connect(app.exit)
        menu.addAction(action_exit)

        # Menüyü traye ekleyelim
        self.tray_icon.setContextMenu(menu)

        # Sol tıklamayla uygulamayı tekrar açalım.
        self.tray_icon.activated.connect(self.show_app)

        self.tray_icon.show()

        self.show()
    
    def show_app(self, reason):
        if reason == QSystemTrayIcon.Trigger: # fareyle sol tiki algılar
            self.showNormal()

    def show_tray_message(self):
        karb_yuzde = round(self.daily_karb / self.ihtiyac_karb * 100)
        protein_yuzde = round(self.daily_protein / self.ihtiyac_protein * 100)
        yag_yuzde = round(self.daily_yag / self.ihtiyac_yag * 100)
        widget = CircularProgress(karb_yuzde, protein_yuzde, yag_yuzde)
        # Widgetın boyutunu ayarlayalım
        widget.setGeometry(0,0,64,64)
        # Widgetı pixmape (resme) çevirelim
        pixmap = QPixmap(widget.size())
        pixmap.fill(Qt.transparent)
        widget.render(pixmap)

        icon = QIcon(pixmap)
        if self.daily_kalori < self.ihtiyac_kalori:
            self.tray_icon.showMessage(
                "Öğünlerini Eklemeyi Unutma!",
                "Şu ana kadar {} kalori tükettin. Eksikleri kapatma zamanı.".format(str(round(self.daily_kalori))),
                icon,
                #QSystemTrayIcon.Information,
                5000 # 5 saniye
            )

    def on_message_clicked(self):
        self.showNormal()

    def print_face_names(self, face_names):
        if len(face_names) == 1 and face_names[0] != "Unknown":
            self.faceid = face_names[0].split(".")[0]

    def show_match_animation(self):
        self.initial_movie.stop()
        self.ui.initial.hide()
        self.ui.fail.hide()

        self.ui.success.show()
        self.match_movie.start()

    def show_fail_animation(self):
        self.faceid = ""
        self.initial_movie.stop()
        self.ui.initial.hide()
        self.ui.success.hide()

        self.ui.fail.show()
        self.fail_movie.start()

    def stop_animation_success(self):
        self.match_movie.stop()
        self.ui.fail.hide()
        self.ui.success.hide()

        self.ui.stackedWidget.setCurrentWidget(self.ui.yemekler)
        self.ui.label_3.setText("Yemek Listesi")
        self.ui.buttons.setVisible(True)

        # Veri tabanına bağlanalım
        mydb = mysql.connect(host="localhost", user="root", password="Gokalp59", database="kalori_sayaci", port=3306)
        mycursor = mydb.cursor()
        mycursor.execute("SELECT * FROM log_db WHERE BINARY Username = %s",(self.faceid,))
        result = mycursor.fetchone()

        if result:
            self.ihtiyac_kalori = result[-4]
            self.ihtiyac_karb = result[-3]
            self.ihtiyac_protein = result[-2]
            self.ihtiyac_yag = result[-1]
            self.ui.label_57.setText(str(result[-4]))

    def stop_animation_fail(self):
        self.fail_movie.stop()
        self.ui.fail.hide()
        self.ui.success.hide()

    def check_frame(self, frame_number):
        if frame_number == self.match_movie.frameCount() - 1:
            self.stop_animation_success()
        if frame_number == self.fail_movie.frameCount() - 1:
            self.stop_animation_fail()
    
    def night_light_mode(self):
        if self.toggle.isChecked() == True: # Aydınlık Modu
            # yemekler sayfası
            bg_color = "#959c9e"
            ust_menu = "#f7f7f7"
            buttons = "#DCDFE4"
            stacked_bg = "#fafafa"
            font_color = "black"
            self.ui.label.setStyleSheet("QLabel{color:black;}")
            self.ui.label_2.setStyleSheet("QLabel{color:black;}")
            self.ui.label_3.setStyleSheet("QLabel{color:black;}")
            self.ui.pushButton_5.setStyleSheet("QPushButton{background-color: white; border-left: 1px solid black; border-top: 1px solid black; border-bottom: 1px solid black;}")
            self.ui.pushButton_5.setMaximumHeight(22)

            # yemek ekle sayfası
            self.ui.frame_16.setStyleSheet("QLabel{font-weight:600; color:black;}")
            self.ui.label_5.setStyleSheet("QLabel{font-weight:600; color:black;}")
            self.ui.label_6.setStyleSheet("QLabel{font-weight:600; color:black;}")

            # Kalori sayfası
            self.ui.dateTimeEdit.setStyleSheet("QDateTimeEdit{font-size: 12pt; font-weight: 600; background-color: #fafafa; color: black;}")
            self.ui.frame_28.setStyleSheet("#frame_28{background-color: #f7f7f7; border-radius: 10px; border: 2px solid rgb(33,43,51);}")
            self.ui.frame_68.setStyleSheet("QLabel{color:black;}")
            self.ui.label_19.setStyleSheet("QLabel{padding-top: 7px; font-size: 10pt; color:black;}")
            self.ui.frame_64.setStyleSheet("QLabel{color:black;}")
            self.ui.frame_77.setStyleSheet("QLabel{font-size:10pt; font-weight: 600; color: black;}")
            self.ui.frame_76.setStyleSheet("QLabel{color:black;}")

            for i in range(self.ui.listWidget_2.count()):
                item = self.ui.listWidget_2.item(i)
                widget = self.ui.listWidget_2.itemWidget(item)
                widget.label.setStyleSheet("QLabel{color:black; font-size: 20px;}")

            self.ui.frame_29.setStyleSheet("#frame_29{background-color: #f7f7f7; border-radius: 10px; border: 2px solid rgb(33,43,51);}")
            self.ui.frame_70.setStyleSheet("QLabel{color:black;}")
            self.ui.label_20.setStyleSheet("QLabel{padding-top: 7px; font-size: 10pt; color:black;}")
            self.ui.frame_65.setStyleSheet("QLabel{color:black;}")

            for i in range(self.ui.listWidget_3.count()):
                item = self.ui.listWidget_3.item(i)
                widget = self.ui.listWidget_3.itemWidget(item)
                widget.label.setStyleSheet("QLabel{color:black; font-size: 20px;}")
            
            self.ui.frame_30.setStyleSheet("#frame_30{background-color: #f7f7f7; border-radius: 10px; border: 2px solid rgb(33,43,51);}")
            self.ui.frame_72.setStyleSheet("QLabel{color:black;}")
            self.ui.label_21.setStyleSheet("QLabel{padding-top: 7px; font-size: 10pt; color:black;}")
            self.ui.frame_66.setStyleSheet("QLabel{color:black;}")

            for i in range(self.ui.listWidget_4.count()):
                item = self.ui.listWidget_4.item(i)
                widget = self.ui.listWidget_4.itemWidget(item)
                widget.label.setStyleSheet("QLabel{color:black; font-size: 20px;}")
            
            self.ui.frame_31.setStyleSheet("#frame_31{background-color: #f7f7f7; border-radius: 10px; border: 2px solid rgb(33,43,51);}")
            self.ui.frame_74.setStyleSheet("QLabel{color:black;}")
            self.ui.label_22.setStyleSheet("QLabel{padding-top: 7px; font-size: 10pt; color:black;}")
            self.ui.frame_67.setStyleSheet("QLabel{color:black;}")

            for i in range(self.ui.listWidget_5.count()):
                item = self.ui.listWidget_5.item(i)
                widget = self.ui.listWidget_5.itemWidget(item)
                widget.label.setStyleSheet("QLabel{color:black; font-size: 20px;}")

            # Kaydetme Sayfası
            lw_6_bg = "#fafafa"
            le_9_bg = "#959c9e"

            # Profilim Sayfası
            self.ui.pushButton_25.setStyleSheet("QPushButton{font-size: 10pt; font-weight: 600; color: black;}")
            self.ui.label_84.setStyleSheet("QLabel{font-weight:600; font-size: 10pt; color: black;}")
            combo_box = "#fafafa"
            self.ui.label_91.setStyleSheet("QLabel{color:black;}")


        if self.toggle.isChecked() == False: # Gece Modu
            # yemekler sayfası
            bg_color = "rgb(33, 43, 51)"
            ust_menu = "rgb(61,80,95)"
            buttons = "rgba(61,80,95,100)"
            stacked_bg = "rgba(61,80,95,100)"
            font_color = "white"
            self.ui.label.setStyleSheet("QLabel{color:white;}")
            self.ui.label_2.setStyleSheet("QLabel{color:white;}")
            self.ui.label_3.setStyleSheet("QLabel{color:white;}")
            self.ui.pushButton_5.setStyleSheet("QPushButton{background-color: white;}")
            self.ui.pushButton_5.setMaximumHeight(20)

            # yemek ekle sayfası
            self.ui.frame_16.setStyleSheet("QLabel{font-weight:600; color:white;}")
            self.ui.label_5.setStyleSheet("QLabel{font-weight:600; color:white;}")
            self.ui.label_6.setStyleSheet("QLabel{font-weight:600; color:white;}")

            # Kalori sayfası
            self.ui.dateTimeEdit.setStyleSheet("QDateTimeEdit{font-size: 12pt; font-weight: 600; background-color: rgba(44, 57, 68, 255); color: white;}")
            self.ui.frame_28.setStyleSheet("#frame_28{background-color:  rgb(33,43,51); border-radius: 10px; border: 2px solid rgb(33,43,51);}")
            self.ui.frame_68.setStyleSheet("QLabel{color:white;}")
            self.ui.label_19.setStyleSheet("QLabel{padding-top: 7px; font-size: 10pt; color:white;}")
            self.ui.frame_64.setStyleSheet("QLabel{color:white;}")
            self.ui.frame_77.setStyleSheet("QLabel{font-size:10pt; font-weight: 600; color: white;}")
            self.ui.frame_76.setStyleSheet("QLabel{color:white;}")

            for i in range(self.ui.listWidget_2.count()):
                item = self.ui.listWidget_2.item(i)
                widget = self.ui.listWidget_2.itemWidget(item)
                widget.label.setStyleSheet("QLabel{color:white; font-size: 20px;}")

            self.ui.frame_29.setStyleSheet("#frame_29{background-color:  rgb(33,43,51); border-radius: 10px; border: 2px solid rgb(33,43,51);}")
            self.ui.frame_70.setStyleSheet("QLabel{color:white;}")
            self.ui.label_20.setStyleSheet("QLabel{padding-top: 7px; font-size: 10pt; color:white;}")
            self.ui.frame_65.setStyleSheet("QLabel{color:white;}")

            for i in range(self.ui.listWidget_3.count()):
                item = self.ui.listWidget_3.item(i)
                widget = self.ui.listWidget_3.itemWidget(item)
                widget.label.setStyleSheet("QLabel{color:white; font-size: 20px;}")
            
            self.ui.frame_30.setStyleSheet("#frame_30{background-color:  rgb(33,43,51); border-radius: 10px; border: 2px solid rgb(33,43,51);}")
            self.ui.frame_72.setStyleSheet("QLabel{color:white;}")
            self.ui.label_21.setStyleSheet("QLabel{padding-top: 7px; font-size: 10pt; color:white;}")
            self.ui.frame_66.setStyleSheet("QLabel{color:white;}")

            for i in range(self.ui.listWidget_4.count()):
                item = self.ui.listWidget_4.item(i)
                widget = self.ui.listWidget_4.itemWidget(item)
                widget.label.setStyleSheet("QLabel{color:white; font-size: 20px;}")
            
            self.ui.frame_31.setStyleSheet("#frame_31{background-color:  rgb(33,43,51); border-radius: 10px; border: 2px solid rgb(33,43,51);}")
            self.ui.frame_74.setStyleSheet("QLabel{color:white;}")
            self.ui.label_22.setStyleSheet("QLabel{padding-top: 7px; font-size: 10pt; color:white;}")
            self.ui.frame_67.setStyleSheet("QLabel{color:white;}")

            for i in range(self.ui.listWidget_5.count()):
                item = self.ui.listWidget_5.item(i)
                widget = self.ui.listWidget_5.itemWidget(item)
                widget.label.setStyleSheet("QLabel{color:white; font-size: 20px;}")

            # Kaydetme Sayfası
            lw_6_bg = "rgba(44,57,68,255)"
            le_9_bg = "rgba(26,34,47,255)"

            # Profilim Sayfası
            self.ui.pushButton_25.setStyleSheet("QPushButton{font-size: 10pt; font-weight: 600; color: white;}")
            self.ui.label_84.setStyleSheet("QLabel{font-weight:600; font-size: 10pt; color: white;}")
            combo_box = "white"
            self.ui.label_91.setStyleSheet("QLabel{color:white;}")

        centralWidgetSheet = """@font-face{
            url:(:/fonts/nova-flat.book.ttf)format("truetype");
        }
        *{
            color: #fff;
            font-family: NovaFlat;
            font-size: 12px;
            border: nine;
            background: none;
        }

        #centralwidget{
            background-color: {BG_COLOR};
        }
        #kalori_sayaci, #frame{
            background-color: {UST_MENU};
        }
        #yemekler, #kalori, #ekle, #select, #log_in, #sign_up, #settings{
            background-color: {STACKED_BG};
        }

        #pushButton_4, #pushButton_6, #pushButton_7{
            background-color:{BUTTONS};
            border-radius: 8px;
            padding: 10px;
            color: {FONT_COLOR};
        }

        #buttons QPushButton{
            background-color: {BUTTONS};
            border-radius: 5px;
            padding: 10px;
            color: {FONT_COLOR};
        }

        #pushButton_4::hover, #buttons QPushButton::hover, #pushButton_6::hover, #pushButton_7::hover{
            background-color: rgb(120,157, 186);
        }"""

        listWidgetSheet = """QListView{
            background: {BUTTONS};
            font-size: 20px;
        }"""

        listWidget_6_Sheet = """QListWidget{
            background: {LW_6_BG};
            font-size: 15pt;
            outline: none;
        }
        QListWidget::item{
            padding-top: 10px;
            padding-bottom: 10px;
            color: {FONT_COLOR};
        }
        QListWidget::item:hover{
            background-color: rgb(174,44,47);
        }
        QListWidget::item:selected{
            background-color: rgb(174,44,47);
        }"""

        lineedit_9_Sheet = """QLineEdit{
            background-color: {LE_9_BG};
            color: {FONT_COLOR};
            font-size: 9pt;
            border-radius: 10px;
            padding-left: 5px;
            height: 30;
        }

        QToolTip{
            color:black;
        }"""

        frame_108_Sheet = """QLineEdit{
            background-color: rgba(0,0,0,0);
            border:none;
            border-bottom: 1px solid {FONT_COLOR};
            color: {FONT_COLOR};
            padding-bottom: 3px;
            font-size: 9pt;
        }

        QLabel{
            font-size: 10pt;
            color: {FONT_COLOR};
        }

        QComboBox{
            color: black;
            font-size: 8pt;
            background: {COMBO_BOX};
        }

        QComboBox QAbstractItemView{
            color: black;
            border: 1px solid black;
        }"""

        newCentralWidget = centralWidgetSheet.replace("{BG_COLOR}", bg_color).replace("{UST_MENU}", ust_menu).replace("{FONT_COLOR}", font_color).replace("{BUTTONS}", buttons).replace("{STACKED_BG}", stacked_bg)
        newListWidget = listWidgetSheet.replace("{BUTTONS}", buttons)
        newListWidget_6 = listWidget_6_Sheet.replace("{LW_6_BG}", lw_6_bg).replace("{FONT_COLOR}", font_color)
        newlineEdit_9 = lineedit_9_Sheet.replace("{LE_9_BG}", le_9_bg).replace("{FONT_COLOR}", font_color)
        newFrame_108 = frame_108_Sheet.replace("{FONT_COLOR}", font_color).replace("{COMBO_BOX}", combo_box)
        self.ui.centralwidget.setStyleSheet(newCentralWidget)
        self.ui.listWidget.setStyleSheet(newListWidget)
        self.ui.listWidget_6.setStyleSheet(newListWidget_6)
        self.ui.lineEdit_9.setStyleSheet(newlineEdit_9)
        self.ui.frame_108.setStyleSheet(newFrame_108)

        self.ui.listWidget.clear()
        self.food_list()

    def log_in(self):
        username = self.ui.lineEdit_10.text()
        password = self.ui.lineEdit_11.text()
        # Veritabanına bağlanalım
        mydb = mysql.connect(host="localhost", user="root", password="Gokalp59", database="kalori_sayaci", port=3306)
        mycursor = mydb.cursor()
        mycursor.execute("SELECT * FROM log_db WHERE BINARY Username = %s AND BINARY Password = %s",(username,password))
        result = mycursor.fetchone()

        if result:
            self.ui.stackedWidget.setCurrentWidget(self.ui.yemekler)
            self.ui.label_3.setText("Yemek Listesi")
            self.ui.buttons.setVisible(True)
            self.ui.label_57.setText(str(result[-4]))
        else:
            self.ui.label_67.setVisible(True)
            self.ui.label_68.setVisible(True)
            
    def sign_up(self):
        fullname = self.ui.lineEdit_12.text()
        tall = self.ui.lineEdit_13.text()
        weight = self.ui.lineEdit_14.text()
        age = self.ui.lineEdit_15.text()
        if self.ui.radioButton.isChecked():
            gender= "Erkek"
        else:
            gender = "Kadın"
        physical = self.ui.comboBox_2.currentText()
        goal = self.ui.comboBox_3.currentText()
        username = self.ui.lineEdit_16.text()
        password = self.ui.lineEdit_17.text()

        # Resmin yolunu alalım
        try:
            photo = self.file_path
        except:
            photo = self.file_path = ""
    
        # Kullanıcının tüm bilgileri eksiksiz yazdığından emin olalım
        if len(tall) != 0 and len(weight) != 0 and len(age) != 0 and len(gender) !=0 and len(physical) != 0 and len(goal) != 0:
            # İlk resmi yükleyelim
            if photo != "":
                destination_path = os.path.join(os.path.dirname(__file__), "faces", username+".jpg")
                shutil.copyfile(photo, destination_path)
                photo=""
            # Veritabanımıza bağlanalım
            mydb = mysql.connect(host="localhost", user="root", password="Gokalp59", database="kalori_sayaci", port=3306)
            mycursor = mydb.cursor()
            # Kullanıcı isminin olup olmadığını kontrol edelim.
            mycursor.execute("SELECT * FROM log_db WHERE BINARY Username=%s",(username,))
            result= mycursor.fetchone()

            if result:
                self.ui.label_74.setPixmap(QPixmap(":/icons/icons/delete-button.png"))
                self.ui.label_75.setText("Bu kullanıcı zaten mevcut.")
            else:
                # Öncelikle olarak makro değerleri hesaplayalım
                kalori, karb, protein, yag = self.mifflinJeorEquation(gender, int(weight), int(tall), int(age), physical, goal)
                self.ui.label_77.setText(str(kalori))
                self.ui.label_79.setText(str(karb))
                self.ui.label_81.setText(str(protein))
                self.ui.label_83.setText(str(yag))

                # Kullanıcıyı veritabanına ekleyelim
                mycursor.execute("INSERT INTO log_db (Fullname, Username, Password, Tall, Weight, Age, Physical, Goal, Gender, Kcal, Carb, Protein, Fat) VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",(fullname, username, password, tall, weight, age, physical, goal, gender, kalori, karb, protein, yag))
                mydb.commit()
                self.ui.frame_96.setVisible(True)
                self.ui.frame_103.setVisible(True)
                self.ui.label_74.setPixmap(QPixmap(":/icons/icons/check.png"))
                self.ui.label_75.setText("Kayıt Başarıyla Tamamlandı. Lütfen Makro Değerlerinizi Kontrol Ediniz.")

        else:
            self.ui.frame_96.setVisible(True)
            self.ui.frame_103.setVisible(False)
            self.ui.label_74.setPixmap(QPixmap(":/icons/icons/delete-button.png"))
            self.ui.label_75.setText("Lütfen tüm bilgileri doldurunuz.")

    def mifflinJeorEquation(self, gender, weight, tall, age, physical, goal):
        if gender == "Erkek":
            bmr = (10 * weight) + (6.25 * tall) - (5 * age) + 5
        else:
            bmr = (10 * weight) + (6.25 * tall) - (5 * age) - 161

        if physical == "Hareketsiz":
            tdee = bmr * 1.2
        elif physical == "Düşük Düzeyde Hareketli":
            tdee = bmr * 1.375
        elif physical == "Orta Düzeyde Hareketli":
            tdee = bmr * 1.55
        elif physical == "Yüksek Düzeyde Hareketli":
            tdee = bmr * 1.725
        elif physical == "Çok Yüksek Düzeyde Hareketli":
            tdee = bmr * 1.9

        if goal == "Zayıflamak":
            tdee = tdee - 300
        elif goal == "Temiz Kilo Almak":
            tdee = tdee + 300
        elif goal == "Kirli Kilo Almak":
            tdee = tdee + 500

        # Makro değerleri
        karbonhidrat = tdee / 8
        protein = tdee / 16
        yag = tdee / 36

        return round(tdee, 2), round(karbonhidrat, 2), round(protein, 2), round(yag, 2)

    def settings(self):
        self.ui.frame_114.setVisible(False)
        self.ui.stackedWidget.setCurrentWidget(self.ui.settings)

        if self.faceid != "":
            self.username = self.faceid
        else:
            self.username = self.ui.lineEdit_10.text()
        # kullanıcının yazdığı değerleri almak için veritabanına bağlanalım
        mydb = mysql.connect(host="localhost", user="root", password="Gokalp59", database="kalori_sayaci", port=3306)
        mycursor = mydb.cursor()
        mycursor.execute("SELECT * FROM log_db WHERE BINARY Username = %s",(self.username,))
        result = mycursor.fetchone()

        name = result[0]
        tall = result[3]
        weight = result[4]
        age = result[5]
        activity = result[6]
        goal = result[7]
        self.gender = result[8]

        if self.gender == "Erkek":
            self.ui.label_85.setPixmap(QPixmap(":/icons/icons/man.png"))
        else:
            self.ui.label_85.setPixmap(QPixmap(":/icons/icons/human.png"))

        # Çektiğimiz verileri ekrana bastıralım
        self.ui.label_84.setText("Tekrar Hoşgeldiniz, "+ name)
        self.ui.lineEdit_18.setText(str(tall))
        self.ui.lineEdit_19.setText(str(weight))
        self.ui.lineEdit_20.setText(str(age))
        self.ui.comboBox_4.setCurrentText(activity)
        self.ui.comboBox_5.setCurrentText(goal)

        self.ui.pushButton_25.clicked.connect(lambda: self.user_settings())

    def user_settings(self):
        new_tall = int(self.ui.lineEdit_18.text())
        new_weight = int(self.ui.lineEdit_19.text())
        new_age = int(self.ui.lineEdit_20.text())
        new_activity = self.ui.comboBox_4.currentText()
        new_goal = self.ui.comboBox_5.currentText()

        new_kalori, new_karb, new_protein, new_yag = self.mifflinJeorEquation(self.gender, new_weight, new_tall, new_age, new_activity, new_goal)
        self.ui.label_57.setText(str(new_kalori))
        # yeni değerleri database yazalım
        mydb = mysql.connect(host="localhost", user="root", password="Gokalp59", database="kalori_sayaci", port=3306)
        mycursor = mydb.cursor()
        mycursor.execute("UPDATE log_db SET Tall = %s, Weight = %s, Age = %s, Physical = %s, Goal = %s, Kcal = %s, Carb = %s, Protein = %s, Fat = %s WHERE BINARY Username = %s", (new_tall, new_weight, new_age, new_activity, new_goal, new_kalori, new_karb, new_protein, new_yag, self.username))
        mydb.commit()

        self.ui.frame_114.setVisible(True)

    def show_password(self, checked):
        if checked:
            self.ui.lineEdit_11.setEchoMode(QtWidgets.QLineEdit.Normal)
            self.ui.pushButton_19.setIcon(QIcon(":/icons/icons/hide.png"))
        else:
            self.ui.lineEdit_11.setEchoMode(QtWidgets.QLineEdit.Password)
            self.ui.pushButton_19.setIcon(QIcon(":/icons/icons/view.png"))

    def photo(self):
        options = QFileDialog.Options()
        self.file_path, _ = QFileDialog.getOpenFileName(self, "Resim Seç", "", "Image Files (*jpg)", options=options)
        self.ui.pushButton_22.setText(self.file_path.split("/")[-1])

    def clear_lines_for_sign_up(self):
        self.ui.lineEdit_12.clear()
        self.ui.lineEdit_13.clear()
        self.ui.lineEdit_14.clear()
        self.ui.lineEdit_15.clear()
        self.ui.radioButton.setAutoExclusive(False)
        self.ui.radioButton_2.setAutoExclusive(False)
        self.ui.radioButton.setChecked(False)
        self.ui.radioButton_2.setChecked(False)
        self.ui.radioButton.setAutoExclusive(True)
        self.ui.radioButton_2.setAutoExclusive(True)
        self.ui.comboBox_2.setCurrentText("Hareketsiz")
        self.ui.comboBox_3.setCurrentText("Zayıflamak")
        self.ui.lineEdit_16.clear()
        self.ui.lineEdit_17.clear()
        self.ui.pushButton_22.setText("Lütfen resminizi yükleyiniz")
        self.ui.frame_96.setVisible(False)
        self.ui.stackedWidget.setCurrentWidget(self.ui.sign_up)

    def food_list(self):
        self.yemekler = pd.read_json("yemekler.json")
        self.yemekler = self.yemekler.sort_values(by="Yemek").reset_index(drop=True)
        self.yemek_isimleri = self.yemekler["Yemek"].values
        self.yemek_degerleri = self.yemekler[["Yemek", "Kalori", "Karbonhidrat (g)", "Protein (g)", "Yağ (g)"]].values
        

        for i in range(len(self.yemekler)):
            yemek = self.yemekler.loc[i]
            kalori = yemek["Kalori"]
            karb = yemek["Karbonhidrat (g)"]
            protein = yemek["Protein (g)"]
            yag = yemek["Yağ (g)"]
            toplam = karb + protein + yag
            
            if self.toggle.isChecked() == True: # Aydınlık Modu
                widget = MyWidget(color="black")
            if self.toggle.isChecked() == False: # Gece Modu
                widget = MyWidget()
            widget.barvalues([(karb/toplam*100), (protein/toplam*100), (100 - (karb/toplam*100) - (protein/toplam*100))])
            widget.set_image("images/{}.jpg".format(yemek["Yemek"]))
            widget.set_Text(yemek["Yemek"].upper(), kalori, karb, protein, yag)

            item = QListWidgetItem()
            item.setSizeHint(QSize(0,170))
            self.ui.listWidget.addItem(item)
            self.ui.listWidget.setItemWidget(item, widget)

    def filter(self):
        typed = self.ui.lineEdit.text()
        yemek_isimleri = self.yemekler["Yemek"].values

        data = np.array([])

        for item in yemek_isimleri:
            if typed.lower() in item.lower():
                data = np.append(data, item)

        # Kalori, karb, protein, yağ verilerini alalım
        self.filtered = []
        for yemek_isimleri in data:
            for veri in self.yemek_degerleri:
                if veri[0] == yemek_isimleri:
                    self.filtered.append(veri)

        self.ui.listWidget.clear()

        for i in self.filtered:
            toplam = i[2] + i[3] + i[4]
            if self.toggle.isChecked() == True: # Aydınlık Modu
                widget = MyWidget(color="black")
            if self.toggle.isChecked() == False: # Gece Modu
                widget = MyWidget()
            widget.barvalues([(i[2]/toplam*100), (i[3]/toplam*100), (100 - (i[2]/toplam*100) - (i[3]/toplam*100))])
            widget.set_image("images/{}.jpg".format(i[0]))
            widget.set_Text(i[0].upper(), i[1], i[2], i[3], i[4])

            item = QListWidgetItem()
            item.setSizeHint(QSize(0,170))
            self.ui.listWidget.addItem(item)
            self.ui.listWidget.setItemWidget(item, widget)

    def add_food_func(self):
        if self.lastButtonPressed == "Yemek Ekle":
            # Kullanıcının yemek adı, kalori, karb, protein, yağ değerlerini boş bırakma ihtimalini inceleyelim.
            if len(self.ui.lineEdit_2.text()) == 0 or len(self.ui.lineEdit_5.text()) == 0 or len(self.ui.lineEdit_6.text()) == 0 or len(self.ui.lineEdit_7.text()) == 0 or len(self.ui.lineEdit_8.text()) == 0:
                self.popup("Lütfen gerekli bilgileri doldurunuz.")

            else:
                yemek_adı = self.ui.lineEdit_2.text().capitalize()
                tur = self.ui.lineEdit_3.text()
                marka = self.ui.lineEdit_4.text()
                try:
                    kalori = np.float64(self.ui.lineEdit_5.text())
                    karb = np.float64(self.ui.lineEdit_6.text())
                    protein = np.float64(self.ui.lineEdit_7.text())
                    yag = np.float64(self.ui.lineEdit_8.text())
                except ValueError:
                    self.popup("Lütfen kalori, karbonhidrat, protein ve yağ değerleri için bir sayı giriniz.")
                    return

                lower_names = np.array([x.capitalize() if isinstance(x, str) else x for x in self.yemekler["Yemek"].values])

                if yemek_adı not in lower_names:
                    dict ={
                        "Tür": tur,
                        "Yemek": yemek_adı,
                        "Marka": marka,
                        "Kalori": kalori,
                        "Karbonhidrat (g)": karb,
                        "Protein (g)": protein,
                        "Yağ (g)": yag}
                    
                    df_dict = pd.DataFrame([dict])
                    self.yemekler = pd.concat([self.yemekler, df_dict], ignore_index = True)

                    self.yemekler.to_json(path_or_buf=r"C:\Users\kasap\Desktop\kalori_sayaci\yemekler.json", force_ascii=False)

                    # Yemeğin resmini ekle
                    if self.image_path != "":
                        file_name = yemek_adı + ".jpg"
                        destination_path = os.path.join(os.path.dirname(__file__), "images", file_name)
                        shutil.copyfile(self.image_path, destination_path)
                        self.image_path = ""

                    self.ui.listWidget.clear()
                    self.food_list()

                    #tüm satırları temizleyelim.
                    self.clear_lines()
                    self.ui.stackedWidget.setCurrentWidget(self.ui.yemekler)

                else:
                    self.popup("Bu yemek zaten ekli.")

    def delete_food_button(self):
        curr_click = self.ui.listWidget.currentRow()
        delete_food_path = "images/" + self.yemekler["Yemek"].values[curr_click] + ".jpg"
        if os.path.exists(delete_food_path):
            os.remove(delete_food_path)
        self.ui.listWidget.takeItem(curr_click)
        self.yemekler = self.yemekler.drop(curr_click)
        self.yemekler = self.yemekler.reset_index(drop=True)
        self.yemekler.to_json(path_or_buf=r"C:\Users\kasap\Desktop\kalori_sayaci\yemekler.json", force_ascii=False)

    def update_food_button(self):
        self.lastButtonPressed = "Değerleri Güncelle"
        self.ui.frame_13.setMaximumHeight(0)
        self.ui.pushButton_8.clicked.connect(lambda: self.closePopup())
        # İzliyeceğimiz yol: Güncellenen yemeği önce sil sonra güncellenmiş halini ekleyelim
        self.ui.stackedWidget.setCurrentWidget(self.ui.ekle)
        self.ui.pushButton_7.clicked.connect(lambda: self.page_1())
        self.ui.pushButton_6.clicked.connect(lambda: self.update_food_infos())
        self.ui.label_6.mousePressEvent = self.open_file_dialog

        # Dashed line kısmını silelim
        self.ui.frame_15.setStyleSheet("")
        
        # Seçilen yemeğin önceki değerlerini ekrana yazdıralım
        selected_item = self.ui.listWidget.currentItem()
        if selected_item:
            widget = self.ui.listWidget.itemWidget(selected_item)
            if isinstance(widget, MyWidget):
                image_path = widget.image_path
                food_name = widget.label_10.text()
                self.selected_food_infos = self.yemekler[self.yemekler["Yemek"].str.upper() == food_name].values[0]

                self.ui.lineEdit_2.setText(self.selected_food_infos[1]) # Yemek ismi
                self.ui.lineEdit_3.setText(self.selected_food_infos[0]) # Yemek türü
                self.ui.lineEdit_4.setText(self.selected_food_infos[-5]) # Yemek markası
                self.ui.lineEdit_5.setText(str(self.selected_food_infos[-4])) # Toplam kalori
                self.ui.lineEdit_6.setText(str(self.selected_food_infos[-3])) # Toplam karbonhidrat
                self.ui.lineEdit_7.setText(str(self.selected_food_infos[-2])) # Toplam protein
                self.ui.lineEdit_8.setText(str(self.selected_food_infos[-1])) # Toplam yağ

                # Resmi ekleyelim
                if os.path.exists(image_path):
                    self.ui.label_6.setPixmap(QPixmap(image_path).scaled(500,500))
                else:
                    self.ui.label_6.setPixmap(QPixmap("images/No image.jpg").scaled(500,500))
        
    def update_food_infos(self):
        if self.lastButtonPressed == "Değerleri Güncelle":
            # Kullanıcının yazdığı değerleri alalım
            yeni_yemek_adı = self.ui.lineEdit_2.text()
            yeni_tur = self.ui.lineEdit_3.text()
            yeni_marka = self.ui.lineEdit_4.text()
            yeni_kalori = float(self.ui.lineEdit_5.text())
            yeni_karb = float(self.ui.lineEdit_6.text())
            yeni_protein = float(self.ui.lineEdit_7.text())
            yeni_yag = float(self.ui.lineEdit_8.text())

            # eski değerleri alalım
            onceki_yemek_adı = self.selected_food_infos[1]
            onceki_tur = self.selected_food_infos[0]
            onceki_marka = self.selected_food_infos[-5]
            onceki_kalori = self.selected_food_infos[-4]
            onceki_karb = self.selected_food_infos[-3]
            onceki_protein = self.selected_food_infos[-2]
            onceki_yag = self.selected_food_infos[-1]

            if yeni_marka == "":
                yeni_marka = None

            # yazılardan önce kullanıcı resim eklemiş olabilir. Bunu güncelleyelim
            if self.image_path != "":
                file_name = yeni_yemek_adı + ".jpg"
                destination_path = os.path.join(os.path.dirname(__file__), "images", file_name)
                shutil.copyfile(self.image_path, destination_path)
                self.image_path = ""
                self.ui.stackedWidget.setCurrentWidget(self.ui.yemekler)
                self.ui.listWidget.clear()
                self.food_list()

            # Kullanıcı değer değiştirmiş mi kontrol edelim
            if onceki_yemek_adı != yeni_yemek_adı or onceki_tur != yeni_tur or onceki_marka != yeni_marka or onceki_kalori != yeni_kalori or onceki_karb != yeni_karb or onceki_protein != yeni_protein or onceki_yag != yeni_yag:
                # Yemeğin indexini alma
                index = self.yemekler[self.yemekler["Yemek"] == onceki_yemek_adı].index[0]
                self.yemekler.iloc[index] = [yeni_tur, yeni_yemek_adı, None, None, yeni_marka, yeni_kalori, yeni_karb, yeni_protein, yeni_yag]
                self.yemekler.to_json(path_or_buf=r"C:\Users\kasap\Desktop\kalori_sayaci\yemekler.json")

                self.ui.stackedWidget.setCurrentWidget(self.ui.yemekler)
                self.ui.listWidget.clear()
                self.food_list()
            else:
                self.popup("Lütfen değişiklik yapınız veya vazgeç butonuna tıklayınız.")

    def open_file_dialog(self, event):
        if event.button() == Qt.LeftButton:
            options = QFileDialog.Options()
            file_path, _ = QFileDialog.getOpenFileName(self, "Resim Seç", "", "Image Files (*.jpg)", options=options)

            if file_path:
                self.ui.frame_15.setStyleSheet("")
                self.image_path = file_path
                pixmap = QPixmap(file_path)
                max_width = 500
                max_height = 500
                if pixmap.width() > max_width or pixmap.height() > max_height:
                    pixmap = pixmap.scaled(max_width, max_height, Qt.KeepAspectRatio)

                self.ui.label_6.setPixmap(pixmap)
        event.accept()

    def context_menu(self, event):
        if event.type() == QEvent.ContextMenu:
            context_menu = QMenu(self)
            delete_food = context_menu.addAction("Yemeği Kaldır")
            delete_food.triggered.connect(self.delete_food_button)
            update_values = context_menu.addAction("Değerleri Güncelle")
            update_values.triggered.connect(self.update_food_button)
            context_menu.exec_(event.globalPos())
            
            return True
        return super().context_menu(event)
    
    def eventFilter(self, source, event):
        if event.type() == QEvent.ContextMenu and source is self.ui.listWidget:
            return self.context_menu(event)
        return super().eventFilter(source, event)

    def slideLeftMenu(self):
        width = self.ui.menu.width()

        if width == 0:
            newWidth = 200
        else:
            newWidth = 0

        self.animation = QPropertyAnimation(self.ui.menu, b"maximumWidth") 
        self.animation.setDuration(250)
        self.animation.setStartValue(width)
        self.animation.setEndValue(newWidth)
        self.animation.setEasingCurve(QEasingCurve.InOutQuart)
        self.animation.start()
    
    def popup(self, hata):
        self.ui.frame_13.setMaximumHeight(0)

        newHeight = 15
        # Hata mesajını göster
        self.ui.pushButton_8.setText(hata)

        self.animation = QPropertyAnimation(self.ui.frame_13, b"maximumHeight") 
        self.animation.setDuration(250)
        self.animation.setStartValue(0)
        self.animation.setEndValue(newHeight)
        self.animation.setEasingCurve(QEasingCurve.InOutQuart)
        self.animation.start()

    def closePopup(self):
        if self.ui.frame_13.height() == 15:
            self.animation = QPropertyAnimation(self.ui.frame_13, b"maximumHeight") 
            self.animation.setDuration(250)
            self.animation.setStartValue(15)
            self.animation.setEndValue(0)
            self.animation.setEasingCurve(QEasingCurve.InOutQuart)
            self.animation.start()

    def clear_lines(self):
        self.ui.lineEdit_2.clear()
        self.ui.lineEdit_3.clear()
        self.ui.lineEdit_4.clear()
        self.ui.lineEdit_5.clear()
        self.ui.lineEdit_6.clear()
        self.ui.lineEdit_7.clear()
        self.ui.lineEdit_8.clear()
        self.ui.label_6.setPixmap(None)
        self.ui.label_6.setText("Resmi seçmek için tıklayınız.")
        self.ui.frame_15.setStyleSheet("""#frame_15{border: 2px dashed #aaa;}""")

    def updateDateTime(self):
        currentDateTime = QDateTime.currentDateTime()
        self.ui.dateTimeEdit.setDateTime(currentDateTime)
                
        hour = currentDateTime.time().hour()
        minute = currentDateTime.time().minute()
        second = currentDateTime.time().second()

        if hour == 15 and minute == 17 and second == 0:
            self.show_tray_message()

    def select(self):
        self.ui.stackedWidget.setCurrentWidget(self.ui.select)
        # Yemek türlerini comboboxa ekleyelim
        self.ui.comboBox.clear()
        combo_tur = set(self.yemekler["Tür"]) # Değerleri bir kez tutalım diye kümeleri kullanalım
        combo_tur.add("Tüm Yemekler")
        combo_tur.remove("")
        self.ui.comboBox.addItems(list(combo_tur))
        self.ui.comboBox.setCurrentText("Tüm Yemekler")
        self.sender_ = self.sender().objectName()

        self.ui.comboBox.currentTextChanged.connect(self.comboBoxFunction)
  
    def comboBoxFunction(self):
        # Kullanıcı tarafından seçilen türe ait yemekleri listeleyelim.
        selected_tur = self.ui.comboBox.currentText()
        if selected_tur == "Tüm Yemekler":
            selected_yemekler = self.yemekler["Yemek"]
        else:
            selected_yemekler = self.yemekler["Yemek"][self.yemekler["Tür"].str.contains(selected_tur)] # türe ait yemek isimlerini aldık

        self.ui.listWidget_6.clear()
        for yemek in selected_yemekler:
            item = QListWidgetItem(yemek)
            self.ui.listWidget_6.addItem(item)

        self.ui.pushButton_17.clicked.connect(self.daily, Qt.UniqueConnection)

    def daily(self):
        self.ui.stackedWidget.setCurrentWidget(self.ui.kalori)
        
        if self.sender_ == "pushButton_9":
            self.ui.frame_64.setVisible(True) # kalori kısmını gösterdik
            self.ui.frame_49.setVisible(True) # sayısal değerleri gösterdik 
            self.ui.listWidget_2.setVisible(True) # list widgetın kendisini gösterdik
            self.ui.frame_48.setStyleSheet("#frame_48{border-bottom: 1px solid rgba(0,0,0,240);}") # Alt siyah çizgiyi tekrar ekledik
            if self.toggle.isChecked():
                self.ui.label_19.setStyleSheet("QLabel{font-size:10pt; color: black;}")
            else:
                self.ui.label_19.setStyleSheet("QLabel{font-size:10pt; color: white;}")
            self.ui.pushButton_9.setStyleSheet("")
            self.ui.frame_28.setMaximumHeight(16777215) # Ana frame'ın yüksekliğini ayarlayalım
            self.ui.frame_33.setMaximumHeight(16777215)

        elif self.sender_ == "pushButton_10":
            self.ui.frame_65.setVisible(True) # kalori kısmını gösterdik
            self.ui.frame_51.setVisible(True) # sayısal değerleri gösterdik 
            self.ui.listWidget_3.setVisible(True) # list widgetın kendisini gösterdik
            self.ui.frame_50.setStyleSheet("#frame_50{border-bottom: 1px solid rgba(0,0,0,240);}") # Alt siyah çizgiyi tekrar ekledik
            if self.toggle.isChecked():
                self.ui.label_20.setStyleSheet("QLabel{font-size:10pt; color: black;}")
            else:
                self.ui.label_20.setStyleSheet("QLabel{font-size:10pt; color: white;}")
            self.ui.pushButton_10.setStyleSheet("")
            self.ui.frame_29.setMaximumHeight(16777215) # Ana frame'ın yüksekliğini ayarlayalım
            self.ui.frame_35.setMaximumHeight(16777215)

        elif self.sender_ == "pushButton_11":
            self.ui.frame_66.setVisible(True) # kalori kısmını gösterdik
            self.ui.frame_53.setVisible(True) # sayısal değerleri gösterdik 
            self.ui.listWidget_4.setVisible(True) # list widgetın kendisini gösterdik
            self.ui.frame_52.setStyleSheet("#frame_52{border-bottom: 1px solid rgba(0,0,0,240);}") # Alt siyah çizgiyi tekrar ekledik
            if self.toggle.isChecked():
                self.ui.label_21.setStyleSheet("QLabel{font-size:10pt; color: black;}")
            else:
                self.ui.label_21.setStyleSheet("QLabel{font-size:10pt; color: white;}")
            self.ui.pushButton_11.setStyleSheet("")
            self.ui.frame_30.setMaximumHeight(16777215) # Ana frame'ın yüksekliğini ayarlayalım
            self.ui.frame_37.setMaximumHeight(16777215)

        elif self.sender_ == "pushButton_12":
            self.ui.frame_67.setVisible(True) # kalori kısmını gösterdik
            self.ui.frame_55.setVisible(True) # sayısal değerleri gösterdik 
            self.ui.listWidget_5.setVisible(True) # list widgetın kendisini gösterdik
            self.ui.frame_54.setStyleSheet("#frame_54{border-bottom: 1px solid rgba(0,0,0,240);}") # Alt siyah çizgiyi tekrar ekledik
            if self.toggle.isChecked():
                self.ui.label_22.setStyleSheet("QLabel{font-size:10pt; color: black;}")
            else:
                self.ui.label_22.setStyleSheet("QLabel{font-size:10pt; color: white;}")
            self.ui.pushButton_12.setStyleSheet("")
            self.ui.frame_31.setMaximumHeight(16777215) # Ana frame'ın yüksekliğini ayarlayalım
            self.ui.frame_39.setMaximumHeight(16777215)

        miktar = float(self.ui.lineEdit_9.text())
        selected_items = self.ui.listWidget_6.selectedItems()
        if selected_items:
            self.ui.pushButton_13.toggled.connect(self.food_menu)
            self.ui.pushButton_14.toggled.connect(self.food_menu)
            self.ui.pushButton_15.toggled.connect(self.food_menu)
            self.ui.pushButton_16.toggled.connect(self.food_menu)

            for item in selected_items:
                foods = self.yemekler[self.yemekler["Yemek"] == item.text()].values
                yemek_ismi = foods[0][1]
                kalori = foods[0][-4] * miktar /100
                karbonhidrat = foods[0][-3] * miktar /100
                protein = foods[0][-2] * miktar /100
                yag = foods[0][-1] * miktar /100

                if self.sender_ == "pushButton_9":
                    #self.ui.listWidget_2.addItem(QListWidgetItem(yemek_ismi))
                    if self.toggle.isChecked():
                        self.widget = FoodList(color="black")
                    else:
                        self.widget = FoodList()
                    self.widget.set_text(yemek_ismi)
                    item = QListWidgetItem()
                    item.setSizeHint(QSize(0, 50))
                    self.ui.listWidget_2.addItem(item)
                    self.ui.listWidget_2.setItemWidget(item, self.widget)
                    self.kahvalti_kalori += kalori
                    self.kahvalti_karb += karbonhidrat
                    self.kahvalti_protein += protein
                    self.kahvalti_yag += yag
                    self.ui.label_24.setText(str(round(self.kahvalti_kalori,2)))
                    self.ui.label_32.setText(str(round(self.kahvalti_karb,2)))
                    self.ui.label_34.setText(str(round(self.kahvalti_protein,2)))
                    self.ui.label_36.setText(str(round(self.kahvalti_yag,2)))

                    # Eğer kullanıcı aynı yemeği tekrar seçerse bunu sadece bir kez ekranda gösterelim
                    if yemek_ismi in self.kahvalti["Yemekler"]: # Kullanıcının aynı yemeği ekleme durumu
                        self.ui.listWidget_2.takeItem(self.ui.listWidget_2.count() - 1)
                        index = self.kahvalti["Yemekler"].index(yemek_ismi)
                        self.kahvalti["Miktar"][index] += miktar
                        
                    if yemek_ismi not in self.kahvalti["Yemekler"]: # Kullanıcının ilk defa bu yemeği ekleme durumu
                        self.kahvalti["Yemekler"].append(yemek_ismi)
                        self.kahvalti["Miktar"].append(miktar)
     
                elif self.sender_ == "pushButton_10":
                    #self.ui.listWidget_3.addItem(QListWidgetItem(yemek_ismi))
                    if self.toggle.isChecked():
                        self.widget = FoodList(color="black")
                    else:
                        self.widget = FoodList()
                    self.widget.set_text(yemek_ismi)
                    item = QListWidgetItem()
                    item.setSizeHint(QSize(0, 50))
                    self.ui.listWidget_3.addItem(item)
                    self.ui.listWidget_3.setItemWidget(item, self.widget)
                    self.ogle_kalori += kalori
                    self.ogle_karb += karbonhidrat
                    self.ogle_protein += protein
                    self.ogle_yag += yag
                    self.ui.label_25.setText(str(round(self.ogle_kalori,2)))
                    self.ui.label_37.setText(str(round(self.ogle_karb,2)))
                    self.ui.label_39.setText(str(round(self.ogle_protein,2)))
                    self.ui.label_41.setText(str(round(self.ogle_yag,2)))

                    # Eğer kullanıcı aynı yemeği tekrar seçerse bunu sadece bir kez ekranda gösterelim
                    if yemek_ismi in self.ogle["Yemekler"]: # Kullanıcının aynı yemeği ekleme durumu
                        self.ui.listWidget_3.takeItem(self.ui.listWidget_3.count() - 1)
                        index = self.ogle["Yemekler"].index(yemek_ismi)
                        self.ogle["Miktar"][index] += miktar
                        
                    if yemek_ismi not in self.ogle["Yemekler"]: # Kullanıcının ilk defa bu yemeği ekleme durumu
                        self.ogle["Yemekler"].append(yemek_ismi)
                        self.ogle["Miktar"].append(miktar)

                elif self.sender_ == "pushButton_11":
                    #self.ui.listWidget_4.addItem(QListWidgetItem(yemek_ismi))
                    if self.toggle.isChecked():
                        self.widget = FoodList(color="black")
                    else:
                        self.widget = FoodList()
                    self.widget.set_text(yemek_ismi)
                    item = QListWidgetItem()
                    item.setSizeHint(QSize(0, 50))
                    self.ui.listWidget_4.addItem(item)
                    self.ui.listWidget_4.setItemWidget(item, self.widget)
                    self.aksam_kalori += kalori
                    self.aksam_karb += karbonhidrat
                    self.aksam_protein += protein
                    self.aksam_yag += yag
                    self.ui.label_27.setText(str(round(self.aksam_kalori,2)))
                    self.ui.label_44.setText(str(round(self.aksam_karb,2)))
                    self.ui.label_45.setText(str(round(self.aksam_protein,2)))
                    self.ui.label_48.setText(str(round(self.aksam_yag,2)))

                    # Eğer kullanıcı aynı yemeği tekrar seçerse bunu sadece bir kez ekranda gösterelim
                    if yemek_ismi in self.aksam["Yemekler"]: # Kullanıcının aynı yemeği ekleme durumu
                        self.ui.listWidget_4.takeItem(self.ui.listWidget_4.count() - 1)
                        index = self.aksam["Yemekler"].index(yemek_ismi)
                        self.aksam["Miktar"][index] += miktar
                        
                    if yemek_ismi not in self.aksam["Yemekler"]: # Kullanıcının ilk defa bu yemeği ekleme durumu
                        self.aksam["Yemekler"].append(yemek_ismi)
                        self.aksam["Miktar"].append(miktar)

                elif self.sender_ == "pushButton_12":
                    #self.ui.listWidget_5.addItem(QListWidgetItem(yemek_ismi))
                    if self.toggle.isChecked():
                        self.widget = FoodList(color="black")
                    else:
                        self.widget = FoodList()
                    self.widget.set_text(yemek_ismi)
                    item = QListWidgetItem()
                    item.setSizeHint(QSize(0, 50))
                    self.ui.listWidget_5.addItem(item)
                    self.ui.listWidget_5.setItemWidget(item, self.widget)
                    self.ara_kalori += kalori
                    self.ara_karb += karbonhidrat
                    self.ara_protein += protein
                    self.ara_yag += yag
                    self.ui.label_29.setText(str(round(self.ara_kalori,2)))
                    self.ui.label_50.setText(str(round(self.ara_karb,2)))
                    self.ui.label_52.setText(str(round(self.ara_protein,2)))
                    self.ui.label_54.setText(str(round(self.ara_yag,2)))

                    # Eğer kullanıcı aynı yemeği tekrar seçerse bunu sadece bir kez ekranda gösterelim
                    if yemek_ismi in self.ara["Yemekler"]: # Kullanıcının aynı yemeği ekleme durumu
                        self.ui.listWidget_5.takeItem(self.ui.listWidget_5.count() - 1)
                        index = self.ara["Yemekler"].index(yemek_ismi)
                        self.ara["Miktar"][index] += miktar
                        
                    if yemek_ismi not in self.ara["Yemekler"]: # Kullanıcının ilk defa bu yemeği ekleme durumu
                        self.ara["Yemekler"].append(yemek_ismi)
                        self.ara["Miktar"].append(miktar)

            self.daily_kalori += kalori
            self.daily_karb += karbonhidrat
            self.daily_protein += protein
            self.daily_yag += yag

            self.ui.label_58.setText(str(round(self.daily_kalori, 2)))
            self.ui.label_60.setText(str(round(self.daily_karb, 2)))
            self.ui.label_62.setText(str(round(self.daily_protein, 2)))
            self.ui.label_64.setText(str(round(self.daily_yag, 2)))

            self.ui.listWidget_2.itemDoubleClicked.connect(self.delete, Qt.UniqueConnection)
            self.ui.listWidget_3.itemDoubleClicked.connect(self.delete, Qt.UniqueConnection)
            self.ui.listWidget_4.itemDoubleClicked.connect(self.delete, Qt.UniqueConnection)
            self.ui.listWidget_5.itemDoubleClicked.connect(self.delete, Qt.UniqueConnection)

            if self.daily_kalori >= self.ihtiyac_kalori:
                self.tray_icon.showMessage(
                    "Hedefine Ulaştın!",
                    "Tebrikler. Günlük kalori ihtiyacına ulaştın. Artık yemeği bırakma zamanı.",
                    QSystemTrayIcon.Information,
                    5000
                )

            self.userData()

    def food_menu(self):
        if self.sender().objectName() == "pushButton_13":
            if self.ui.pushButton_13.isChecked(): # Menüyü kapatma
                self.ui.pushButton_13.setIcon(QIcon(":/icons/icons/arrow-up-sign-to-navigate.png"))
                self.ui.frame_28.setMaximumHeight(105)
                self.ui.listWidget_2.setVisible(False)
            else: # Menüyü açma
                self.ui.pushButton_13.setIcon(QIcon(":/icons/icons/arrow-down-sign-to-navigate.png"))
                self.ui.frame_28.setMaximumHeight(16777215)
                self.ui.listWidget_2.setVisible(True)

        if self.sender().objectName() == "pushButton_14":
            if self.ui.pushButton_14.isChecked(): # Menüyü kapatma
                self.ui.pushButton_14.setIcon(QIcon(":/icons/icons/arrow-up-sign-to-navigate.png"))
                self.ui.frame_29.setMaximumHeight(105)
                self.ui.listWidget_3.setVisible(False)
            else: # Menüyü açma
                self.ui.pushButton_14.setIcon(QIcon(":/icons/icons/arrow-down-sign-to-navigate.png"))
                self.ui.frame_29.setMaximumHeight(16777215)
                self.ui.listWidget_3.setVisible(True)

        if self.sender().objectName() == "pushButton_15":
            if self.ui.pushButton_15.isChecked(): # Menüyü kapatma
                self.ui.pushButton_15.setIcon(QIcon(":/icons/icons/arrow-up-sign-to-navigate.png"))
                self.ui.frame_30.setMaximumHeight(105)
                self.ui.listWidget_4.setVisible(False)
            else: # Menüyü açma
                self.ui.pushButton_15.setIcon(QIcon(":/icons/icons/arrow-down-sign-to-navigate.png"))
                self.ui.frame_30.setMaximumHeight(16777215)
                self.ui.listWidget_4.setVisible(True)

        if self.sender().objectName() == "pushButton_16":
            if self.ui.pushButton_16.isChecked(): # Menüyü kapatma
                self.ui.pushButton_16.setIcon(QIcon(":/icons/icons/arrow-up-sign-to-navigate.png"))
                self.ui.frame_31.setMaximumHeight(105)
                self.ui.listWidget_5.setVisible(False)
            else: # Menüyü açma
                self.ui.pushButton_16.setIcon(QIcon(":/icons/icons/arrow-down-sign-to-navigate.png"))
                self.ui.frame_31.setMaximumHeight(16777215)
                self.ui.listWidget_5.setVisible(True)

    def delete(self):
        # Silme butonunun açılıp kapanma fonksiyonun yazıldığı kısım
        if self.sender().objectName() == "listWidget_2":
            # Kullanıcının seçtiği itemı al
            selected_item = self.ui.listWidget_2.currentItem()
            if selected_item:
                widget = self.ui.listWidget_2.itemWidget(selected_item)
                if widget.frame_2.width() == 0:
                    self.animation_1 = QPropertyAnimation(widget.frame_2, b"minimumWidth")
                    self.animation_1.setDuration(250)
                    self.animation_1.setStartValue(0)
                    self.animation_1.setEndValue(150)
                    self.animation_1.setEasingCurve(QEasingCurve.InOutQuart)
                    self.animation_1.start()

                    widget.pushButton.clicked.connect(lambda: self.delete_values_kahvalti())
            
            # Hataları gidermek için tüm açık olan silme butonlarını kapatalım
            for i in range(self.ui.listWidget_2.count()):
                item = self.ui.listWidget_2.item(i)
                widget = self.ui.listWidget_2.itemWidget(item)
                if widget.frame_2.width() == 150:
                    self.animation_2 = QPropertyAnimation(widget.frame_2, b"minimumWidth")
                    self.animation_2.setDuration(250)
                    self.animation_2.setStartValue(150)
                    self.animation_2.setEndValue(0)
                    self.animation_2.setEasingCurve(QEasingCurve.InOutQuart)
                    self.animation_2.start()

        if self.sender().objectName() == "listWidget_3":
            # Kullanıcının seçtiği itemı al
            selected_item = self.ui.listWidget_3.currentItem()
            if selected_item:
                widget = self.ui.listWidget_3.itemWidget(selected_item)
                if widget.frame_2.width() == 0:
                    self.animation_1 = QPropertyAnimation(widget.frame_2, b"minimumWidth")
                    self.animation_1.setDuration(250)
                    self.animation_1.setStartValue(0)
                    self.animation_1.setEndValue(150)
                    self.animation_1.setEasingCurve(QEasingCurve.InOutQuart)
                    self.animation_1.start()

                    widget.pushButton.clicked.connect(lambda: self.delete_values_ogle())
            
            # Hataları gidermek için tüm açık olan silme butonlarını kapatalım
            for i in range(self.ui.listWidget_3.count()):
                item = self.ui.listWidget_3.item(i)
                widget = self.ui.listWidget_3.itemWidget(item)
                if widget.frame_2.width() == 150:
                    self.animation_2 = QPropertyAnimation(widget.frame_2, b"minimumWidth")
                    self.animation_2.setDuration(250)
                    self.animation_2.setStartValue(150)
                    self.animation_2.setEndValue(0)
                    self.animation_2.setEasingCurve(QEasingCurve.InOutQuart)
                    self.animation_2.start()

        if self.sender().objectName() == "listWidget_4":
            # Kullanıcının seçtiği itemı al
            selected_item = self.ui.listWidget_4.currentItem()
            if selected_item:
                widget = self.ui.listWidget_4.itemWidget(selected_item)
                if widget.frame_2.width() == 0:
                    self.animation_1 = QPropertyAnimation(widget.frame_2, b"minimumWidth")
                    self.animation_1.setDuration(250)
                    self.animation_1.setStartValue(0)
                    self.animation_1.setEndValue(150)
                    self.animation_1.setEasingCurve(QEasingCurve.InOutQuart)
                    self.animation_1.start()

                    widget.pushButton.clicked.connect(lambda: self.delete_values_aksam())
            
            # Hataları gidermek için tüm açık olan silme butonlarını kapatalım
            for i in range(self.ui.listWidget_4.count()):
                item = self.ui.listWidget_4.item(i)
                widget = self.ui.listWidget_4.itemWidget(item)
                if widget.frame_2.width() == 150:
                    self.animation_2 = QPropertyAnimation(widget.frame_2, b"minimumWidth")
                    self.animation_2.setDuration(250)
                    self.animation_2.setStartValue(150)
                    self.animation_2.setEndValue(0)
                    self.animation_2.setEasingCurve(QEasingCurve.InOutQuart)
                    self.animation_2.start()

        if self.sender().objectName() == "listWidget_5":
            # Kullanıcının seçtiği itemı al
            selected_item = self.ui.listWidget_5.currentItem()
            if selected_item:
                widget = self.ui.listWidget_5.itemWidget(selected_item)
                if widget.frame_2.width() == 0:
                    self.animation_1 = QPropertyAnimation(widget.frame_2, b"minimumWidth")
                    self.animation_1.setDuration(250)
                    self.animation_1.setStartValue(0)
                    self.animation_1.setEndValue(150)
                    self.animation_1.setEasingCurve(QEasingCurve.InOutQuart)
                    self.animation_1.start()

                    widget.pushButton.clicked.connect(lambda: self.delete_values_ara())
            
            # Hataları gidermek için tüm açık olan silme butonlarını kapatalım
            for i in range(self.ui.listWidget_5.count()):
                item = self.ui.listWidget_5.item(i)
                widget = self.ui.listWidget_5.itemWidget(item)
                if widget.frame_2.width() == 150:
                    self.animation_2 = QPropertyAnimation(widget.frame_2, b"minimumWidth")
                    self.animation_2.setDuration(250)
                    self.animation_2.setStartValue(150)
                    self.animation_2.setEndValue(0)
                    self.animation_2.setEasingCurve(QEasingCurve.InOutQuart)
                    self.animation_2.start()

    def delete_values_kahvalti(self):
        selected_row = self.ui.listWidget_2.currentRow()
        selected_item = self.ui.listWidget_2.currentItem()
        widget = self.ui.listWidget_2.itemWidget(selected_item)
        try:
            yemek_ismi = widget.label.text()
        except AttributeError:
            pass
        index = self.kahvalti["Yemekler"].index(yemek_ismi)
        miktar = self.kahvalti["Miktar"][index]
        yemek_degerleri = self.yemekler[self.yemekler["Yemek"] == yemek_ismi].values[0]
        deleted_kalori = yemek_degerleri[-4] * miktar / 100
        deleted_karb = yemek_degerleri[-3] * miktar / 100
        deleted_protein = yemek_degerleri[-2] * miktar / 100
        deleted_yag = yemek_degerleri[-1] * miktar / 100

        # Kalori, Karb, Protein ve Yağ değerlerini güncelleyelim
        self.kahvalti_kalori -= deleted_kalori
        self.kahvalti_karb -= deleted_karb
        self.kahvalti_protein -= deleted_protein
        self.kahvalti_yag -= deleted_yag
        # Kahvalti değerlerini ekrana yazdıralım
        self.ui.label_24.setText(str(round(self.kahvalti_kalori, 2)))
        self.ui.label_32.setText(str(round(self.kahvalti_karb, 2)))
        self.ui.label_34.setText(str(round(self.kahvalti_protein, 2)))
        self.ui.label_36.setText(str(round(self.kahvalti_yag, 2)))
        # Günlük değerleri güncelleyelim
        self.daily_kalori -= deleted_kalori
        self.daily_karb -= deleted_karb
        self.daily_protein -= deleted_protein
        self.daily_yag -= deleted_yag
        # Günlük değerleri ekrana yazdıralım
        self.ui.label_58.setText(str(round(self.daily_kalori, 2)))
        self.ui.label_60.setText(str(round(self.daily_karb, 2)))
        self.ui.label_62.setText(str(round(self.daily_protein, 2)))
        self.ui.label_64.setText(str(round(self.daily_yag, 2)))

        self.ui.listWidget_2.takeItem(selected_row)
        del self.kahvalti["Yemekler"][index]
        del self.kahvalti["Miktar"][index]
        self.userData()

        if self.ui.listWidget_2.count() == 0:
            self.ui.frame_64.setVisible(False) # kalori kısmını gizledik
            self.ui.frame_49.setVisible(False) # sayısal değerleri gizledik 
            self.ui.listWidget_2.setVisible(False) # list widgetın kendisini gizleyelim
            self.ui.frame_48.setStyleSheet("") # Alt siyah çizgiyi kaldıralım
            if self.toggle.isChecked():
                self.ui.label_19.setStyleSheet("QLabel{padding-top: 7px; font-size:10pt; color: black;}") # Menünün ismini ortalayalım
            else:
                self.ui.label_19.setStyleSheet("QLabel{padding-top: 7px; font-size:10pt; color: white;}") # Menünün ismini ortalayalım
            self.ui.pushButton_9.setStyleSheet("QPushButton{padding-top: 7px;}") # Butonu ortalayalım
            self.ui.frame_28.setMaximumHeight(58) # Ana frame'ın yüksekliğini sabitleyelim

    def delete_values_ogle(self):
        selected_row = self.ui.listWidget_3.currentRow()
        selected_item = self.ui.listWidget_3.currentItem()
        widget = self.ui.listWidget_3.itemWidget(selected_item)
        try:
            yemek_ismi = widget.label.text()
        except AttributeError:
            pass
        index = self.ogle["Yemekler"].index(yemek_ismi)
        miktar = self.ogle["Miktar"][index]
        yemek_degerleri = self.yemekler[self.yemekler["Yemek"] == yemek_ismi].values[0]
        deleted_kalori = yemek_degerleri[-4] * miktar / 100
        deleted_karb = yemek_degerleri[-3] * miktar / 100
        deleted_protein = yemek_degerleri[-2] * miktar / 100
        deleted_yag = yemek_degerleri[-1] * miktar / 100

        # Kalori, Karb, Protein ve Yağ değerlerini güncelleyelim
        self.ogle_kalori -= deleted_kalori
        self.ogle_karb -= deleted_karb
        self.ogle_protein -= deleted_protein
        self.ogle_yag -= deleted_yag
        # Öğle Yemeği değerlerini ekrana yazdıralım
        self.ui.label_25.setText(str(round(self.ogle_kalori, 2)))
        self.ui.label_37.setText(str(round(self.ogle_karb, 2)))
        self.ui.label_39.setText(str(round(self.ogle_protein, 2)))
        self.ui.label_41.setText(str(round(self.ogle_yag, 2)))
        # Günlük değerleri güncelleyelim
        self.daily_kalori -= deleted_kalori
        self.daily_karb -= deleted_karb
        self.daily_protein -= deleted_protein
        self.daily_yag -= deleted_yag
        # Günlük değerleri ekrana yazdıralım
        self.ui.label_58.setText(str(round(self.daily_kalori, 2)))
        self.ui.label_60.setText(str(round(self.daily_karb, 2)))
        self.ui.label_62.setText(str(round(self.daily_protein, 2)))
        self.ui.label_64.setText(str(round(self.daily_yag, 2)))

        self.ui.listWidget_3.takeItem(selected_row)
        del self.ogle["Yemekler"][index]
        del self.ogle["Miktar"][index]
        self.userData()

        if self.ui.listWidget_3.count() == 0:
            self.ui.frame_65.setVisible(False) # kalori kısmını gizledik
            self.ui.frame_51.setVisible(False) # sayısal değerleri gizledik 
            self.ui.listWidget_3.setVisible(False) # list widgetın kendisini gizleyelim
            self.ui.frame_50.setStyleSheet("") # Alt siyah çizgiyi kaldıralım
            if self.toggle.isChecked():
                self.ui.label_20.setStyleSheet("QLabel{padding-top: 7px; font-size:10pt; color: black;}") # Menünün ismini ortalayalım
            else:
                self.ui.label_20.setStyleSheet("QLabel{padding-top: 7px; font-size:10pt; color: white;}") # Menünün ismini ortalayalım
            self.ui.pushButton_10.setStyleSheet("QPushButton{padding-top: 7px;}") # Butonu ortalayalım
            self.ui.frame_29.setMaximumHeight(58) # Ana frame'ın yüksekliğini sabitleyelim

    def delete_values_aksam(self):
        selected_row = self.ui.listWidget_4.currentRow()
        selected_item = self.ui.listWidget_4.currentItem()
        widget = self.ui.listWidget_4.itemWidget(selected_item)
        try:
            yemek_ismi = widget.label.text()
        except AttributeError:
            pass
        index = self.aksam["Yemekler"].index(yemek_ismi)
        miktar = self.aksam["Miktar"][index]
        yemek_degerleri = self.yemekler[self.yemekler["Yemek"] == yemek_ismi].values[0]
        deleted_kalori = yemek_degerleri[-4] * miktar / 100
        deleted_karb = yemek_degerleri[-3] * miktar / 100
        deleted_protein = yemek_degerleri[-2] * miktar / 100
        deleted_yag = yemek_degerleri[-1] * miktar / 100

        # Kalori, Karb, Protein ve Yağ değerlerini güncelleyelim
        self.aksam_kalori -= deleted_kalori
        self.aksam_karb -= deleted_karb
        self.aksam_protein -= deleted_protein
        self.aksam_yag -= deleted_yag
        # Öğle Yemeği değerlerini ekrana yazdıralım
        self.ui.label_27.setText(str(round(self.aksam_kalori, 2)))
        self.ui.label_44.setText(str(round(self.aksam_karb, 2)))
        self.ui.label_45.setText(str(round(self.aksam_protein, 2)))
        self.ui.label_48.setText(str(round(self.aksam_yag, 2)))
        # Günlük değerleri güncelleyelim
        self.daily_kalori -= deleted_kalori
        self.daily_karb -= deleted_karb
        self.daily_protein -= deleted_protein
        self.daily_yag -= deleted_yag
        # Günlük değerleri ekrana yazdıralım
        self.ui.label_58.setText(str(round(self.daily_kalori, 2)))
        self.ui.label_60.setText(str(round(self.daily_karb, 2)))
        self.ui.label_62.setText(str(round(self.daily_protein, 2)))
        self.ui.label_64.setText(str(round(self.daily_yag, 2)))

        self.ui.listWidget_4.takeItem(selected_row)
        del self.aksam["Yemekler"][index]
        del self.aksam["Miktar"][index]
        self.userData()

        if self.ui.listWidget_4.count() == 0:
            self.ui.frame_66.setVisible(False) # kalori kısmını gizledik
            self.ui.frame_53.setVisible(False) # sayısal değerleri gizledik 
            self.ui.listWidget_4.setVisible(False) # list widgetın kendisini gizleyelim
            self.ui.frame_52.setStyleSheet("") # Alt siyah çizgiyi kaldıralım
            if self.toggle.isChecked():
                self.ui.label_21.setStyleSheet("QLabel{padding-top: 7px; font-size:10pt; color: black;}") # Menünün ismini ortalayalım
            else:
                self.ui.label_21.setStyleSheet("QLabel{padding-top: 7px; font-size:10pt; color: white;}") # Menünün ismini ortalayalım
            self.ui.pushButton_11.setStyleSheet("QPushButton{padding-top: 7px;}") # Butonu ortalayalım
            self.ui.frame_30.setMaximumHeight(58) # Ana frame'ın yüksekliğini sabitleyelim

    def delete_values_ara(self):
        selected_row = self.ui.listWidget_5.currentRow()
        selected_item = self.ui.listWidget_5.currentItem()
        widget = self.ui.listWidget_5.itemWidget(selected_item)
        try:
            yemek_ismi = widget.label.text()
        except AttributeError:
            pass
        index = self.ara["Yemekler"].index(yemek_ismi)
        miktar = self.ara["Miktar"][index]
        yemek_degerleri = self.yemekler[self.yemekler["Yemek"] == yemek_ismi].values[0]
        deleted_kalori = yemek_degerleri[-4] * miktar / 100
        deleted_karb = yemek_degerleri[-3] * miktar / 100
        deleted_protein = yemek_degerleri[-2] * miktar / 100
        deleted_yag = yemek_degerleri[-1] * miktar / 100

        # Kalori, Karb, Protein ve Yağ değerlerini güncelleyelim
        self.ara_kalori -= deleted_kalori
        self.ara_karb -= deleted_karb
        self.ara_protein -= deleted_protein
        self.ara_yag -= deleted_yag
        # Öğle Yemeği değerlerini ekrana yazdıralım
        self.ui.label_29.setText(str(round(self.ara_kalori, 2)))
        self.ui.label_50.setText(str(round(self.ara_karb, 2)))
        self.ui.label_52.setText(str(round(self.ara_protein, 2)))
        self.ui.label_54.setText(str(round(self.ara_yag, 2)))
        # Günlük değerleri güncelleyelim
        self.daily_kalori -= deleted_kalori
        self.daily_karb -= deleted_karb
        self.daily_protein -= deleted_protein
        self.daily_yag -= deleted_yag
        # Günlük değerleri ekrana yazdıralım
        self.ui.label_58.setText(str(round(self.daily_kalori, 2)))
        self.ui.label_60.setText(str(round(self.daily_karb, 2)))
        self.ui.label_62.setText(str(round(self.daily_protein, 2)))
        self.ui.label_64.setText(str(round(self.daily_yag, 2)))

        self.ui.listWidget_5.takeItem(selected_row)
        del self.ara["Yemekler"][index]
        del self.ara["Miktar"][index]
        self.userData()

        if self.ui.listWidget_5.count() == 0:
            self.ui.frame_67.setVisible(False) # kalori kısmını gizledik
            self.ui.frame_55.setVisible(False) # sayısal değerleri gizledik 
            self.ui.listWidget_5.setVisible(False) # list widgetın kendisini gizleyelim
            self.ui.frame_54.setStyleSheet("") # Alt siyah çizgiyi kaldıralım
            if self.toggle.isChecked():
                self.ui.label_22.setStyleSheet("QLabel{padding-top: 7px; font-size:10pt; color: black;}") # Menünün ismini ortalayalım
            else:
                self.ui.label_22.setStyleSheet("QLabel{padding-top: 7px; font-size:10pt; color: white;}") # Menünün ismini ortalayalım
            self.ui.pushButton_12.setStyleSheet("QPushButton{padding-top: 7px;}") # Butonu ortalayalım
            self.ui.frame_31.setMaximumHeight(58) # Ana frame'ın yüksekliğini sabitleyelim

    def userData(self, readMode=False):
        with open("data.json", "r", encoding="utf-8") as file:
            data =json.load(file)
            curr_date = QDate.currentDate().toString("dd-MM-yyyy")

        excelData = {
            "Kahvalti": {
                "Yemekler": self.kahvalti["Yemekler"],
                "Miktar": self.kahvalti["Miktar"],
                "Kalori": round(self.kahvalti_kalori, 2),
                "Karbonhidrat": round(self.kahvalti_karb, 2),
                "Protein": round(self.kahvalti_protein, 2),
                "Yag": round(self.kahvalti_yag, 2),
            },
            "Ogle": {
                "Yemekler": self.ogle["Yemekler"],
                "Miktar": self.ogle["Miktar"],
                "Kalori": round(self.ogle_kalori, 2),
                "Karbonhidrat": round(self.ogle_karb, 2),
                "Protein": round(self.ogle_protein, 2),
                "Yag": round(self.ogle_yag, 2),
            },
            "Aksam": {
                "Yemekler": self.aksam["Yemekler"],
                "Miktar": self.aksam["Miktar"],
                "Kalori": round(self.aksam_kalori, 2),
                "Karbonhidrat": round(self.aksam_karb, 2),
                "Protein": round(self.aksam_protein, 2),
                "Yag": round(self.aksam_yag, 2),
            },
            "Ara": {
                "Yemekler": self.ara["Yemekler"],
                "Miktar": self.ara["Miktar"],
                "Kalori": round(self.ara_kalori, 2),
                "Karbonhidrat": round(self.ara_karb, 2),
                "Protein": round(self.ara_protein, 2),
                "Yag": round(self.ara_yag, 2),
            },
            "Toplam": {
                "Kalori": round(self.daily_kalori, 2),
                "Karbonhidrat": round(self.daily_karb, 2),
                "Protein": round(self.daily_protein, 2),
                "Yag": round(self.daily_yag, 2),
            }
        }
        if readMode:
            try:
                return data[curr_date]
            except:
                return excelData
            
        else:
            data[curr_date] = excelData
            with open("data.json", "w", encoding="utf-8") as file:
                json.dump(data, file, ensure_ascii=False, indent=4)

    def page_1(self):
        self.ui.label_3.setText("Yemek Listesi")
        self.ui.stackedWidget.setCurrentWidget(self.ui.yemekler)

    def page_2(self):
        # Tarih ve saati ayarlayalım
        currentDateTime = QDateTime.currentDateTime()
        self.ui.dateTimeEdit.setDateTime(currentDateTime)

        self.ui.label_3.setText("Kalori Takibim")
        self.ui.stackedWidget.setCurrentWidget(self.ui.kalori)

        # Kullanıcı öğünününe herhangi bir yemek eklemezse değerleri gizleyelim
        if self.ui.listWidget_2.count() == 0:
            self.ui.frame_64.setVisible(False) # kalori kısmını gizledik
            self.ui.frame_49.setVisible(False) # sayısal değerleri gizledik 
            self.ui.listWidget_2.setVisible(False) # list widgetın kendisini gizleyelim
            self.ui.frame_48.setStyleSheet("") # Alt siyah çizgiyi kaldıralım
            if self.toggle.isChecked():
                self.ui.label_19.setStyleSheet("QLabel{padding-top: 7px; font-size:10pt; color: black;}") # Menünün ismini ortalayalım
            else:
                self.ui.label_19.setStyleSheet("QLabel{padding-top: 7px; font-size:10pt; color: white;}") # Menünün ismini ortalayalım
            self.ui.pushButton_9.setStyleSheet("QPushButton{padding-top: 7px;}") # Butonu ortalayalım
            self.ui.frame_28.setMaximumHeight(58) # Ana frame'ın yüksekliğini sabitleyelim

        if self.ui.listWidget_3.count() == 0:
            self.ui.frame_65.setVisible(False) # kalori kısmını gizledik
            self.ui.frame_51.setVisible(False) # sayısal değerleri gizledik 
            self.ui.listWidget_3.setVisible(False) # list widgetın kendisini gizleyelim
            self.ui.frame_50.setStyleSheet("") # Alt siyah çizgiyi kaldıralım
            if self.toggle.isChecked():
                self.ui.label_20.setStyleSheet("QLabel{padding-top: 7px; font-size:10pt; color: black;}") # Menünün ismini ortalayalım
            else:
                self.ui.label_20.setStyleSheet("QLabel{padding-top: 7px; font-size:10pt; color: white;}") # Menünün ismini ortalayalım
            self.ui.pushButton_10.setStyleSheet("QPushButton{padding-top: 7px;}") # Butonu ortalayalım
            self.ui.frame_29.setMaximumHeight(58) # Ana frame'ın yüksekliğini sabitleyelim

        if self.ui.listWidget_4.count() == 0:
            self.ui.frame_66.setVisible(False) # kalori kısmını gizledik
            self.ui.frame_53.setVisible(False) # sayısal değerleri gizledik 
            self.ui.listWidget_4.setVisible(False) # list widgetın kendisini gizleyelim
            self.ui.frame_52.setStyleSheet("") # Alt siyah çizgiyi kaldıralım
            if self.toggle.isChecked():
                self.ui.label_21.setStyleSheet("QLabel{padding-top: 7px; font-size:10pt; color: black;}") # Menünün ismini ortalayalım
            else:
                self.ui.label_21.setStyleSheet("QLabel{padding-top: 7px; font-size:10pt; color: white;}") # Menünün ismini ortalayalım
            self.ui.pushButton_11.setStyleSheet("QPushButton{padding-top: 7px;}") # Butonu ortalayalım
            self.ui.frame_30.setMaximumHeight(58) # Ana frame'ın yüksekliğini sabitleyelim

        if self.ui.listWidget_5.count() == 0:
            self.ui.frame_67.setVisible(False) # kalori kısmını gizledik
            self.ui.frame_55.setVisible(False) # sayısal değerleri gizledik 
            self.ui.listWidget_5.setVisible(False) # list widgetın kendisini gizleyelim
            self.ui.frame_54.setStyleSheet("") # Alt siyah çizgiyi kaldıralım
            if self.toggle.isChecked():
                self.ui.label_22.setStyleSheet("QLabel{padding-top: 7px; font-size:10pt; color: black;}") # Menünün ismini ortalayalım
            else:
                self.ui.label_22.setStyleSheet("QLabel{padding-top: 7px; font-size:10pt; color: white;}") # Menünün ismini ortalayalım
            self.ui.pushButton_12.setStyleSheet("QPushButton{padding-top: 7px;}") # Butonu ortalayalım
            self.ui.frame_31.setMaximumHeight(58) # Ana frame'ın yüksekliğini sabitleyelim

        # Yemek ekleme butonunu aktif hale getirelim
        self.ui.pushButton_9.clicked.connect(self.select)
        self.ui.pushButton_10.clicked.connect(self.select)
        self.ui.pushButton_11.clicked.connect(self.select)
        self.ui.pushButton_12.clicked.connect(self.select)

    def add_food(self):
        self.lastButtonPressed = "Yemek Ekle"

        self.ui.frame_13.setMaximumHeight(0)
        self.clear_lines()
        self.ui.stackedWidget.setCurrentWidget(self.ui.ekle)
        self.ui.pushButton_7.clicked.connect(lambda: self.page_1())
        self.ui.pushButton_6.clicked.connect(lambda: self.add_food_func())
        self.ui.pushButton_8.clicked.connect(lambda: self.closePopup())
        self.ui.label_6.mousePressEvent = self.open_file_dialog
        

        

if __name__ == '__main__':
    app = QApplication(sys.argv)
    # Uygulamamızın arkaplanda çalışmasını sağlayalım.
    app.setQuitOnLastWindowClosed(False)
    window = MainWindow() 
    window.show()
    sys.exit(app.exec_())