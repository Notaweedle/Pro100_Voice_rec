# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'create_command.ui'
##
## Created by: Qt User Interface Compiler version 6.9.2
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

class Ui_CreateCommandWidget(object):
    def setupUi(self, CreateCommandWidget):
        if not CreateCommandWidget.objectName():
            CreateCommandWidget.setObjectName(u"CreateCommandWidget")
        CreateCommandWidget.setWindowModality(Qt.WindowModality.ApplicationModal)
        CreateCommandWidget.resize(600, 300)
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(CreateCommandWidget.sizePolicy().hasHeightForWidth())
        CreateCommandWidget.setSizePolicy(sizePolicy)
        CreateCommandWidget.setMinimumSize(QSize(600, 300))
        CreateCommandWidget.setMaximumSize(QSize(600, 300))
        self.verticalLayout = QVBoxLayout(CreateCommandWidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.gridLayout = QGridLayout()
        self.gridLayout.setSpacing(16)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(6, 6, 6, 6)
        self.verticalLayout_6 = QVBoxLayout()
        self.verticalLayout_6.setSpacing(2)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalSpacer_7 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_6.addItem(self.verticalSpacer_7)

        self.label_4 = QLabel(CreateCommandWidget)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)

        self.verticalLayout_6.addWidget(self.label_4)

        self.nameEdit = QLineEdit(CreateCommandWidget)
        self.nameEdit.setObjectName(u"nameEdit")
        self.nameEdit.setMaxLength(32767)

        self.verticalLayout_6.addWidget(self.nameEdit)


        self.gridLayout.addLayout(self.verticalLayout_6, 0, 0, 1, 1)

        self.verticalLayout_5 = QVBoxLayout()
        self.verticalLayout_5.setSpacing(2)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalSpacer_5 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_5.addItem(self.verticalSpacer_5)

        self.label_3 = QLabel(CreateCommandWidget)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_5.addWidget(self.label_3)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalSpacer = QSpacerItem(40, 0, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer)

        self.enabledCheck = QCheckBox(CreateCommandWidget)
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

        self.verticalLayout_8 = QVBoxLayout()
        self.verticalLayout_8.setSpacing(2)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.label_6 = QLabel(CreateCommandWidget)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)

        self.verticalLayout_8.addWidget(self.label_6)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.targetEdit = QLineEdit(CreateCommandWidget)
        self.targetEdit.setObjectName(u"targetEdit")
        self.targetEdit.setEchoMode(QLineEdit.EchoMode.Normal)
        self.targetEdit.setReadOnly(False)
        self.targetEdit.setClearButtonEnabled(False)

        self.horizontalLayout_3.addWidget(self.targetEdit)


        self.verticalLayout_8.addLayout(self.horizontalLayout_3)

        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_5.addItem(self.horizontalSpacer_3)

        self.chooseTargetBtn = QPushButton(CreateCommandWidget)
        self.chooseTargetBtn.setObjectName(u"chooseTargetBtn")
        self.chooseTargetBtn.setMinimumSize(QSize(120, 0))
        self.chooseTargetBtn.setMaximumSize(QSize(80, 16777215))

        self.horizontalLayout_5.addWidget(self.chooseTargetBtn)

        self.horizontalSpacer_4 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_5.addItem(self.horizontalSpacer_4)


        self.verticalLayout_8.addLayout(self.horizontalLayout_5)

        self.verticalSpacer_12 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_8.addItem(self.verticalSpacer_12)


        self.gridLayout.addLayout(self.verticalLayout_8, 2, 2, 1, 1)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.cancelBtn = QPushButton(CreateCommandWidget)
        self.cancelBtn.setObjectName(u"cancelBtn")
        self.cancelBtn.setMinimumSize(QSize(0, 40))

        self.horizontalLayout.addWidget(self.cancelBtn)

        self.createBtn = QPushButton(CreateCommandWidget)
        self.createBtn.setObjectName(u"createBtn")
        self.createBtn.setEnabled(False)
        self.createBtn.setMinimumSize(QSize(0, 40))

        self.horizontalLayout.addWidget(self.createBtn)


        self.gridLayout.addLayout(self.horizontalLayout, 3, 0, 1, 3)

        self.verticalLayout_7 = QVBoxLayout()
        self.verticalLayout_7.setSpacing(2)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.verticalSpacer_9 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_7.addItem(self.verticalSpacer_9)

        self.label_5 = QLabel(CreateCommandWidget)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)

        self.verticalLayout_7.addWidget(self.label_5)

        self.speechEdit = QLineEdit(CreateCommandWidget)
        self.speechEdit.setObjectName(u"speechEdit")

        self.verticalLayout_7.addWidget(self.speechEdit)


        self.gridLayout.addLayout(self.verticalLayout_7, 0, 1, 1, 1)

        self.verticalLayout_4 = QVBoxLayout()
        self.verticalLayout_4.setSpacing(2)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.label = QLabel(CreateCommandWidget)
        self.label.setObjectName(u"label")
        self.label.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)

        self.verticalLayout_4.addWidget(self.label)

        self.typeCombo = QComboBox(CreateCommandWidget)
        self.typeCombo.addItem("")
        self.typeCombo.addItem("")
        self.typeCombo.addItem("")
        self.typeCombo.setObjectName(u"typeCombo")

        self.verticalLayout_4.addWidget(self.typeCombo)

        self.verticalSpacer_4 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_4.addItem(self.verticalSpacer_4)


        self.gridLayout.addLayout(self.verticalLayout_4, 2, 1, 1, 1)

        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setSpacing(2)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.label_2 = QLabel(CreateCommandWidget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)

        self.verticalLayout_2.addWidget(self.label_2)

        self.categoryEdit = QLineEdit(CreateCommandWidget)
        self.categoryEdit.setObjectName(u"categoryEdit")

        self.verticalLayout_2.addWidget(self.categoryEdit)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_2.addItem(self.verticalSpacer_2)


        self.gridLayout.addLayout(self.verticalLayout_2, 2, 0, 1, 1)


        self.verticalLayout.addLayout(self.gridLayout)


        self.retranslateUi(CreateCommandWidget)

        QMetaObject.connectSlotsByName(CreateCommandWidget)
    # setupUi

    def retranslateUi(self, CreateCommandWidget):
        CreateCommandWidget.setWindowTitle(QCoreApplication.translate("CreateCommandWidget", u"Create Command", None))
        self.label_4.setText(QCoreApplication.translate("CreateCommandWidget", u"Command Name", None))
        self.nameEdit.setInputMask("")
        self.nameEdit.setPlaceholderText(QCoreApplication.translate("CreateCommandWidget", u"Command Name", None))
        self.label_3.setText(QCoreApplication.translate("CreateCommandWidget", u"Enabled", None))
        self.enabledCheck.setText("")
        self.label_6.setText(QCoreApplication.translate("CreateCommandWidget", u"Target", None))
        self.targetEdit.setText("")
        self.targetEdit.setPlaceholderText(QCoreApplication.translate("CreateCommandWidget", u"Enter Website link or...", None))
        self.chooseTargetBtn.setText(QCoreApplication.translate("CreateCommandWidget", u"Choose File", None))
        self.cancelBtn.setText(QCoreApplication.translate("CreateCommandWidget", u"Cancel", None))
        self.createBtn.setText(QCoreApplication.translate("CreateCommandWidget", u"Create", None))
        self.label_5.setText(QCoreApplication.translate("CreateCommandWidget", u"Command Speech", None))
        self.speechEdit.setInputMask("")
        self.speechEdit.setPlaceholderText(QCoreApplication.translate("CreateCommandWidget", u"Command Speech", None))
        self.label.setText(QCoreApplication.translate("CreateCommandWidget", u"Type", None))
        self.typeCombo.setItemText(0, QCoreApplication.translate("CreateCommandWidget", u"Program", None))
        self.typeCombo.setItemText(1, QCoreApplication.translate("CreateCommandWidget", u"Browser", None))
        self.typeCombo.setItemText(2, QCoreApplication.translate("CreateCommandWidget", u"Script", None))

        self.typeCombo.setPlaceholderText(QCoreApplication.translate("CreateCommandWidget", u"Command Type", None))
        self.label_2.setText(QCoreApplication.translate("CreateCommandWidget", u"Category", None))
        self.categoryEdit.setPlaceholderText(QCoreApplication.translate("CreateCommandWidget", u"Command Category", None))
    # retranslateUi

