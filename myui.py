# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'myui.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1737, 925)
        MainWindow.setStyleSheet("")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setStyleSheet("")
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout_23 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_23.setObjectName("horizontalLayout_23")
        self.widget = QtWidgets.QWidget(self.centralwidget)
        self.widget.setStyleSheet("background-color: rgb(230, 230, 230);\n"
"border-radius:10px;\n"
"")
        self.widget.setObjectName("widget")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.widget)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.gridLayout_3 = QtWidgets.QGridLayout()
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.gridLayout_4.addLayout(self.gridLayout_3, 0, 0, 1, 1)
        self.horizontalLayout_23.addWidget(self.widget)
        self.verticalLayout_4 = QtWidgets.QVBoxLayout()
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.textBrowser_1 = QtWidgets.QTextBrowser(self.centralwidget)
        self.textBrowser_1.setStyleSheet("background-color: rgb(230, 230, 230);\n"
"border-radius:10px;\n"
"font: 17pt \"楷体\";\n"
"color: rgb(176,23,31);")
        self.textBrowser_1.setObjectName("textBrowser_1")
        self.verticalLayout_4.addWidget(self.textBrowser_1)
        self.widget5 = QtWidgets.QWidget(self.centralwidget)
        self.widget5.setObjectName("widget5")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.widget5)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label10 = QtWidgets.QLabel(self.widget5)
        self.label10.setStyleSheet("background-color: rgb(230, 230, 230);\n"
"border-radius:10px;\n"
"\n"
"\n"
"font: 20pt \"楷体\";\n"
"color: rgb(41, 36, 33);")
        self.label10.setObjectName("label10")
        self.horizontalLayout_2.addWidget(self.label10)
        self.gridWidget = QtWidgets.QWidget(self.widget5)
        self.gridWidget.setStyleSheet("height:10px;\n"
"border-radius:10px;\n"
"font: 15pt \"楷体\";\n"
"color: rgb(240, 240, 240);")
        self.gridWidget.setObjectName("gridWidget")
        self.gridLayout_5 = QtWidgets.QGridLayout(self.gridWidget)
        self.gridLayout_5.setObjectName("gridLayout_5")
        self.label3 = QtWidgets.QLabel(self.gridWidget)
        self.label3.setStyleSheet("background-color:rgb(255,97,0)\n"
"")
        self.label3.setObjectName("label3")
        self.gridLayout_5.addWidget(self.label3, 2, 1, 1, 1)
        self.label0 = QtWidgets.QLabel(self.gridWidget)
        self.label0.setStyleSheet("background-color:rgb(255,97,0)\n"
"")
        self.label0.setObjectName("label0")
        self.gridLayout_5.addWidget(self.label0, 0, 0, 1, 1)
        self.label2 = QtWidgets.QLabel(self.gridWidget)
        self.label2.setStyleSheet("background-color:rgb(255,97,0)\n"
"")
        self.label2.setObjectName("label2")
        self.gridLayout_5.addWidget(self.label2, 2, 0, 1, 1)
        self.label1 = QtWidgets.QLabel(self.gridWidget)
        self.label1.setStyleSheet("background-color:rgb(255,97,0)\n"
"")
        self.label1.setObjectName("label1")
        self.gridLayout_5.addWidget(self.label1, 0, 1, 1, 1)
        self.horizontalLayout_2.addWidget(self.gridWidget)
        self.horizontalLayout_2.setStretch(0, 1)
        self.horizontalLayout_2.setStretch(1, 2)
        self.verticalLayout_4.addWidget(self.widget5)
        self.textBrowser_3 = QtWidgets.QTextBrowser(self.centralwidget)
        self.textBrowser_3.setStyleSheet("background-color: rgb(230, 230, 230);\n"
"border-radius:10px;\n"
"font: 15pt \"楷体\";\n"
"color: rgb(41, 36, 33);")
        self.textBrowser_3.setObjectName("textBrowser_3")
        self.verticalLayout_4.addWidget(self.textBrowser_3)
        self.verticalLayout_4.setStretch(0, 1)
        self.verticalLayout_4.setStretch(1, 1)
        self.verticalLayout_4.setStretch(2, 20)
        self.horizontalLayout_23.addLayout(self.verticalLayout_4)
        self.QWidget2 = QtWidgets.QWidget(self.centralwidget)
        self.QWidget2.setStyleSheet("")
        self.QWidget2.setObjectName("QWidget2")
        self.verticalLayout_15 = QtWidgets.QVBoxLayout(self.QWidget2)
        self.verticalLayout_15.setObjectName("verticalLayout_15")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.widget4 = QtWidgets.QWidget(self.QWidget2)
        self.widget4.setStyleSheet("font: 20pt \"楷体\";\n"
"")
        self.widget4.setObjectName("widget4")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.widget4)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.spinBox = QtWidgets.QSpinBox(self.widget4)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.spinBox.sizePolicy().hasHeightForWidth())
        self.spinBox.setSizePolicy(sizePolicy)
        self.spinBox.setAutoFillBackground(True)
        self.spinBox.setStyleSheet("background-color: rgb(250, 200, 127);\n"
"height:40px;\n"
"font: 30pt \"楷体\";\n"
"color: rgb(0, 0, 127);")
        self.spinBox.setButtonSymbols(QtWidgets.QAbstractSpinBox.UpDownArrows)
        self.spinBox.setSpecialValueText("")
        self.spinBox.setProperty("showGroupSeparator", False)
        self.spinBox.setSuffix("")
        self.spinBox.setMinimum(6)
        self.spinBox.setMaximum(15)
        self.spinBox.setSingleStep(1)
        self.spinBox.setProperty("value", 6)
        self.spinBox.setObjectName("spinBox")
        self.verticalLayout_3.addWidget(self.spinBox)
        self.pushButton_2 = QtWidgets.QPushButton(self.widget4)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_2.sizePolicy().hasHeightForWidth())
        self.pushButton_2.setSizePolicy(sizePolicy)
        self.pushButton_2.setStyleSheet("\n"
"font: 20pt \"楷体\";\n"
"color: rgb(255, 255, 255);\n"
"background-color:rgb(38, 131, 245);")
        self.pushButton_2.setObjectName("pushButton_2")
        self.verticalLayout_3.addWidget(self.pushButton_2)
        self.pushButton_3 = QtWidgets.QPushButton(self.widget4)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_3.sizePolicy().hasHeightForWidth())
        self.pushButton_3.setSizePolicy(sizePolicy)
        self.pushButton_3.setStyleSheet("height:40px;\n"
"font: 20pt \"楷体\";\n"
"color: rgb(255, 255, 255);\n"
"background-color:rgb(38, 131, 245);")
        self.pushButton_3.setObjectName("pushButton_3")
        self.verticalLayout_3.addWidget(self.pushButton_3)
        self.pushButton_4 = QtWidgets.QPushButton(self.widget4)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_4.sizePolicy().hasHeightForWidth())
        self.pushButton_4.setSizePolicy(sizePolicy)
        self.pushButton_4.setStyleSheet("height:40px;\n"
"font: 20pt \"楷体\";\n"
"color: rgb(255, 255, 255);\n"
"background-color:rgb(38, 131, 245);")
        self.pushButton_4.setObjectName("pushButton_4")
        self.verticalLayout_3.addWidget(self.pushButton_4)
        self.pushButton_5 = QtWidgets.QPushButton(self.widget4)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_5.sizePolicy().hasHeightForWidth())
        self.pushButton_5.setSizePolicy(sizePolicy)
        self.pushButton_5.setStyleSheet("height:40px;\n"
"font: 20pt \"楷体\";\n"
"color: rgb(255, 255, 255);\n"
"background-color:rgb(38, 131, 245);")
        self.pushButton_5.setObjectName("pushButton_5")
        self.verticalLayout_3.addWidget(self.pushButton_5)
        self.pushButton_6 = QtWidgets.QPushButton(self.widget4)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_6.sizePolicy().hasHeightForWidth())
        self.pushButton_6.setSizePolicy(sizePolicy)
        self.pushButton_6.setStyleSheet("height:40px;\n"
"font: 20pt \"楷体\";\n"
"color: rgb(255, 255, 255);\n"
"background-color:rgb(38, 131, 245);")
        self.pushButton_6.setObjectName("pushButton_6")
        self.verticalLayout_3.addWidget(self.pushButton_6)
        self.pushButton_7 = QtWidgets.QPushButton(self.widget4)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_7.sizePolicy().hasHeightForWidth())
        self.pushButton_7.setSizePolicy(sizePolicy)
        self.pushButton_7.setStyleSheet("height:40px;\n"
"font: 20pt \"楷体\";\n"
"color: rgb(255, 255, 255);\n"
"background-color:rgb(38, 131, 245);")
        self.pushButton_7.setObjectName("pushButton_7")
        self.verticalLayout_3.addWidget(self.pushButton_7)
        self.pushButton_8 = QtWidgets.QPushButton(self.widget4)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_8.sizePolicy().hasHeightForWidth())
        self.pushButton_8.setSizePolicy(sizePolicy)
        self.pushButton_8.setStyleSheet("height:40px;\n"
"font: 20pt \"楷体\";\n"
"color: rgb(255, 255, 255);\n"
"background-color:rgb(38, 131, 245);")
        self.pushButton_8.setObjectName("pushButton_8")
        self.verticalLayout_3.addWidget(self.pushButton_8)
        self.pushButton_9 = QtWidgets.QPushButton(self.widget4)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_9.sizePolicy().hasHeightForWidth())
        self.pushButton_9.setSizePolicy(sizePolicy)
        self.pushButton_9.setStyleSheet("height:40px;\n"
"font: 20pt \"楷体\";\n"
"color: rgb(255, 255, 255);\n"
"background-color:rgb(38, 131, 245);")
        self.pushButton_9.setObjectName("pushButton_9")
        self.verticalLayout_3.addWidget(self.pushButton_9)
        self.pushButton_10 = QtWidgets.QPushButton(self.widget4)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_10.sizePolicy().hasHeightForWidth())
        self.pushButton_10.setSizePolicy(sizePolicy)
        self.pushButton_10.setStyleSheet("height:40px;\n"
"font: 20pt \"楷体\";\n"
"color: rgb(255, 255, 255);\n"
"background-color:rgb(38, 131, 245);")
        self.pushButton_10.setObjectName("pushButton_10")
        self.verticalLayout_3.addWidget(self.pushButton_10)
        self.horizontalLayout.addWidget(self.widget4)
        self.widget3 = QtWidgets.QWidget(self.QWidget2)
        self.widget3.setStyleSheet("background-color: rgb(230, 230, 230);\n"
"border-radius:10px;\n"
"\n"
"\n"
"font: 20pt \"楷体\";\n"
"color: rgb(41, 36, 33);")
        self.widget3.setObjectName("widget3")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.widget3)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label_1 = QtWidgets.QLabel(self.widget3)
        self.label_1.setStyleSheet("")
        self.label_1.setAlignment(QtCore.Qt.AlignCenter)
        self.label_1.setObjectName("label_1")
        self.verticalLayout_2.addWidget(self.label_1)
        self.label_2 = QtWidgets.QLabel(self.widget3)
        self.label_2.setStyleSheet("")
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.verticalLayout_2.addWidget(self.label_2)
        self.label_3 = QtWidgets.QLabel(self.widget3)
        self.label_3.setStyleSheet("")
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setObjectName("label_3")
        self.verticalLayout_2.addWidget(self.label_3)
        self.label_4 = QtWidgets.QLabel(self.widget3)
        self.label_4.setStyleSheet("")
        self.label_4.setAlignment(QtCore.Qt.AlignCenter)
        self.label_4.setObjectName("label_4")
        self.verticalLayout_2.addWidget(self.label_4)
        self.label_5 = QtWidgets.QLabel(self.widget3)
        self.label_5.setStyleSheet("")
        self.label_5.setAlignment(QtCore.Qt.AlignCenter)
        self.label_5.setObjectName("label_5")
        self.verticalLayout_2.addWidget(self.label_5)
        self.label_6 = QtWidgets.QLabel(self.widget3)
        self.label_6.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_6.sizePolicy().hasHeightForWidth())
        self.label_6.setSizePolicy(sizePolicy)
        self.label_6.setMouseTracking(False)
        self.label_6.setStyleSheet("")
        self.label_6.setScaledContents(False)
        self.label_6.setAlignment(QtCore.Qt.AlignCenter)
        self.label_6.setObjectName("label_6")
        self.verticalLayout_2.addWidget(self.label_6)
        self.label_7 = QtWidgets.QLabel(self.widget3)
        self.label_7.setStyleSheet("")
        self.label_7.setAlignment(QtCore.Qt.AlignCenter)
        self.label_7.setObjectName("label_7")
        self.verticalLayout_2.addWidget(self.label_7)
        self.label_8 = QtWidgets.QLabel(self.widget3)
        self.label_8.setStyleSheet("")
        self.label_8.setAlignment(QtCore.Qt.AlignCenter)
        self.label_8.setObjectName("label_8")
        self.verticalLayout_2.addWidget(self.label_8)
        self.label_9 = QtWidgets.QLabel(self.widget3)
        self.label_9.setStyleSheet("")
        self.label_9.setAlignment(QtCore.Qt.AlignCenter)
        self.label_9.setObjectName("label_9")
        self.verticalLayout_2.addWidget(self.label_9)
        self.label_10 = QtWidgets.QLabel(self.widget3)
        self.label_10.setStyleSheet("")
        self.label_10.setAlignment(QtCore.Qt.AlignCenter)
        self.label_10.setObjectName("label_10")
        self.verticalLayout_2.addWidget(self.label_10)
        self.horizontalLayout.addWidget(self.widget3)
        self.verticalLayout_15.addLayout(self.horizontalLayout)
        self.label_11 = QtWidgets.QLabel(self.QWidget2)
        self.label_11.setStyleSheet("background-color: rgb(230, 230, 230);\n"
"border-radius:10px;\n"
"font: 20pt \"楷体\";\n"
"color: rgb(41, 36, 33);\n"
"\n"
"")
        self.label_11.setObjectName("label_11")
        self.verticalLayout_15.addWidget(self.label_11)
        self.verticalLayout_15.setStretch(0, 10)
        self.verticalLayout_15.setStretch(1, 1)
        self.horizontalLayout_23.addWidget(self.QWidget2)
        self.horizontalLayout_23.setStretch(0, 5)
        self.horizontalLayout_23.setStretch(1, 2)
        self.verticalLayout.addLayout(self.horizontalLayout_23)
        self.widget2 = QtWidgets.QWidget(self.centralwidget)
        self.widget2.setObjectName("widget2")
        self.horizontalLayout_24 = QtWidgets.QHBoxLayout(self.widget2)
        self.horizontalLayout_24.setObjectName("horizontalLayout_24")
        self.start = QtWidgets.QPushButton(self.widget2)
        self.start.setStyleSheet("height:100px;\n"
"font: 35pt \"楷体\";\n"
"color: rgb(255, 255, 255);\n"
"background-color:rgb(38, 131, 245);")
        self.start.setObjectName("start")
        self.horizontalLayout_24.addWidget(self.start)
        self.textBrowser_2 = QtWidgets.QTextBrowser(self.widget2)
        self.textBrowser_2.setStyleSheet("background-color: rgb(230, 230, 230);\n"
"border-radius:10px;\n"
"font: 20pt \"楷体\";\n"
"color: rgb(41, 36, 33);")
        self.textBrowser_2.setObjectName("textBrowser_2")
        self.horizontalLayout_24.addWidget(self.textBrowser_2)
        self.verticalLayout.addWidget(self.widget2)
        self.verticalLayout.setStretch(0, 40)
        self.verticalLayout.setStretch(1, 5)
        self.gridLayout_2.addLayout(self.verticalLayout, 0, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.textBrowser_1.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'楷体\'; font-size:17pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:16pt;\"><br /></p></body></html>"))
        self.label10.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\">未勾画:</p></body></html>"))
        self.label3.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\">纵断彩色</p></body></html>"))
        self.label0.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\">横断灰阶</p></body></html>"))
        self.label2.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\">横断彩色</p></body></html>"))
        self.label1.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\">纵断灰阶</p></body></html>"))
        self.textBrowser_3.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'楷体\'; font-size:15pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
        self.pushButton_2.setText(_translate("MainWindow", "管壁层次"))
        self.pushButton_3.setText(_translate("MainWindow", "阑尾腔内"))
        self.pushButton_4.setText(_translate("MainWindow", "周围系膜肿胀"))
        self.pushButton_5.setText(_translate("MainWindow", "周围肿胀形式"))
        self.pushButton_6.setText(_translate("MainWindow", "回盲部肠管肿胀"))
        self.pushButton_7.setText(_translate("MainWindow", "腹腔游离积液"))
        self.pushButton_8.setText(_translate("MainWindow", "淋巴结胀大"))
        self.pushButton_9.setText(_translate("MainWindow", "肠管扩张"))
        self.pushButton_10.setText(_translate("MainWindow", "阑尾炎类别"))
        self.label_1.setText(_translate("MainWindow", "直径"))
        self.label_2.setText(_translate("MainWindow", "双层"))
        self.label_3.setText(_translate("MainWindow", "液体"))
        self.label_4.setText(_translate("MainWindow", "有"))
        self.label_5.setText(_translate("MainWindow", "无"))
        self.label_6.setText(_translate("MainWindow", "无"))
        self.label_7.setText(_translate("MainWindow", "无"))
        self.label_8.setText(_translate("MainWindow", "无"))
        self.label_9.setText(_translate("MainWindow", "有"))
        self.label_10.setText(_translate("MainWindow", "1"))
        self.label_11.setText(_translate("MainWindow", "<html><head/><body><p>单纯性阑尾炎</p></body></html>"))
        self.start.setText(_translate("MainWindow", "开始"))
        self.textBrowser_2.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'楷体\'; font-size:20pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:18pt; font-weight:600; color:#ff0000;\">左键</span><span style=\" font-size:18pt; color:#ff0000;\">、</span><span style=\" font-size:18pt; font-weight:600; color:#ff0000;\">右键：</span><span style=\" font-size:18pt; color:#000000;\">勾画横、纵断灰阶图 </span><span style=\" font-size:18pt; font-weight:600; color:#ff0000;\">滚轮、Q、E：</span><span style=\" font-size:18pt; color:#000000;\">切换图片 </span><span style=\" font-size:18pt; font-weight:600; color:#ff0000;\">S：</span><span style=\" font-size:18pt; color:#000000;\">保存 </span><span style=\" font-size:18pt; font-weight:600; color:#ff0000;\">R、F：</span><span style=\" font-size:18pt; color:#000000;\">切换病人 </span><span style=\" font-size:18pt; font-weight:600; color:#ff0000;\">W</span><span style=\" font-size:18pt; color:#ff0000;\">：</span><span style=\" font-size:18pt; color:#000000;\">清除画布 </span><span style=\" font-size:18pt; font-weight:600; color:#ff0000;\">A</span><span style=\" font-size:18pt; color:#ff0000;\">、</span><span style=\" font-size:18pt; font-weight:600; color:#ff0000;\">D：</span><span style=\" font-size:18pt; color:#000000;\">分别保存横断、纵断彩色原图</span><span style=\" font-size:18pt;\"> </span><span style=\" font-size:18pt; font-weight:600; color:#ff0000;\">ESC:</span><span style=\" font-size:18pt;\">退出</span></p></body></html>"))

