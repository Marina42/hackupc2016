from PyQt4 import QtCore
from PyQt4 import QtGui
import sys
from time import sleep
import serial
ser = serial.Serial('/dev/tty.usbmodem1411', 9600) # Establish the connection on a specific port

app = QtGui.QApplication(sys.argv)

print('wirks')

@QtCore.pyqtSlot(str)
def file_changed(path):
    ser.write(str('hello')) # Convert the decimal number to ASCII then send it to the Arduino
    print ser.readline() # Read the newest output from the Arduino
    sleep(.1) # Delay for one tenth of a second

fs_watcher = QtCore.QFileSystemWatcher(['fileToMonitor.txt'])

fs_watcher.connect(fs_watcher, QtCore.SIGNAL('fileChanged(QString)'), file_changed)

app.exec_()
