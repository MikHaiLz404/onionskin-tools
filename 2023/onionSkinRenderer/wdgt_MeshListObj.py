# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'onionSkinRendererObjectWidget.ui'
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

class Ui_onionSkinObject_layout(object):
    def setupUi(self, onionSkinObject_layout):
        onionSkinObject_layout.setObjectName("onionSkinObject_layout")
        onionSkinObject_layout.resize(204, 38)
        self.horizontalLayout = QtWidgets.QHBoxLayout(onionSkinObject_layout)
        self.horizontalLayout.setSpacing(3)
        self.horizontalLayout.setContentsMargins(4, 2, 4, 2)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.object_label = QtWidgets.QLabel(onionSkinObject_layout)
        self.object_label.setObjectName("object_label")
        self.horizontalLayout.addWidget(self.object_label)
        self.object_remove_btn = QtWidgets.QPushButton(onionSkinObject_layout)
        if PYSIDE_VERSION == 6:
            sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Minimum)
        else:
            sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.object_remove_btn.sizePolicy().hasHeightForWidth())
        self.object_remove_btn.setSizePolicy(sizePolicy)
        self.object_remove_btn.setMinimumSize(QtCore.QSize(16, 16))
        self.object_remove_btn.setMaximumSize(QtCore.QSize(16, 16))
        self.object_remove_btn.setObjectName("object_remove_btn")
        self.horizontalLayout.addWidget(self.object_remove_btn)

        self.retranslateUi(onionSkinObject_layout)
        QtCore.QMetaObject.connectSlotsByName(onionSkinObject_layout)

    def retranslateUi(self, onionSkinObject_layout):
        if PYSIDE_VERSION == 6:
            _translate = QtCore.QCoreApplication.translate
        else:
            def _translate(context, text, disambiguation=None, encoding=None):
                try:
                    return QtWidgets.QApplication.translate(context, text, disambiguation)
                except:
                    return text
        
        onionSkinObject_layout.setWindowTitle(_translate("onionSkinObject_layout", "Form"))
        self.object_label.setText(_translate("onionSkinObject_layout", "objectName"))
        self.object_remove_btn.setText(_translate("onionSkinObject_layout", "rm"))