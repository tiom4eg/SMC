# Первая заповедь кода - не трогай, пока работает
from PyQt5 import QtCore, QtGui, QtWidgets
import sys
import requests


def cutRectangle(toponym):
    size = toponym["boundedBy"]["Envelope"]["lowerCorner"].split()
    size1 = toponym["boundedBy"]["Envelope"]["upperCorner"].split()
    return str(abs(float(size[0]) - float(size1[0])) / 2), str(abs(float(size[1]) - float(size1[1])) / 2)


class UI(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(950, 505)
        self.pixmapHolder = QtWidgets.QLabel(Form)
        self.pixmapHolder.setGeometry(QtCore.QRect(15, 27, 600, 450))
        self.pixmapHolder.setText("")
        self.pixmapHolder.setObjectName("pixmapHolder")
        self.settingsLabel = QtWidgets.QLabel(Form)
        self.settingsLabel.setGeometry(QtCore.QRect(650, 10, 160, 15))
        self.settingsLabel.setText("")
        self.mapTypeLabel = QtWidgets.QLabel(Form)
        self.mapTypeLabel.setGeometry(QtCore.QRect(620, 45, 160, 15))
        self.mapTypeLabel.setText("")
        self.verticalLayoutWidget = QtWidgets.QWidget(Form)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(620, 60, 160, 90))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.schemeButton = QtWidgets.QRadioButton(self.verticalLayoutWidget)
        self.schemeButton.setObjectName("schemeButton")
        self.verticalLayout.addWidget(self.schemeButton)
        self.satteliteButton = QtWidgets.QRadioButton(self.verticalLayoutWidget)
        self.satteliteButton.setObjectName("satteliteButton")
        self.verticalLayout.addWidget(self.satteliteButton)
        self.hybridButton = QtWidgets.QRadioButton(self.verticalLayoutWidget)
        self.hybridButton.setObjectName("hybridButton")
        self.verticalLayout.addWidget(self.hybridButton)
        self.showButton = QtWidgets.QPushButton(Form)
        self.showButton.setGeometry(QtCore.QRect(780, 40, 161, 28))
        self.showButton.setObjectName("showButton")
        self.toSearchLabel = QtWidgets.QLabel(Form)
        self.toSearchLabel.setGeometry(QtCore.QRect(620, 180, 160, 15))
        self.toSearchLabel.setText("")
        self.toSearch = QtWidgets.QLineEdit(Form)
        self.toSearch.setGeometry(QtCore.QRect(620, 200, 161, 22))
        self.toSearch.setObjectName("toSearch")
        self.toOrganizationLabel = QtWidgets.QLabel(Form)
        self.toOrganizationLabel.setGeometry(QtCore.QRect(620, 240, 160, 15))
        self.toOrganizationLabel.setText("")
        self.toOrganization = QtWidgets.QLineEdit(Form)
        self.toOrganization.setGeometry(QtCore.QRect(620, 260, 161, 22))
        self.toOrganization.setObjectName("toOrganization")
        self.resetButton = QtWidgets.QPushButton(Form)
        self.resetButton.setGeometry(QtCore.QRect(780, 70, 161, 25))
        self.resetButton.setObjectName("resetButton")
        self.addressLabel = QtWidgets.QLabel(Form)
        self.addressLabel.setGeometry(QtCore.QRect(620, 295, 160, 15))
        self.addressLabel.setText("")
        self.addressField = QtWidgets.QTextEdit(Form)
        self.addressField.setGeometry(QtCore.QRect(620, 310, 161, 70))
        self.addressField.setObjectName("addressField")
        self.addressField.setReadOnly(True)
        self.organizationLabel = QtWidgets.QLabel(Form)
        self.organizationLabel.setGeometry(QtCore.QRect(620, 400, 160, 15))
        self.organizationLabel.setText("")
        self.organizationField = QtWidgets.QTextEdit(Form)
        self.organizationField.setGeometry(QtCore.QRect(620, 420, 161, 70))
        self.organizationField.setObjectName("organizationField")
        self.organizationField.setReadOnly(True)
        self.miscellaneousLabel = QtWidgets.QLabel(Form)
        self.miscellaneousLabel.setGeometry(QtCore.QRect(820, 150, 160, 15))
        self.miscellaneousLabel.setText("")
        self.isPostCBox = QtWidgets.QCheckBox(Form)
        self.isPostCBox.setGeometry(QtCore.QRect(800, 170, 161, 20))
        self.isPostCBox.setObjectName("isPostCBox")
        self.isTrafficCBox = QtWidgets.QCheckBox(Form)
        self.isTrafficCBox.setGeometry(QtCore.QRect(800, 200, 161, 20))
        self.isTrafficCBox.setObjectName("isTrafficCBox")
        self.takeScreenshotTrigger = QtWidgets.QPushButton(Form)
        self.takeScreenshotTrigger.setGeometry(QtCore.QRect(780, 100, 161, 25))
        self.takeScreenshotTrigger.setObjectName("takeScreenshotTrigger")
        self.actionLabel = QtWidgets.QLabel(Form)
        self.actionLabel.setGeometry(QtCore.QRect(835, 10, 160, 15))
        self.actionLabel.setText("")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Standalone Map Client"))
        self.settingsLabel.setText(_translate("Form", "Настройки карты"))
        self.mapTypeLabel.setText(_translate("Form", "Тип карты:"))
        self.schemeButton.setText(_translate("Form", "Cхема"))
        self.satteliteButton.setText(_translate("Form", "Cпутник"))
        self.hybridButton.setText(_translate("Form", "Гибрид"))
        self.toSearchLabel.setText(_translate("Form", "Поиск по запросу:"))
        self.toOrganizationLabel.setText(_translate("Form", "Поиск по организации:"))
        self.organizationLabel.setText(_translate("Form", "Организация:"))
        self.addressLabel.setText(_translate("Form", "Адрес:"))
        self.showButton.setText(_translate("Form", "Показать объект"))
        self.resetButton.setText(_translate("Form", "Сброс настроек"))
        self.miscellaneousLabel.setText(_translate("Form", "Дополнительно:"))
        self.isPostCBox.setText(_translate("Form", "Показывать индекс"))
        self.isTrafficCBox.setText(_translate("Form", "Показывать пробки"))
        self.actionLabel.setText(_translate("Form", "Действия"))
        self.takeScreenshotTrigger.setText(_translate("Form", "Сохранить карту"))


class App(QtWidgets.QWidget, UI):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.type = "map"
        self.search = "Moscow"
        self.coordX, self.coordY = 37.622504, 55.753215
        self.pX, self.pY = 37.622504, 55.753215
        self.spnX, self.spnY = 1, 1
        self.address = "Россия, Москва"
        self.organizationInfo = ""
        self.orgX, self.orgY = None, None
        self.isPost = False
        self.isTraffic = False
        self.loadImage()
        self.showButton.clicked.connect(self.run)
        self.resetButton.clicked.connect(self.reset)
        self.isPostCBox.clicked.connect(self.switchPost)
        self.isTrafficCBox.clicked.connect(self.switchTraffic)
        self.takeScreenshotTrigger.clicked.connect(self.takeScreenshot)
        self.radioButtons = [self.schemeButton, self.satteliteButton, self.hybridButton]

    # Processing key manipulations | tiom4eg
    def keyPressEvent(self, event):
        if event.key() == QtCore.Qt.Key_PageUp:
            if self.spnX < 180 - min(self.spnX / self.spnY, 1) * (self.spnX / 10) and self.spnY < 180 - min(self.spnY / self.spnX, 1) * (self.spnY / 10):
                self.spnX, self.spnY = self.spnX + min(self.spnX / self.spnY, 1) * (self.spnX / 10),\
                                       self.spnY + min(self.spnY / self.spnX, 1) * (self.spnY / 10)
                self.loadImage()
        elif event.key() == QtCore.Qt.Key_PageDown:
            if self.spnX > min(self.spnX / self.spnY, 1) * (self.spnX / 10) and self.spnY > min(self.spnY / self.spnX, 1) * (self.spnY / 10):
                self.spnX, self.spnY = self.spnX - min(self.spnX / self.spnY, 1) * (self.spnX / 10),\
                                       self.spnY - min(self.spnY / self.spnX, 1) * (self.spnY / 10)
                self.loadImage()
        elif event.key() == QtCore.Qt.Key_Left:
            if -180 < self.coordX <= -180 + (self.spnX / 10):
                self.coordX = 180 - (self.spnX / 10)
            else:
                self.coordX -= (self.spnX / 10)
            self.loadImage()
        elif event.key() == QtCore.Qt.Key_Right:
            if 180 - (self.spnX / 10) <= self.coordX < 180:
                self.coordX = -180 + (self.spnX / 10)
            else:
                self.coordX += (self.spnX / 10)
            self.loadImage()
        elif event.key() == QtCore.Qt.Key_Up:
            if 90 - (self.spnY / 10) <= self.coordY < 90:
                self.coordY = -90 + (self.spnY / 10)
            else:
                self.coordY += (self.spnY / 10)
            self.loadImage()
        elif event.key() == QtCore.Qt.Key_Down:
            if -90 < self.coordY <= -90 + (self.spnY / 10):
                self.coordY = 90 - (self.spnY / 10)
            else:
                self.coordY -= (self.spnY / 10)
            self.loadImage()

    # Load image with geocode&static | Ju5t_Nick
    def loadImage(self):
        # Get map with static and show it
        mapRequest = f'http://static-maps.yandex.ru/1.x/?ll={self.coordX},{self.coordY}' \
                         f'&spn={self.spnX},{self.spnY}&l={self.type}{",trf" if self.isTraffic else ""}&pt={self.pX},{self.pY},pmdbm{f"~{self.orgX},{self.orgY},pmdom" if self.orgX else ""}'
        response = requests.get(mapRequest)
        with open("map.png", "wb") as file:
            file.write(response.content)
            file.close()
            self.pixmap = QtGui.QPixmap("map.png")
            self.pixmapHolder.setPixmap(self.pixmap)

    def newCoords(self):
        # Get coords from geocode
        coordsRequest = f"http://geocode-maps.yandex.ru/1.x/?apikey=40d1649f-0493-4b70-98ba-98533de7710b" \
                        f"&geocode={self.search}&format=json"
        response = requests.get(coordsRequest)
        jsonResponse = response.json()
        try:
            geoObject = jsonResponse["response"]["GeoObjectCollection"]["featureMember"][0]["GeoObject"]
            address = geoObject["metaDataProperty"]["GeocoderMetaData"]["text"]
            if self.isPost:
                try:
                    address = f'{address}\nПочтовый индекс: {geoObject["metaDataProperty"]["GeocoderMetaData"]["Address"]["postal_code"]}'
                except KeyError:
                    # Object's post index doesn't exist at all.
                    pass
            self.addressField.setText(address)
            longitude, latitude = geoObject["Point"]["pos"].split(" ")
            delta, delta1 = cutRectangle(geoObject)
            # Converting map coords to class coords for moving/scaling
            self.coordX, self.coordY, self.spnX, self.spnY = float(longitude), float(latitude), float(delta), float(
                delta1)
            self.pX, self.pY = float(longitude), float(latitude)
        except IndexError:
            self.addressField.setText("Такой объект не найден.")

        if self.toOrganization.text():
            organizationRequest = f"https://search-maps.yandex.ru/v1/?apikey=dda3ddba-c9ea-4ead-9010-f43fbc15c6e3&text={self.toOrganization.text()}&lang=ru_RU&ll={self.coordX},{self.coordY}&spn={self.spnX},{self.spnY}&type=biz"
            response = requests.get(organizationRequest)
            jsonResponse = response.json()
            try:
                geoObject = jsonResponse["features"][0]
                orgCoords, orgName, orgAddress, orgTime = geoObject["geometry"]["coordinates"], geoObject["properties"]["name"], geoObject["properties"]["description"], geoObject["properties"]["CompanyMetaData"]["Hours"]["text"]
                self.spnX = max(self.spnX, abs(self.coordX - orgCoords[0]) * 2 + 0.001)
                self.spnY = max(self.spnY, abs(self.coordY - orgCoords[1]) * 2 + 0.001)
                self.organizationField.setText(f"Ближайшая организация: {orgName}\nАдрес: {orgAddress}\nВремя работы: {orgTime}")
                self.orgX, self.orgY = orgCoords
            except IndexError:
                self.organizationField.setText("Такая организация не найдена.")
        self.loadImage()

    def run(self):
        if self.schemeButton.isChecked():
            self.type = "map"
        if self.satteliteButton.isChecked():
            self.type = "sat"
        if self.hybridButton.isChecked():
            self.type = "sat,skl"
        self.search = self.toSearch.text()
        if not self.search:
            self.search = "Moscow"
        self.newCoords()

    def reset(self):
        self.type = "map"
        self.search = "Moscow"
        self.coordX, self.coordY = 37.622504, 55.753215
        self.pX, self.pY = 37.622504, 55.753215
        self.spnX, self.spnY = 1, 1
        self.toSearch.setText("")
        self.toOrganization.setText("")
        self.addressField.setText("Россия, Москва")
        self.organizationField.setText("")
        self.isPost = False
        self.isTraffic = False
        self.isPostCBox.setChecked(False)
        self.isTrafficCBox.setChecked(False)
        self.loadImage()

    def switchPost(self):
        self.isPost = ~self.isPost
        self.newCoords()

    def switchTraffic(self):
        self.isTraffic = ~self.isTraffic
        self.newCoords()

    def takeScreenshot(self):
        filename = QtWidgets.QFileDialog.getSaveFileName(self, 'Сохранение карты', f'map-{self.coordX}-{self.coordY}-{self.spnX}-{self.spnY}.png', "PNG")[0]
        with open("map.png", "rb") as ifile:
            binaryContent = ifile.read()
        with open(filename, "wb") as ofile:
            ofile.write(binaryContent)
            ofile.close()


def except_hook(cls, exception, traceback):
    sys.__excepthook__(cls, exception, traceback)


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    form = App()
    form.show()
    sys.excepthook = except_hook
    sys.exit(app.exec())
