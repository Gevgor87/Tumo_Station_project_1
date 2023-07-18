# 1.Please install and activate venv(virtual environment). Steps below (write in terminal)
#       py -m venv venv
#       .\venv\Scripts\activate         for windows
#       source ./venv/bin/activate      for Mac or Linux
# 2.Install PyQt6 library
#       pip install PyQt6

import sys
from PyQt6.QtGui import QIcon
from PyQt6.QtWidgets import QApplication, QMainWindow, QLineEdit, QPushButton, QLabel


#-------------------------------------------------------------------
#                       Window Initialization
#-------------------------------------------------------------------
class Main(QMainWindow):
    def __init__(self) -> None:
        super(Main, self).__init__()

        self.setWindowTitle("Station Project 1(task 2)")
        self.setGeometry(400,200,650,500)
        self.setWindowIcon(QIcon(".\Images\window_icon.png"))


#-------------------------------------------------------------------
#                       LABELS FOR INPUT
#-------------------------------------------------------------------
        self.pers_name = QLabel(self)
        self.pers_name.setText("Input Person’s name")
        self.pers_name.move(50,20)
        self.pers_name.adjustSize()
        self.pers_name_text = QLineEdit("Bob", self)
        self.pers_name_text.move(180, 15)
        self.pers_name_text.setFixedSize(100,25)

        self.noun_1 = QLabel(self)
        self.noun_1.setText("Input noun")
        self.noun_1.move(50,50)
        self.noun_1.adjustSize()
        self.noun_1_text = QLineEdit("dog", self)
        self.noun_1_text.move(180, 45)
        self.noun_1_text.setFixedSize(100,25)

        self.adjective_1 = QLabel(self)
        self.adjective_1.setText("Input adjective(feeling)")
        self.adjective_1.move(50,80)
        self.adjective_1.adjustSize()
        self.adjective_1_text = QLineEdit("fear", self)
        self.adjective_1_text.move(180, 75)
        self.adjective_1_text.setFixedSize(100,25)

        self.verb_1 = QLabel(self)
        self.verb_1.setText("Input verb")
        self.verb_1.move(50,110)
        self.verb_1.adjustSize()
        self.verb_1_text = QLineEdit("dance", self)
        self.verb_1_text.move(180, 105)
        self.verb_1_text.setFixedSize(100,25)

        self.adjective_2 = QLabel(self)
        self.adjective_2.setText("Input adjective(feeling)")
        self.adjective_2.move(50,140)
        self.adjective_2.adjustSize()
        self.adjective_2_text = QLineEdit("nervouse", self)
        self.adjective_2_text.move(180, 135)
        self.adjective_2_text.setFixedSize(100,25)

        self.animal_1 = QLabel(self)
        self.animal_1.setText("Input an animal")
        self.animal_1.move(50,170)
        self.animal_1.adjustSize()
        self.animal_1_text = QLineEdit("frog", self)
        self.animal_1_text.move(180, 165)
        self.animal_1_text.setFixedSize(100,25)

        self.verb_2 = QLabel(self)
        self.verb_2.setText("Input verb")
        self.verb_2.move(50,200)
        self.verb_2.adjustSize()
        self.verb_2_text = QLineEdit("squize", self)
        self.verb_2_text.move(180, 195)
        self.verb_2_text.setFixedSize(100,25)

        self.color_1 = QLabel(self)
        self.color_1.setText("Input color")
        self.color_1.move(50,230)
        self.color_1.adjustSize()
        self.color_1_text = QLineEdit("skyblue", self)
        self.color_1_text.move(180, 225)
        self.color_1_text.setFixedSize(100,25)

        self.verb_3 = QLabel(self)
        self.verb_3.setText("Input verb + ly")
        self.verb_3.move(50,260)
        self.verb_3.adjustSize()
        self.verb_3_text = QLineEdit("barking", self)
        self.verb_3_text.move(180, 255)
        self.verb_3_text.setFixedSize(100,25)

        self.adjective_3 = QLabel(self)
        self.adjective_3.setText("Input adjective + ly")
        self.adjective_3.move(350,20)
        self.adjective_3.adjustSize()
        self.adjective_3_text = QLineEdit("lovely", self)
        self.adjective_3_text.move(480, 15)
        self.adjective_3_text.setFixedSize(100,25)

        self.number_1 = QLabel(self)
        self.number_1.setText("Input number")
        self.number_1.move(350,50)
        self.number_1.adjustSize()
        self.number_1_text = QLineEdit("429", self)
        self.number_1_text.move(480, 45)
        self.number_1_text.setFixedSize(100,25)

        self.measure_of_time = QLabel(self)
        self.measure_of_time.setText("Input measure of time")
        self.measure_of_time.move(350,80)
        self.measure_of_time.adjustSize()
        self.measure_of_time_text = QLineEdit("decade", self)
        self.measure_of_time_text.move(480, 75)
        self.measure_of_time_text.setFixedSize(100,25)

        self.color_2 = QLabel(self)
        self.color_2.setText("Input color")
        self.color_2.move(350,110)
        self.color_2.adjustSize()
        self.color_2_text = QLineEdit("dark black", self)
        self.color_2_text.move(480, 105)
        self.color_2_text.setFixedSize(100,25)

        self.animal_2 = QLabel(self)
        self.animal_2.setText("Input animal")
        self.animal_2.move(350,140)
        self.animal_2.adjustSize()
        self.animal_2_text = QLineEdit("chicken", self)
        self.animal_2_text.move(480, 135)
        self.animal_2_text.setFixedSize(100,25)

        self.number_2 = QLabel(self)
        self.number_2.setText("Input number")
        self.number_2.move(350,170)
        self.number_2.adjustSize()
        self.number_2_text = QLineEdit("32", self)
        self.number_2_text.move(480, 165)
        self.number_2_text.setFixedSize(100,25)

        self.silly_word = QLabel(self)
        self.silly_word.setText("Input silly word")
        self.silly_word.move(350,200)
        self.silly_word.adjustSize()
        self.silly_word_text = QLineEdit("fifi", self)
        self.silly_word_text.move(480, 195)
        self.silly_word_text.setFixedSize(100,25)

        self.noun_2 = QLabel(self)
        self.noun_2.setText("Input noun")
        self.noun_2.move(350,230)
        self.noun_2.adjustSize()
        self.noun_2_text = QLineEdit("pen", self)
        self.noun_2_text.move(480, 225)
        self.noun_2_text.setFixedSize(100,25)



#-------------------------------------------------------------------
#                           Creating Text
#-------------------------------------------------------------------
        self.text = f"""This weekend I am going camping with <em style='color:red'>{self.pers_name_text.text()}</em>. 
I packed my lantern, sleeping bag, and <em style='color:red'>{self.noun_1_text.text()}</em>. 
I am so <em style='color:red'>{self.adjective_1_text.text()}</em> to <br> 
<em style='color:red'>{self.verb_1_text.text()}</em> in a tent. 
I am <em style='color:red'>{self.adjective_2_text.text()}</em> we might see a(n) 
<em style='color:red'>{self.animal_1_text.text()}</em>, I hear they’re kind of dangerous. 
While we’re <br>camping, we are going to hike, fish, and 
<em style='color:red'>{self.verb_2_text.text()}</em>. I have heard that the 
<em style='color:red'>{self.color_1_text.text()}</em> lake is great for 
<em style='color:red'>{self.verb_3_text.text()}</em>. <br>
Then we will <em style='color:red'>{self.adjective_3_text.text()}</em> hike through the forest for 
<em style='color:red'>{self.number_1_text.text()}</em> 
<em style='color:red'>{self.measure_of_time_text.text()}</em>. If I see a 
<em style='color:red'>{self.color_2_text.text()}</em> <em style='color:red'>{self.animal_2_text.text()}</em> while hiking,<br>
I am going to bring it home as a pet! At night we will tell 
<em style='color:red'>{self.number_2_text.text()}</em> 
<em style='color:red'>{self.silly_word_text.text()}</em> stories and roast 
<em style='color:red'>{self.noun_2_text.text()}</em> around the <br>campfire!!"""



#-------------------------------------------------------------------
#                   Button and text show
#-------------------------------------------------------------------
        self.btn = QPushButton(self, text="Update text")
        self.btn.move(280,310)
        self.btn.clicked.connect(self.button_click)
        self.new_text = QLabel(self)
        self.new_text.setText(self.text)
        self.new_text.move(50,370)
        self.new_text.adjustSize()


#-------------------------------------------------------------------
#                   Button click event
#------------------------------------------------------------------- 
    def button_click(self):
        self.text = f"""This weekend I am going camping with <em style='color:red'>{self.pers_name_text.text()}</em>. 
I packed my lantern, sleeping bag, and <em style='color:red'>{self.noun_1_text.text()}</em>. 
I am so <em style='color:red'>{self.adjective_1_text.text()}</em> to <br> 
<em style='color:red'>{self.verb_1_text.text()}</em> in a tent. 
I am <em style='color:red'>{self.adjective_2_text.text()}</em> we might see a(n) 
<em style='color:red'>{self.animal_1_text.text()}</em>, I hear they’re kind of dangerous. 
While we’re <br>camping, we are going to hike, fish, and 
<em style='color:red'>{self.verb_2_text.text()}</em>. I have heard that the 
<em style='color:red'>{self.color_1_text.text()}</em> lake is great for 
<em style='color:red'>{self.verb_3_text.text()}</em>. <br>
Then we will <em style='color:red'>{self.adjective_3_text.text()}</em> hike through the forest for 
<em style='color:red'>{self.number_1_text.text()}</em> 
<em style='color:red'>{self.measure_of_time_text.text()}</em>. If I see a 
<em style='color:red'>{self.color_2_text.text()}</em> <em style='color:red'>{self.animal_2_text.text()}</em> while hiking,<br>
I am going to bring it home as a pet! At night we will tell 
<em style='color:red'>{self.number_2_text.text()}</em> 
<em style='color:red'>{self.silly_word_text.text()}</em> stories and roast 
<em style='color:red'>{self.noun_2_text.text()}</em> around the <br>campfire!!"""
        self.new_text.setText(self.text)
        self.new_text.adjustSize()


#-------------------------------------------------------------------
#                       RUN WINDOW
#------------------------------------------------------------------- 
def application():
    app = QApplication(sys.argv)
    main_window = Main()
    main_window.show()
    sys.exit(app.exec())

if __name__ == "__main__":
    application()

