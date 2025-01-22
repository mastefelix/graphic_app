from PyQt6.QtWidgets import QApplication, QWidget

app = QApplication([])
window = QWidget()
window.resize(400,200)
window.setWindowTitle("Первое приложение")

window.show()
app.exec()

