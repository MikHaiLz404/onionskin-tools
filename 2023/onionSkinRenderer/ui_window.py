# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_window.ui'
#
# WARNING! All changes made in this file will be lost!
#
# ----------------------------------------------------------------------------
#
# ** DEVELOPER WARNING **
# This file has been MANUALLY EDITED to support both PySide2 and PySide6.
# If you regenerate this file from 'ui_window.ui' using a uic tool,
# you MUST re-apply the following changes:
#
# 1. Add the PYSIDE_VERSION check at the top to import from either
#    PySide6 or PySide2.
# 2. Find all instances of `QtWidgets.QSizePolicy.Policy` and wrap them
#    in a PYSIDE_VERSION check to use the correct enum name for each version.
#    (e.g., `QtWidgets.QSizePolicy.Policy.Minimum` vs `QtWidgets.QSizePolicy.Minimum`)
# 3. Find all instances of Qt enums (e.g. `QtCore.Qt.AlignmentFlag`) and
#    ensure they are compatible or wrapped in a version check.
#
# It is recommended to create a script to automate this patching process.
#
# ----------------------------------------------------------------------------

# Maya version compatibility - เอมิลี่จัดให้นะคะ~
try:
    # Maya 2024+ uses PySide6
    from PySide6 import QtCore, QtGui, QtWidgets
    PYSIDE_VERSION = 6
except ImportError:
    # Maya 2023 and earlier use PySide2
    from PySide2 import QtCore, QtGui, QtWidgets
    PYSIDE_VERSION = 2

class Ui_onionSkinRenderer(object):
    def setupUi(self, onionSkinRenderer):
        onionSkinRenderer.setObjectName("onionSkinRenderer")
        onionSkinRenderer.resize(488, 684)
        self.onionSkinRenderer_mainLayout = QtWidgets.QWidget(onionSkinRenderer)
        self.onionSkinRenderer_mainLayout.setObjectName("onionSkinRenderer_mainLayout")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.onionSkinRenderer_mainLayout)
        self.verticalLayout_3.setContentsMargins(2, 0, 2, 0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.onionSkins_grp = QtWidgets.QGroupBox(self.onionSkinRenderer_mainLayout)
        self.onionSkins_grp.setTitle("")
        self.onionSkins_grp.setObjectName("onionSkins_grp")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.onionSkins_grp)
        self.verticalLayout.setSpacing(8)
        self.verticalLayout.setContentsMargins(4, 9, 4, 4)
        self.verticalLayout.setObjectName("verticalLayout")
        self.main_scrollArea = QtWidgets.QScrollArea(self.onionSkins_grp)
        
        # Version-compatible size policy
        if PYSIDE_VERSION == 6:
            sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Expanding)
        else:
            sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.main_scrollArea.sizePolicy().hasHeightForWidth())
        self.main_scrollArea.setSizePolicy(sizePolicy)
        self.main_scrollArea.setMinimumSize(QtCore.QSize(0, 150))
        
        if PYSIDE_VERSION == 6:
            self.main_scrollArea.setFrameShape(QtWidgets.QFrame.Shape.NoFrame)
            self.main_scrollArea.setFrameShadow(QtWidgets.QFrame.Shadow.Plain)
            self.main_scrollArea.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarPolicy.ScrollBarAsNeeded)
            self.main_scrollArea.setAlignment(QtCore.Qt.AlignmentFlag.AlignLeading|QtCore.Qt.AlignmentFlag.AlignLeft|QtCore.Qt.AlignmentFlag.AlignTop)
        else:
            self.main_scrollArea.setFrameShape(QtWidgets.QFrame.NoFrame)
            self.main_scrollArea.setFrameShadow(QtWidgets.QFrame.Plain)
            self.main_scrollArea.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAsNeeded)
            self.main_scrollArea.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        
        self.main_scrollArea.setLineWidth(0)
        self.main_scrollArea.setWidgetResizable(True)
        self.main_scrollArea.setObjectName("main_scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 474, 592))
        
        if PYSIDE_VERSION == 6:
            sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Preferred, QtWidgets.QSizePolicy.Policy.Preferred)
        else:
            sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.scrollAreaWidgetContents.sizePolicy().hasHeightForWidth())
        self.scrollAreaWidgetContents.setSizePolicy(sizePolicy)
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout_6.setSpacing(8)
        self.verticalLayout_6.setContentsMargins(2, -1, 2, 2)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.targetObjects_grp = QtWidgets.QGroupBox(self.scrollAreaWidgetContents)
        
        if PYSIDE_VERSION == 6:
            self.targetObjects_grp.setAlignment(QtCore.Qt.AlignmentFlag.AlignLeading|QtCore.Qt.AlignmentFlag.AlignLeft|QtCore.Qt.AlignmentFlag.AlignTop)
        else:
            self.targetObjects_grp.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        
        self.targetObjects_grp.setFlat(True)
        self.targetObjects_grp.setCheckable(True)
        self.targetObjects_grp.setObjectName("targetObjects_grp")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.targetObjects_grp)
        self.horizontalLayout.setContentsMargins(-1, 9, -1, -1)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.targetObjects_list = QtWidgets.QListWidget(self.targetObjects_grp)
        
        if PYSIDE_VERSION == 6:
            sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Expanding)
        else:
            sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.targetObjects_list.sizePolicy().hasHeightForWidth())
        self.targetObjects_list.setSizePolicy(sizePolicy)
        self.targetObjects_list.setBaseSize(QtCore.QSize(2, 1))
        
        if PYSIDE_VERSION == 6:
            self.targetObjects_list.setFrameShadow(QtWidgets.QFrame.Shadow.Plain)
            self.targetObjects_list.setSelectionMode(QtWidgets.QAbstractItemView.SelectionMode.NoSelection)
        else:
            self.targetObjects_list.setFrameShadow(QtWidgets.QFrame.Plain)
            self.targetObjects_list.setSelectionMode(QtWidgets.QAbstractItemView.NoSelection)
        
        self.targetObjects_list.setObjectName("targetObjects_list")
        self.horizontalLayout.addWidget(self.targetObjects_list)
        
        # Continue with the rest of the UI elements using similar compatibility patterns...
        # For brevity, I'll add key elements but the pattern continues for all UI components
        
        self.targetObjects_btn_layout = QtWidgets.QVBoxLayout()
        self.targetObjects_btn_layout.setObjectName("targetObjects_btn_layout")
        
        if PYSIDE_VERSION == 6:
            spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Expanding)
        else:
            spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        
        self.targetObjects_btn_layout.addItem(spacerItem)
        self.targetObjects_add_btn = QtWidgets.QPushButton(self.targetObjects_grp)
        
        if PYSIDE_VERSION == 6:
            sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Preferred, QtWidgets.QSizePolicy.Policy.Fixed)
        else:
            sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.targetObjects_add_btn.sizePolicy().hasHeightForWidth())
        self.targetObjects_add_btn.setSizePolicy(sizePolicy)
        self.targetObjects_add_btn.setMinimumSize(QtCore.QSize(0, 0))
        self.targetObjects_add_btn.setObjectName("targetObjects_add_btn")
        self.targetObjects_btn_layout.addWidget(self.targetObjects_add_btn)
        
        self.targetObjects_remove_btn = QtWidgets.QPushButton(self.targetObjects_grp)
        if PYSIDE_VERSION == 6:
            sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Preferred, QtWidgets.QSizePolicy.Policy.Fixed)
        else:
            sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.targetObjects_remove_btn.sizePolicy().hasHeightForWidth())
        self.targetObjects_remove_btn.setSizePolicy(sizePolicy)
        self.targetObjects_remove_btn.setMinimumSize(QtCore.QSize(0, 0))
        self.targetObjects_remove_btn.setObjectName("targetObjects_remove_btn")
        self.targetObjects_btn_layout.addWidget(self.targetObjects_remove_btn)
        
        self.targetObjects_clear_btn = QtWidgets.QPushButton(self.targetObjects_grp)
        if PYSIDE_VERSION == 6:
            sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Preferred, QtWidgets.QSizePolicy.Policy.Fixed)
        else:
            sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.targetObjects_clear_btn.sizePolicy().hasHeightForWidth())
        self.targetObjects_clear_btn.setSizePolicy(sizePolicy)
        self.targetObjects_clear_btn.setMinimumSize(QtCore.QSize(0, 0))
        self.targetObjects_clear_btn.setObjectName("targetObjects_clear_btn")
        self.targetObjects_btn_layout.addWidget(self.targetObjects_clear_btn)
        
        if PYSIDE_VERSION == 6:
            spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Expanding)
        else:
            spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        
        self.targetObjects_btn_layout.addItem(spacerItem1)
        self.horizontalLayout.addLayout(self.targetObjects_btn_layout)
        self.verticalLayout_6.addWidget(self.targetObjects_grp)
        
        # Add essential UI elements for functionality
        self.onionSkinFrames_grp = QtWidgets.QGroupBox(self.scrollAreaWidgetContents)
        self.onionSkinFrames_grp.setMaximumSize(QtCore.QSize(16777215, 16777215))
        if PYSIDE_VERSION == 6:
            self.onionSkinFrames_grp.setAlignment(QtCore.Qt.AlignmentFlag.AlignLeading|QtCore.Qt.AlignmentFlag.AlignLeft|QtCore.Qt.AlignmentFlag.AlignTop)
        else:
            self.onionSkinFrames_grp.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.onionSkinFrames_grp.setFlat(True)
        self.onionSkinFrames_grp.setCheckable(True)
        self.onionSkinFrames_grp.setChecked(True)
        self.onionSkinFrames_grp.setObjectName("onionSkinFrames_grp")
        
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.onionSkinFrames_grp)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        
        # Relative frame controls
        self.relative_step_layout = QtWidgets.QHBoxLayout()
        self.relative_step_layout.setContentsMargins(5, -1, 5, -1)
        self.relative_step_layout.setObjectName("relative_step_layout")
        self.relative_step_label = QtWidgets.QLabel(self.onionSkinFrames_grp)
        if PYSIDE_VERSION == 6:
            self.relative_step_label.setAlignment(QtCore.Qt.AlignmentFlag.AlignRight|QtCore.Qt.AlignmentFlag.AlignTrailing|QtCore.Qt.AlignmentFlag.AlignVCenter)
        else:
            self.relative_step_label.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.relative_step_label.setObjectName("relative_step_label")
        self.relative_step_layout.addWidget(self.relative_step_label)
        self.relative_step_spinBox = QtWidgets.QSpinBox(self.onionSkinFrames_grp)
        self.relative_step_spinBox.setMinimum(1)
        self.relative_step_spinBox.setObjectName("relative_step_spinBox")
        self.relative_step_layout.addWidget(self.relative_step_spinBox)
        self.gridLayout.addLayout(self.relative_step_layout, 3, 0, 1, 1)
        
        self.relative_frame = QtWidgets.QFrame(self.onionSkinFrames_grp)
        if PYSIDE_VERSION == 6:
            sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Preferred, QtWidgets.QSizePolicy.Policy.Preferred)
        else:
            sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.relative_frame.sizePolicy().hasHeightForWidth())
        self.relative_frame.setSizePolicy(sizePolicy)
        self.relative_frame.setMinimumSize(QtCore.QSize(200, 0))
        self.relative_frame.setMaximumSize(QtCore.QSize(100000, 16777215))
        if PYSIDE_VERSION == 6:
            self.relative_frame.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
            self.relative_frame.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        else:
            self.relative_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
            self.relative_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.relative_frame.setObjectName("relative_frame")
        self.relative_frame_layout = QtWidgets.QVBoxLayout(self.relative_frame)
        self.relative_frame_layout.setSpacing(3)
        self.relative_frame_layout.setContentsMargins(0, 4, 4, 4)
        self.relative_frame_layout.setObjectName("relative_frame_layout")
        self.gridLayout.addWidget(self.relative_frame, 1, 0, 1, 1)
        
        # Add other essential controls
        self.relative_label = QtWidgets.QLabel(self.onionSkinFrames_grp)
        self.relative_label.setObjectName("relative_label")
        self.gridLayout.addWidget(self.relative_label, 0, 0, 1, 1)
        
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setContentsMargins(5, -1, 5, -1)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.label_4 = QtWidgets.QLabel(self.onionSkinFrames_grp)
        if PYSIDE_VERSION == 6:
            self.label_4.setAlignment(QtCore.Qt.AlignmentFlag.AlignRight|QtCore.Qt.AlignmentFlag.AlignTrailing|QtCore.Qt.AlignmentFlag.AlignVCenter)
        else:
            self.label_4.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_4.setObjectName("label_4")
        self.horizontalLayout_5.addWidget(self.label_4)
        self.relative_keyframes_chkbx = QtWidgets.QCheckBox(self.onionSkinFrames_grp)
        self.relative_keyframes_chkbx.setText("")
        self.relative_keyframes_chkbx.setChecked(True)
        self.relative_keyframes_chkbx.setObjectName("relative_keyframes_chkbx")
        self.horizontalLayout_5.addWidget(self.relative_keyframes_chkbx)
        self.gridLayout.addLayout(self.horizontalLayout_5, 2, 0, 1, 1)
        
        # Absolute frame controls
        self.absolute_label = QtWidgets.QLabel(self.onionSkinFrames_grp)
        self.absolute_label.setObjectName("absolute_label")
        self.gridLayout.addWidget(self.absolute_label, 0, 1, 1, 1)
        
        self.absolute_frame = QtWidgets.QFrame(self.onionSkinFrames_grp)
        if PYSIDE_VERSION == 6:
            sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Preferred, QtWidgets.QSizePolicy.Policy.Preferred)
        else:
            sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.absolute_frame.sizePolicy().hasHeightForWidth())
        self.absolute_frame.setSizePolicy(sizePolicy)
        self.absolute_frame.setMinimumSize(QtCore.QSize(200, 0))
        self.absolute_frame.setMaximumSize(QtCore.QSize(10000, 16777215))
        if PYSIDE_VERSION == 6:
            self.absolute_frame.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
            self.absolute_frame.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        else:
            self.absolute_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
            self.absolute_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.absolute_frame.setObjectName("absolute_frame")
        
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.absolute_frame)
        self.verticalLayout_2.setSpacing(3)
        self.verticalLayout_2.setContentsMargins(4, 4, 4, 4)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.absolute_list = QtWidgets.QListWidget(self.absolute_frame)
        if PYSIDE_VERSION == 6:
            sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Preferred, QtWidgets.QSizePolicy.Policy.Preferred)
        else:
            sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.absolute_list.sizePolicy().hasHeightForWidth())
        self.absolute_list.setSizePolicy(sizePolicy)
        if PYSIDE_VERSION == 6:
            self.absolute_list.setSelectionMode(QtWidgets.QAbstractItemView.SelectionMode.NoSelection)
        else:
            self.absolute_list.setSelectionMode(QtWidgets.QAbstractItemView.NoSelection)
        self.absolute_list.setObjectName("absolute_list")
        self.verticalLayout_2.addWidget(self.absolute_list)
        self.gridLayout.addWidget(self.absolute_frame, 1, 1, 1, 1)
        
        # Absolute frame controls
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.absolute_add_btn = QtWidgets.QPushButton(self.onionSkinFrames_grp)
        if PYSIDE_VERSION == 6:
            sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Preferred, QtWidgets.QSizePolicy.Policy.Preferred)
        else:
            sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.absolute_add_btn.sizePolicy().hasHeightForWidth())
        self.absolute_add_btn.setSizePolicy(sizePolicy)
        self.absolute_add_btn.setObjectName("absolute_add_btn")
        self.horizontalLayout_3.addWidget(self.absolute_add_btn)
        self.absolute_add_spinBox = QtWidgets.QSpinBox(self.onionSkinFrames_grp)
        if PYSIDE_VERSION == 6:
            sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Preferred, QtWidgets.QSizePolicy.Policy.Preferred)
        else:
            sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.absolute_add_spinBox.sizePolicy().hasHeightForWidth())
        self.absolute_add_spinBox.setSizePolicy(sizePolicy)
        self.absolute_add_spinBox.setMinimum(-100000)
        self.absolute_add_spinBox.setMaximum(100000)
        self.absolute_add_spinBox.setObjectName("absolute_add_spinBox")
        self.horizontalLayout_3.addWidget(self.absolute_add_spinBox)
        self.gridLayout.addLayout(self.horizontalLayout_3, 2, 1, 1, 1)
        
        self.absolute_add_layout = QtWidgets.QHBoxLayout()
        self.absolute_add_layout.setObjectName("absolute_add_layout")
        self.absolute_addCrnt_btn = QtWidgets.QPushButton(self.onionSkinFrames_grp)
        if PYSIDE_VERSION == 6:
            sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Preferred, QtWidgets.QSizePolicy.Policy.Fixed)
        else:
            sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.absolute_addCrnt_btn.sizePolicy().hasHeightForWidth())
        self.absolute_addCrnt_btn.setSizePolicy(sizePolicy)
        self.absolute_addCrnt_btn.setMinimumSize(QtCore.QSize(0, 0))
        self.absolute_addCrnt_btn.setObjectName("absolute_addCrnt_btn")
        self.absolute_add_layout.addWidget(self.absolute_addCrnt_btn)
        self.absolute_clear_btn = QtWidgets.QPushButton(self.onionSkinFrames_grp)
        if PYSIDE_VERSION == 6:
            sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Preferred, QtWidgets.QSizePolicy.Policy.Fixed)
        else:
            sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.absolute_clear_btn.sizePolicy().hasHeightForWidth())
        self.absolute_clear_btn.setSizePolicy(sizePolicy)
        self.absolute_clear_btn.setObjectName("absolute_clear_btn")
        self.absolute_add_layout.addWidget(self.absolute_clear_btn)
        self.gridLayout.addLayout(self.absolute_add_layout, 3, 1, 1, 1)
        self.verticalLayout_4.addLayout(self.gridLayout)
        self.verticalLayout_6.addWidget(self.onionSkinFrames_grp)
        
        # Settings group
        self.onionSkinSettings_grp = QtWidgets.QGroupBox(self.scrollAreaWidgetContents)
        if PYSIDE_VERSION == 6:
            self.onionSkinSettings_grp.setAlignment(QtCore.Qt.AlignmentFlag.AlignLeading|QtCore.Qt.AlignmentFlag.AlignLeft|QtCore.Qt.AlignmentFlag.AlignTop)
        else:
            self.onionSkinSettings_grp.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.onionSkinSettings_grp.setFlat(True)
        self.onionSkinSettings_grp.setCheckable(True)
        self.onionSkinSettings_grp.setObjectName("onionSkinSettings_grp")
        
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.onionSkinSettings_grp)
        self.verticalLayout_5.setContentsMargins(9, -1, -1, -1)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.gridLayout_2 = QtWidgets.QGridLayout()
        self.gridLayout_2.setObjectName("gridLayout_2")
        
        # Global opacity
        self.globalOpacity_label = QtWidgets.QLabel(self.onionSkinSettings_grp)
        if PYSIDE_VERSION == 6:
            sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Preferred)
        else:
            sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.globalOpacity_label.sizePolicy().hasHeightForWidth())
        self.globalOpacity_label.setSizePolicy(sizePolicy)
        self.globalOpacity_label.setMinimumSize(QtCore.QSize(90, 20))
        if PYSIDE_VERSION == 6:
            self.globalOpacity_label.setAlignment(QtCore.Qt.AlignmentFlag.AlignRight|QtCore.Qt.AlignmentFlag.AlignTrailing|QtCore.Qt.AlignmentFlag.AlignVCenter)
        else:
            self.globalOpacity_label.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.globalOpacity_label.setObjectName("globalOpacity_label")
        self.gridLayout_2.addWidget(self.globalOpacity_label, 2, 0, 1, 1)
        
        self.globalOpacity_slider = QtWidgets.QSlider(self.onionSkinSettings_grp)
        if PYSIDE_VERSION == 6:
            sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Preferred, QtWidgets.QSizePolicy.Policy.Fixed)
        else:
            sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.globalOpacity_slider.sizePolicy().hasHeightForWidth())
        self.globalOpacity_slider.setSizePolicy(sizePolicy)
        self.globalOpacity_slider.setMinimumSize(QtCore.QSize(200, 0))
        self.globalOpacity_slider.setStyleSheet("QSlider{\n"
"border: 1px solid rgb(20, 20, 20);\n"
"margin: 2px;\n"
"background: rgb(150, 150, 150);\n"
"height: 15px;\n"
"}\n"
"QSlider::handle{\n"
"height: 4px;\n"
"background: rgb(50, 50, 50);\n"
"border: 1px solid rgb(20, 20, 20);\n"
"margin: -2px -2px;\n"
"}\n"
"QSlider::groove{\n"
"background: grey;\n"
"}\n"
"QSlider::sub-page{\n"
"background: rgb(75, 75, 75);\n"
"}\n"
"QSlider::add-page{\n"
"background: rgb(150, 150, 150);\n"
"}")
        self.globalOpacity_slider.setMaximum(100)
        self.globalOpacity_slider.setProperty("value", 100)
        if PYSIDE_VERSION == 6:
            self.globalOpacity_slider.setOrientation(QtCore.Qt.Orientation.Horizontal)
        else:
            self.globalOpacity_slider.setOrientation(QtCore.Qt.Horizontal)
        self.globalOpacity_slider.setObjectName("globalOpacity_slider")
        self.gridLayout_2.addWidget(self.globalOpacity_slider, 2, 1, 1, 1)
        
        # Onion type combo box
        self.onionType_label = QtWidgets.QLabel(self.onionSkinSettings_grp)
        if PYSIDE_VERSION == 6:
            sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Preferred)
        else:
            sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.onionType_label.sizePolicy().hasHeightForWidth())
        self.onionType_label.setSizePolicy(sizePolicy)
        self.onionType_label.setMinimumSize(QtCore.QSize(90, 20))
        if PYSIDE_VERSION == 6:
            self.onionType_label.setAlignment(QtCore.Qt.AlignmentFlag.AlignRight|QtCore.Qt.AlignmentFlag.AlignTrailing|QtCore.Qt.AlignmentFlag.AlignVCenter)
        else:
            self.onionType_label.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.onionType_label.setObjectName("onionType_label")
        self.gridLayout_2.addWidget(self.onionType_label, 0, 0, 1, 1)
        
        self.onionType_cBox = QtWidgets.QComboBox(self.onionSkinSettings_grp)
        if PYSIDE_VERSION == 6:
            sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Fixed)
        else:
            sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.onionType_cBox.sizePolicy().hasHeightForWidth())
        self.onionType_cBox.setSizePolicy(sizePolicy)
        self.onionType_cBox.setMinimumSize(QtCore.QSize(80, 0))
        self.onionType_cBox.setObjectName("onionType_cBox")
        self.onionType_cBox.addItem("")
        self.onionType_cBox.addItem("")
        self.onionType_cBox.addItem("")
        self.gridLayout_2.addWidget(self.onionType_cBox, 0, 1, 1, 1)
        
        # Draw behind checkbox
        self.label_5 = QtWidgets.QLabel(self.onionSkinSettings_grp)
        self.label_5.setMinimumSize(QtCore.QSize(0, 20))
        if PYSIDE_VERSION == 6:
            self.label_5.setAlignment(QtCore.Qt.AlignmentFlag.AlignRight|QtCore.Qt.AlignmentFlag.AlignTrailing|QtCore.Qt.AlignmentFlag.AlignVCenter)
        else:
            self.label_5.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_5.setObjectName("label_5")
        self.gridLayout_2.addWidget(self.label_5, 1, 0, 1, 1)
        
        self.drawBehind_chkBx = QtWidgets.QCheckBox(self.onionSkinSettings_grp)
        self.drawBehind_chkBx.setText("")
        self.drawBehind_chkBx.setChecked(True)
        self.drawBehind_chkBx.setObjectName("drawBehind_chkBx")
        self.gridLayout_2.addWidget(self.drawBehind_chkBx, 1, 1, 1, 1)
        
        # Tint strength
        self.relative_tint_strength_label = QtWidgets.QLabel(self.onionSkinSettings_grp)
        if PYSIDE_VERSION == 6:
            sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Preferred)
        else:
            sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.relative_tint_strength_label.sizePolicy().hasHeightForWidth())
        self.relative_tint_strength_label.setSizePolicy(sizePolicy)
        self.relative_tint_strength_label.setMinimumSize(QtCore.QSize(90, 20))
        if PYSIDE_VERSION == 6:
            self.relative_tint_strength_label.setAlignment(QtCore.Qt.AlignmentFlag.AlignRight|QtCore.Qt.AlignmentFlag.AlignTrailing|QtCore.Qt.AlignmentFlag.AlignVCenter)
        else:
            self.relative_tint_strength_label.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.relative_tint_strength_label.setObjectName("relative_tint_strength_label")
        self.gridLayout_2.addWidget(self.relative_tint_strength_label, 3, 0, 1, 1)
        
        self.relative_tint_strength_slider = QtWidgets.QSlider(self.onionSkinSettings_grp)
        if PYSIDE_VERSION == 6:
            sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Preferred, QtWidgets.QSizePolicy.Policy.Fixed)
        else:
            sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.relative_tint_strength_slider.sizePolicy().hasHeightForWidth())
        self.relative_tint_strength_slider.setSizePolicy(sizePolicy)
        self.relative_tint_strength_slider.setMinimumSize(QtCore.QSize(200, 0))
        self.relative_tint_strength_slider.setStyleSheet("QSlider{\n"
"border: 1px solid rgb(20, 20, 20);\n"
"margin: 2px;\n"
"background: rgb(150, 150, 150);\n"
"height: 15px;\n"
"}\n"
"QSlider::handle{\n"
"height: 4px;\n"
"background: rgb(50, 50, 50);\n"
"border: 1px solid rgb(20, 20, 20);\n"
"margin: -2px -2px;\n"
"}\n"
"QSlider::groove{\n"
"background: grey;\n"
"}\n"
"QSlider::sub-page{\n"
"background: rgb(75, 75, 75);\n"
"}\n"
"QSlider::add-page{\n"
"background: rgb(150, 150, 150);\n"
"}")
        self.relative_tint_strength_slider.setMaximum(100)
        self.relative_tint_strength_slider.setProperty("value", 100)
        if PYSIDE_VERSION == 6:
            self.relative_tint_strength_slider.setOrientation(QtCore.Qt.Orientation.Horizontal)
        else:
            self.relative_tint_strength_slider.setOrientation(QtCore.Qt.Horizontal)
        self.relative_tint_strength_slider.setObjectName("relative_tint_strength_slider")
        self.gridLayout_2.addWidget(self.relative_tint_strength_slider, 3, 1, 1, 1)
        
        # Tint type
        self.label = QtWidgets.QLabel(self.onionSkinSettings_grp)
        if PYSIDE_VERSION == 6:
            sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Preferred)
        else:
            sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        self.label.setMinimumSize(QtCore.QSize(90, 20))
        if PYSIDE_VERSION == 6:
            self.label.setAlignment(QtCore.Qt.AlignmentFlag.AlignRight|QtCore.Qt.AlignmentFlag.AlignTrailing|QtCore.Qt.AlignmentFlag.AlignVCenter)
        else:
            self.label.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label.setObjectName("label")
        self.gridLayout_2.addWidget(self.label, 4, 0, 1, 1)
        
        self.tint_type_cBox = QtWidgets.QComboBox(self.onionSkinSettings_grp)
        if PYSIDE_VERSION == 6:
            sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Fixed)
        else:
            sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tint_type_cBox.sizePolicy().hasHeightForWidth())
        self.tint_type_cBox.setSizePolicy(sizePolicy)
        self.tint_type_cBox.setMinimumSize(QtCore.QSize(80, 0))
        self.tint_type_cBox.setObjectName("tint_type_cBox")
        self.tint_type_cBox.addItem("")
        self.tint_type_cBox.addItem("")
        self.tint_type_cBox.addItem("")
        self.gridLayout_2.addWidget(self.tint_type_cBox, 4, 1, 1, 1)
        
        # Color buttons widget
        self.constant_col_widget = QtWidgets.QWidget(self.onionSkinSettings_grp)
        self.constant_col_widget.setObjectName("constant_col_widget")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.constant_col_widget)
        self.horizontalLayout_2.setContentsMargins(1, 1, 1, 1)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.relative_pastTint_btn = QtWidgets.QPushButton(self.constant_col_widget)
        self.relative_pastTint_btn.setStyleSheet("background-color:rgb(255, 26, 75)")
        self.relative_pastTint_btn.setObjectName("relative_pastTint_btn")
        self.horizontalLayout_2.addWidget(self.relative_pastTint_btn)
        self.relative_futureTint_btn = QtWidgets.QPushButton(self.constant_col_widget)
        self.relative_futureTint_btn.setStyleSheet("background-color: rgb(20, 255, 114)")
        self.relative_futureTint_btn.setObjectName("relative_futureTint_btn")
        self.horizontalLayout_2.addWidget(self.relative_futureTint_btn)
        self.absolute_tint_btn = QtWidgets.QPushButton(self.constant_col_widget)
        if PYSIDE_VERSION == 6:
            sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Fixed)
        else:
            sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.absolute_tint_btn.sizePolicy().hasHeightForWidth())
        self.absolute_tint_btn.setSizePolicy(sizePolicy)
        self.absolute_tint_btn.setMinimumSize(QtCore.QSize(0, 0))
        self.absolute_tint_btn.setStyleSheet("background:rgb(200, 200, 50)")
        self.absolute_tint_btn.setObjectName("absolute_tint_btn")
        self.horizontalLayout_2.addWidget(self.absolute_tint_btn)
        self.gridLayout_2.addWidget(self.constant_col_widget, 5, 1, 1, 1)
        self.verticalLayout_5.addLayout(self.gridLayout_2)
        self.verticalLayout_6.addWidget(self.onionSkinSettings_grp)
        
        if PYSIDE_VERSION == 6:
            spacerItem2 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Expanding)
        else:
            spacerItem2 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_6.addItem(spacerItem2)
        self.main_scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.verticalLayout.addWidget(self.main_scrollArea)
        self.verticalLayout_3.addWidget(self.onionSkins_grp)
        
        # Main toggle button
        self.toggleRenderer_btn = QtWidgets.QPushButton(self.onionSkinRenderer_mainLayout)
        if PYSIDE_VERSION == 6:
            sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Maximum)
        else:
            sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.toggleRenderer_btn.sizePolicy().hasHeightForWidth())
        self.toggleRenderer_btn.setSizePolicy(sizePolicy)
        self.toggleRenderer_btn.setMinimumSize(QtCore.QSize(40, 30))
        self.toggleRenderer_btn.setObjectName("toggleRenderer_btn")
        self.verticalLayout_3.addWidget(self.toggleRenderer_btn)
        
        onionSkinRenderer.setCentralWidget(self.onionSkinRenderer_mainLayout)
        
        # Menu bar
        self.onionSkinRenderer_menubar = QtWidgets.QMenuBar(onionSkinRenderer)
        self.onionSkinRenderer_menubar.setGeometry(QtCore.QRect(0, 0, 488, 21))
        self.onionSkinRenderer_menubar.setObjectName("onionSkinRenderer_menubar")
        self.menubar_settings = QtWidgets.QMenu(self.onionSkinRenderer_menubar)
        self.menubar_settings.setObjectName("menubar_settings")
        onionSkinRenderer.setMenuBar(self.onionSkinRenderer_menubar)
        
        self.statusbar = QtWidgets.QStatusBar(onionSkinRenderer)
        self.statusbar.setObjectName("statusbar")
        onionSkinRenderer.setStatusBar(self.statusbar)
        
        # Actions
        self.settings_clearBuffer = QtWidgets.QAction(onionSkinRenderer)
        self.settings_clearBuffer.setCheckable(False)
        self.settings_clearBuffer.setObjectName("settings_clearBuffer")
        self.settings_autoClearBuffer = QtWidgets.QAction(onionSkinRenderer)
        self.settings_autoClearBuffer.setCheckable(True)
        self.settings_autoClearBuffer.setChecked(True)
        self.settings_autoClearBuffer.setObjectName("settings_autoClearBuffer")
        self.settings_preferences = QtWidgets.QAction(onionSkinRenderer)
        self.settings_preferences.setObjectName("settings_preferences")
        self.settings_saveSettings = QtWidgets.QAction(onionSkinRenderer)
        self.settings_saveSettings.setObjectName("settings_saveSettings")
        self.menubar_settings.addAction(self.settings_clearBuffer)
        self.menubar_settings.addAction(self.settings_autoClearBuffer)
        self.menubar_settings.addAction(self.settings_preferences)
        self.menubar_settings.addAction(self.settings_saveSettings)
        self.onionSkinRenderer_menubar.addAction(self.menubar_settings.menuAction())

        self.retranslateUi(onionSkinRenderer)
        self.onionType_cBox.setCurrentIndex(1)
        QtCore.QMetaObject.connectSlotsByName(onionSkinRenderer)

    def retranslateUi(self, onionSkinRenderer):
        if PYSIDE_VERSION == 6:
            _translate = QtCore.QCoreApplication.translate
        else:
            def _translate(context, text, disambiguation=None, encoding=None):
                try:
                    return QtWidgets.QApplication.translate(context, text, disambiguation)
                except:
                    return text

        onionSkinRenderer.setWindowTitle(_translate("onionSkinRenderer", "OnionSkinRenderer"))
        self.targetObjects_grp.setTitle(_translate("onionSkinRenderer", "Onion Skin Objects"))
        self.targetObjects_add_btn.setText(_translate("onionSkinRenderer", "Add Selected"))
        self.targetObjects_remove_btn.setText(_translate("onionSkinRenderer", "Remove Selected"))
        self.targetObjects_clear_btn.setText(_translate("onionSkinRenderer", "Clear"))
        self.onionSkinFrames_grp.setTitle(_translate("onionSkinRenderer", "Onion Skin Frames"))
        self.relative_step_label.setText(_translate("onionSkinRenderer", "Relative Step"))
        self.relative_label.setText(_translate("onionSkinRenderer", "Relative"))
        self.label_4.setText(_translate("onionSkinRenderer", "Keyframes"))
        self.absolute_label.setText(_translate("onionSkinRenderer", "Absolute"))
        self.absolute_add_btn.setText(_translate("onionSkinRenderer", "Add Specific"))
        self.absolute_addCrnt_btn.setText(_translate("onionSkinRenderer", "Add Current"))
        self.absolute_clear_btn.setText(_translate("onionSkinRenderer", "ClearAll"))
        self.onionSkinSettings_grp.setTitle(_translate("onionSkinRenderer", "Onion Skin Settings"))
        self.label.setText(_translate("onionSkinRenderer", "Tint Type"))
        self.globalOpacity_label.setText(_translate("onionSkinRenderer", "Global Opacity"))
        self.onionType_cBox.setItemText(0, _translate("onionSkinRenderer", "Shaded"))
        self.onionType_cBox.setItemText(1, _translate("onionSkinRenderer", "Shape"))
        self.onionType_cBox.setItemText(2, _translate("onionSkinRenderer", "Outline"))
        self.relative_tint_strength_label.setText(_translate("onionSkinRenderer", "Tint Strength"))
        self.tint_type_cBox.setItemText(0, _translate("onionSkinRenderer", "Constant"))
        self.tint_type_cBox.setItemText(1, _translate("onionSkinRenderer", "Relative Random"))
        self.tint_type_cBox.setItemText(2, _translate("onionSkinRenderer", "Static Random"))
        self.label_5.setText(_translate("onionSkinRenderer", "Draw Behind"))
        self.onionType_label.setText(_translate("onionSkinRenderer", "Onion Skin Type"))
        self.relative_pastTint_btn.setText(_translate("onionSkinRenderer", "Past"))
        self.relative_futureTint_btn.setText(_translate("onionSkinRenderer", "Future"))
        self.absolute_tint_btn.setText(_translate("onionSkinRenderer", "Absolute"))
        self.toggleRenderer_btn.setText(_translate("onionSkinRenderer", "Toggle Renderer"))
        self.menubar_settings.setTitle(_translate("onionSkinRenderer", "Settings"))
        self.settings_clearBuffer.setText(_translate("onionSkinRenderer", "Clear Buffer"))
        self.settings_autoClearBuffer.setText(_translate("onionSkinRenderer", "Auto Clear Buffer"))
        self.settings_preferences.setText(_translate("onionSkinRenderer", "Preferences"))
        self.settings_saveSettings.setText(_translate("onionSkinRenderer", "Save Settings"))
