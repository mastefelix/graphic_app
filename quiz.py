from PyQt6.QtWidgets import QApplication, QWidget, QLabel, QMessageBox, QPushButton,\
    QRadioButton, QHBoxLayout, QVBoxLayout
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QIcon

def check_answer():
    win = QMessageBox()
    win.setWindowTitle("Результат")
    win.setWindowIcon(QIcon("correct_answer.png"))
    if btn_2.isChecked():
        win.setText("Верно!")
    elif btn_1.isChecked() or btn_3.isChecked() or btn_4.isChecked():
        win.setText("Неверно!")
    else:
        win.setText("Ответ не выбран!")
    win.exec()

app = QApplication([])
window = QWidget()
window.resize(400,200)
window.setWindowTitle("Викторина")
window.setWindowIcon(QIcon("icon_quiz.png"))

label = QLabel("Для чего используется оператор break?")
btn_1 = QRadioButton("Остановки программы")
btn_2 = QRadioButton("Остановки цикла")
btn_3 = QRadioButton("Остановки функции")
btn_4 = QRadioButton("Остановки приложения")

btn_answer = QPushButton("Проверка")

line_v = QVBoxLayout()
line_h1 = QHBoxLayout()
line_h2 = QHBoxLayout()

line_h1.addWidget(btn_1)
line_h1.addWidget(btn_2)
line_h2.addWidget(btn_3)
line_h2.addWidget(btn_4)

line_v.addWidget(label, alignment=Qt.AlignmentFlag.AlignCenter)
line_v.addLayout(line_h1)
line_v.addLayout(line_h2)
line_v.addWidget(btn_answer)
window.setLayout(line_v)

btn_answer.pressed.connect(check_answer)

window.show()
app.exec()


# btn_1.clicked.connect(wrong_answer)
# btn_2.clicked.connect(correct_answer)
# btn_3.clicked.connect(wrong_answer)
# btn_4.clicked.connect(wrong_answer)

# def correct_answer():
#     win = QMessageBox()
#     win.setWindowTitle("Результат")
#     win.setWindowIcon(QIcon("correct_answer.png"))
#     win.setText("Верно!")
#     win.exec()

# def wrong_answer():
#     win = QMessageBox()
#     win.setWindowTitle("Результат")
#     win.setWindowIcon(QIcon("wrong_answer.png"))
#     win.setText("Неверно!")
#     win.exec()
