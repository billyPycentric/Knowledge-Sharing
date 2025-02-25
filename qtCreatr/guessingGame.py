from PySide6.QtWidgets import (
    QWidget,
    QVBoxLayout,
    QLabel,
    QLineEdit,
    QProgressBar,
    QPushButton,
)
from PySide6.QtCore import QTimer


class RocWidget(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Brainwaves Analyzer")
        self.setup_ui()

    def setup_ui(self):
        layout = QVBoxLayout()

        self.label = QLabel("Enter a number to analyze your brainwaves:")
        layout.addWidget(self.label)

        self.input_field = QLineEdit()
        self.input_field.setPlaceholderText("Enter a number here...")
        layout.addWidget(self.input_field)

        self.progress_bar = QProgressBar()
        self.progress_bar.setRange(0, 100)
        self.progress_bar.setValue(0)
        layout.addWidget(self.progress_bar)

        self.analyze_button = QPushButton("Analyze Brainwaves")
        self.analyze_button.clicked.connect(self.start_analysis)
        layout.addWidget(self.analyze_button)

        self.result_label = QLabel("")
        layout.addWidget(self.result_label)

        self.setLayout(layout)

    def start_analysis(self):
        user_input = self.input_field.text()

        if not user_input.isdigit():
            self.result_label.setText("Invalid input! Please enter a number.")
            return

        self.analyze_button.setEnabled(False)
        self.input_field.setEnabled(False)

        self.progress_bar.setValue(0)
        self.timer = QTimer()
        self.timer.timeout.connect(lambda: self.update_progress(user_input))
        self.timer.start(1000)

    def update_progress(self, user_input):
        current_value = self.progress_bar.value()
        if current_value < 100:
            self.progress_bar.setValue(current_value + 1)
        else:

            self.timer.stop()
            self.analyze_button.setEnabled(True)
            self.input_field.setEnabled(True)

            self.result_label.setText(
                f"Brainwaves analyzed! Your number is: {user_input}"
            )
