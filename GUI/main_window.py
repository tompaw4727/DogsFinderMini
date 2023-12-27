from PySide6.QtCore import Qt
from PySide6.QtWidgets import QMainWindow
from PySide6.QtGui import QPixmap, QImage
import torch
from torchvision import models
from PIL import Image
from ui_main_window import Ui_main_window
from history_window import Ui_history_widget
from functions import (perform_pred, info_web_scrapping, history_web_scrapping)

class Main_window(QMainWindow, Ui_main_window):
    def __init__(self,app):
        super().__init__()
        self.setupUi(self)
        self.app = app
        self.setAcceptDrops(True)
        self.setWindowTitle('DogsFinderMini')

        self.history_window = None

        self.image_path = ""
        self.breed = ""
        self.info = ""
        self.history = ""

        self.submit_button.clicked.connect(self.submit_button_logic)
        self.history_button.clicked.connect(self.history_button_logic)
        self.info_button.clicked.connect(self.info_button_logic)

    def dragEnterEvent(self, e):
        if e.mimeData().hasUrls():
            e.acceptProposedAction()
        else:
            e.ignoreProposedAction()

    def dropEvent(self, e):
        image_path = e.mimeData().urls()[0]
        if image_path.isLocalFile():
            image = QImage(image_path.toLocalFile())
            self.image_path = image_path.toLocalFile()
            if not image.isNull():
                self.displayImage(image)

    def displayImage(self, image):
        scaled_image = image.scaled(self.image_label.size(), Qt.KeepAspectRatio, Qt.SmoothTransformation)
        self.image_label.setPixmap(QPixmap.fromImage(scaled_image))

    def submit_button_logic(self):
        saved_model_path = r"../model/saved_model/final_model"
        weights = models.ResNet34_Weights.DEFAULT
        loaded_model = models.resnet34(weights = weights)
        loaded_model.fc = torch.nn.Linear(in_features=512,
                                          out_features=120,
                                          bias=True)
        loaded_model.load_state_dict(torch.load(f=saved_model_path))

        custom_image = Image.open(self.image_path)
        auto_transforms = weights.transforms()
        custom_image_transformed = auto_transforms(custom_image)

        self.breed = perform_pred(loaded_model, custom_image_transformed)

        self.text_breed.setPlainText(self.breed.replace('-', ' ').upper())
        self.text_breed.setAlignment(Qt.AlignCenter)

    def history_button_logic(self):
        self.history = history_web_scrapping(self.breed)
        self.history_window = QMainWindow()
        self.ui = Ui_history_widget()
        self.ui.setupUi(self.history_window)
        self.history_window.show()
        self.history_window.setWindowTitle('History')

        if self.history == "":
            self.ui.textBrowser.setPlainText(f"Sorry, but this app doesn't provide information about that breed. If you're curious, you can try finding this information on Wikipedia. ")
        else:
            self.ui.textBrowser.setPlainText(self.history)

    def info_button_logic(self):
        self.info = info_web_scrapping(self.breed)

        if self.info == "":
            self.text_description.setPlainText(f"Sorry, but this app doesn't provide information about that breed. If you're curious, you can try finding this information on Wikiepedia.")
        else:
            self.text_description.setPlainText(self.info)