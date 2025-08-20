# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'form.ui'
##
## Created by: Qt User Interface Compiler version 6.9.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QAbstractItemView, QAbstractScrollArea, QApplication, QCheckBox,
    QComboBox, QDoubleSpinBox, QGridLayout, QHBoxLayout,
    QHeaderView, QLabel, QLayout, QLineEdit,
    QListWidget, QListWidgetItem, QPushButton, QSizePolicy,
    QSlider, QSpacerItem, QTabWidget, QTableWidget,
    QTableWidgetItem, QVBoxLayout, QWidget)

class Ui_Widget(object):
    def setupUi(self, Widget):
        if not Widget.objectName():
            Widget.setObjectName(u"Widget")
        Widget.resize(700, 562)
        Widget.setContextMenuPolicy(Qt.ContextMenuPolicy.DefaultContextMenu)
        icon = QIcon()
        icon.addFile(u"../../../../../Downloads/1345442634985898067.webp", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        Widget.setWindowIcon(icon)
        Widget.setWindowOpacity(1.000000000000000)
        Widget.setAutoFillBackground(False)
        self.horizontalLayout_5 = QHBoxLayout(Widget)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(10, 10, 10, 10)
        self.tabWidget = QTabWidget(Widget)
        self.tabWidget.setObjectName(u"tabWidget")
        self.tabWidget.setTabPosition(QTabWidget.TabPosition.North)
        self.tabWidget.setTabShape(QTabWidget.TabShape.Rounded)
        self.tabWidget.setUsesScrollButtons(False)
        self.tabWidget.setDocumentMode(True)
        self.tabWidget.setTabsClosable(False)
        self.tabWidget.setMovable(False)
        self.tabWidget.setTabBarAutoHide(True)
        self.homeTab = QWidget()
        self.homeTab.setObjectName(u"homeTab")
        self.verticalLayout_2 = QVBoxLayout(self.homeTab)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setSpacing(10)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(-1, 0, -1, -1)
        self.listWidget = QListWidget(self.homeTab)
        self.listWidget.setObjectName(u"listWidget")
        self.listWidget.setMinimumSize(QSize(250, 0))

        self.verticalLayout.addWidget(self.listWidget)


        self.gridLayout.addLayout(self.verticalLayout, 1, 0, 1, 1)

        self.label_2 = QLabel(self.homeTab)
        self.label_2.setObjectName(u"label_2")
        font = QFont()
        font.setPointSize(12)
        font.setBold(True)
        self.label_2.setFont(font)
        self.label_2.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout.addWidget(self.label_2, 0, 0, 1, 1)

        self.clearHistoryBtn = QPushButton(self.homeTab)
        self.clearHistoryBtn.setObjectName(u"clearHistoryBtn")
        self.clearHistoryBtn.setMinimumSize(QSize(100, 40))

        self.gridLayout.addWidget(self.clearHistoryBtn, 2, 0, 1, 1)


        self.verticalLayout_2.addLayout(self.gridLayout)

        self.recordingButtonLayout = QHBoxLayout()
        self.recordingButtonLayout.setSpacing(10)
        self.recordingButtonLayout.setObjectName(u"recordingButtonLayout")
        self.startRecordingBtn = QPushButton(self.homeTab)
        self.startRecordingBtn.setObjectName(u"startRecordingBtn")
        self.startRecordingBtn.setMinimumSize(QSize(0, 40))

        self.recordingButtonLayout.addWidget(self.startRecordingBtn)

        self.stopRecordingBtn = QPushButton(self.homeTab)
        self.stopRecordingBtn.setObjectName(u"stopRecordingBtn")
        self.stopRecordingBtn.setEnabled(False)
        self.stopRecordingBtn.setMinimumSize(QSize(0, 40))
        self.stopRecordingBtn.setContextMenuPolicy(Qt.ContextMenuPolicy.NoContextMenu)

        self.recordingButtonLayout.addWidget(self.stopRecordingBtn)


        self.verticalLayout_2.addLayout(self.recordingButtonLayout)

        self.tabWidget.addTab(self.homeTab, "")
        self.commandHistoryTab = QWidget()
        self.commandHistoryTab.setObjectName(u"commandHistoryTab")
        self.verticalLayout_12 = QVBoxLayout(self.commandHistoryTab)
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.gridLayout_2 = QGridLayout()
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.sortOptionsHistoryBtn = QPushButton(self.commandHistoryTab)
        self.sortOptionsHistoryBtn.setObjectName(u"sortOptionsHistoryBtn")
        self.sortOptionsHistoryBtn.setMinimumSize(QSize(100, 40))

        self.gridLayout_2.addWidget(self.sortOptionsHistoryBtn, 5, 1, 1, 1)

        self.executedCommandTable = QTableWidget(self.commandHistoryTab)
        if (self.executedCommandTable.columnCount() < 5):
            self.executedCommandTable.setColumnCount(5)
        self.executedCommandTable.setObjectName(u"executedCommandTable")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.executedCommandTable.sizePolicy().hasHeightForWidth())
        self.executedCommandTable.setSizePolicy(sizePolicy)
        font1 = QFont()
        font1.setBold(False)
        self.executedCommandTable.setFont(font1)
        self.executedCommandTable.setVerticalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAsNeeded)
        self.executedCommandTable.setHorizontalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAsNeeded)
        self.executedCommandTable.setSizeAdjustPolicy(QAbstractScrollArea.SizeAdjustPolicy.AdjustIgnored)
        self.executedCommandTable.setAutoScroll(True)
        self.executedCommandTable.setEditTriggers(QAbstractItemView.EditTrigger.NoEditTriggers)
        self.executedCommandTable.setSelectionMode(QAbstractItemView.SelectionMode.SingleSelection)
        self.executedCommandTable.setSelectionBehavior(QAbstractItemView.SelectionBehavior.SelectRows)
        self.executedCommandTable.setTextElideMode(Qt.TextElideMode.ElideRight)
        self.executedCommandTable.setVerticalScrollMode(QAbstractItemView.ScrollMode.ScrollPerPixel)
        self.executedCommandTable.setHorizontalScrollMode(QAbstractItemView.ScrollMode.ScrollPerPixel)
        self.executedCommandTable.setGridStyle(Qt.PenStyle.SolidLine)
        self.executedCommandTable.setRowCount(0)
        self.executedCommandTable.setColumnCount(5)
        self.executedCommandTable.verticalHeader().setVisible(True)

        self.gridLayout_2.addWidget(self.executedCommandTable, 3, 1, 1, 1)

        self.label_10 = QLabel(self.commandHistoryTab)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setFont(font)
        self.label_10.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout_2.addWidget(self.label_10, 0, 1, 1, 1)

        self.verticalLayout_13 = QVBoxLayout()
        self.verticalLayout_13.setObjectName(u"verticalLayout_13")
        self.verticalSpacer = QSpacerItem(0, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_13.addItem(self.verticalSpacer)

        self.label_12 = QLabel(self.commandHistoryTab)
        self.label_12.setObjectName(u"label_12")

        self.verticalLayout_13.addWidget(self.label_12)

        self.timeEdit = QLineEdit(self.commandHistoryTab)
        self.timeEdit.setObjectName(u"timeEdit")
        self.timeEdit.setMinimumSize(QSize(50, 0))
        self.timeEdit.setMaximumSize(QSize(200, 16777215))
        self.timeEdit.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_13.addWidget(self.timeEdit)

        self.dateEdit = QLineEdit(self.commandHistoryTab)
        self.dateEdit.setObjectName(u"dateEdit")
        self.dateEdit.setMinimumSize(QSize(50, 0))
        self.dateEdit.setMaximumSize(QSize(200, 16777215))
        self.dateEdit.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_13.addWidget(self.dateEdit)

        self.commandEdit = QLineEdit(self.commandHistoryTab)
        self.commandEdit.setObjectName(u"commandEdit")
        self.commandEdit.setMinimumSize(QSize(50, 0))
        self.commandEdit.setMaximumSize(QSize(200, 16777215))
        self.commandEdit.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_13.addWidget(self.commandEdit)

        self.speechEdit = QLineEdit(self.commandHistoryTab)
        self.speechEdit.setObjectName(u"speechEdit")
        self.speechEdit.setMinimumSize(QSize(50, 0))
        self.speechEdit.setMaximumSize(QSize(200, 16777215))
        self.speechEdit.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_13.addWidget(self.speechEdit)

        self.typeEdit = QLineEdit(self.commandHistoryTab)
        self.typeEdit.setObjectName(u"typeEdit")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.MinimumExpanding, QSizePolicy.Policy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.typeEdit.sizePolicy().hasHeightForWidth())
        self.typeEdit.setSizePolicy(sizePolicy1)
        self.typeEdit.setMinimumSize(QSize(50, 0))
        self.typeEdit.setMaximumSize(QSize(200, 16777215))
        self.typeEdit.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_13.addWidget(self.typeEdit)

        self.addItemHistoryBtn = QPushButton(self.commandHistoryTab)
        self.addItemHistoryBtn.setObjectName(u"addItemHistoryBtn")
        self.addItemHistoryBtn.setMaximumSize(QSize(200, 16777215))

        self.verticalLayout_13.addWidget(self.addItemHistoryBtn)

        self.verticalSpacer_2 = QSpacerItem(0, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_13.addItem(self.verticalSpacer_2)


        self.gridLayout_2.addLayout(self.verticalLayout_13, 3, 0, 1, 1)

        self.deleteRowHistoryBtn = QPushButton(self.commandHistoryTab)
        self.deleteRowHistoryBtn.setObjectName(u"deleteRowHistoryBtn")
        self.deleteRowHistoryBtn.setMinimumSize(QSize(100, 40))

        self.gridLayout_2.addWidget(self.deleteRowHistoryBtn, 4, 1, 1, 1)


        self.verticalLayout_12.addLayout(self.gridLayout_2)

        self.tabWidget.addTab(self.commandHistoryTab, "")
        self.customCommandsTab = QWidget()
        self.customCommandsTab.setObjectName(u"customCommandsTab")
        self.verticalLayout_6 = QVBoxLayout(self.customCommandsTab)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.gridLayout_4 = QGridLayout()
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.customCommandsTable = QTableWidget(self.customCommandsTab)
        if (self.customCommandsTable.columnCount() < 5):
            self.customCommandsTable.setColumnCount(5)
        self.customCommandsTable.setObjectName(u"customCommandsTable")
        sizePolicy.setHeightForWidth(self.customCommandsTable.sizePolicy().hasHeightForWidth())
        self.customCommandsTable.setSizePolicy(sizePolicy)
        self.customCommandsTable.setFont(font1)
        self.customCommandsTable.setVerticalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAsNeeded)
        self.customCommandsTable.setHorizontalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAsNeeded)
        self.customCommandsTable.setSizeAdjustPolicy(QAbstractScrollArea.SizeAdjustPolicy.AdjustIgnored)
        self.customCommandsTable.setAutoScroll(True)
        self.customCommandsTable.setEditTriggers(QAbstractItemView.EditTrigger.NoEditTriggers)
        self.customCommandsTable.setSelectionMode(QAbstractItemView.SelectionMode.SingleSelection)
        self.customCommandsTable.setSelectionBehavior(QAbstractItemView.SelectionBehavior.SelectRows)
        self.customCommandsTable.setTextElideMode(Qt.TextElideMode.ElideRight)
        self.customCommandsTable.setVerticalScrollMode(QAbstractItemView.ScrollMode.ScrollPerPixel)
        self.customCommandsTable.setHorizontalScrollMode(QAbstractItemView.ScrollMode.ScrollPerPixel)
        self.customCommandsTable.setGridStyle(Qt.PenStyle.SolidLine)
        self.customCommandsTable.setRowCount(0)
        self.customCommandsTable.setColumnCount(5)
        self.customCommandsTable.verticalHeader().setVisible(True)

        self.gridLayout_4.addWidget(self.customCommandsTable, 3, 1, 1, 1)

        self.sortOptionsCustomBtn = QPushButton(self.customCommandsTab)
        self.sortOptionsCustomBtn.setObjectName(u"sortOptionsCustomBtn")
        self.sortOptionsCustomBtn.setMinimumSize(QSize(100, 40))

        self.gridLayout_4.addWidget(self.sortOptionsCustomBtn, 5, 1, 1, 1)

        self.label_11 = QLabel(self.customCommandsTab)
        self.label_11.setObjectName(u"label_11")
        self.label_11.setFont(font)
        self.label_11.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout_4.addWidget(self.label_11, 0, 1, 1, 1)

        self.horizontalLayout_7 = QHBoxLayout()
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.pushButton = QPushButton(self.customCommandsTab)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setMinimumSize(QSize(0, 40))

        self.horizontalLayout_7.addWidget(self.pushButton)

        self.editCustomRowBtn = QPushButton(self.customCommandsTab)
        self.editCustomRowBtn.setObjectName(u"editCustomRowBtn")
        self.editCustomRowBtn.setEnabled(False)
        self.editCustomRowBtn.setMinimumSize(QSize(100, 40))

        self.horizontalLayout_7.addWidget(self.editCustomRowBtn)


        self.gridLayout_4.addLayout(self.horizontalLayout_7, 4, 1, 1, 1)


        self.verticalLayout_6.addLayout(self.gridLayout_4)

        self.tabWidget.addTab(self.customCommandsTab, "")
        self.settingsTab = QWidget()
        self.settingsTab.setObjectName(u"settingsTab")
        self.gridLayout_3 = QGridLayout(self.settingsTab)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.gridLayout_3.setHorizontalSpacing(60)
        self.gridLayout_3.setVerticalSpacing(0)
        self.gridLayout_3.setContentsMargins(20, -1, 20, -1)
        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setSpacing(8)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setSizeConstraint(QLayout.SizeConstraint.SetDefaultConstraint)
        self.verticalSpacer_3 = QSpacerItem(20, 20, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.MinimumExpanding)

        self.verticalLayout_3.addItem(self.verticalSpacer_3)

        self.label_3 = QLabel(self.settingsTab)
        self.label_3.setObjectName(u"label_3")
        sizePolicy2 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Fixed)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.label_3.sizePolicy().hasHeightForWidth())
        self.label_3.setSizePolicy(sizePolicy2)
        font2 = QFont()
        font2.setPointSize(11)
        font2.setBold(True)
        self.label_3.setFont(font2)
        self.label_3.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)

        self.verticalLayout_3.addWidget(self.label_3)

        self.label_4 = QLabel(self.settingsTab)
        self.label_4.setObjectName(u"label_4")
        sizePolicy2.setHeightForWidth(self.label_4.sizePolicy().hasHeightForWidth())
        self.label_4.setSizePolicy(sizePolicy2)

        self.verticalLayout_3.addWidget(self.label_4)

        self.verticalSpacer_4 = QSpacerItem(20, 20, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.MinimumExpanding)

        self.verticalLayout_3.addItem(self.verticalSpacer_4)


        self.gridLayout_3.addLayout(self.verticalLayout_3, 4, 0, 1, 1)

        self.verticalLayout_9 = QVBoxLayout()
        self.verticalLayout_9.setSpacing(8)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.verticalLayout_9.setSizeConstraint(QLayout.SizeConstraint.SetDefaultConstraint)
        self.verticalSpacer_7 = QSpacerItem(20, 30, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.MinimumExpanding)

        self.verticalLayout_9.addItem(self.verticalSpacer_7)

        self.label_6 = QLabel(self.settingsTab)
        self.label_6.setObjectName(u"label_6")
        sizePolicy2.setHeightForWidth(self.label_6.sizePolicy().hasHeightForWidth())
        self.label_6.setSizePolicy(sizePolicy2)
        self.label_6.setFont(font2)

        self.verticalLayout_9.addWidget(self.label_6)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalSlider_4 = QSlider(self.settingsTab)
        self.horizontalSlider_4.setObjectName(u"horizontalSlider_4")
        sizePolicy3 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Fixed)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.horizontalSlider_4.sizePolicy().hasHeightForWidth())
        self.horizontalSlider_4.setSizePolicy(sizePolicy3)
        self.horizontalSlider_4.setMinimumSize(QSize(50, 0))
        self.horizontalSlider_4.setOrientation(Qt.Orientation.Horizontal)

        self.horizontalLayout_3.addWidget(self.horizontalSlider_4)

        self.doubleSpinBox_2 = QDoubleSpinBox(self.settingsTab)
        self.doubleSpinBox_2.setObjectName(u"doubleSpinBox_2")

        self.horizontalLayout_3.addWidget(self.doubleSpinBox_2)


        self.verticalLayout_9.addLayout(self.horizontalLayout_3)

        self.verticalSpacer_8 = QSpacerItem(20, 30, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.MinimumExpanding)

        self.verticalLayout_9.addItem(self.verticalSpacer_8)


        self.gridLayout_3.addLayout(self.verticalLayout_9, 5, 1, 1, 1)

        self.verticalLayout_5 = QVBoxLayout()
        self.verticalLayout_5.setSpacing(8)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalSpacer_13 = QSpacerItem(20, 30, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.MinimumExpanding)

        self.verticalLayout_5.addItem(self.verticalSpacer_13)

        self.label_9 = QLabel(self.settingsTab)
        self.label_9.setObjectName(u"label_9")
        sizePolicy2.setHeightForWidth(self.label_9.sizePolicy().hasHeightForWidth())
        self.label_9.setSizePolicy(sizePolicy2)
        self.label_9.setFont(font2)

        self.verticalLayout_5.addWidget(self.label_9)

        self.inputDeviceBox = QComboBox(self.settingsTab)
        self.inputDeviceBox.addItem("")
        self.inputDeviceBox.addItem("")
        self.inputDeviceBox.setObjectName(u"inputDeviceBox")

        self.verticalLayout_5.addWidget(self.inputDeviceBox)

        self.verticalSpacer_14 = QSpacerItem(20, 30, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.MinimumExpanding)

        self.verticalLayout_5.addItem(self.verticalSpacer_14)


        self.gridLayout_3.addLayout(self.verticalLayout_5, 0, 0, 1, 1)

        self.verticalLayout_7 = QVBoxLayout()
        self.verticalLayout_7.setSpacing(8)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.verticalLayout_7.setSizeConstraint(QLayout.SizeConstraint.SetDefaultConstraint)
        self.verticalSpacer_9 = QSpacerItem(20, 30, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.MinimumExpanding)

        self.verticalLayout_7.addItem(self.verticalSpacer_9)

        self.label = QLabel(self.settingsTab)
        self.label.setObjectName(u"label")
        sizePolicy2.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy2)
        self.label.setFont(font2)

        self.verticalLayout_7.addWidget(self.label)

        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.inputVolSlider = QSlider(self.settingsTab)
        self.inputVolSlider.setObjectName(u"inputVolSlider")
        sizePolicy3.setHeightForWidth(self.inputVolSlider.sizePolicy().hasHeightForWidth())
        self.inputVolSlider.setSizePolicy(sizePolicy3)
        self.inputVolSlider.setMinimumSize(QSize(50, 0))
        self.inputVolSlider.setOrientation(Qt.Orientation.Horizontal)

        self.horizontalLayout_6.addWidget(self.inputVolSlider)

        self.doubleSpinBox_4 = QDoubleSpinBox(self.settingsTab)
        self.doubleSpinBox_4.setObjectName(u"doubleSpinBox_4")
        self.doubleSpinBox_4.setMaximum(100.000000000000000)

        self.horizontalLayout_6.addWidget(self.doubleSpinBox_4)


        self.verticalLayout_7.addLayout(self.horizontalLayout_6)

        self.verticalSpacer_10 = QSpacerItem(20, 30, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.MinimumExpanding)

        self.verticalLayout_7.addItem(self.verticalSpacer_10)


        self.gridLayout_3.addLayout(self.verticalLayout_7, 0, 1, 1, 1)

        self.openCalibrationBtn = QPushButton(self.settingsTab)
        self.openCalibrationBtn.setObjectName(u"openCalibrationBtn")
        self.openCalibrationBtn.setMinimumSize(QSize(0, 40))

        self.gridLayout_3.addWidget(self.openCalibrationBtn, 6, 0, 1, 2)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setSizeConstraint(QLayout.SizeConstraint.SetFixedSize)
        self.horizontalLayout_2.setContentsMargins(-1, -1, 12, 0)
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer)

        self.ttsCheckBox = QCheckBox(self.settingsTab)
        self.ttsCheckBox.setObjectName(u"ttsCheckBox")
        sizePolicy4 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Minimum)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.ttsCheckBox.sizePolicy().hasHeightForWidth())
        self.ttsCheckBox.setSizePolicy(sizePolicy4)
        self.ttsCheckBox.setMinimumSize(QSize(10, 10))
        self.ttsCheckBox.setMaximumSize(QSize(200, 200))
        self.ttsCheckBox.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.ttsCheckBox.setChecked(False)
        self.ttsCheckBox.setAutoRepeat(False)
        self.ttsCheckBox.setTristate(False)

        self.horizontalLayout_2.addWidget(self.ttsCheckBox)


        self.gridLayout_3.addLayout(self.horizontalLayout_2, 4, 1, 1, 1)

        self.verticalLayout_4 = QVBoxLayout()
        self.verticalLayout_4.setSpacing(8)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalSpacer_15 = QSpacerItem(20, 30, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.MinimumExpanding)

        self.verticalLayout_4.addItem(self.verticalSpacer_15)

        self.label_8 = QLabel(self.settingsTab)
        self.label_8.setObjectName(u"label_8")
        sizePolicy2.setHeightForWidth(self.label_8.sizePolicy().hasHeightForWidth())
        self.label_8.setSizePolicy(sizePolicy2)
        self.label_8.setFont(font2)

        self.verticalLayout_4.addWidget(self.label_8)

        self.outputDeviceBox = QComboBox(self.settingsTab)
        self.outputDeviceBox.addItem("")
        self.outputDeviceBox.addItem("")
        self.outputDeviceBox.setObjectName(u"outputDeviceBox")
        sizePolicy3.setHeightForWidth(self.outputDeviceBox.sizePolicy().hasHeightForWidth())
        self.outputDeviceBox.setSizePolicy(sizePolicy3)

        self.verticalLayout_4.addWidget(self.outputDeviceBox)

        self.verticalSpacer_16 = QSpacerItem(20, 30, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.MinimumExpanding)

        self.verticalLayout_4.addItem(self.verticalSpacer_16)


        self.gridLayout_3.addLayout(self.verticalLayout_4, 3, 0, 1, 1)

        self.verticalLayout_10 = QVBoxLayout()
        self.verticalLayout_10.setSpacing(8)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.verticalLayout_10.setSizeConstraint(QLayout.SizeConstraint.SetDefaultConstraint)
        self.verticalSpacer_11 = QSpacerItem(20, 30, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.MinimumExpanding)

        self.verticalLayout_10.addItem(self.verticalSpacer_11)

        self.label_7 = QLabel(self.settingsTab)
        self.label_7.setObjectName(u"label_7")
        sizePolicy2.setHeightForWidth(self.label_7.sizePolicy().hasHeightForWidth())
        self.label_7.setSizePolicy(sizePolicy2)
        self.label_7.setFont(font2)

        self.verticalLayout_10.addWidget(self.label_7)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.outputVolSlider = QSlider(self.settingsTab)
        self.outputVolSlider.setObjectName(u"outputVolSlider")
        sizePolicy3.setHeightForWidth(self.outputVolSlider.sizePolicy().hasHeightForWidth())
        self.outputVolSlider.setSizePolicy(sizePolicy3)
        self.outputVolSlider.setMinimumSize(QSize(50, 0))
        self.outputVolSlider.setOrientation(Qt.Orientation.Horizontal)

        self.horizontalLayout_4.addWidget(self.outputVolSlider)

        self.doubleSpinBox_3 = QDoubleSpinBox(self.settingsTab)
        self.doubleSpinBox_3.setObjectName(u"doubleSpinBox_3")
        self.doubleSpinBox_3.setMaximum(100.000000000000000)

        self.horizontalLayout_4.addWidget(self.doubleSpinBox_3)


        self.verticalLayout_10.addLayout(self.horizontalLayout_4)

        self.verticalSpacer_12 = QSpacerItem(20, 30, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.MinimumExpanding)

        self.verticalLayout_10.addItem(self.verticalSpacer_12)


        self.gridLayout_3.addLayout(self.verticalLayout_10, 3, 1, 1, 1)

        self.verticalLayout_8 = QVBoxLayout()
        self.verticalLayout_8.setSpacing(8)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.verticalLayout_8.setSizeConstraint(QLayout.SizeConstraint.SetDefaultConstraint)
        self.verticalSpacer_5 = QSpacerItem(20, 30, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.MinimumExpanding)

        self.verticalLayout_8.addItem(self.verticalSpacer_5)

        self.label_5 = QLabel(self.settingsTab)
        self.label_5.setObjectName(u"label_5")
        sizePolicy2.setHeightForWidth(self.label_5.sizePolicy().hasHeightForWidth())
        self.label_5.setSizePolicy(sizePolicy2)
        self.label_5.setFont(font2)

        self.verticalLayout_8.addWidget(self.label_5)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalSlider_3 = QSlider(self.settingsTab)
        self.horizontalSlider_3.setObjectName(u"horizontalSlider_3")
        sizePolicy3.setHeightForWidth(self.horizontalSlider_3.sizePolicy().hasHeightForWidth())
        self.horizontalSlider_3.setSizePolicy(sizePolicy3)
        self.horizontalSlider_3.setMinimumSize(QSize(50, 0))
        self.horizontalSlider_3.setOrientation(Qt.Orientation.Horizontal)

        self.horizontalLayout.addWidget(self.horizontalSlider_3)

        self.doubleSpinBox = QDoubleSpinBox(self.settingsTab)
        self.doubleSpinBox.setObjectName(u"doubleSpinBox")
        self.doubleSpinBox.setMinimum(0.500000000000000)
        self.doubleSpinBox.setMaximum(10.000000000000000)

        self.horizontalLayout.addWidget(self.doubleSpinBox)


        self.verticalLayout_8.addLayout(self.horizontalLayout)

        self.verticalSpacer_6 = QSpacerItem(20, 30, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.MinimumExpanding)

        self.verticalLayout_8.addItem(self.verticalSpacer_6)


        self.gridLayout_3.addLayout(self.verticalLayout_8, 5, 0, 1, 1)

        self.tabWidget.addTab(self.settingsTab, "")

        self.horizontalLayout_5.addWidget(self.tabWidget)


        self.retranslateUi(Widget)

        self.tabWidget.setCurrentIndex(2)


        QMetaObject.connectSlotsByName(Widget)
    # setupUi

    def retranslateUi(self, Widget):
        Widget.setWindowTitle(QCoreApplication.translate("Widget", u"Speech Recognition TEST GUI", None))
        self.label_2.setText(QCoreApplication.translate("Widget", u"Detected Speech History", None))
        self.clearHistoryBtn.setText(QCoreApplication.translate("Widget", u"Clear History", None))
        self.startRecordingBtn.setText(QCoreApplication.translate("Widget", u"Start Recording", None))
        self.stopRecordingBtn.setText(QCoreApplication.translate("Widget", u"Stop Recording", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.homeTab), QCoreApplication.translate("Widget", u"Home", None))
        self.sortOptionsHistoryBtn.setText(QCoreApplication.translate("Widget", u"Sort Options", None))
        self.label_10.setText(QCoreApplication.translate("Widget", u"Executed Command History", None))
        self.label_12.setText(QCoreApplication.translate("Widget", u"This will be removed!!!!!!!", None))
        self.timeEdit.setPlaceholderText(QCoreApplication.translate("Widget", u"Time", None))
        self.dateEdit.setPlaceholderText(QCoreApplication.translate("Widget", u"Date", None))
        self.commandEdit.setPlaceholderText(QCoreApplication.translate("Widget", u"Command", None))
        self.speechEdit.setPlaceholderText(QCoreApplication.translate("Widget", u"Speech", None))
        self.typeEdit.setInputMask("")
        self.typeEdit.setText("")
        self.typeEdit.setPlaceholderText(QCoreApplication.translate("Widget", u"Type", None))
        self.addItemHistoryBtn.setText(QCoreApplication.translate("Widget", u"Add Item", None))
        self.deleteRowHistoryBtn.setText(QCoreApplication.translate("Widget", u"Delete Row", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.commandHistoryTab), QCoreApplication.translate("Widget", u"Command History", None))
        self.sortOptionsCustomBtn.setText(QCoreApplication.translate("Widget", u"Sort Options", None))
        self.label_11.setText(QCoreApplication.translate("Widget", u"Custom Commands", None))
        self.pushButton.setText(QCoreApplication.translate("Widget", u"Create Command", None))
        self.editCustomRowBtn.setText(QCoreApplication.translate("Widget", u"Edit Command", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.customCommandsTab), QCoreApplication.translate("Widget", u"Custom Commands", None))
        self.label_3.setText(QCoreApplication.translate("Widget", u"Text To Speech", None))
        self.label_4.setText(QCoreApplication.translate("Widget", u"Reads executed commands aloud", None))
#if QT_CONFIG(whatsthis)
        self.label_6.setWhatsThis(QCoreApplication.translate("Widget", u"<html><head/><body><p><br/></p></body></html>", None))
#endif // QT_CONFIG(whatsthis)
        self.label_6.setText(QCoreApplication.translate("Widget", u"Setting Name", None))
        self.label_9.setText(QCoreApplication.translate("Widget", u"Input Device", None))
        self.inputDeviceBox.setItemText(0, QCoreApplication.translate("Widget", u"Test Input 1", None))
        self.inputDeviceBox.setItemText(1, QCoreApplication.translate("Widget", u"Test Input 2", None))

        self.label.setText(QCoreApplication.translate("Widget", u"Input Volume", None))
        self.openCalibrationBtn.setText(QCoreApplication.translate("Widget", u"Open Calibration", None))
        self.ttsCheckBox.setText("")
        self.label_8.setText(QCoreApplication.translate("Widget", u"Output Device", None))
        self.outputDeviceBox.setItemText(0, QCoreApplication.translate("Widget", u"Test Output 1", None))
        self.outputDeviceBox.setItemText(1, QCoreApplication.translate("Widget", u"Test Output 2", None))

        self.label_7.setText(QCoreApplication.translate("Widget", u"Output Volume", None))
#if QT_CONFIG(tooltip)
        self.label_5.setToolTip(QCoreApplication.translate("Widget", u"<html><head/><body><p>Minimum length of silence (in seconds) before a phrase ends and begins processing</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(whatsthis)
        self.label_5.setWhatsThis(QCoreApplication.translate("Widget", u"<html><head/><body><p><br/></p></body></html>", None))
#endif // QT_CONFIG(whatsthis)
        self.label_5.setText(QCoreApplication.translate("Widget", u"Pause Threshold", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.settingsTab), QCoreApplication.translate("Widget", u"Settings", None))
    # retranslateUi

