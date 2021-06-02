import sys
from datetime import datetime

from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QMainWindow, QApplication
from PyQt5.uic import loadUi

from Axis import Axis, Degree_of_freedom
from DefineVariables import *
from MethodConnects import *
from RobotPart import robotPartToDecrement, robotPartToIncrement, RobotPart
from RobotStructuralFlag import RobotStructuralFlag
from SerialPorts import SerialPorts


class CosirobConnect(QMainWindow):

    def __init__(self):
        super(CosirobConnect, self).__init__()
        loadUi('Cosirob_gui.ui', self)

        self.date = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
        self.statusbar.addPermanentWidget(self.statusLabel)
        DefineVariables.lists(self)

        for i in range(0, len(SerialPorts.getports(self))):
            self.PortBox.addItem(SerialPorts.getports(self)[i])

        self.stackedWidget.setCurrentWidget(self.blankPage)
        self.actionConnect.triggered.connect(lambda: self.stackedWidget.setCurrentWidget(self.connectPage))
        self.positionTable.setRowCount(100)

        self.JoggroupBox.setVisible(False)
        self.XYZgroupBox.setVisible(False)

        MethodConnects.default(self)

    def XyzJogChecked(self):
        self.XYZgroupBox.setVisible(True)
        self.JoggroupBox.setVisible(False)

    def JointJogChecked(self):
        self.JoggroupBox.setVisible(True)
        self.XYZgroupBox.setVisible(False)


    def connectClicked(self):
        self.openedPort= serial.Serial(self.PortBox.currentText()[:4], int(self.BaudRateBox.currentText()),
                                       self.DataBits[self.BitsBox.currentText()], self.Parity[self.ParityBox.currentText()],
                                       self.StopBits[self.StopBitsBox.currentText()], None, self.xonXoffradioButton.isChecked(),
                                       self.rtsCtsradioButton.isChecked(), self.dsrDtrradioButton.isChecked())
        MethodConnects.onConnect(self)
        self.statusLabel.setText("Status Port : Open")
        self.logEdit.append(self.date + " Port " + self.PortBox.currentText()[:4] + " opened")
        self.stackedWidget.setCurrentWidget(self.communicationPage)
        self.openedPort.write((str.encode("WH\rSP 1\r")))
        self.logEdit.append(self.date + " Sent WH ")
        self.logEdit.append(self.date + " Sent SP 1 ")
        self.readPosition()

    def readPosition(self):
        self.position = (str(self.openedPort.read(54), 'utf-8'))
        self.encodedPosition = self.position.split(",")
        self.robotpositionList.append(self.encodedPosition)
        self.row = len(self.robotpositionList) - 1
        self.robotxyzPosition = (', '.join(self.robotpositionList[self.row][0:3]))
        self.robotabcRotation = (', '.join(self.robotpositionList[self.row][3:6]))
        self.robotstructFlag = (', '.join(self.robotpositionList[self.row][6:10]))
        self.positionTable2.setRowCount(len(self.robotpositionList))
        self.positionTable2.setItem(self.row, 0, QtWidgets.QTableWidgetItem(self.robotxyzPosition))
        self.positionTable2.setItem(self.row, 1, QtWidgets.QTableWidgetItem(self.robotabcRotation))
        self.positionTable2.setItem(self.row, 2, QtWidgets.QTableWidgetItem(self.robotstructFlag))

    def sendClicked(self):
        self.openedPort.write(str.encode(self.MessageBox.toPlainText() + "\r"))
        self.logEdit.append(self.date + " Sent " + self.MessageBox.toPlainText())
        if self.MessageBox.toPlainText() == "WH":
            self.readPosition()

    def send2Clicked(self):
        self.openedPort.write(str.encode(self.sendEdit.text() + "\r"))
        self.logEdit.append(self.date + " Sent " + self.sendEdit.text())
        if self.MessageBox.toPlainText() == "WH":
            self.readPosition()

    def handClicked(self):
        if self.handButton.text() == "Open Hand":
            self.handButton.setText("Close Hand")
            self.openedPort.write(str.encode("GO\r"))
            self.logEdit.append(self.date + " Sent " + "GO")
        else:
            self.handButton.setText("Open Hand")
            self.openedPort.write(str.encode("GC\r"))
            self.logEdit.append(self.date + " Sent " + "GC")

    def jogSpeedValue(self):
        self.speedEdit.setText(str(self.jogSpeedSlider.value()))

    def sendjogSpeedValue(self):
        self.openedPort.write(str.encode("SP " + str(self.jogSpeedSlider.value()) + "\r"))
        self.logEdit.append(self.date + " Sent SP" + str(self.jogSpeedSlider.value()))

    def jogIncrementValue(self):
        self.rotationEdit.setText(str(self.jogIncrementSlider.value()))
        self.linearEdit.setText(str(self.jogIncrementSlider.value()*5))


    def waistIncrementClicked(self):
        self.send_jog_command_to_robot(robotPartToIncrement(RobotPart.WAIST))

    def shoulderIncrementClicked(self):
        self.send_jog_command_to_robot(robotPartToIncrement(RobotPart.SHOULDER))

    def elbowIncrementClicked(self):
        self.send_jog_command_to_robot(robotPartToIncrement(RobotPart.ELBOW))

    def twistIncrementClicked(self):
        self.send_jog_command_to_robot(robotPartToIncrement(RobotPart.TWIST))

    def pitchIncrementClicked(self):
        self.send_jog_command_to_robot(robotPartToIncrement(RobotPart.PITCH))

    def rollIncrementClicked(self):
        self.send_jog_command_to_robot(robotPartToIncrement(RobotPart.ROLL))

    def waistDecrementClicked(self):
        self.send_jog_command_to_robot(robotPartToDecrement(RobotPart.WAIST))

    def shoulderDecrementClicked(self):
        self.send_jog_command_to_robot(robotPartToDecrement(RobotPart.SHOULDER))

    def elbowDecrementClicked(self):
        self.send_jog_command_to_robot(robotPartToDecrement(RobotPart.ELBOW))

    def twistDecrementClicked(self):
        self.send_jog_command_to_robot(robotPartToDecrement(RobotPart.TWIST))

    def pitchDecrementClicked(self):
        self.send_jog_command_to_robot(robotPartToDecrement(RobotPart.PITCH))

    def rollDecrementClicked(self):
        self.send_jog_command_to_robot(robotPartToDecrement(RobotPart.ROLL))

    def send_jog_command_to_robot(self, command: str):
        self.openedPort.write(str.encode(command + str(self.jogIncrementSlider.value()) + "\r"))
        self.logEdit.append(self.date + " Sent " + command + str(self.jogIncrementSlider.value()))

    def getCommand(self):
        self.sendEdit.setText(self.commandList.currentItem().text())

    def addPosition(self):
        self.xyzPosition = [self.xEdit.text(), self.yEdit.text(), self.zEdit.text()]
        self.abcRotation = [self.aRotation.text(), self.bRotation.text(), self.cRotation.text()]
        RobotStructuralFlag.getrobotStructuralFlag(self)
        self.positionList[int(self.numberEdit.text())] = ', '.join([', '.join(self.xyzPosition), ', '.join(self.abcRotation), ', '.join(self.structFlag)])
        self.rowPositionTable = int(self.numberEdit.text()) - 1
        self.positionTable.setItem(self.rowPositionTable, 0, QtWidgets.QTableWidgetItem(self.numberEdit.text()))
        self.positionTable.setItem(self.rowPositionTable, 1, QtWidgets.QTableWidgetItem(', '.join(self.xyzPosition)))
        self.positionTable.setItem(self.rowPositionTable, 2, QtWidgets.QTableWidgetItem(', '.join(self.abcRotation)))
        self.positionTable.setItem(self.rowPositionTable, 3, QtWidgets.QTableWidgetItem(', '.join(self.structFlag)))
        self.positionTable.setItem(self.rowPositionTable, 4, QtWidgets.QTableWidgetItem(self.commentEdit.text()))
        self.openedPort.write(str.encode(
            "PD " + self.numberEdit.text() + ", " + self.positionList[int(self.numberEdit.text())] + "\r"))
        self.logEdit.append(self.date + " Added Position:" + str(self.positionList[int(self.numberEdit.text())]))

    def addPositionFromCurrent(self):
        self.encodePosition()
        self.positionList[self.positionSpinBox.value()] = ', '.join(self.encodedPosition)
        self.openedPort.write(
            str.encode("PD " + str(self.positionSpinBox.value()) + ", " + self.positionList[self.positionSpinBox.value()] + "\r"))
        self.robotxyzPosition = (', '.join(self.robotpositionList[self.row][0:3]))
        self.robotabcRotation = (', '.join(self.robotpositionList[self.row][3:6]))
        self.robotstructFlag = (', '.join(self.robotpositionList[self.row][6:10]))
        self.rowPositionTable = self.positionSpinBox.value() - 1
        self.positionTable.setItem(self.rowPositionTable, 0, QtWidgets.QTableWidgetItem(str(self.positionSpinBox.value())))
        self.positionTable.setItem(self.rowPositionTable, 1, QtWidgets.QTableWidgetItem(self.robotxyzPosition))
        self.positionTable.setItem(self.rowPositionTable, 2, QtWidgets.QTableWidgetItem(self.robotabcRotation))
        self.positionTable.setItem(self.rowPositionTable, 3, QtWidgets.QTableWidgetItem(self.robotstructFlag))
        self.logEdit.append(self.date + " Added Position:" + str(self.positionList[self.positionSpinBox.value()]))

    def send_xyzJog_command_to_robot(self, axis: None):
        self.openedPort.write(str.encode("MP " + str(', '.join(self.encodedPosition)) + "\r"))
        self.logEdit.append(self.date + " Sent " "MP" + str(self.encodedPosition))

    def axisIncrement(self, axis: Axis, degree_of_freedom: Degree_of_freedom):
        self.encodePosition()
        self.encodedPosition[axis] = int(self.encodedPosition[axis]) + self.jogIncrementSlider.value() * degree_of_freedom
        self.encodedPosition[axis] = str(self.encodedPosition[axis])

    def axisDecrement(self, axis: Axis, degree_of_freedom: Degree_of_freedom):
        self.encodePosition()
        self.encodedPosition[axis] = int(self.encodedPosition[axis]) - self.jogIncrementSlider.value() * degree_of_freedom
        self.encodedPosition[axis] = str(self.encodedPosition[axis])


    def encodePosition(self):
        self.openedPort.write(str.encode("WH\r"))
        self.position = (str(self.openedPort.read(54), 'utf-8'))
        self.encodedPosition = self.position.split(",")

    def IncreaseAClicked(self):
        self.send_xyzJog_command_to_robot(self.axisIncrement(Axis.A, Degree_of_freedom.rotational))

    def IncreaseBClicked(self):
        self.send_xyzJog_command_to_robot(self.axisIncrement(Axis.B, Degree_of_freedom.rotational))

    def IncreaseCClicked(self):
        self.send_xyzJog_command_to_robot(self.axisIncrement(Axis.C, Degree_of_freedom.rotational))

    def DecreaseAClicked(self):
        self.send_xyzJog_command_to_robot(self.axisDecrement(Axis.A, Degree_of_freedom.rotational))

    def DecreaseBClicked(self):
        self.send_xyzJog_command_to_robot(self.axisDecrement(Axis.B, Degree_of_freedom.rotational))

    def DecreaseCClicked(self):
        self.send_xyzJog_command_to_robot(self.axisDecrement(Axis.C, Degree_of_freedom.rotational))

    def IncreaseXClicked(self):
        self.send_xyzJog_command_to_robot(self.axisIncrement(Axis.X, Degree_of_freedom.linear))

    def IncreaseYClicked(self):
        self.send_xyzJog_command_to_robot(self.axisIncrement(Axis.Y, Degree_of_freedom.linear))

    def IncreaseZClicked(self):
        self.send_xyzJog_command_to_robot(self.axisIncrement(Axis.Z, Degree_of_freedom.linear))

    def DecreaseXClicked(self):
        self.send_xyzJog_command_to_robot(self.axisDecrement(Axis.Z, Degree_of_freedom.linear))

    def DecreaseYClicked(self):
        self.send_xyzJog_command_to_robot(self.axisDecrement(Axis.Y, Degree_of_freedom.linear))

    def DecreaseZClicked(self):
        self.send_xyzJog_command_to_robot(self.axisDecrement(Axis.Z, Degree_of_freedom.linear))







app = QApplication(sys.argv)
window = CosirobConnect()
widget = QtWidgets.QStackedWidget()
widget.addWidget(window)
widget.setGeometry(650, 350, 750, 450)
widget.show()
app.exec_()
