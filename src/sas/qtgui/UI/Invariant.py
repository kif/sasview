# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Invariant.ui'
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

class Ui_InvariantUI(object):
    def setupUi(self, InvariantUI):
        InvariantUI.setObjectName(_fromUtf8("InvariantUI"))
        InvariantUI.resize(439, 636)
        self.gridLayout_6 = QtGui.QGridLayout(InvariantUI)
        self.gridLayout_6.setObjectName(_fromUtf8("gridLayout_6"))
        self.groupBox = QtGui.QGroupBox(InvariantUI)
        self.groupBox.setObjectName(_fromUtf8("groupBox"))
        self.gridLayout_2 = QtGui.QGridLayout(self.groupBox)
        self.gridLayout_2.setObjectName(_fromUtf8("gridLayout_2"))
        self.horizontalLayout_4 = QtGui.QHBoxLayout()
        self.horizontalLayout_4.setObjectName(_fromUtf8("horizontalLayout_4"))
        self.label = QtGui.QLabel(self.groupBox)
        self.label.setObjectName(_fromUtf8("label"))
        self.horizontalLayout_4.addWidget(self.label)
        self.lineEdit = QtGui.QLineEdit(self.groupBox)
        self.lineEdit.setEnabled(False)
        self.lineEdit.setReadOnly(False)
        self.lineEdit.setObjectName(_fromUtf8("lineEdit"))
        self.horizontalLayout_4.addWidget(self.lineEdit)
        self.gridLayout_2.addLayout(self.horizontalLayout_4, 0, 0, 1, 1)
        self.groupBox_2 = QtGui.QGroupBox(self.groupBox)
        self.groupBox_2.setObjectName(_fromUtf8("groupBox_2"))
        self.gridLayout = QtGui.QGridLayout(self.groupBox_2)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.label_3 = QtGui.QLabel(self.groupBox_2)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.horizontalLayout.addWidget(self.label_3)
        self.lineEdit_2 = QtGui.QLineEdit(self.groupBox_2)
        self.lineEdit_2.setEnabled(False)
        self.lineEdit_2.setObjectName(_fromUtf8("lineEdit_2"))
        self.horizontalLayout.addWidget(self.lineEdit_2)
        self.label_4 = QtGui.QLabel(self.groupBox_2)
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.horizontalLayout.addWidget(self.label_4)
        self.lineEdit_3 = QtGui.QLineEdit(self.groupBox_2)
        self.lineEdit_3.setEnabled(False)
        self.lineEdit_3.setObjectName(_fromUtf8("lineEdit_3"))
        self.horizontalLayout.addWidget(self.lineEdit_3)
        self.label_2 = QtGui.QLabel(self.groupBox_2)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.horizontalLayout.addWidget(self.label_2)
        self.gridLayout.addLayout(self.horizontalLayout, 0, 0, 1, 1)
        self.gridLayout_2.addWidget(self.groupBox_2, 1, 0, 1, 1)
        self.gridLayout_6.addWidget(self.groupBox, 0, 0, 1, 1)
        self.groupBox_3 = QtGui.QGroupBox(InvariantUI)
        self.groupBox_3.setObjectName(_fromUtf8("groupBox_3"))
        self.gridLayout_4 = QtGui.QGridLayout(self.groupBox_3)
        self.gridLayout_4.setObjectName(_fromUtf8("gridLayout_4"))
        self.gridLayout_3 = QtGui.QGridLayout()
        self.gridLayout_3.setObjectName(_fromUtf8("gridLayout_3"))
        self.label_5 = QtGui.QLabel(self.groupBox_3)
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.gridLayout_3.addWidget(self.label_5, 0, 0, 1, 1)
        self.lineEdit_4 = QtGui.QLineEdit(self.groupBox_3)
        self.lineEdit_4.setObjectName(_fromUtf8("lineEdit_4"))
        self.gridLayout_3.addWidget(self.lineEdit_4, 0, 1, 1, 1)
        self.label_8 = QtGui.QLabel(self.groupBox_3)
        self.label_8.setObjectName(_fromUtf8("label_8"))
        self.gridLayout_3.addWidget(self.label_8, 0, 2, 1, 1)
        self.label_9 = QtGui.QLabel(self.groupBox_3)
        self.label_9.setObjectName(_fromUtf8("label_9"))
        self.gridLayout_3.addWidget(self.label_9, 0, 3, 1, 1)
        self.lineEdit_6 = QtGui.QLineEdit(self.groupBox_3)
        self.lineEdit_6.setObjectName(_fromUtf8("lineEdit_6"))
        self.gridLayout_3.addWidget(self.lineEdit_6, 0, 4, 1, 1)
        self.label_6 = QtGui.QLabel(self.groupBox_3)
        self.label_6.setObjectName(_fromUtf8("label_6"))
        self.gridLayout_3.addWidget(self.label_6, 1, 0, 1, 1)
        self.lineEdit_5 = QtGui.QLineEdit(self.groupBox_3)
        self.lineEdit_5.setObjectName(_fromUtf8("lineEdit_5"))
        self.gridLayout_3.addWidget(self.lineEdit_5, 1, 1, 1, 1)
        self.label_7 = QtGui.QLabel(self.groupBox_3)
        self.label_7.setObjectName(_fromUtf8("label_7"))
        self.gridLayout_3.addWidget(self.label_7, 1, 2, 1, 1)
        self.label_10 = QtGui.QLabel(self.groupBox_3)
        self.label_10.setObjectName(_fromUtf8("label_10"))
        self.gridLayout_3.addWidget(self.label_10, 1, 3, 1, 1)
        self.lineEdit_7 = QtGui.QLineEdit(self.groupBox_3)
        self.lineEdit_7.setObjectName(_fromUtf8("lineEdit_7"))
        self.gridLayout_3.addWidget(self.lineEdit_7, 1, 4, 1, 1)
        self.label_11 = QtGui.QLabel(self.groupBox_3)
        self.label_11.setObjectName(_fromUtf8("label_11"))
        self.gridLayout_3.addWidget(self.label_11, 1, 5, 1, 1)
        self.gridLayout_4.addLayout(self.gridLayout_3, 0, 0, 1, 1)
        self.gridLayout_6.addWidget(self.groupBox_3, 1, 0, 1, 1)
        self.groupBox_4 = QtGui.QGroupBox(InvariantUI)
        self.groupBox_4.setObjectName(_fromUtf8("groupBox_4"))
        self.gridLayout_9 = QtGui.QGridLayout(self.groupBox_4)
        self.gridLayout_9.setObjectName(_fromUtf8("gridLayout_9"))
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.label_12 = QtGui.QLabel(self.groupBox_4)
        self.label_12.setObjectName(_fromUtf8("label_12"))
        self.horizontalLayout_2.addWidget(self.label_12)
        self.label_14 = QtGui.QLabel(self.groupBox_4)
        self.label_14.setObjectName(_fromUtf8("label_14"))
        self.horizontalLayout_2.addWidget(self.label_14)
        self.lineEdit_8 = QtGui.QLineEdit(self.groupBox_4)
        self.lineEdit_8.setEnabled(False)
        self.lineEdit_8.setObjectName(_fromUtf8("lineEdit_8"))
        self.horizontalLayout_2.addWidget(self.lineEdit_8)
        self.label_13 = QtGui.QLabel(self.groupBox_4)
        self.label_13.setObjectName(_fromUtf8("label_13"))
        self.horizontalLayout_2.addWidget(self.label_13)
        self.lineEdit_9 = QtGui.QLineEdit(self.groupBox_4)
        self.lineEdit_9.setEnabled(False)
        self.lineEdit_9.setObjectName(_fromUtf8("lineEdit_9"))
        self.horizontalLayout_2.addWidget(self.lineEdit_9)
        self.label_15 = QtGui.QLabel(self.groupBox_4)
        self.label_15.setObjectName(_fromUtf8("label_15"))
        self.horizontalLayout_2.addWidget(self.label_15)
        self.gridLayout_9.addLayout(self.horizontalLayout_2, 0, 0, 1, 2)
        self.groupBox_5 = QtGui.QGroupBox(self.groupBox_4)
        self.groupBox_5.setObjectName(_fromUtf8("groupBox_5"))
        self.gridLayout_7 = QtGui.QGridLayout(self.groupBox_5)
        self.gridLayout_7.setObjectName(_fromUtf8("gridLayout_7"))
        self.checkBox = QtGui.QCheckBox(self.groupBox_5)
        self.checkBox.setObjectName(_fromUtf8("checkBox"))
        self.gridLayout_7.addWidget(self.checkBox, 0, 0, 1, 1)
        self.horizontalLayout_3 = QtGui.QHBoxLayout()
        self.horizontalLayout_3.setObjectName(_fromUtf8("horizontalLayout_3"))
        self.label_16 = QtGui.QLabel(self.groupBox_5)
        self.label_16.setObjectName(_fromUtf8("label_16"))
        self.horizontalLayout_3.addWidget(self.label_16)
        self.lineEdit_10 = QtGui.QLineEdit(self.groupBox_5)
        self.lineEdit_10.setObjectName(_fromUtf8("lineEdit_10"))
        self.horizontalLayout_3.addWidget(self.lineEdit_10)
        self.gridLayout_7.addLayout(self.horizontalLayout_3, 1, 0, 1, 1)
        self.formLayout = QtGui.QFormLayout()
        self.formLayout.setObjectName(_fromUtf8("formLayout"))
        self.radioButton = QtGui.QRadioButton(self.groupBox_5)
        self.radioButton.setObjectName(_fromUtf8("radioButton"))
        self.buttonGroup = QtGui.QButtonGroup(InvariantUI)
        self.buttonGroup.setObjectName(_fromUtf8("buttonGroup"))
        self.buttonGroup.addButton(self.radioButton)
        self.formLayout.setWidget(0, QtGui.QFormLayout.LabelRole, self.radioButton)
        self.radioButton_3 = QtGui.QRadioButton(self.groupBox_5)
        self.radioButton_3.setObjectName(_fromUtf8("radioButton_3"))
        self.buttonGroup_2 = QtGui.QButtonGroup(InvariantUI)
        self.buttonGroup_2.setObjectName(_fromUtf8("buttonGroup_2"))
        self.buttonGroup_2.addButton(self.radioButton_3)
        self.formLayout.setWidget(0, QtGui.QFormLayout.FieldRole, self.radioButton_3)
        self.radioButton_2 = QtGui.QRadioButton(self.groupBox_5)
        self.radioButton_2.setObjectName(_fromUtf8("radioButton_2"))
        self.buttonGroup.addButton(self.radioButton_2)
        self.formLayout.setWidget(1, QtGui.QFormLayout.LabelRole, self.radioButton_2)
        self.radioButton_4 = QtGui.QRadioButton(self.groupBox_5)
        self.radioButton_4.setObjectName(_fromUtf8("radioButton_4"))
        self.buttonGroup_2.addButton(self.radioButton_4)
        self.formLayout.setWidget(1, QtGui.QFormLayout.FieldRole, self.radioButton_4)
        self.gridLayout_7.addLayout(self.formLayout, 2, 0, 1, 1)
        self.horizontalLayout_6 = QtGui.QHBoxLayout()
        self.horizontalLayout_6.setObjectName(_fromUtf8("horizontalLayout_6"))
        self.label_17 = QtGui.QLabel(self.groupBox_5)
        self.label_17.setObjectName(_fromUtf8("label_17"))
        self.horizontalLayout_6.addWidget(self.label_17)
        self.lineEdit_11 = QtGui.QLineEdit(self.groupBox_5)
        self.lineEdit_11.setObjectName(_fromUtf8("lineEdit_11"))
        self.horizontalLayout_6.addWidget(self.lineEdit_11)
        self.gridLayout_7.addLayout(self.horizontalLayout_6, 3, 0, 1, 1)
        self.gridLayout_9.addWidget(self.groupBox_5, 1, 0, 1, 1)
        self.groupBox_6 = QtGui.QGroupBox(self.groupBox_4)
        self.groupBox_6.setObjectName(_fromUtf8("groupBox_6"))
        self.gridLayout_8 = QtGui.QGridLayout(self.groupBox_6)
        self.gridLayout_8.setObjectName(_fromUtf8("gridLayout_8"))
        self.checkBox_2 = QtGui.QCheckBox(self.groupBox_6)
        self.checkBox_2.setObjectName(_fromUtf8("checkBox_2"))
        self.gridLayout_8.addWidget(self.checkBox_2, 0, 0, 1, 1)
        self.horizontalLayout_5 = QtGui.QHBoxLayout()
        self.horizontalLayout_5.setObjectName(_fromUtf8("horizontalLayout_5"))
        self.label_18 = QtGui.QLabel(self.groupBox_6)
        self.label_18.setObjectName(_fromUtf8("label_18"))
        self.horizontalLayout_5.addWidget(self.label_18)
        self.lineEdit_12 = QtGui.QLineEdit(self.groupBox_6)
        self.lineEdit_12.setObjectName(_fromUtf8("lineEdit_12"))
        self.horizontalLayout_5.addWidget(self.lineEdit_12)
        self.gridLayout_8.addLayout(self.horizontalLayout_5, 1, 0, 1, 1)
        self.formLayout_2 = QtGui.QFormLayout()
        self.formLayout_2.setObjectName(_fromUtf8("formLayout_2"))
        self.radioButton_7 = QtGui.QRadioButton(self.groupBox_6)
        self.radioButton_7.setObjectName(_fromUtf8("radioButton_7"))
        self.buttonGroup_3 = QtGui.QButtonGroup(InvariantUI)
        self.buttonGroup_3.setObjectName(_fromUtf8("buttonGroup_3"))
        self.buttonGroup_3.addButton(self.radioButton_7)
        self.formLayout_2.setWidget(0, QtGui.QFormLayout.LabelRole, self.radioButton_7)
        self.radioButton_8 = QtGui.QRadioButton(self.groupBox_6)
        self.radioButton_8.setObjectName(_fromUtf8("radioButton_8"))
        self.buttonGroup_3.addButton(self.radioButton_8)
        self.formLayout_2.setWidget(1, QtGui.QFormLayout.LabelRole, self.radioButton_8)
        self.gridLayout_8.addLayout(self.formLayout_2, 2, 0, 1, 1)
        self.horizontalLayout_7 = QtGui.QHBoxLayout()
        self.horizontalLayout_7.setObjectName(_fromUtf8("horizontalLayout_7"))
        self.label_19 = QtGui.QLabel(self.groupBox_6)
        self.label_19.setObjectName(_fromUtf8("label_19"))
        self.horizontalLayout_7.addWidget(self.label_19)
        self.lineEdit_13 = QtGui.QLineEdit(self.groupBox_6)
        self.lineEdit_13.setObjectName(_fromUtf8("lineEdit_13"))
        self.horizontalLayout_7.addWidget(self.lineEdit_13)
        self.gridLayout_8.addLayout(self.horizontalLayout_7, 3, 0, 1, 1)
        self.gridLayout_9.addWidget(self.groupBox_6, 1, 1, 1, 1)
        self.gridLayout_6.addWidget(self.groupBox_4, 2, 0, 1, 1)
        self.groupBox_7 = QtGui.QGroupBox(InvariantUI)
        self.groupBox_7.setObjectName(_fromUtf8("groupBox_7"))
        self.gridLayout_5 = QtGui.QGridLayout(self.groupBox_7)
        self.gridLayout_5.setObjectName(_fromUtf8("gridLayout_5"))
        self.label_21 = QtGui.QLabel(self.groupBox_7)
        self.label_21.setObjectName(_fromUtf8("label_21"))
        self.gridLayout_5.addWidget(self.label_21, 0, 0, 1, 1)
        self.lineEdit_14 = QtGui.QLineEdit(self.groupBox_7)
        self.lineEdit_14.setEnabled(True)
        self.lineEdit_14.setReadOnly(True)
        self.lineEdit_14.setObjectName(_fromUtf8("lineEdit_14"))
        self.gridLayout_5.addWidget(self.lineEdit_14, 0, 1, 1, 1)
        self.label_20 = QtGui.QLabel(self.groupBox_7)
        self.label_20.setObjectName(_fromUtf8("label_20"))
        self.gridLayout_5.addWidget(self.label_20, 0, 2, 1, 1)
        self.lineEdit_15 = QtGui.QLineEdit(self.groupBox_7)
        self.lineEdit_15.setEnabled(True)
        self.lineEdit_15.setReadOnly(True)
        self.lineEdit_15.setObjectName(_fromUtf8("lineEdit_15"))
        self.gridLayout_5.addWidget(self.lineEdit_15, 0, 3, 1, 1)
        self.label_22 = QtGui.QLabel(self.groupBox_7)
        self.label_22.setObjectName(_fromUtf8("label_22"))
        self.gridLayout_5.addWidget(self.label_22, 1, 0, 1, 1)
        self.lineEdit_17 = QtGui.QLineEdit(self.groupBox_7)
        self.lineEdit_17.setEnabled(True)
        self.lineEdit_17.setReadOnly(True)
        self.lineEdit_17.setObjectName(_fromUtf8("lineEdit_17"))
        self.gridLayout_5.addWidget(self.lineEdit_17, 1, 1, 1, 1)
        self.label_23 = QtGui.QLabel(self.groupBox_7)
        self.label_23.setObjectName(_fromUtf8("label_23"))
        self.gridLayout_5.addWidget(self.label_23, 1, 2, 1, 1)
        self.lineEdit_16 = QtGui.QLineEdit(self.groupBox_7)
        self.lineEdit_16.setEnabled(True)
        self.lineEdit_16.setReadOnly(True)
        self.lineEdit_16.setObjectName(_fromUtf8("lineEdit_16"))
        self.gridLayout_5.addWidget(self.lineEdit_16, 1, 3, 1, 1)
        self.label_24 = QtGui.QLabel(self.groupBox_7)
        self.label_24.setObjectName(_fromUtf8("label_24"))
        self.gridLayout_5.addWidget(self.label_24, 1, 4, 1, 1)
        self.line = QtGui.QFrame(self.groupBox_7)
        self.line.setFrameShape(QtGui.QFrame.HLine)
        self.line.setFrameShadow(QtGui.QFrame.Sunken)
        self.line.setObjectName(_fromUtf8("line"))
        self.gridLayout_5.addWidget(self.line, 2, 0, 1, 5)
        self.label_25 = QtGui.QLabel(self.groupBox_7)
        self.label_25.setObjectName(_fromUtf8("label_25"))
        self.gridLayout_5.addWidget(self.label_25, 3, 0, 1, 1)
        self.lineEdit_19 = QtGui.QLineEdit(self.groupBox_7)
        self.lineEdit_19.setEnabled(True)
        self.lineEdit_19.setStyleSheet(_fromUtf8("background-color: rgb(253, 253, 126);"))
        self.lineEdit_19.setReadOnly(True)
        self.lineEdit_19.setObjectName(_fromUtf8("lineEdit_19"))
        self.gridLayout_5.addWidget(self.lineEdit_19, 3, 1, 1, 1)
        self.label_26 = QtGui.QLabel(self.groupBox_7)
        self.label_26.setObjectName(_fromUtf8("label_26"))
        self.gridLayout_5.addWidget(self.label_26, 3, 2, 1, 1)
        self.lineEdit_18 = QtGui.QLineEdit(self.groupBox_7)
        self.lineEdit_18.setEnabled(True)
        self.lineEdit_18.setStyleSheet(_fromUtf8("background-color: rgb(253, 253, 126);"))
        self.lineEdit_18.setReadOnly(True)
        self.lineEdit_18.setObjectName(_fromUtf8("lineEdit_18"))
        self.gridLayout_5.addWidget(self.lineEdit_18, 3, 3, 1, 1)
        self.label_27 = QtGui.QLabel(self.groupBox_7)
        self.label_27.setObjectName(_fromUtf8("label_27"))
        self.gridLayout_5.addWidget(self.label_27, 3, 4, 1, 1)
        self.gridLayout_6.addWidget(self.groupBox_7, 3, 0, 1, 1)
        self.horizontalLayout_8 = QtGui.QHBoxLayout()
        self.horizontalLayout_8.setObjectName(_fromUtf8("horizontalLayout_8"))
        self.pushButton = QtGui.QPushButton(InvariantUI)
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        self.horizontalLayout_8.addWidget(self.pushButton)
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_8.addItem(spacerItem)
        self.pushButton_2 = QtGui.QPushButton(InvariantUI)
        self.pushButton_2.setObjectName(_fromUtf8("pushButton_2"))
        self.horizontalLayout_8.addWidget(self.pushButton_2)
        self.pushButton_3 = QtGui.QPushButton(InvariantUI)
        self.pushButton_3.setObjectName(_fromUtf8("pushButton_3"))
        self.horizontalLayout_8.addWidget(self.pushButton_3)
        self.gridLayout_6.addLayout(self.horizontalLayout_8, 4, 0, 1, 1)

        self.retranslateUi(InvariantUI)
        QtCore.QMetaObject.connectSlotsByName(InvariantUI)

    def retranslateUi(self, InvariantUI):
        InvariantUI.setWindowTitle(_translate("InvariantUI", "Dialog", None))
        self.groupBox.setTitle(_translate("InvariantUI", "I(q) data source", None))
        self.label.setText(_translate("InvariantUI", "Name:", None))
        self.groupBox_2.setTitle(_translate("InvariantUI", "Total Q range", None))
        self.label_3.setText(_translate("InvariantUI", "Min:", None))
        self.label_4.setText(_translate("InvariantUI", "Max:", None))
        self.label_2.setText(_translate("InvariantUI", "<html><head/><body><p>Å<span style=\" vertical-align:super;\">-1</span></p></body></html>", None))
        self.groupBox_3.setTitle(_translate("InvariantUI", "Customized input", None))
        self.label_5.setText(_translate("InvariantUI", "Background:", None))
        self.label_8.setText(_translate("InvariantUI", "<html><head/><body><p>cm<span style=\" vertical-align:super;\">-1</span></p></body></html>", None))
        self.label_9.setText(_translate("InvariantUI", "Scale:", None))
        self.label_6.setText(_translate("InvariantUI", "Contrast:", None))
        self.label_7.setText(_translate("InvariantUI", "<html><head/><body><p>Å<span style=\" vertical-align:super;\">-2</span></p></body></html>", None))
        self.label_10.setText(_translate("InvariantUI", "<html><head/><body><p>Porod<br/>constant:</p></body></html>", None))
        self.label_11.setText(_translate("InvariantUI", "<html><head/><body><p>(cm Å<span style=\" vertical-align:super;\">4</span>)<span style=\" vertical-align:super;\">-1</span></p></body></html>", None))
        self.groupBox_4.setTitle(_translate("InvariantUI", "Extrapolation", None))
        self.label_12.setText(_translate("InvariantUI", "Q Range:", None))
        self.label_14.setText(_translate("InvariantUI", "Min", None))
        self.label_13.setText(_translate("InvariantUI", "Max", None))
        self.label_15.setText(_translate("InvariantUI", "<html><head/><body><p>Å<span style=\" vertical-align:super;\">-1</span></p></body></html>", None))
        self.groupBox_5.setTitle(_translate("InvariantUI", "Low Q", None))
        self.checkBox.setText(_translate("InvariantUI", "Enable Low-Q extrapolation", None))
        self.label_16.setText(_translate("InvariantUI", "Npts:", None))
        self.radioButton.setText(_translate("InvariantUI", "Guinier", None))
        self.radioButton_3.setText(_translate("InvariantUI", "Fit", None))
        self.radioButton_2.setText(_translate("InvariantUI", "Power law", None))
        self.radioButton_4.setText(_translate("InvariantUI", "Fix", None))
        self.label_17.setText(_translate("InvariantUI", "Power:", None))
        self.groupBox_6.setTitle(_translate("InvariantUI", "High Q", None))
        self.checkBox_2.setText(_translate("InvariantUI", "Enable High-Q extrapolation", None))
        self.label_18.setText(_translate("InvariantUI", "Npts:", None))
        self.radioButton_7.setText(_translate("InvariantUI", "Fit", None))
        self.radioButton_8.setText(_translate("InvariantUI", "Fix", None))
        self.label_19.setText(_translate("InvariantUI", "Power:", None))
        self.groupBox_7.setTitle(_translate("InvariantUI", "Output", None))
        self.label_21.setText(_translate("InvariantUI", "Volume fraction:", None))
        self.label_20.setText(_translate("InvariantUI", "+/-", None))
        self.label_22.setText(_translate("InvariantUI", "Specific Surface:", None))
        self.label_23.setText(_translate("InvariantUI", "+/-", None))
        self.label_24.setText(_translate("InvariantUI", "<html><head/><body><p>Å<span style=\" vertical-align:super;\">-1</span></p></body></html>", None))
        self.label_25.setText(_translate("InvariantUI", "Invariant Total [Q]:", None))
        self.label_26.setText(_translate("InvariantUI", "+/-", None))
        self.label_27.setText(_translate("InvariantUI", "<html><head/><body><p>(cm Å<span style=\" vertical-align:super;\">3</span>)<span style=\" vertical-align:super;\">-1</span></p></body></html>", None))
        self.pushButton.setText(_translate("InvariantUI", "Calculate", None))
        self.pushButton_2.setText(_translate("InvariantUI", "Status", None))
        self.pushButton_3.setText(_translate("InvariantUI", "Help", None))


class InvariantUI(QtGui.QDialog, Ui_InvariantUI):
    def __init__(self, parent=None, f=QtCore.Qt.WindowFlags()):
        QtGui.QDialog.__init__(self, parent, f)

        self.setupUi(self)

