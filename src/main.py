import sys
from core.configs import envs
from PyQt6.QtWidgets import QApplication, QWidget


if __name__ == "__main__":
  print(envs["version"])

  app = QApplication(sys.argv)
  window = QWidget()
  window.show()
  app.exec()

