import os

styles = ''
dirPath = os.getcwd() + '/src/qss';

for filename in os.listdir(dirPath):
  with open(dirPath + '/' + filename, "r", encoding="utf-8") as io_wrapper:
    styles += io_wrapper.read() + '\n'