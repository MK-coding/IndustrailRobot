class RobotStructuralFlag:
     def getrobotStructuralFlag(self):
         self.structFlag.clear()
         if not self.ignoreCheckBox.isChecked():
             if self.LeftCheckBox.isChecked() and not self.RightCheckBox.isChecked():
                 self.structFlag.append("L")
             if self.RightCheckBox.isChecked() and not self.LeftCheckBox.isChecked():
                 self.structFlag.append("R")
             if self.LeftCheckBox.isChecked() and self.RightCheckBox.isChecked():
                 self.statusbar.showMessage("Check Left or Right", 5000)
             if self.AboveCheckBox.isChecked() and not self.BelowCheckBox.isChecked():
                 self.structFlag.append("A")
             if self.BelowCheckBox.isChecked() and not self.AboveCheckBox.isChecked():
                 self.structFlag.append("B")
             if self.AboveCheckBox.isChecked() and self.BelowCheckBox.isChecked():
                 self.statusbar.showMessage("Check Above or Below", 5000)
             if self.FlipCheckBox.isChecked() and not self.NoFlipCheckBox.isChecked():
                 self.structFlag.append("F")
             if self.NoFlipCheckBox.isChecked() and not self.FlipCheckBox.isChecked():
                 self.structFlag.append("N")
             if self.NoFlipCheckBox.isChecked() and self.FlipCheckBox.isChecked():
                 self.statusbar.showMessage("Check Flip or No Flip", 5000)
         else:
             self.structFlag.clear()
         if not self.ignoreGripStateRadioButton.isChecked():
             if self.openGripRadioButton.isChecked() and not self.closedGripRadioButton.isChecked():
                 self.structFlag.append("O")
             if self.closedGripRadioButton.isChecked() and not self.openGripRadioButton.isChecked():
                 self.structFlag.append("C")



