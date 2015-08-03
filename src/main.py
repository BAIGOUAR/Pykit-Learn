# -*- coding: utf-8 -*-
# -*- coding: utf-8 -*-
"""
Created on Mon Aug  3 18:13:25 2015

@author: bhavesh
"""

import sys
from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_TabWidget(QtGui.QTabWidget):
    def __init__(self):
        QtGui.QWidget.__init__(self)
        self.setupUi(self)
    def setupUi(self, TabWidget):
        TabWidget.setObjectName(_fromUtf8("TabWidget"))
        TabWidget.resize(987, 737)
        self.Supervised = QtGui.QWidget()
        self.Supervised.setObjectName(_fromUtf8("Supervised"))
        self.horizontalWidget = QtGui.QWidget(self.Supervised)
        self.horizontalWidget.setGeometry(QtCore.QRect(0, 0, 501, 51))
        self.horizontalWidget.setObjectName(_fromUtf8("horizontalWidget"))
        self.horizontalLayout = QtGui.QHBoxLayout(self.horizontalWidget)
        self.horizontalLayout.setMargin(0)
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.pushButton_5 = QtGui.QPushButton(self.horizontalWidget)
        self.pushButton_5.setObjectName(_fromUtf8("pushButton_5"))
        self.horizontalLayout.addWidget(self.pushButton_5)
        self.pushButton_4 = QtGui.QPushButton(self.horizontalWidget)
        self.pushButton_4.setObjectName(_fromUtf8("pushButton_4"))
        self.horizontalLayout.addWidget(self.pushButton_4)
        self.pushButton_3 = QtGui.QPushButton(self.horizontalWidget)
        self.pushButton_3.setObjectName(_fromUtf8("pushButton_3"))
        self.horizontalLayout.addWidget(self.pushButton_3)
        self.verticalLayoutWidget = QtGui.QWidget(self.Supervised)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(20, 50, 391, 621))
        self.verticalLayoutWidget.setObjectName(_fromUtf8("verticalLayoutWidget"))
        self.verticalLayout = QtGui.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setMargin(0)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.label = QtGui.QLabel(self.verticalLayoutWidget)
        self.label.setObjectName(_fromUtf8("label"))
        self.verticalLayout.addWidget(self.label)
        self.textBrowser = QtGui.QTextBrowser(self.verticalLayoutWidget)
        self.textBrowser.setObjectName(_fromUtf8("textBrowser"))
        self.verticalLayout.addWidget(self.textBrowser)
        self.verticalLayoutWidget_2 = QtGui.QWidget(self.Supervised)
        self.verticalLayoutWidget_2.setGeometry(QtCore.QRect(420, 50, 541, 621))
        self.verticalLayoutWidget_2.setObjectName(_fromUtf8("verticalLayoutWidget_2"))
        self.verticalLayout_2 = QtGui.QVBoxLayout(self.verticalLayoutWidget_2)
        self.verticalLayout_2.setMargin(0)
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.label_2 = QtGui.QLabel(self.verticalLayoutWidget_2)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.verticalLayout_2.addWidget(self.label_2)
        self.graphicsView = QtGui.QGraphicsView(self.verticalLayoutWidget_2)
        self.graphicsView.setObjectName(_fromUtf8("graphicsView"))
        self.verticalLayout_2.addWidget(self.graphicsView)
        self.progressBar = QtGui.QProgressBar(self.Supervised)
        self.progressBar.setGeometry(QtCore.QRect(20, 683, 941, 16))
        self.progressBar.setProperty("value", 24)
        self.progressBar.setObjectName(_fromUtf8("progressBar"))
        TabWidget.addTab(self.Supervised, _fromUtf8(""))
        self.Unsupervised = QtGui.QWidget()
        self.Unsupervised.setEnabled(True)
        self.Unsupervised.setAutoFillBackground(False)
        self.Unsupervised.setObjectName(_fromUtf8("Unsupervised"))
        self.horizontalWidget_2 = QtGui.QWidget(self.Unsupervised)
        self.horizontalWidget_2.setGeometry(QtCore.QRect(0, 0, 811, 51))
        self.horizontalWidget_2.setObjectName(_fromUtf8("horizontalWidget_2"))
        self.horizontalLayout_2 = QtGui.QHBoxLayout(self.horizontalWidget_2)
        self.horizontalLayout_2.setMargin(0)
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.pushButton_6 = QtGui.QPushButton(self.horizontalWidget_2)
        self.pushButton_6.setObjectName(_fromUtf8("pushButton_6"))
        self.horizontalLayout_2.addWidget(self.pushButton_6)
        self.pushButton_7 = QtGui.QPushButton(self.horizontalWidget_2)
        self.pushButton_7.setObjectName(_fromUtf8("pushButton_7"))
        self.horizontalLayout_2.addWidget(self.pushButton_7)
        self.pushButton_8 = QtGui.QPushButton(self.horizontalWidget_2)
        self.pushButton_8.setObjectName(_fromUtf8("pushButton_8"))
        self.horizontalLayout_2.addWidget(self.pushButton_8)
        self.pushButton_24 = QtGui.QPushButton(self.horizontalWidget_2)
        self.pushButton_24.setObjectName(_fromUtf8("pushButton_24"))
        self.horizontalLayout_2.addWidget(self.pushButton_24)
        self.pushButton_33 = QtGui.QPushButton(self.horizontalWidget_2)
        self.pushButton_33.setObjectName(_fromUtf8("pushButton_33"))
        self.horizontalLayout_2.addWidget(self.pushButton_33)
        self.label_3 = QtGui.QLabel(self.Unsupervised)
        self.label_3.setGeometry(QtCore.QRect(20, 60, 81, 17))
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.verticalLayoutWidget_3 = QtGui.QWidget(self.Unsupervised)
        self.verticalLayoutWidget_3.setGeometry(QtCore.QRect(10, 80, 421, 251))
        self.verticalLayoutWidget_3.setObjectName(_fromUtf8("verticalLayoutWidget_3"))
        self.verticalLayout_3 = QtGui.QVBoxLayout(self.verticalLayoutWidget_3)
        self.verticalLayout_3.setMargin(0)
        self.verticalLayout_3.setObjectName(_fromUtf8("verticalLayout_3"))
        self.checkBox_2 = QtGui.QCheckBox(self.verticalLayoutWidget_3)
        self.checkBox_2.setObjectName(_fromUtf8("checkBox_2"))
        self.verticalLayout_3.addWidget(self.checkBox_2)
        self.checkBox_3 = QtGui.QCheckBox(self.verticalLayoutWidget_3)
        self.checkBox_3.setObjectName(_fromUtf8("checkBox_3"))
        self.verticalLayout_3.addWidget(self.checkBox_3)
        self.checkBox_4 = QtGui.QCheckBox(self.verticalLayoutWidget_3)
        self.checkBox_4.setObjectName(_fromUtf8("checkBox_4"))
        self.verticalLayout_3.addWidget(self.checkBox_4)
        self.checkBox_5 = QtGui.QCheckBox(self.verticalLayoutWidget_3)
        self.checkBox_5.setObjectName(_fromUtf8("checkBox_5"))
        self.verticalLayout_3.addWidget(self.checkBox_5)
        self.checkBox = QtGui.QCheckBox(self.verticalLayoutWidget_3)
        self.checkBox.setObjectName(_fromUtf8("checkBox"))
        self.verticalLayout_3.addWidget(self.checkBox)
        self.pushButton_25 = QtGui.QPushButton(self.Unsupervised)
        self.pushButton_25.setGeometry(QtCore.QRect(10, 330, 419, 26))
        self.pushButton_25.setObjectName(_fromUtf8("pushButton_25"))
        TabWidget.addTab(self.Unsupervised, _fromUtf8(""))
        self.e = QtGui.QWidget()
        self.e.setObjectName(_fromUtf8("e"))
        self.horizontalWidget_3 = QtGui.QWidget(self.e)
        self.horizontalWidget_3.setGeometry(QtCore.QRect(0, 0, 801, 51))
        self.horizontalWidget_3.setObjectName(_fromUtf8("horizontalWidget_3"))
        self.horizontalLayout_3 = QtGui.QHBoxLayout(self.horizontalWidget_3)
        self.horizontalLayout_3.setMargin(0)
        self.horizontalLayout_3.setObjectName(_fromUtf8("horizontalLayout_3"))
        self.pushButton_9 = QtGui.QPushButton(self.horizontalWidget_3)
        self.pushButton_9.setObjectName(_fromUtf8("pushButton_9"))
        self.horizontalLayout_3.addWidget(self.pushButton_9)
        self.pushButton = QtGui.QPushButton(self.horizontalWidget_3)
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        self.horizontalLayout_3.addWidget(self.pushButton)
        self.pushButton_2 = QtGui.QPushButton(self.horizontalWidget_3)
        self.pushButton_2.setObjectName(_fromUtf8("pushButton_2"))
        self.horizontalLayout_3.addWidget(self.pushButton_2)
        self.pushButton_10 = QtGui.QPushButton(self.horizontalWidget_3)
        self.pushButton_10.setObjectName(_fromUtf8("pushButton_10"))
        self.horizontalLayout_3.addWidget(self.pushButton_10)
        self.pushButton_11 = QtGui.QPushButton(self.horizontalWidget_3)
        self.pushButton_11.setObjectName(_fromUtf8("pushButton_11"))
        self.horizontalLayout_3.addWidget(self.pushButton_11)
        TabWidget.addTab(self.e, _fromUtf8(""))
        self.tab = QtGui.QWidget()
        self.tab.setObjectName(_fromUtf8("tab"))
        self.horizontalWidget_4 = QtGui.QWidget(self.tab)
        self.horizontalWidget_4.setGeometry(QtCore.QRect(0, 0, 841, 51))
        self.horizontalWidget_4.setObjectName(_fromUtf8("horizontalWidget_4"))
        self.horizontalLayout_4 = QtGui.QHBoxLayout(self.horizontalWidget_4)
        self.horizontalLayout_4.setMargin(0)
        self.horizontalLayout_4.setObjectName(_fromUtf8("horizontalLayout_4"))
        self.pushButton_12 = QtGui.QPushButton(self.horizontalWidget_4)
        self.pushButton_12.setObjectName(_fromUtf8("pushButton_12"))
        self.horizontalLayout_4.addWidget(self.pushButton_12)
        self.pushButton_13 = QtGui.QPushButton(self.horizontalWidget_4)
        self.pushButton_13.setObjectName(_fromUtf8("pushButton_13"))
        self.horizontalLayout_4.addWidget(self.pushButton_13)
        self.pushButton_14 = QtGui.QPushButton(self.horizontalWidget_4)
        self.pushButton_14.setObjectName(_fromUtf8("pushButton_14"))
        self.horizontalLayout_4.addWidget(self.pushButton_14)
        self.pushButton_26 = QtGui.QPushButton(self.horizontalWidget_4)
        self.pushButton_26.setObjectName(_fromUtf8("pushButton_26"))
        self.horizontalLayout_4.addWidget(self.pushButton_26)
        self.pushButton_27 = QtGui.QPushButton(self.horizontalWidget_4)
        self.pushButton_27.setObjectName(_fromUtf8("pushButton_27"))
        self.horizontalLayout_4.addWidget(self.pushButton_27)
        self.pushButton_28 = QtGui.QPushButton(self.horizontalWidget_4)
        self.pushButton_28.setObjectName(_fromUtf8("pushButton_28"))
        self.horizontalLayout_4.addWidget(self.pushButton_28)
        self.pushButton_29 = QtGui.QPushButton(self.horizontalWidget_4)
        self.pushButton_29.setObjectName(_fromUtf8("pushButton_29"))
        self.horizontalLayout_4.addWidget(self.pushButton_29)
        TabWidget.addTab(self.tab, _fromUtf8(""))
        self.tab_2 = QtGui.QWidget()
        self.tab_2.setObjectName(_fromUtf8("tab_2"))
        self.horizontalWidget_5 = QtGui.QWidget(self.tab_2)
        self.horizontalWidget_5.setGeometry(QtCore.QRect(0, 0, 841, 51))
        self.horizontalWidget_5.setObjectName(_fromUtf8("horizontalWidget_5"))
        self.horizontalLayout_5 = QtGui.QHBoxLayout(self.horizontalWidget_5)
        self.horizontalLayout_5.setMargin(0)
        self.horizontalLayout_5.setObjectName(_fromUtf8("horizontalLayout_5"))
        self.pushButton_15 = QtGui.QPushButton(self.horizontalWidget_5)
        self.pushButton_15.setObjectName(_fromUtf8("pushButton_15"))
        self.horizontalLayout_5.addWidget(self.pushButton_15)
        self.pushButton_16 = QtGui.QPushButton(self.horizontalWidget_5)
        self.pushButton_16.setObjectName(_fromUtf8("pushButton_16"))
        self.horizontalLayout_5.addWidget(self.pushButton_16)
        self.pushButton_17 = QtGui.QPushButton(self.horizontalWidget_5)
        self.pushButton_17.setObjectName(_fromUtf8("pushButton_17"))
        self.horizontalLayout_5.addWidget(self.pushButton_17)
        self.pushButton_30 = QtGui.QPushButton(self.horizontalWidget_5)
        self.pushButton_30.setObjectName(_fromUtf8("pushButton_30"))
        self.horizontalLayout_5.addWidget(self.pushButton_30)
        self.pushButton_31 = QtGui.QPushButton(self.horizontalWidget_5)
        self.pushButton_31.setObjectName(_fromUtf8("pushButton_31"))
        self.horizontalLayout_5.addWidget(self.pushButton_31)
        self.pushButton_32 = QtGui.QPushButton(self.horizontalWidget_5)
        self.pushButton_32.setObjectName(_fromUtf8("pushButton_32"))
        self.horizontalLayout_5.addWidget(self.pushButton_32)
        TabWidget.addTab(self.tab_2, _fromUtf8(""))
        self.tab_3 = QtGui.QWidget()
        self.tab_3.setObjectName(_fromUtf8("tab_3"))
        self.horizontalWidget_6 = QtGui.QWidget(self.tab_3)
        self.horizontalWidget_6.setGeometry(QtCore.QRect(0, 0, 501, 51))
        self.horizontalWidget_6.setObjectName(_fromUtf8("horizontalWidget_6"))
        self.horizontalLayout_6 = QtGui.QHBoxLayout(self.horizontalWidget_6)
        self.horizontalLayout_6.setMargin(0)
        self.horizontalLayout_6.setObjectName(_fromUtf8("horizontalLayout_6"))
        self.pushButton_18 = QtGui.QPushButton(self.horizontalWidget_6)
        self.pushButton_18.setObjectName(_fromUtf8("pushButton_18"))
        self.horizontalLayout_6.addWidget(self.pushButton_18)
        self.pushButton_19 = QtGui.QPushButton(self.horizontalWidget_6)
        self.pushButton_19.setObjectName(_fromUtf8("pushButton_19"))
        self.horizontalLayout_6.addWidget(self.pushButton_19)
        self.pushButton_20 = QtGui.QPushButton(self.horizontalWidget_6)
        self.pushButton_20.setObjectName(_fromUtf8("pushButton_20"))
        self.horizontalLayout_6.addWidget(self.pushButton_20)
        TabWidget.addTab(self.tab_3, _fromUtf8(""))
        self.tab_5 = QtGui.QWidget()
        self.tab_5.setObjectName(_fromUtf8("tab_5"))
        TabWidget.addTab(self.tab_5, _fromUtf8(""))
        self.tab_4 = QtGui.QWidget()
        self.tab_4.setObjectName(_fromUtf8("tab_4"))
        TabWidget.addTab(self.tab_4, _fromUtf8(""))

        self.retranslateUi(TabWidget)
        TabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(TabWidget)

    def retranslateUi(self, TabWidget):
        TabWidget.setWindowTitle(_translate("TabWidget", "Scikit GUI", None))
        self.pushButton_5.setText(_translate("TabWidget", "Open File", None))
        self.pushButton_4.setText(_translate("TabWidget", "Open URL", None))
        self.pushButton_3.setText(_translate("TabWidget", "Generate", None))
        self.label.setText(_translate("TabWidget", "Dataset Information", None))
        self.label_2.setText(_translate("TabWidget", "Dataset Plotter", None))
        TabWidget.setTabText(TabWidget.indexOf(self.Supervised), _translate("TabWidget", "Upload", None))
        self.pushButton_6.setText(_translate("TabWidget", "Normalization", None))
        self.pushButton_7.setText(_translate("TabWidget", "Standarization", None))
        self.pushButton_8.setText(_translate("TabWidget", "Binarization", None))
        self.pushButton_24.setText(_translate("TabWidget", "Imputation", None))
        self.pushButton_33.setText(_translate("TabWidget", "Whitening", None))
        self.label_3.setText(_translate("TabWidget", "Attributes", None))
        self.checkBox_2.setText(_translate("TabWidget", "Attribute 1", None))
        self.checkBox_3.setText(_translate("TabWidget", "Attribute 2", None))
        self.checkBox_4.setText(_translate("TabWidget", "Attribute 3", None))
        self.checkBox_5.setText(_translate("TabWidget", "Attribute 4", None))
        self.checkBox.setText(_translate("TabWidget", "Attribute 5", None))
        self.pushButton_25.setText(_translate("TabWidget", "Remove", None))
        TabWidget.setTabText(TabWidget.indexOf(self.Unsupervised), _translate("TabWidget", "Preprocess", None))
        self.pushButton_9.setText(_translate("TabWidget", "Linear", None))
        self.pushButton.setText(_translate("TabWidget", "Polynomial", None))
        self.pushButton_2.setText(_translate("TabWidget", "Least Squares", None))
        self.pushButton_10.setText(_translate("TabWidget", "Logistic", None))
        self.pushButton_11.setText(_translate("TabWidget", "Gradient Descent", None))
        TabWidget.setTabText(TabWidget.indexOf(self.e), _translate("TabWidget", "Regression", None))
        self.pushButton_12.setText(_translate("TabWidget", "Decision Tree", None))
        self.pushButton_13.setText(_translate("TabWidget", "Ensemble", None))
        self.pushButton_14.setText(_translate("TabWidget", "Neural Nets", None))
        self.pushButton_26.setText(_translate("TabWidget", "SVM", None))
        self.pushButton_27.setText(_translate("TabWidget", "Bayes Nets", None))
        self.pushButton_28.setText(_translate("TabWidget", "kNN", None))
        self.pushButton_29.setText(_translate("TabWidget", "Others", None))
        TabWidget.setTabText(TabWidget.indexOf(self.tab), _translate("TabWidget", "Classify", None))
        self.pushButton_15.setText(_translate("TabWidget", "kMeans", None))
        self.pushButton_16.setText(_translate("TabWidget", "EM", None))
        self.pushButton_17.setText(_translate("TabWidget", "Affinity Propogation", None))
        self.pushButton_30.setText(_translate("TabWidget", "Spectral", None))
        self.pushButton_31.setText(_translate("TabWidget", "Agglomerative", None))
        self.pushButton_32.setText(_translate("TabWidget", "DBSCAN", None))
        TabWidget.setTabText(TabWidget.indexOf(self.tab_2), _translate("TabWidget", "Cluster", None))
        self.pushButton_18.setText(_translate("TabWidget", "PCA", None))
        self.pushButton_19.setText(_translate("TabWidget", "ICA", None))
        self.pushButton_20.setText(_translate("TabWidget", "Random Projection", None))
        TabWidget.setTabText(TabWidget.indexOf(self.tab_3), _translate("TabWidget", "Reduce", None))
        TabWidget.setTabText(TabWidget.indexOf(self.tab_5), _translate("TabWidget", "Visualize", None))
        TabWidget.setTabText(TabWidget.indexOf(self.tab_4), _translate("TabWidget", "Other", None))

if __name__ == '__main__':
    app = QtGui.QApplication(sys.argv)
    ex = Ui_TabWidget()
    ex.show()
    sys.exit(app.exec_())