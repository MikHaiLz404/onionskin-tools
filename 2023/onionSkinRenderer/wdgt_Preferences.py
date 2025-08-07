# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'onionSkinRendererPreferences.ui'
# Updated for Maya 2023 - PySide2/PySide6 compatibility
#
# WARNING! All changes made in this file will be lost!

# Maya version compatibility - เอมิลี่จัดให้นะคะ~
try:
    # Maya 2024+ uses PySide6
    from PySide6 import QtCore, QtGui, QtWidgets
    PYSIDE_VERSION = 6
except ImportError:
    # Maya 2023 and earlier use PySide2
    from PySide2 import QtCore, QtGui, QtWidgets
    PYSIDE_VERSION = 2

class Ui_onionSkinRendererPreferences(object):
    def setupUi(self, onionSkinRendererPreferences):
        onionSkinRendererPreferences.setObjectName("onionSkinRendererPreferences")
        onionSkinRendererPreferences.resize(279, 157)
        self.verticalLayout = QtWidgets.QVBoxLayout(onionSkinRendererPreferences)
        self.verticalLayout.setObjectName("verticalLayout")
        self.prefs_maxBuffer_layout = QtWidgets.QHBoxLayout()
        self.prefs_maxBuffer_layout.setObjectName("prefs_maxBuffer_layout")
        self.maxBuffer_label = QtWidgets.QLabel(onionSkinRendererPreferences)
        self.maxBuffer_label.setObjectName("maxBuffer_label")
        self.prefs_maxBuffer_layout.addWidget(self.maxBuffer_label)
        self.maxBuffer_spinBox = QtWidgets.QSpinBox(onionSkinRendererPreferences)
        self.maxBuffer_spinBox.setMinimum(1)
        self.maxBuffer_spinBox.setMaximum(10000)
        self.maxBuffer_spinBox.setProperty("value", 200)
        self.maxBuffer_spinBox.setObjectName("maxBuffer_spinBox")
        self.prefs_maxBuffer_layout.addWidget(self.maxBuffer_spinBox)
        self.verticalLayout.addLayout(self.prefs_maxBuffer_layout)
        self.prefs_relativeKeyCount_layout = QtWidgets.QHBoxLayout()
        self.prefs_relativeKeyCount_layout.setObjectName("prefs_relativeKeyCount_layout")
        self.relativeKeyCount_label = QtWidgets.QLabel(onionSkinRendererPreferences)
        self.relativeKeyCount_label.setObjectName("relativeKeyCount_label")
        self.prefs_relativeKeyCount_layout.addWidget(self.relativeKeyCount_label)
        self.relativeKeyCount_spinBox = QtWidgets.QSpinBox(onionSkinRendererPreferences)
        self.relativeKeyCount_spinBox.setMinimum(1)
        self.relativeKeyCount_spinBox.setMaximum(10)
        self.relativeKeyCount_spinBox.setProperty("value", 4)
        self.relativeKeyCount_spinBox.setObjectName("relativeKeyCount_spinBox")
        self.prefs_relativeKeyCount_layout.addWidget(self.relativeKeyCount_spinBox)
        self.verticalLayout.addLayout(self.prefs_relativeKeyCount_layout)
        self.prefs_outlineWidth = QtWidgets.QHBoxLayout()
        self.prefs_outlineWidth.setObjectName("prefs_outlineWidth")
        self.outlineWidth_label = QtWidgets.QLabel(onionSkinRendererPreferences)
        self.outlineWidth_label.setObjectName("outlineWidth_label")
        self.prefs_outlineWidth.addWidget(self.outlineWidth_label)
        self.outlineWidth_spinBox = QtWidgets.QSpinBox(onionSkinRendererPreferences)
        self.outlineWidth_spinBox.setMinimum(1)
        self.outlineWidth_spinBox.setMaximum(512)
        self.outlineWidth_spinBox.setProperty("value", 3)
        self.outlineWidth_spinBox.setObjectName("outlineWidth_spinBox")
        self.prefs_outlineWidth.addWidget(self.outlineWidth_spinBox)
        self.verticalLayout.addLayout(self.prefs_outlineWidth)
        self.prefs_tintSeed = QtWidgets.QHBoxLayout()
        self.prefs_tintSeed.setObjectName("prefs_tintSeed")
        self.tintSeed_label = QtWidgets.QLabel(onionSkinRendererPreferences)
        self.tintSeed_label.setObjectName("tintSeed_label")
        self.prefs_tintSeed.addWidget(self.tintSeed_label)
        self.tintSeed_spinBox = QtWidgets.QSpinBox(onionSkinRendererPreferences)
        self.tintSeed_spinBox.setObjectName("tintSeed_spinBox")
        self.prefs_tintSeed.addWidget(self.tintSeed_spinBox)
        self.verticalLayout.addLayout(self.prefs_tintSeed)
        self.prefs_dialogButtonBox = QtWidgets.QDialogButtonBox(onionSkinRendererPreferences)
        if PYSIDE_VERSION == 6:
            self.prefs_dialogButtonBox.setOrientation(QtCore.Qt.Orientation.Horizontal)
            self.prefs_dialogButtonBox.setStandardButtons(QtWidgets.QDialogButtonBox.StandardButton.Cancel|QtWidgets.QDialogButtonBox.StandardButton.Ok)
        else:
            self.prefs_dialogButtonBox.setOrientation(QtCore.Qt.Horizontal)
            self.prefs_dialogButtonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.prefs_dialogButtonBox.setObjectName("prefs_dialogButtonBox")
        self.verticalLayout.addWidget(self.prefs_dialogButtonBox)

        self.retranslateUi(onionSkinRendererPreferences)
        # Updated signal connection for both PySide versions
        if PYSIDE_VERSION == 6:
            self.prefs_dialogButtonBox.accepted.connect(onionSkinRendererPreferences.accept)
            self.prefs_dialogButtonBox.rejected.connect(onionSkinRendererPreferences.reject)
        else:
            self.prefs_dialogButtonBox.accepted.connect(onionSkinRendererPreferences.accept)
            self.prefs_dialogButtonBox.rejected.connect(onionSkinRendererPreferences.reject)
        QtCore.QMetaObject.connectSlotsByName(onionSkinRendererPreferences)

    def retranslateUi(self, onionSkinRendererPreferences):
        if PYSIDE_VERSION == 6:
            _translate = QtCore.QCoreApplication.translate
        else:
            def _translate(context, text, disambiguation=None, encoding=None):
                try:
                    return QtWidgets.QApplication.translate(context, text, disambiguation)
                except:
                    return text
        
        onionSkinRendererPreferences.setWindowTitle(_translate("onionSkinRendererPreferences", "Dialog"))
        self.maxBuffer_label.setText(_translate("onionSkinRendererPreferences", "Maximum Buffer Size"))
        self.relativeKeyCount_label.setText(_translate("onionSkinRendererPreferences", "Relative Keys Count"))
        self.outlineWidth_label.setText(_translate("onionSkinRendererPreferences", "Outline Width"))
        self.tintSeed_label.setText(_translate("onionSkinRendererPreferences", "Tint Seed"))