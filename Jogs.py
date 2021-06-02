class Jogs:
    def Decrements(self):
        def waistDecrementClicked(self):
            self.openedPort.write(str.encode(str("DJ 1,-" + str(self.jogIncrementSlider.value()) + "\r")))
            self.logEdit.append(self.date + " Sent " + str("DJ 1,-" + str(self.jogIncrementSlider.value())))

        def shoulderDecrementClicked(self):
            self.openedPort.write(str.encode(str("DJ 2,-" + str(self.jogIncrementSlider.value()) + "\r")))
            self.logEdit.append(self.date + " Sent " + str("DJ 2,-" + str(self.jogIncrementSlider.value())))

        def elbowDecrementClicked(self):
            self.openedPort.write(str.encode(str("DJ 3,-" + str(self.jogIncrementSlider.value()) + "\r")))
            self.logEdit.append(self.date + " Sent " + str("DJ 3,-" + str(self.jogIncrementSlider.value())))

        def twistDecrementClicked(self):
            self.openedPort.write(str.encode(str("DJ 4,-" + str(self.jogIncrementSlider.value()) + "\r")))
            self.logEdit.append(self.date + " Sent " + str("DJ 4,-" + str(self.jogIncrementSlider.value())))

        def pitchDecrementClicked(self):
            self.openedPort.write(str.encode(str("DJ 5,-" + str(self.jogIncrementSlider.value()) + "\r")))
            self.logEdit.append(self.date + " Sent " + str("DJ 5,-" + str(self.jogIncrementSlider.value())))

        def rollDecrementClicked(self):
            self.openedPort.write(str.encode(str("DJ 6,-" + str(self.jogIncrementSlider.value()) + "\r")))
            self.logEdit.append(self.date + " Sent " + str("DJ 6,-" + str(self.jogIncrementSlider.value())))