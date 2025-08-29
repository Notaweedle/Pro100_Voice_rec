# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'confirm_dialog.ui'
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
from PySide6.QtWidgets import (QApplication, QDialog, QHBoxLayout, QLabel,
    QPushButton, QSizePolicy, QSpacerItem, QVBoxLayout,
    QWidget)

class Ui_ConfirmDialog(object):
    def setupUi(self, ConfirmDialog):
        if not ConfirmDialog.objectName():
            ConfirmDialog.setObjectName(u"ConfirmDialog")
        ConfirmDialog.resize(300, 125)
        self.verticalLayout = QVBoxLayout(ConfirmDialog)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalSpacer = QSpacerItem(0, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.dialogText = QLabel(ConfirmDialog)
        self.dialogText.setObjectName(u"dialogText")
        self.dialogText.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout_3.addWidget(self.dialogText)


        self.verticalLayout.addLayout(self.horizontalLayout_3)

        self.verticalSpacer_2 = QSpacerItem(0, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer_2)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(6, 6, 6, 6)
        self.cancelBtn = QPushButton(ConfirmDialog)
        self.cancelBtn.setObjectName(u"cancelBtn")

        self.horizontalLayout.addWidget(self.cancelBtn)

        self.confirmBtn = QPushButton(ConfirmDialog)
        self.confirmBtn.setObjectName(u"confirmBtn")

        self.horizontalLayout.addWidget(self.confirmBtn)


        self.verticalLayout.addLayout(self.horizontalLayout)


        self.retranslateUi(ConfirmDialog)

        QMetaObject.connectSlotsByName(ConfirmDialog)
    # setupUi

    def retranslateUi(self, ConfirmDialog):
        ConfirmDialog.setWindowTitle(QCoreApplication.translate("ConfirmDialog", u"Warning", None))
        self.dialogText.setText(QCoreApplication.translate("ConfirmDialog", u"dialogText", None))
        self.cancelBtn.setText(QCoreApplication.translate("ConfirmDialog", u"Cancel", None))
        self.confirmBtn.setText(QCoreApplication.translate("ConfirmDialog", u"Confirm", None))
    # retranslateUi

