import sys

from utils.qss_style import styles
from PyQt5.QtWidgets import QApplication
from views.home.home_widget import HomeWidget

if __name__ == "__main__":
  app = QApplication(sys.argv)
  window = HomeWidget()
  window.setStyleSheet(styles)
  window.show()
  app.exec()

