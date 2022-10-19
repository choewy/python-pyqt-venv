from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QWidget, QLabel, QVBoxLayout

class HomeWidget(QWidget):
  def __init__(self) -> None:
    super().__init__()
    self.setObjectName('home-widget')
    self.setMinimumSize(600, 400)
    self.setLayout(self.setUI())

  def setSize(self):
    self.width = '100%' 
  
  def setUI(self):
    label = QLabel()
    label.setObjectName('home-widget-label-hello-world')
    label.setText('Hello World!')

    virtualLayout = QVBoxLayout()
    virtualLayout.setContentsMargins(0, 0, 0, 0)
    virtualLayout.addWidget(label, alignment=Qt.AlignCenter)

    return virtualLayout
    
  
  