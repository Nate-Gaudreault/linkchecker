# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui/options.ui'
#
# Created: Sat Nov  6 16:37:30 2010
#      by: PyQt4 UI code generator 4.7.3
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

class Ui_Options(object):
    def setupUi(self, Options):
        Options.setObjectName("Options")
        Options.setWindowModality(QtCore.Qt.ApplicationModal)
        Options.resize(271, 258)
        self.verticalLayout = QtGui.QVBoxLayout(Options)
        self.verticalLayout.setObjectName("verticalLayout")
        self.tabWidget = QtGui.QTabWidget(Options)
        self.tabWidget.setToolTip("")
        self.tabWidget.setObjectName("tabWidget")
        self.gui_options = QtGui.QWidget()
        self.gui_options.setToolTip("")
        self.gui_options.setObjectName("gui_options")
        self.verticalLayout_3 = QtGui.QVBoxLayout(self.gui_options)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.label_8 = QtGui.QLabel(self.gui_options)
        self.label_8.setTextFormat(QtCore.Qt.AutoText)
        self.label_8.setWordWrap(True)
        self.label_8.setObjectName("label_8")
        self.verticalLayout_3.addWidget(self.label_8)
        self.line = QtGui.QFrame(self.gui_options)
        self.line.setFrameShape(QtGui.QFrame.HLine)
        self.line.setFrameShadow(QtGui.QFrame.Sunken)
        self.line.setObjectName("line")
        self.verticalLayout_3.addWidget(self.line)
        self.frame = QtGui.QFrame(self.gui_options)
        self.frame.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtGui.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.formLayout = QtGui.QFormLayout(self.frame)
        self.formLayout.setFieldGrowthPolicy(QtGui.QFormLayout.ExpandingFieldsGrow)
        self.formLayout.setObjectName("formLayout")
        self.label = QtGui.QLabel(self.frame)
        self.label.setObjectName("label")
        self.formLayout.setWidget(0, QtGui.QFormLayout.LabelRole, self.label)
        self.recursionlevel = QtGui.QSpinBox(self.frame)
        self.recursionlevel.setMinimum(-1)
        self.recursionlevel.setMaximum(100)
        self.recursionlevel.setProperty("value", -1)
        self.recursionlevel.setObjectName("recursionlevel")
        self.formLayout.setWidget(0, QtGui.QFormLayout.FieldRole, self.recursionlevel)
        self.label_2 = QtGui.QLabel(self.frame)
        self.label_2.setObjectName("label_2")
        self.formLayout.setWidget(1, QtGui.QFormLayout.LabelRole, self.label_2)
        self.verbose = QtGui.QCheckBox(self.frame)
        self.verbose.setEnabled(True)
        self.verbose.setText("")
        self.verbose.setObjectName("verbose")
        self.formLayout.setWidget(1, QtGui.QFormLayout.FieldRole, self.verbose)
        self.label_4 = QtGui.QLabel(self.frame)
        self.label_4.setObjectName("label_4")
        self.formLayout.setWidget(2, QtGui.QFormLayout.LabelRole, self.label_4)
        self.debug = QtGui.QCheckBox(self.frame)
        self.debug.setText("")
        self.debug.setObjectName("debug")
        self.formLayout.setWidget(2, QtGui.QFormLayout.FieldRole, self.debug)
        spacerItem = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.formLayout.setItem(3, QtGui.QFormLayout.LabelRole, spacerItem)
        self.verticalLayout_3.addWidget(self.frame)
        self.widget = QtGui.QWidget(self.gui_options)
        self.widget.setObjectName("widget")
        self.horizontalLayout = QtGui.QHBoxLayout(self.widget)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.resetButton = QtGui.QPushButton(self.widget)
        self.resetButton.setObjectName("resetButton")
        self.horizontalLayout.addWidget(self.resetButton)
        self.closeButton = QtGui.QPushButton(self.widget)
        self.closeButton.setObjectName("closeButton")
        self.horizontalLayout.addWidget(self.closeButton)
        self.verticalLayout_3.addWidget(self.widget)
        self.tabWidget.addTab(self.gui_options, "")
        self.config_options = QtGui.QWidget()
        self.config_options.setToolTip("")
        self.config_options.setObjectName("config_options")
        self.verticalLayout_5 = QtGui.QVBoxLayout(self.config_options)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.label_9 = QtGui.QLabel(self.config_options)
        self.label_9.setTextFormat(QtCore.Qt.AutoText)
        self.label_9.setWordWrap(True)
        self.label_9.setObjectName("label_9")
        self.verticalLayout_5.addWidget(self.label_9)
        self.line_2 = QtGui.QFrame(self.config_options)
        self.line_2.setFrameShape(QtGui.QFrame.HLine)
        self.line_2.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.verticalLayout_5.addWidget(self.line_2)
        self.frame_2 = QtGui.QFrame(self.config_options)
        self.frame_2.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtGui.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.verticalLayout_4 = QtGui.QVBoxLayout(self.frame_2)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.label_6 = QtGui.QLabel(self.frame_2)
        self.label_6.setToolTip("")
        self.label_6.setObjectName("label_6")
        self.verticalLayout_4.addWidget(self.label_6)
        self.sys_config_button = QtGui.QPushButton(self.frame_2)
        self.sys_config_button.setEnabled(False)
        self.sys_config_button.setToolTip("")
        self.sys_config_button.setObjectName("sys_config_button")
        self.verticalLayout_4.addWidget(self.sys_config_button)
        spacerItem1 = QtGui.QSpacerItem(20, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.verticalLayout_4.addItem(spacerItem1)
        self.label_7 = QtGui.QLabel(self.frame_2)
        self.label_7.setObjectName("label_7")
        self.verticalLayout_4.addWidget(self.label_7)
        self.user_config_button = QtGui.QPushButton(self.frame_2)
        self.user_config_button.setEnabled(False)
        self.user_config_button.setToolTip("")
        self.user_config_button.setObjectName("user_config_button")
        self.verticalLayout_4.addWidget(self.user_config_button)
        spacerItem2 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout_4.addItem(spacerItem2)
        self.verticalLayout_5.addWidget(self.frame_2)
        self.tabWidget.addTab(self.config_options, "")
        self.verticalLayout.addWidget(self.tabWidget)

        self.retranslateUi(Options)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(Options)

    def retranslateUi(self, Options):
        Options.setWindowTitle(_("Dialog"))
        self.label_8.setText(_("The most common check options are configurable. They override any configuration file settings."))
        self.label.setToolTip(_("Check recursively all links up to given depth. A negative depth will enable infinite recursion."))
        self.label.setText(_("Recursive depth"))
        self.recursionlevel.setToolTip(_("Check recursively all links up to given depth. A negative depth will enable infinite recursion."))
        self.label_2.setToolTip(_("Log all checked URLs once. Default is to log only errors and warnings."))
        self.label_2.setText(_("Verbose output"))
        self.verbose.setToolTip(_("Log all checked URLs once. Default is to log only errors and warnings."))
        self.label_4.setText(_("Debug"))
        self.resetButton.setToolTip(_("Reset all options to default values."))
        self.resetButton.setText(_("Reset"))
        self.closeButton.setText(_("Close"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.gui_options), _("GUI options"))
        self.label_9.setText(_("The configuration files can be edited with an integrated text editor."))
        self.label_6.setText(_("System wide configuration file"))
        self.sys_config_button.setText(_("Edit"))
        self.label_7.setToolTip(_("Overrides system wide configuration file settings."))
        self.label_7.setText(_("User specific configuration file"))
        self.user_config_button.setText(_("Edit"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.config_options), _("Configuration files"))

