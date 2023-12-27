from PySide6.QtCore import (QCoreApplication, QMetaObject, QRect, Qt)
from PySide6.QtGui import QFont
from PySide6.QtWidgets import (QGroupBox, QLabel, QPushButton, QTextBrowser, QWidget)
import resources_rc

class Ui_main_window(object):
    def setupUi(self, main_window):
        if not main_window.objectName():
            main_window.setObjectName(u"main_window")
        main_window.resize(800, 605)
        main_window.setFixedSize(800, 605)
        main_window.setStyleSheet(u"")
        self.widget = QWidget(main_window)
        self.widget.setObjectName(u"widget")
        self.widget.setStyleSheet(u"QWidget {\n"
                                  "background: #E1ECC8\n"
                                  "}")
        self.group_box = QGroupBox(self.widget)
        self.group_box.setObjectName(u"group_box")
        self.group_box.setGeometry(QRect(520, 110, 261, 461))
        self.group_box.setStyleSheet(u"QGroupBox {background: #C4D7B2;\n"
                                     "border: 1px solid #000000;\n"
                                     "border-radius: 20px;\n"
                                     "border-style: outset;\n"
                                     "}")
        self.history_button = QPushButton(self.group_box)
        self.history_button.setObjectName(u"history_button")
        self.history_button.setGeometry(QRect(50, 410, 171, 41))
        font = QFont()
        font.setFamilies([u"Garamond"])
        font.setPointSize(12)
        font.setBold(True)
        self.history_button.setFont(font)
        self.history_button.setStyleSheet(u"QPushButton {\n"
                                          "    color: #000000;\n"
                                          "    border: 1px solid #000000;\n"
                                          "    border-radius: 20px;\n"
                                          "    border-style: outset;\n"
                                          "    background: #A0C49D;\n"
                                          "    padding: 5px;\n"
                                          "    }\n"
                                          "QPushButton:hover {\n"
                                          "background-color: #80A27B\n"
                                          "}\n")
        self.text_description = QTextBrowser(self.group_box)
        self.text_description.setObjectName(u"text_description")
        self.text_description.setGeometry(QRect(20, 150, 221, 251))
        font1 = QFont()
        font1.setFamilies([u"Times New Roman"])
        self.text_description.setFont(font1)
        self.text_description.setStyleSheet(u"QTextBrowser {\n"
                                            "background: #F7FFE5;\n"
                                            "border: 1px solid #000000\n"
                                            "}")
        self.text_breed = QTextBrowser(self.group_box)
        self.text_breed.setObjectName(u"text_breed")
        self.text_breed.setGeometry(QRect(20, 70, 221, 31))
        font2 = QFont()
        font2.setFamilies([u"Times New Roman"])
        font2.setPointSize(12)
        self.text_breed.setFont(font2)
        self.text_breed.setStyleSheet(u"QTextBrowser {\n"
                                     "background: #F7FFE5;\n"
                                     "border: 1px solid #000000;\n"
                                     "border-radius: 10px;\n"
                                     "border-style: outset;\n"
                                     "}")
        self.label_2 = QLabel(self.group_box)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(20, 20, 221, 31))
        font3 = QFont()
        font3.setFamilies([u"Garamond"])
        font3.setPointSize(12)
        self.label_2.setFont(font3)
        self.label_2.setStyleSheet(u"QLabel {\n"
                                   "background: #F7FFE5;\n"
                                   "border: 1px solid #000000\n"
                                   "}")
        self.info_button = QPushButton(self.group_box)
        self.info_button.setObjectName(u"info_button")
        self.info_button.setGeometry(QRect(80, 110, 101, 31))
        font4 = QFont()
        font4.setFamilies([u"Garamond"])
        font4.setPointSize(12)
        font4.setBold(True)
        self.info_button.setFont(font4)
        self.info_button.setStyleSheet(u"QPushButton {\n"
                                       "    color: #000000;\n"
                                       "    border: 1px solid #000000;\n"
                                       "    border-radius: 10px;\n"
                                       "    border-style: outset;\n"
                                       "    background: #A0C49D;\n"
                                       "    padding: 5px;\n"
                                       "    }\n"
                                       "QPushButton:hover {\n"
                                       "background-color: #80A27B\n"
                                       "}\n")

        self.submit_button = QPushButton(self.widget)
        self.submit_button.setObjectName(u"submit_button")
        self.submit_button.setGeometry(QRect(540, 40, 221, 61))
        font5 = QFont()
        font5.setFamilies([u"Garamond"])
        font5.setPointSize(16)
        font5.setBold(True)
        font5.setItalic(False)
        self.submit_button.setFont(font5)
        self.submit_button.setStyleSheet(u"QPushButton {\n"
                                         "    color: #000000;\n"
                                         "    border: 1px solid #000000;\n"
                                         "    border-radius: 20px;\n"
                                         "    border-style: outset;\n"
                                         "    background: #A0C49D;\n"
                                         "    padding: 5px;\n"
                                         "    }\n"
                                         "QPushButton:hover {\n"
                                         "background-color: #80A27B\n"
                                         "}")
        self.image_widget = QWidget(self.widget)
        self.image_widget.setObjectName(u"image_widget")
        self.image_widget.setGeometry(QRect(20, 110, 451, 461))
        self.image_widget.setStyleSheet(u"QWidget {\n"
                                        "background: #F7FFE5;\n"
                                        "border: 1px solid #000000;\n"
                                        "border-radius: 20px;\n"
                                        "border-style: outset;\n"
                                        "}")
        self.image_label = QLabel(self.image_widget)
        self.image_label.setGeometry(self.image_widget.rect())
        self.image_label.setAlignment(Qt.AlignCenter)

        self.label_image = QLabel(self.widget)
        self.label_image.setObjectName(u"label_image")
        self.label_image.setGeometry(QRect(0, 20, 131, 81))
        self.label_image.setStyleSheet(u"image: url(:/icons8-poodle-96.png);")
        self.label_1 = QLabel(self.widget)
        self.label_1.setObjectName(u"label_1")
        self.label_1.setGeometry(QRect(120, 30, 391, 71))
        font6 = QFont()
        font6.setFamilies([u"Garamond"])
        font6.setPointSize(38)
        self.label_1.setFont(font6)
        main_window.setCentralWidget(self.widget)

        self.retranslateUi(main_window)

        QMetaObject.connectSlotsByName(main_window)
    # setupUi

    def retranslateUi(self, main_window):
        main_window.setWindowTitle(QCoreApplication.translate("main_window", u"MainWindow", None))
        self.group_box.setTitle("")
        self.history_button.setText(QCoreApplication.translate("main_window", u" History", None))
        self.text_description.setHtml(QCoreApplication.translate("main_window", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:'Times New Roman'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>", None))
        self.text_breed.setHtml(QCoreApplication.translate("main_window", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:'Times New Roman'; font-size:12pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>", None))
        self.label_2.setText(QCoreApplication.translate("main_window", u"It's propably...", None))
        self.info_button.setText(QCoreApplication.translate("main_window", u"Show info", None))
#if QT_CONFIG(tooltip)
        self.submit_button.setToolTip(QCoreApplication.translate("main_window", u"<html><head/><body><pre style=\" margin-top:12px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'inherit'; background-color:transparent;\">QPushButton {</span></pre><pre style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'inherit'; background-color:transparent;\"/><span style=\" font-family:'inherit'; font-size:13px; color:#000000; background-color:transparent;\">color</span><span style=\" font-family:'inherit'; background-color:transparent;\">: </span><span style=\" font-family:'inherit'; font-size:13px; color:#000000; background-color:transparent;\">#333</span><span style=\" font-family:'inherit'; background-color:transparent;\">;</span></pre><pre style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'inherit'; background-color:transparent;\"/><span styl"
                        "e=\" font-family:'inherit'; font-size:13px; color:#000000; background-color:transparent;\">border</span><span style=\" font-family:'inherit'; background-color:transparent;\">: </span><span style=\" font-family:'inherit'; font-size:13px; color:#000000; background-color:transparent;\">2px</span><span style=\" font-family:'inherit'; background-color:transparent;\"> solid </span><span style=\" font-family:'inherit'; font-size:13px; color:#000000; background-color:transparent;\">#555</span><span style=\" font-family:'inherit'; background-color:transparent;\">;</span></pre><pre style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'inherit'; background-color:transparent;\"/><span style=\" font-family:'inherit'; font-size:13px; color:#000000; background-color:transparent;\">border-radius</span><span style=\" font-family:'inherit'; background-color:transparent;\">: </span><span style=\" font-family:'inherit'; font-size:13px; col"
                        "or:#000000; background-color:transparent;\">20px</span><span style=\" font-family:'inherit'; background-color:transparent;\">;</span></pre><pre style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'inherit'; background-color:transparent;\"/><span style=\" font-family:'inherit'; font-size:13px; color:#000000; background-color:transparent;\">border-style</span><span style=\" font-family:'inherit'; background-color:transparent;\">: outset;</span></pre><pre style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'inherit'; background-color:transparent;\"/><span style=\" font-family:'inherit'; font-size:13px; color:#000000; background-color:transparent;\">background</span><span style=\" font-family:'inherit'; background-color:transparent;\">: </span><span style=\" font-family:'inherit'; font-size:13px; color:#000000; background-color:tra"
                        "nsparent;\">qradialgradient</span><span style=\" font-family:'inherit'; background-color:transparent;\">(</span></pre><pre style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'inherit'; background-color:transparent;\">        cx: </span><span style=\" font-family:'inherit'; font-size:13px; color:#000000; background-color:transparent;\">0.3</span><span style=\" font-family:'inherit'; background-color:transparent;\">, cy: -</span><span style=\" font-family:'inherit'; font-size:13px; color:#000000; background-color:transparent;\">0.4</span><span style=\" font-family:'inherit'; background-color:transparent;\">, fx: </span><span style=\" font-family:'inherit'; font-size:13px; color:#000000; background-color:transparent;\">0.3</span><span style=\" font-family:'inherit'; background-color:transparent;\">, fy: -</span><span style=\" font-family:'inherit'; font-size:13px; color:#000000; background-color:transparent;\">0.4</span>"
                        "<span style=\" font-family:'inherit'; background-color:transparent;\">,</span></pre><pre style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'inherit'; background-color:transparent;\">        radius: </span><span style=\" font-family:'inherit'; font-size:13px; color:#000000; background-color:transparent;\">1.35</span><span style=\" font-family:'inherit'; background-color:transparent;\">, stop: </span><span style=\" font-family:'inherit'; font-size:13px; color:#000000; background-color:transparent;\">0</span><span style=\" font-family:'inherit'; background-color:transparent;\"/><span style=\" font-family:'inherit'; font-size:13px; color:#000000; background-color:transparent;\">#fff</span><span style=\" font-family:'inherit'; background-color:transparent;\">, stop: </span><span style=\" font-family:'inherit'; font-size:13px; color:#000000; background-color:transparent;\">1</span><span style=\" font-family:'inherit'; back"
                        "ground-color:transparent;\"/><span style=\" font-family:'inherit'; font-size:13px; color:#000000; background-color:transparent;\">#888</span></pre><pre style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'inherit'; background-color:transparent;\">        );</span></pre><pre style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'inherit'; background-color:transparent;\"/><span style=\" font-family:'inherit'; font-size:13px; color:#000000; background-color:transparent;\">padding</span><span style=\" font-family:'inherit'; background-color:transparent;\">: </span><span style=\" font-family:'inherit'; font-size:13px; color:#000000; background-color:transparent;\">5px</span><span style=\" font-family:'inherit'; background-color:transparent;\">;</span></pre><pre style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:"
                        "0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'inherit'; background-color:transparent;\">    }</span></pre><pre style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:'inherit';\"><br/></pre><pre style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'inherit'; background-color:transparent;\">QPushButton</span><span style=\" font-family:'inherit'; font-size:13px; color:#000000; background-color:transparent;\">:hover</span><span style=\" font-family:'inherit'; background-color:transparent;\"> {</span></pre><pre style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'inherit'; background-color:transparent;\"/><span style=\" font-family:'inherit'; font-size:13px; color:#000000; background-color:transparent;\">backgr"
                        "ound</span><span style=\" font-family:'inherit'; background-color:transparent;\">: </span><span style=\" font-family:'inherit'; font-size:13px; color:#000000; background-color:transparent;\">qradialgradient</span><span style=\" font-family:'inherit'; background-color:transparent;\">(</span></pre><pre style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'inherit'; background-color:transparent;\">        cx: </span><span style=\" font-family:'inherit'; font-size:13px; color:#000000; background-color:transparent;\">0.3</span><span style=\" font-family:'inherit'; background-color:transparent;\">, cy: -</span><span style=\" font-family:'inherit'; font-size:13px; color:#000000; background-color:transparent;\">0.4</span><span style=\" font-family:'inherit'; background-color:transparent;\">, fx: </span><span style=\" font-family:'inherit'; font-size:13px; color:#000000; background-color:transparent;\">0.3</span><span style=\" f"
                        "ont-family:'inherit'; background-color:transparent;\">, fy: -</span><span style=\" font-family:'inherit'; font-size:13px; color:#000000; background-color:transparent;\">0.4</span><span style=\" font-family:'inherit'; background-color:transparent;\">,</span></pre><pre style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'inherit'; background-color:transparent;\">        radius: </span><span style=\" font-family:'inherit'; font-size:13px; color:#000000; background-color:transparent;\">1.35</span><span style=\" font-family:'inherit'; background-color:transparent;\">, stop: </span><span style=\" font-family:'inherit'; font-size:13px; color:#000000; background-color:transparent;\">0</span><span style=\" font-family:'inherit'; background-color:transparent;\"/><span style=\" font-family:'inherit'; font-size:13px; color:#000000; background-color:transparent;\">#fff</span><span style=\" font-family:'inherit'; background-color:tr"
                        "ansparent;\">, stop: </span><span style=\" font-family:'inherit'; font-size:13px; color:#000000; background-color:transparent;\">1</span><span style=\" font-family:'inherit'; background-color:transparent;\"/><span style=\" font-family:'inherit'; font-size:13px; color:#000000; background-color:transparent;\">#bbb</span></pre><pre style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'inherit'; background-color:transparent;\">        );</span></pre><pre style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'inherit'; background-color:transparent;\">    }</span></pre><pre style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:'inherit';\"><br/></pre><pre style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-bl"
                        "ock-indent:0; text-indent:0px;\"><span style=\" font-family:'inherit'; background-color:transparent;\">QPushButton:pressed {</span></pre><pre style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'inherit'; background-color:transparent;\"/><span style=\" font-family:'inherit'; font-size:13px; color:#000000; background-color:transparent;\">border-style</span><span style=\" font-family:'inherit'; background-color:transparent;\">: inset;</span></pre><pre style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'inherit'; background-color:transparent;\"/><span style=\" font-family:'inherit'; font-size:13px; color:#000000; background-color:transparent;\">background</span><span style=\" font-family:'inherit'; background-color:transparent;\">: </span><span style=\" font-family:'inherit'; font-size:13px; color:#000000; background-color:transp"
                        "arent;\">qradialgradient</span><span style=\" font-family:'inherit'; background-color:transparent;\">(</span></pre><pre style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'inherit'; background-color:transparent;\">        cx: </span><span style=\" font-family:'inherit'; font-size:13px; color:#000000; background-color:transparent;\">0.4</span><span style=\" font-family:'inherit'; background-color:transparent;\">, cy: -</span><span style=\" font-family:'inherit'; font-size:13px; color:#000000; background-color:transparent;\">0.1</span><span style=\" font-family:'inherit'; background-color:transparent;\">, fx: </span><span style=\" font-family:'inherit'; font-size:13px; color:#000000; background-color:transparent;\">0.4</span><span style=\" font-family:'inherit'; background-color:transparent;\">, fy: -</span><span style=\" font-family:'inherit'; font-size:13px; color:#000000; background-color:transparent;\">0.1</span><sp"
                        "an style=\" font-family:'inherit'; background-color:transparent;\">,</span></pre><pre style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'inherit'; background-color:transparent;\">        radius: </span><span style=\" font-family:'inherit'; font-size:13px; color:#000000; background-color:transparent;\">1.35</span><span style=\" font-family:'inherit'; background-color:transparent;\">, stop: </span><span style=\" font-family:'inherit'; font-size:13px; color:#000000; background-color:transparent;\">0</span><span style=\" font-family:'inherit'; background-color:transparent;\"/><span style=\" font-family:'inherit'; font-size:13px; color:#000000; background-color:transparent;\">#fff</span><span style=\" font-family:'inherit'; background-color:transparent;\">, stop: </span><span style=\" font-family:'inherit'; font-size:13px; color:#000000; background-color:transparent;\">1</span><span style=\" font-family:'inherit'; backgro"
                        "und-color:transparent;\"/><span style=\" font-family:'inherit'; font-size:13px; color:#000000; background-color:transparent;\">#ddd</span></pre><pre style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'inherit'; background-color:transparent;\">        );</span></pre><pre style=\" margin-top:0px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'inherit'; background-color:transparent;\">    }</span></pre></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.submit_button.setText(QCoreApplication.translate("main_window", u"Let's Check", None))
        self.label_image.setText("")
        self.label_1.setText(QCoreApplication.translate("main_window", u"DogsFinderMini", None))
    # retranslateUi

