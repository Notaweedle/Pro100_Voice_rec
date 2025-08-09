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
from PySide6.QtWidgets import (QApplication, QGridLayout, QHBoxLayout, QLabel,
    QLineEdit, QListWidget, QListWidgetItem, QPushButton,
    QSizePolicy, QSpacerItem, QVBoxLayout, QWidget)

class Ui_Widget(object):
    def setupUi(self, Widget):
        if not Widget.objectName():
            Widget.setObjectName(u"Widget")
        Widget.resize(700, 500)
        icon = QIcon()
        icon.addFile(u"../../../../../Downloads/1345442634985898067.webp", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        Widget.setWindowIcon(icon)
        Widget.setWindowOpacity(1.000000000000000)
        self.gridLayout_2 = QGridLayout(Widget)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout_2.setContentsMargins(10, 10, 10, 10)
        self.recordingButtonLayout = QHBoxLayout()
        self.recordingButtonLayout.setSpacing(10)
        self.recordingButtonLayout.setObjectName(u"recordingButtonLayout")
        self.startRecordingBtn = QPushButton(Widget)
        self.startRecordingBtn.setObjectName(u"startRecordingBtn")
        self.startRecordingBtn.setMinimumSize(QSize(0, 40))

        self.recordingButtonLayout.addWidget(self.startRecordingBtn)

        self.stopRecordingBtn = QPushButton(Widget)
        self.stopRecordingBtn.setObjectName(u"stopRecordingBtn")
        self.stopRecordingBtn.setEnabled(False)
        self.stopRecordingBtn.setMinimumSize(QSize(0, 40))

        self.recordingButtonLayout.addWidget(self.stopRecordingBtn)


        self.gridLayout_2.addLayout(self.recordingButtonLayout, 3, 0, 1, 1)

        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.label_2 = QLabel(Widget)
        self.label_2.setObjectName(u"label_2")

        self.gridLayout.addWidget(self.label_2, 0, 1, 1, 1, Qt.AlignmentFlag.AlignHCenter)

        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setSpacing(10)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(-1, 0, -1, -1)
        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer)

        self.label = QLabel(Widget)
        self.label.setObjectName(u"label")

        self.verticalLayout.addWidget(self.label, 0, Qt.AlignmentFlag.AlignHCenter)

        self.itemEdit = QLineEdit(Widget)
        self.itemEdit.setObjectName(u"itemEdit")
        self.itemEdit.setMinimumSize(QSize(150, 0))

        self.verticalLayout.addWidget(self.itemEdit, 0, Qt.AlignmentFlag.AlignHCenter|Qt.AlignmentFlag.AlignVCenter)

        self.addItemButton = QPushButton(Widget)
        self.addItemButton.setObjectName(u"addItemButton")
        self.addItemButton.setMinimumSize(QSize(100, 0))

        self.verticalLayout.addWidget(self.addItemButton, 0, Qt.AlignmentFlag.AlignHCenter|Qt.AlignmentFlag.AlignVCenter)

        self.removeItemButton = QPushButton(Widget)
        self.removeItemButton.setObjectName(u"removeItemButton")
        self.removeItemButton.setMinimumSize(QSize(100, 0))

        self.verticalLayout.addWidget(self.removeItemButton, 0, Qt.AlignmentFlag.AlignHCenter|Qt.AlignmentFlag.AlignVCenter)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer_2)


        self.gridLayout.addLayout(self.verticalLayout, 1, 0, 1, 1)

        self.listWidget = QListWidget(Widget)
        self.listWidget.setObjectName(u"listWidget")
        self.listWidget.setMinimumSize(QSize(250, 0))

        self.gridLayout.addWidget(self.listWidget, 1, 1, 1, 1)


        self.gridLayout_2.addLayout(self.gridLayout, 2, 0, 1, 1)

        self.openCalibrationBtn = QPushButton(Widget)
        self.openCalibrationBtn.setObjectName(u"openCalibrationBtn")

        self.gridLayout_2.addWidget(self.openCalibrationBtn, 4, 0, 1, 1)


        self.retranslateUi(Widget)

        QMetaObject.connectSlotsByName(Widget)
    # setupUi

    def retranslateUi(self, Widget):
        Widget.setWindowTitle(QCoreApplication.translate("Widget", u"Speech Recognition TEST GUI", None))
        self.startRecordingBtn.setText(QCoreApplication.translate("Widget", u"Start Recording", None))
        self.stopRecordingBtn.setText(QCoreApplication.translate("Widget", u"Stop Recording", None))
        self.label_2.setText(QCoreApplication.translate("Widget", u"Detected Speech History", None))
        self.label.setText(QCoreApplication.translate("Widget", u"Input Testing", None))
        self.addItemButton.setText(QCoreApplication.translate("Widget", u"Add Item", None))
        self.removeItemButton.setText(QCoreApplication.translate("Widget", u"Remove", None))
        self.openCalibrationBtn.setText(QCoreApplication.translate("Widget", u"Open Calibration", None))
    # retranslateUi

