from PyQt6.QtWidgets import QMainWindow,QWidget,QTextEdit,QVBoxLayout,QPushButton,QHBoxLayout, QFileDialog

class MainWindow(QMainWindow):
    def __init__ (self):
        super().__init__()

        self.setWindowTitle('My App1')

        self.button_open = QPushButton("Открыть")
        self.button_open.clicked.connect(self.button_open_click)

        self.button_save = QPushButton("Сохранить")
        self.button_save.clicked.connect(self.button_save_click)

        self.input = QTextEdit()

        button_layout = QHBoxLayout()
        button_layout.addWidget(self.button_open)
        button_layout.addWidget(self.button_save)
        button_container = QWidget()
        button_container.setLayout(button_layout)

        layout = QVBoxLayout()
        layout.addWidget(button_container)
        layout.addWidget(self.input)

        container = QWidget()
        container.setLayout(layout)

        self.setCentralWidget(container)
    
    def button_open_click(self):
        file = QFileDialog.getOpenFileName(self, "Open File", "/", "Text (*.txt)")
        if file:
            self.open_file(file)
    
    def button_save_click(self):
        file = QFileDialog.getOpenFileName(self, "Open File", "/", "Text (*.txt)")
        if file:
            self.save_file(file)
    
    def open_file(self, file):
        content = ""
        with open(file[0], "r") as f:
            content += f.read()
        self.input.setText(content)

    def save_file(self, file):
        content = self.input.toPlainText()
        with open(file[0], "w") as f:
            f.write(content)
        print("Спасибо!")