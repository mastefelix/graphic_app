from PyQt6.QtWidgets import QApplication, QWidget, QLabel, QPushButton, QHBoxLayout, QVBoxLayout
from PyQt6.QtCore import Qt


def set_label():
    global click
    click += 1
    label_click.setText(str(click))

app = QApplication([])
window = QWidget()
window.resize(400,200)
window.setWindowTitle("Кликер")

click = 0
label = QLabel("Счетчик кликов:")
label_click = QLabel(str(click))

button = QPushButton("Клик")
line = QVBoxLayout()

line.addWidget(label, alignment=Qt.AlignmentFlag.AlignCenter)
line.addWidget(label_click, alignment=Qt.AlignmentFlag.AlignCenter)
line.addWidget(button)
window.setLayout(line)

button.clicked.connect(set_label)

window.show()
app.exec()
