# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'manuskript/ui/editors/mainEditor_ui.ui'
#
# Created: Sat Oct 14 21:30:36 2017
#      by: PyQt5 UI code generator 5.2.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_mainEditor(object):
    def setupUi(self, mainEditor):
        mainEditor.setObjectName("mainEditor")
        mainEditor.resize(791, 319)
        self.verticalLayout = QtWidgets.QVBoxLayout(mainEditor)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.tabSplitter = tabSplitter(mainEditor)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tabSplitter.sizePolicy().hasHeightForWidth())
        self.tabSplitter.setSizePolicy(sizePolicy)
        self.tabSplitter.setObjectName("tabSplitter")
        self.verticalLayout.addWidget(self.tabSplitter)
        self.horizontalLayout_19 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_19.setObjectName("horizontalLayout_19")
        self.btnGoUp = QtWidgets.QPushButton(mainEditor)
        self.btnGoUp.setText("")
        icon = QtGui.QIcon.fromTheme("go-up")
        self.btnGoUp.setIcon(icon)
        self.btnGoUp.setFlat(True)
        self.btnGoUp.setObjectName("btnGoUp")
        self.horizontalLayout_19.addWidget(self.btnGoUp)
        self.btnRedacFolderText = QtWidgets.QPushButton(mainEditor)
        self.btnRedacFolderText.setCheckable(True)
        self.btnRedacFolderText.setFlat(True)
        self.btnRedacFolderText.setObjectName("btnRedacFolderText")
        self.buttonGroup = QtWidgets.QButtonGroup(mainEditor)
        self.buttonGroup.setObjectName("buttonGroup")
        self.buttonGroup.addButton(self.btnRedacFolderText)
        self.horizontalLayout_19.addWidget(self.btnRedacFolderText)
        self.btnRedacFolderCork = QtWidgets.QPushButton(mainEditor)
        self.btnRedacFolderCork.setCheckable(True)
        self.btnRedacFolderCork.setChecked(True)
        self.btnRedacFolderCork.setFlat(True)
        self.btnRedacFolderCork.setObjectName("btnRedacFolderCork")
        self.buttonGroup.addButton(self.btnRedacFolderCork)
        self.horizontalLayout_19.addWidget(self.btnRedacFolderCork)
        self.btnRedacFolderOutline = QtWidgets.QPushButton(mainEditor)
        self.btnRedacFolderOutline.setCheckable(True)
        self.btnRedacFolderOutline.setFlat(True)
        self.btnRedacFolderOutline.setObjectName("btnRedacFolderOutline")
        self.buttonGroup.addButton(self.btnRedacFolderOutline)
        self.horizontalLayout_19.addWidget(self.btnRedacFolderOutline)
        self.btnImport = QtWidgets.QPushButton(mainEditor)
        self.btnImport.setText("")
        icon = QtGui.QIcon.fromTheme("document-open")
        self.btnImport.setIcon(icon)
        self.btnImport.setFlat(True)
        self.btnImport.setObjectName("btnImport")
        self.buttonGroup.addButton(self.btnImport)
        self.horizontalLayout_19.addWidget(self.btnImport)
        self.sldCorkSizeFactor = QtWidgets.QSlider(mainEditor)
        self.sldCorkSizeFactor.setMinimumSize(QtCore.QSize(100, 0))
        self.sldCorkSizeFactor.setMaximumSize(QtCore.QSize(200, 16777215))
        self.sldCorkSizeFactor.setMinimum(50)
        self.sldCorkSizeFactor.setMaximum(200)
        self.sldCorkSizeFactor.setProperty("value", 100)
        self.sldCorkSizeFactor.setOrientation(QtCore.Qt.Horizontal)
        self.sldCorkSizeFactor.setObjectName("sldCorkSizeFactor")
        self.horizontalLayout_19.addWidget(self.sldCorkSizeFactor)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_19.addItem(spacerItem)
        self.textFormat = textFormat(mainEditor)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.textFormat.sizePolicy().hasHeightForWidth())
        self.textFormat.setSizePolicy(sizePolicy)
        self.textFormat.setMinimumSize(QtCore.QSize(20, 20))
        self.textFormat.setObjectName("textFormat")
        self.horizontalLayout_19.addWidget(self.textFormat)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_19.addItem(spacerItem1)
        self.lblRedacWC = QtWidgets.QLabel(mainEditor)
        self.lblRedacWC.setMinimumSize(QtCore.QSize(10, 0))
        self.lblRedacWC.setText("")
        self.lblRedacWC.setObjectName("lblRedacWC")
        self.horizontalLayout_19.addWidget(self.lblRedacWC)
        self.lblRedacProgress = QtWidgets.QLabel(mainEditor)
        self.lblRedacProgress.setMinimumSize(QtCore.QSize(100, 6))
        self.lblRedacProgress.setMaximumSize(QtCore.QSize(200, 14))
        self.lblRedacProgress.setText("")
        self.lblRedacProgress.setObjectName("lblRedacProgress")
        self.horizontalLayout_19.addWidget(self.lblRedacProgress)
        self.btnRedacFullscreen = QtWidgets.QPushButton(mainEditor)
        self.btnRedacFullscreen.setText("")
        icon = QtGui.QIcon.fromTheme("view-fullscreen")
        self.btnRedacFullscreen.setIcon(icon)
        self.btnRedacFullscreen.setFlat(True)
        self.btnRedacFullscreen.setObjectName("btnRedacFullscreen")
        self.horizontalLayout_19.addWidget(self.btnRedacFullscreen)
        self.verticalLayout.addLayout(self.horizontalLayout_19)

        self.retranslateUi(mainEditor)
        QtCore.QMetaObject.connectSlotsByName(mainEditor)

    def retranslateUi(self, mainEditor):
        _translate = QtCore.QCoreApplication.translate
        mainEditor.setWindowTitle(_translate("mainEditor", "Form"))
        self.btnGoUp.setToolTip(_translate("mainEditor", "Go to parent item"))
        self.btnGoUp.setShortcut(_translate("mainEditor", "Alt+Up"))
        self.btnRedacFolderText.setText(_translate("mainEditor", "Text"))
        self.btnRedacFolderCork.setText(_translate("mainEditor", "Index cards"))
        self.btnRedacFolderOutline.setText(_translate("mainEditor", "Outline"))
        self.btnRedacFullscreen.setShortcut(_translate("mainEditor", "F11"))
        # TODO: Translation
        self.btnImport.setToolTip(_translate("mainEditor", "Import items from an OPML file into the current folder"))

from manuskript.ui.editors.tabSplitter import tabSplitter
from manuskript.ui.editors.textFormat import textFormat
