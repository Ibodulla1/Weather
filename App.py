from PyQt5.QtWidgets import QApplication, QWidget, QHBoxLayout, QVBoxLayout, QLineEdit, QLabel
import datetime as dt
import requests


class My_Weather(QWidget):
    def __init__(self):
        super().__init__()


        self.Main_label = QLabel("WHEATHER APPLICATION")
        self.Main_label.setStyleSheet("color:dark;")

        self.Data_label = QLabel("")
        self.Hlay_data = QHBoxLayout()
        self.Hlay_data.addStretch()
        self.Hlay_data.addWidget(self.Data_label)
        self.Hlay_data.addStretch()


        self.for_label = QHBoxLayout()

        self.for_label.addStretch()
        self.for_label.addWidget(self.Main_label)
        self.for_label.addStretch()

        self.Enter_city = QLineEdit("")
        self.Enter_city.returnPressed.connect(self.plus)
        self.Enter_city.setPlaceholderText("Enter city...")
        self.Enter_city.setStyleSheet("background-color:black; color:white;")
        self.Enter_city.setFixedSize(200,30)


        self.V_lay = QVBoxLayout()

        self.H_for_Edit = QHBoxLayout()
        self.H_for_Edit.addStretch()
        self.H_for_Edit.addWidget(self.Enter_city)
        self.H_for_Edit.addStretch()

        self.V_lay.addLayout(self.for_label)
        self.V_lay.addStretch()
        self.V_lay.addLayout(self.H_for_Edit)
        self.V_lay.addStretch()
        self.V_lay.addLayout(self.Hlay_data)

        self.V_lay.addStretch()
        self.V_lay.addStretch()

        

        self.setLayout(self.V_lay)



    def plus(self):
        if self.Enter_city.text() is not None and self.Enter_city.text()[0].isupper():

            
            api_key = "41416f76e0242481abb32720414267ce"
            
            users_city = self.Enter_city.text()

            weather_data = requests.get(f"https://api.openweathermap.org/data/2.5/weather?q={users_city}&units=imperial&APPID={api_key}")


            weather = weather_data.json()['weather'][0]['main']

            temp = weather_data.json()['main']['temp']


            temp = int((temp - 32) * (5/9))

            try:

                self.Data_label.setText(f"{self.Enter_city.text()}  {temp}°C\nToday at {dt.datetime.now().hour} o'clock")
                self.Data_label.adjustSize()

            except:
                self.Data_label.setText("No such city found")
                self.Data_label.setStyleSheet("color:red;")
                self.Data_label.adjustSize()    



if __name__ == "__main__":
    ap = QApplication([])

    obj = My_Weather()
    obj.setWindowTitle("IBODULLA")
    obj.setStyleSheet("background-color: #477eec; font: bold 20px Nunito Sans Light;")

    obj.show()

    ap.exec_()        
