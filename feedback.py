from PyQt6.QtWidgets import QApplication, QWidget, QLabel, QPushButton, QHBoxLayout, QVBoxLayout, QSlider
from PyQt6.QtCore import Qt

def set_score():
    label1.setText(str(button.value()))

app = QApplication([])
window = QWidget()
window.resize(400,200)
window.setWindowTitle("Оценка")

button = QSlider()
label = QLabel("Выберите оценку:")
label1 = QLabel("0")

line = QHBoxLayout()

line.addWidget(label, alignment=Qt.AlignmentFlag.AlignCenter)
line.addWidget(label1, alignment=Qt.AlignmentFlag.AlignCenter)
line.addWidget(button)
window.setLayout(line)

button.valueChanged[int].connect(set_score)
window.show()
app.exec()
