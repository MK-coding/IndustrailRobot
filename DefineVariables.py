import serial


class DefineVariables:
    def lists(self):
        self.positionList = [None] * 100
        self.xyzPosition = []
        self.abcRotation = []
        self.structFlag = []
        self.robotpositionList = []
        self.robotxyzPosition = []
        self.robotabcRotation = []
        self.robotstructFlag = []

        self.DataBits = dict({
            "5": serial.FIVEBITS,
            "6": serial.SIXBITS,
            "7": serial.SEVENBITS,
            "8": serial.EIGHTBITS
        })
        self.Parity = dict({
            "Even": serial.PARITY_EVEN,
            "Odd": serial.PARITY_ODD,
            "Mark": serial.PARITY_MARK,
            "None": serial.PARITY_NONE,
            "Space": serial.PARITY_SPACE
        })
        self.StopBits = dict({
            "1": serial.STOPBITS_ONE,
            "1.5": serial.STOPBITS_ONE_POINT_FIVE,
            "2": serial.STOPBITS_TWO
        })