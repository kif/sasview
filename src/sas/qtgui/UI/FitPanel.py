# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'FitPanel.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

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

class Ui_FitPanel(object):
    def setupUi(self, FitPanel):
        FitPanel.setObjectName(_fromUtf8("FitPanel"))
        FitPanel.resize(636, 659)
        self.tab = QtGui.QWidget()
        self.tab.setObjectName(_fromUtf8("tab"))
        self.gridLayout_10 = QtGui.QGridLayout(self.tab)
        self.gridLayout_10.setObjectName(_fromUtf8("gridLayout_10"))
        self.groupBox = QtGui.QGroupBox(self.tab)
        self.groupBox.setObjectName(_fromUtf8("groupBox"))
        self.gridLayout_3 = QtGui.QGridLayout(self.groupBox)
        self.gridLayout_3.setObjectName(_fromUtf8("gridLayout_3"))
        self.horizontalLayout_4 = QtGui.QHBoxLayout()
        self.horizontalLayout_4.setObjectName(_fromUtf8("horizontalLayout_4"))
        self.label = QtGui.QLabel(self.groupBox)
        self.label.setObjectName(_fromUtf8("label"))
        self.horizontalLayout_4.addWidget(self.label)
        self.lineEdit = QtGui.QLineEdit(self.groupBox)
        self.lineEdit.setObjectName(_fromUtf8("lineEdit"))
        self.horizontalLayout_4.addWidget(self.lineEdit)
        self.gridLayout_3.addLayout(self.horizontalLayout_4, 0, 0, 1, 1)
        self.gridLayout_10.addWidget(self.groupBox, 0, 0, 1, 1)
        self.horizontalLayout_8 = QtGui.QHBoxLayout()
        self.horizontalLayout_8.setObjectName(_fromUtf8("horizontalLayout_8"))
        self.groupBox_2 = QtGui.QGroupBox(self.tab)
        self.groupBox_2.setObjectName(_fromUtf8("groupBox_2"))
        self.gridLayout_2 = QtGui.QGridLayout(self.groupBox_2)
        self.gridLayout_2.setObjectName(_fromUtf8("gridLayout_2"))
        self.gridLayout = QtGui.QGridLayout()
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.groupBox_3 = QtGui.QGroupBox(self.groupBox_2)
        self.groupBox_3.setObjectName(_fromUtf8("groupBox_3"))
        self.formLayout = QtGui.QFormLayout(self.groupBox_3)
        self.formLayout.setObjectName(_fromUtf8("formLayout"))
        self.comboBox = QtGui.QComboBox(self.groupBox_3)
        self.comboBox.setObjectName(_fromUtf8("comboBox"))
        self.comboBox.addItem(_fromUtf8(""))
        self.comboBox.addItem(_fromUtf8(""))
        self.comboBox.addItem(_fromUtf8(""))
        self.comboBox.addItem(_fromUtf8(""))
        self.comboBox.addItem(_fromUtf8(""))
        self.formLayout.setWidget(0, QtGui.QFormLayout.LabelRole, self.comboBox)
        self.pushButton = QtGui.QPushButton(self.groupBox_3)
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        self.formLayout.setWidget(0, QtGui.QFormLayout.FieldRole, self.pushButton)
        self.gridLayout.addWidget(self.groupBox_3, 0, 0, 2, 1)
        self.pushButton_2 = QtGui.QPushButton(self.groupBox_2)
        self.pushButton_2.setObjectName(_fromUtf8("pushButton_2"))
        self.gridLayout.addWidget(self.pushButton_2, 0, 1, 1, 1)
        self.pushButton_4 = QtGui.QPushButton(self.groupBox_2)
        self.pushButton_4.setEnabled(False)
        self.pushButton_4.setObjectName(_fromUtf8("pushButton_4"))
        self.gridLayout.addWidget(self.pushButton_4, 0, 2, 1, 1)
        self.pushButton_3 = QtGui.QPushButton(self.groupBox_2)
        self.pushButton_3.setObjectName(_fromUtf8("pushButton_3"))
        self.gridLayout.addWidget(self.pushButton_3, 1, 1, 1, 1)
        self.gridLayout_2.addLayout(self.gridLayout, 0, 0, 1, 1)
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.comboBox_2 = QtGui.QComboBox(self.groupBox_2)
        self.comboBox_2.setObjectName(_fromUtf8("comboBox_2"))
        self.horizontalLayout.addWidget(self.comboBox_2)
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.gridLayout_2.addLayout(self.horizontalLayout, 1, 0, 1, 1)
        self.horizontalLayout_8.addWidget(self.groupBox_2)
        spacerItem1 = QtGui.QSpacerItem(98, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_8.addItem(spacerItem1)
        self.gridLayout_10.addLayout(self.horizontalLayout_8, 1, 0, 1, 1)
        self.horizontalLayout_7 = QtGui.QHBoxLayout()
        self.horizontalLayout_7.setObjectName(_fromUtf8("horizontalLayout_7"))
        self.groupBox_4 = QtGui.QGroupBox(self.tab)
        self.groupBox_4.setObjectName(_fromUtf8("groupBox_4"))
        self.gridLayout_8 = QtGui.QGridLayout(self.groupBox_4)
        self.gridLayout_8.setObjectName(_fromUtf8("gridLayout_8"))
        self.horizontalLayout_3 = QtGui.QHBoxLayout()
        self.horizontalLayout_3.setObjectName(_fromUtf8("horizontalLayout_3"))
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.radioButton = QtGui.QRadioButton(self.groupBox_4)
        self.radioButton.setObjectName(_fromUtf8("radioButton"))
        self.horizontalLayout_2.addWidget(self.radioButton)
        self.radioButton_2 = QtGui.QRadioButton(self.groupBox_4)
        self.radioButton_2.setObjectName(_fromUtf8("radioButton_2"))
        self.horizontalLayout_2.addWidget(self.radioButton_2)
        self.pushButton_5 = QtGui.QPushButton(self.groupBox_4)
        self.pushButton_5.setObjectName(_fromUtf8("pushButton_5"))
        self.horizontalLayout_2.addWidget(self.pushButton_5)
        self.horizontalLayout_3.addLayout(self.horizontalLayout_2)
        self.gridLayout_8.addLayout(self.horizontalLayout_3, 0, 0, 1, 1)
        self.horizontalLayout_7.addWidget(self.groupBox_4)
        spacerItem2 = QtGui.QSpacerItem(371, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_7.addItem(spacerItem2)
        self.gridLayout_10.addLayout(self.horizontalLayout_7, 2, 0, 1, 2)
        self.groupBox_5 = QtGui.QGroupBox(self.tab)
        self.groupBox_5.setObjectName(_fromUtf8("groupBox_5"))
        self.gridLayout_9 = QtGui.QGridLayout(self.groupBox_5)
        self.gridLayout_9.setObjectName(_fromUtf8("gridLayout_9"))
        self.groupBox_6 = QtGui.QGroupBox(self.groupBox_5)
        self.groupBox_6.setObjectName(_fromUtf8("groupBox_6"))
        self.gridLayout_4 = QtGui.QGridLayout(self.groupBox_6)
        self.gridLayout_4.setObjectName(_fromUtf8("gridLayout_4"))
        self.horizontalLayout_5 = QtGui.QHBoxLayout()
        self.horizontalLayout_5.setObjectName(_fromUtf8("horizontalLayout_5"))
        self.comboBox_3 = QtGui.QComboBox(self.groupBox_6)
        self.comboBox_3.setObjectName(_fromUtf8("comboBox_3"))
        self.comboBox_3.addItem(_fromUtf8(""))
        self.comboBox_3.addItem(_fromUtf8(""))
        self.comboBox_3.addItem(_fromUtf8(""))
        self.comboBox_3.addItem(_fromUtf8(""))
        self.horizontalLayout_5.addWidget(self.comboBox_3)
        self.pushButton_6 = QtGui.QPushButton(self.groupBox_6)
        self.pushButton_6.setObjectName(_fromUtf8("pushButton_6"))
        self.horizontalLayout_5.addWidget(self.pushButton_6)
        self.gridLayout_4.addLayout(self.horizontalLayout_5, 0, 0, 1, 1)
        self.label_2 = QtGui.QLabel(self.groupBox_6)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.gridLayout_4.addWidget(self.label_2, 1, 0, 1, 1)
        self.gridLayout_9.addWidget(self.groupBox_6, 0, 0, 1, 1)
        self.groupBox_7 = QtGui.QGroupBox(self.groupBox_5)
        self.groupBox_7.setObjectName(_fromUtf8("groupBox_7"))
        self.gridLayout_6 = QtGui.QGridLayout(self.groupBox_7)
        self.gridLayout_6.setObjectName(_fromUtf8("gridLayout_6"))
        self.horizontalLayout_6 = QtGui.QHBoxLayout()
        self.horizontalLayout_6.setObjectName(_fromUtf8("horizontalLayout_6"))
        self.comboBox_5 = QtGui.QComboBox(self.groupBox_7)
        self.comboBox_5.setObjectName(_fromUtf8("comboBox_5"))
        self.comboBox_5.addItem(_fromUtf8(""))
        self.comboBox_5.addItem(_fromUtf8(""))
        self.comboBox_5.addItem(_fromUtf8(""))
        self.comboBox_5.addItem(_fromUtf8(""))
        self.horizontalLayout_6.addWidget(self.comboBox_5)
        self.pushButton_8 = QtGui.QPushButton(self.groupBox_7)
        self.pushButton_8.setObjectName(_fromUtf8("pushButton_8"))
        self.horizontalLayout_6.addWidget(self.pushButton_8)
        self.gridLayout_6.addLayout(self.horizontalLayout_6, 0, 0, 1, 1)
        self.gridLayout_9.addWidget(self.groupBox_7, 0, 1, 1, 1)
        self.gridLayout_7 = QtGui.QGridLayout()
        self.gridLayout_7.setObjectName(_fromUtf8("gridLayout_7"))
        self.label_4 = QtGui.QLabel(self.groupBox_5)
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.gridLayout_7.addWidget(self.label_4, 0, 0, 1, 1)
        self.label_5 = QtGui.QLabel(self.groupBox_5)
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.gridLayout_7.addWidget(self.label_5, 0, 1, 1, 1)
        self.label_6 = QtGui.QLabel(self.groupBox_5)
        self.label_6.setObjectName(_fromUtf8("label_6"))
        self.gridLayout_7.addWidget(self.label_6, 0, 2, 1, 1)
        self.label_7 = QtGui.QLabel(self.groupBox_5)
        self.label_7.setObjectName(_fromUtf8("label_7"))
        self.gridLayout_7.addWidget(self.label_7, 0, 3, 1, 1)
        self.pushButton_9 = QtGui.QPushButton(self.groupBox_5)
        self.pushButton_9.setObjectName(_fromUtf8("pushButton_9"))
        self.gridLayout_7.addWidget(self.pushButton_9, 1, 0, 1, 1)
        self.lineEdit_2 = QtGui.QLineEdit(self.groupBox_5)
        self.lineEdit_2.setObjectName(_fromUtf8("lineEdit_2"))
        self.gridLayout_7.addWidget(self.lineEdit_2, 1, 1, 1, 1)
        self.lineEdit_3 = QtGui.QLineEdit(self.groupBox_5)
        self.lineEdit_3.setObjectName(_fromUtf8("lineEdit_3"))
        self.gridLayout_7.addWidget(self.lineEdit_3, 1, 2, 1, 1)
        self.pushButton_10 = QtGui.QPushButton(self.groupBox_5)
        self.pushButton_10.setObjectName(_fromUtf8("pushButton_10"))
        self.gridLayout_7.addWidget(self.pushButton_10, 1, 3, 1, 1)
        self.gridLayout_9.addLayout(self.gridLayout_7, 1, 0, 1, 2)
        self.gridLayout_5 = QtGui.QGridLayout()
        self.gridLayout_5.setObjectName(_fromUtf8("gridLayout_5"))
        self.label_3 = QtGui.QLabel(self.groupBox_5)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.gridLayout_5.addWidget(self.label_3, 0, 0, 1, 1)
        self.label_8 = QtGui.QLabel(self.groupBox_5)
        self.label_8.setObjectName(_fromUtf8("label_8"))
        self.gridLayout_5.addWidget(self.label_8, 0, 1, 1, 1)
        self.horizontalLayout_9 = QtGui.QHBoxLayout()
        self.horizontalLayout_9.setObjectName(_fromUtf8("horizontalLayout_9"))
        self.label_9 = QtGui.QLabel(self.groupBox_5)
        self.label_9.setObjectName(_fromUtf8("label_9"))
        self.horizontalLayout_9.addWidget(self.label_9)
        self.checkBox = QtGui.QCheckBox(self.groupBox_5)
        self.checkBox.setObjectName(_fromUtf8("checkBox"))
        self.horizontalLayout_9.addWidget(self.checkBox)
        self.gridLayout_5.addLayout(self.horizontalLayout_9, 0, 2, 1, 1)
        self.lineEdit_4 = QtGui.QLineEdit(self.groupBox_5)
        self.lineEdit_4.setObjectName(_fromUtf8("lineEdit_4"))
        self.gridLayout_5.addWidget(self.lineEdit_4, 1, 0, 1, 1)
        self.lineEdit_5 = QtGui.QLineEdit(self.groupBox_5)
        self.lineEdit_5.setObjectName(_fromUtf8("lineEdit_5"))
        self.gridLayout_5.addWidget(self.lineEdit_5, 1, 1, 1, 1)
        self.lineEdit_6 = QtGui.QLineEdit(self.groupBox_5)
        self.lineEdit_6.setObjectName(_fromUtf8("lineEdit_6"))
        self.gridLayout_5.addWidget(self.lineEdit_6, 1, 2, 1, 1)
        self.gridLayout_9.addLayout(self.gridLayout_5, 2, 0, 1, 2)
        self.horizontalLayout_10 = QtGui.QHBoxLayout()
        self.horizontalLayout_10.setObjectName(_fromUtf8("horizontalLayout_10"))
        self.pushButton_7 = QtGui.QPushButton(self.groupBox_5)
        self.pushButton_7.setObjectName(_fromUtf8("pushButton_7"))
        self.horizontalLayout_10.addWidget(self.pushButton_7)
        self.pushButton_11 = QtGui.QPushButton(self.groupBox_5)
        self.pushButton_11.setObjectName(_fromUtf8("pushButton_11"))
        self.horizontalLayout_10.addWidget(self.pushButton_11)
        spacerItem3 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_10.addItem(spacerItem3)
        self.pushButton_12 = QtGui.QPushButton(self.groupBox_5)
        self.pushButton_12.setObjectName(_fromUtf8("pushButton_12"))
        self.horizontalLayout_10.addWidget(self.pushButton_12)
        self.gridLayout_9.addLayout(self.horizontalLayout_10, 3, 0, 1, 2)
        self.gridLayout_10.addWidget(self.groupBox_5, 3, 0, 1, 1)
        spacerItem4 = QtGui.QSpacerItem(90, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout_10.addItem(spacerItem4, 3, 1, 1, 1)
        FitPanel.addTab(self.tab, _fromUtf8(""))
        self.tab1 = QtGui.QWidget()
        self.tab1.setObjectName(_fromUtf8("tab1"))
        FitPanel.addTab(self.tab1, _fromUtf8(""))

        self.retranslateUi(FitPanel)
        FitPanel.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(FitPanel)

    def retranslateUi(self, FitPanel):
        FitPanel.setWindowTitle(_translate("FitPanel", "TabWidget", None))
        self.groupBox.setTitle(_translate("FitPanel", "I(q) data source", None))
        self.label.setText(_translate("FitPanel", "Name", None))
        self.groupBox_2.setTitle(_translate("FitPanel", "Model [M1]", None))
        self.groupBox_3.setTitle(_translate("FitPanel", "Category", None))
        self.comboBox.setItemText(0, _translate("FitPanel", "Uncategorized", None))
        self.comboBox.setItemText(1, _translate("FitPanel", "Shape-Independent", None))
        self.comboBox.setItemText(2, _translate("FitPanel", "Shapes", None))
        self.comboBox.setItemText(3, _translate("FitPanel", "Structure factor", None))
        self.comboBox.setItemText(4, _translate("FitPanel", "Customized Models", None))
        self.pushButton.setText(_translate("FitPanel", "Modify", None))
        self.pushButton_2.setText(_translate("FitPanel", "Description", None))
        self.pushButton_4.setText(_translate("FitPanel", "1D Mode", None))
        self.pushButton_3.setText(_translate("FitPanel", "Help", None))
        self.groupBox_4.setTitle(_translate("FitPanel", "Polydyspersity and Orientational Distribution", None))
        self.radioButton.setText(_translate("FitPanel", "On", None))
        self.radioButton_2.setText(_translate("FitPanel", "Off", None))
        self.pushButton_5.setText(_translate("FitPanel", "Help", None))
        self.groupBox_5.setTitle(_translate("FitPanel", "Fitting", None))
        self.groupBox_6.setTitle(_translate("FitPanel", "Instrumental Smearing", None))
        self.comboBox_3.setItemText(0, _translate("FitPanel", "None", None))
        self.comboBox_3.setItemText(1, _translate("FitPanel", "Use dQ Data", None))
        self.comboBox_3.setItemText(2, _translate("FitPanel", "Custom Pinhole Smear", None))
        self.comboBox_3.setItemText(3, _translate("FitPanel", "Custom Slit Smear", None))
        self.pushButton_6.setText(_translate("FitPanel", "Help", None))
        self.label_2.setText(_translate("FitPanel", "No smearing selected", None))
        self.groupBox_7.setTitle(_translate("FitPanel", "Set Weighting by Selecting dI Source", None))
        self.comboBox_5.setItemText(0, _translate("FitPanel", "No Weighting", None))
        self.comboBox_5.setItemText(1, _translate("FitPanel", "Use dI Data", None))
        self.comboBox_5.setItemText(2, _translate("FitPanel", "Use [sqrt(I Data)]", None))
        self.comboBox_5.setItemText(3, _translate("FitPanel", "Use [I Data]", None))
        self.pushButton_8.setText(_translate("FitPanel", "Help", None))
        self.label_4.setText(_translate("FitPanel", "Q Range", None))
        self.label_5.setText(_translate("FitPanel", "Min[1/A]", None))
        self.label_6.setText(_translate("FitPanel", "Max[1/A]", None))
        self.label_7.setText(_translate("FitPanel", "Masking (2D)", None))
        self.pushButton_9.setText(_translate("FitPanel", "Reset", None))
        self.pushButton_10.setText(_translate("FitPanel", "Editor", None))
        self.label_3.setText(_translate("FitPanel", "Chi2/Npts", None))
        self.label_8.setText(_translate("FitPanel", "Npts(Fit)", None))
        self.label_9.setText(_translate("FitPanel", "Npts", None))
        self.checkBox.setText(_translate("FitPanel", "Log", None))
        self.pushButton_7.setText(_translate("FitPanel", "Compute", None))
        self.pushButton_11.setText(_translate("FitPanel", "Fit", None))
        self.pushButton_12.setText(_translate("FitPanel", "Help", None))
        FitPanel.setTabText(FitPanel.indexOf(self.tab), _translate("FitPanel", "FitPage1", None))
        FitPanel.setTabText(FitPanel.indexOf(self.tab1), _translate("FitPanel", "FitPage2", None))
