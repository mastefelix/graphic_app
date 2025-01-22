from PyQt6.QtWidgets import QApplication, QWidget, QLabel, QPushButton, QHBoxLayout, QVBoxLayout
from PyQt6.QtCore import Qt
from random import randint

def set_winner():
    label1.setText("Победитель!")
    label1.setText(str(randint(1, 1000000)))

app = QApplication([])
window = QWidget()
window.resize(400,200)
window.setWindowTitle("Лотерея")

label = QLabel("Для участия нажми кнопку")
label1 = QLabel("?")

button = QPushButton("Учавствовать")
line = QVBoxLayout()

line.addWidget(label, alignment=Qt.AlignmentFlag.AlignCenter)
line.addWidget(label1, alignment=Qt.AlignmentFlag.AlignCenter)
line.addWidget(button, stretch=1)
window.setLayout(line)

button.clicked.connect(set_winner)

window.show()
app.exec()
