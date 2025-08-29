# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'edit_command.ui'
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
from PySide6.QtWidgets import (QApplication, QCheckBox, QComboBox, QGridLayout,
    QHBoxLayout, QLabel, QLineEdit, QPushButton,
    QSizePolicy, QSpacerItem, QVBoxLayout, QWidget)

class Ui_EditCommandWidget(object):
    def setupUi(self, EditCommandWidget):
        if not EditCommandWidget.objectName():
            EditCommandWidget.setObjectName(u"EditCommandWidget")
        EditCommandWidget.setWindowModality(Qt.WindowModality.ApplicationModal)
        EditCommandWidget.resize(600, 300)
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(EditCommandWidget.sizePolicy().hasHeightForWidth())
        EditCommandWidget.setSizePolicy(sizePolicy)
        EditCommandWidget.setMinimumSize(QSize(600, 300))
        EditCommandWidget.setMaximumSize(QSize(600, 300))
        self.verticalLayout = QVBoxLayout(EditCommandWidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.gridLayout = QGridLayout()
        self.gridLayout.setSpacing(16)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(6, 6, 6, 6)
        self.verticalLayout_7 = QVBoxLayout()
        self.verticalLayout_7.setSpacing(2)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.verticalSpacer_9 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_7.addItem(self.verticalSpacer_9)

        self.label_5 = QLabel(EditCommandWidget)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_7.addWidget(self.label_5)

        self.speechEdit = QLineEdit(EditCommandWidget)
        self.speechEdit.setObjectName(u"speechEdit")

        self.verticalLayout_7.addWidget(self.speechEdit)


        self.gridLayout.addLayout(self.verticalLayout_7, 0, 1, 1, 1)

        self.verticalLayout_6 = QVBoxLayout()
        self.verticalLayout_6.setSpacing(2)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalSpacer_7 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_6.addItem(self.verticalSpacer_7)

        self.label_4 = QLabel(EditCommandWidget)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_6.addWidget(self.label_4)

        self.nameEdit = QLineEdit(EditCommandWidget)
        self.nameEdit.setObjectName(u"nameEdit")
        self.nameEdit.setMaxLength(32767)

        self.verticalLayout_6.addWidget(self.nameEdit)


        self.gridLayout.addLayout(self.verticalLayout_6, 0, 0, 1, 1)

        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setSpacing(2)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.label_2 = QLabel(EditCommandWidget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_2.addWidget(self.label_2)

        self.categoryEdit = QLineEdit(EditCommandWidget)
        self.categoryEdit.setObjectName(u"categoryEdit")

        self.verticalLayout_2.addWidget(self.categoryEdit)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_2.addItem(self.verticalSpacer_2)


        self.gridLayout.addLayout(self.verticalLayout_2, 2, 0, 1, 1)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.cancelBtn = QPushButton(EditCommandWidget)
        self.cancelBtn.setObjectName(u"cancelBtn")
        self.cancelBtn.setMinimumSize(QSize(0, 40))

        self.horizontalLayout.addWidget(self.cancelBtn)

        self.deleteBtn = QPushButton(EditCommandWidget)
        self.deleteBtn.setObjectName(u"deleteBtn")
        self.deleteBtn.setMinimumSize(QSize(0, 40))

        self.horizontalLayout.addWidget(self.deleteBtn)

        self.saveBtn = QPushButton(EditCommandWidget)
        self.saveBtn.setObjectName(u"saveBtn")
        self.saveBtn.setMinimumSize(QSize(0, 40))

        self.horizontalLayout.addWidget(self.saveBtn)


        self.gridLayout.addLayout(self.horizontalLayout, 3, 0, 1, 3)

        self.verticalLayout_4 = QVBoxLayout()
        self.verticalLayout_4.setSpacing(2)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.label = QLabel(EditCommandWidget)
        self.label.setObjectName(u"label")
        self.label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_4.addWidget(self.label)

        self.typeCombo = QComboBox(EditCommandWidget)
        self.typeCombo.addItem("")
        self.typeCombo.addItem("")
        self.typeCombo.addItem("")
        self.typeCombo.setObjectName(u"typeCombo")

        self.verticalLayout_4.addWidget(self.typeCombo)

        self.verticalSpacer_4 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_4.addItem(self.verticalSpacer_4)


        self.gridLayout.addLayout(self.verticalLayout_4, 2, 1, 1, 1)

        self.verticalLayout_5 = QVBoxLayout()
        self.verticalLayout_5.setSpacing(2)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalSpacer_5 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_5.addItem(self.verticalSpacer_5)

        self.label_3 = QLabel(EditCommandWidget)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_5.addWidget(self.label_3)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalSpacer = QSpacerItem(40, 0, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer)

        self.enabledCheck = QCheckBox(EditCommandWidget)
        self.enabledCheck.setObjectName(u"enabledCheck")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Expanding)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.enabledCheck.sizePolicy().hasHeightForWidth())
        self.enabledCheck.setSizePolicy(sizePolicy1)
        self.enabledCheck.setMaximumSize(QSize(16777215, 20))
        self.enabledCheck.setLayoutDirection(Qt.LayoutDirection.LeftToRight)

        self.horizontalLayout_2.addWidget(self.enabledCheck)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_2)


        self.verticalLayout_5.addLayout(self.horizontalLayout_2)


        self.gridLayout.addLayout(self.verticalLayout_5, 0, 2, 1, 1)

        self.verticalLayout_10 = QVBoxLayout()
        self.verticalLayout_10.setSpacing(2)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.label_8 = QLabel(EditCommandWidget)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_10.addWidget(self.label_8)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.targetEdit = QLineEdit(EditCommandWidget)
        self.targetEdit.setObjectName(u"targetEdit")
        self.targetEdit.setEchoMode(QLineEdit.EchoMode.Normal)
        self.targetEdit.setReadOnly(False)
        self.targetEdit.setClearButtonEnabled(False)

        self.horizontalLayout_4.addWidget(self.targetEdit)


        self.verticalLayout_10.addLayout(self.horizontalLayout_4)

        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalSpacer_5 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_6.addItem(self.horizontalSpacer_5)

        self.chooseTargetBtn = QPushButton(EditCommandWidget)
        self.chooseTargetBtn.setObjectName(u"chooseTargetBtn")

        self.horizontalLayout_6.addWidget(self.chooseTargetBtn)

        self.horizontalSpacer_6 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_6.addItem(self.horizontalSpacer_6)


        self.verticalLayout_10.addLayout(self.horizontalLayout_6)

        self.verticalSpacer_14 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_10.addItem(self.verticalSpacer_14)


        self.gridLayout.addLayout(self.verticalLayout_10, 2, 2, 1, 1)


        self.verticalLayout.addLayout(self.gridLayout)


        self.retranslateUi(EditCommandWidget)

        QMetaObject.connectSlotsByName(EditCommandWidget)
    # setupUi

    def retranslateUi(self, EditCommandWidget):
        EditCommandWidget.setWindowTitle(QCoreApplication.translate("EditCommandWidget", u"Edit Command", None))
        self.label_5.setText(QCoreApplication.translate("EditCommandWidget", u"Command Speech", None))
        self.speechEdit.setInputMask("")
        self.speechEdit.setPlaceholderText(QCoreApplication.translate("EditCommandWidget", u"Command Speech", None))
        self.label_4.setText(QCoreApplication.translate("EditCommandWidget", u"Command Name", None))
        self.nameEdit.setInputMask("")
        self.nameEdit.setPlaceholderText(QCoreApplication.translate("EditCommandWidget", u"Command Name", None))
        self.label_2.setText(QCoreApplication.translate("EditCommandWidget", u"Category", None))
        self.categoryEdit.setPlaceholderText(QCoreApplication.translate("EditCommandWidget", u"Command Category", None))
        self.cancelBtn.setText(QCoreApplication.translate("EditCommandWidget", u"Cancel", None))
        self.deleteBtn.setText(QCoreApplication.translate("EditCommandWidget", u"Delete", None))
        self.saveBtn.setText(QCoreApplication.translate("EditCommandWidget", u"Save", None))
        self.label.setText(QCoreApplication.translate("EditCommandWidget", u"Type", None))
        self.typeCombo.setItemText(0, QCoreApplication.translate("EditCommandWidget", u"Program", None))
        self.typeCombo.setItemText(1, QCoreApplication.translate("EditCommandWidget", u"Browser", None))
        self.typeCombo.setItemText(2, QCoreApplication.translate("EditCommandWidget", u"Script", None))

        self.typeCombo.setPlaceholderText(QCoreApplication.translate("EditCommandWidget", u"Command Type", None))
        self.label_3.setText(QCoreApplication.translate("EditCommandWidget", u"Enabled", None))
        self.enabledCheck.setText("")
        self.label_8.setText(QCoreApplication.translate("EditCommandWidget", u"Target", None))
        self.targetEdit.setText("")
        self.targetEdit.setPlaceholderText(QCoreApplication.translate("EditCommandWidget", u"Website/Program", None))
        self.chooseTargetBtn.setText(QCoreApplication.translate("EditCommandWidget", u"Choose File", None))
    # retranslateUi

