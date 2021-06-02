class MethodConnects:
    def default(self):
        self.connectButton.clicked.connect(self.connectClicked)
        self.sendButton.clicked.connect(self.sendClicked)
        self.handButton.clicked.connect(self.handClicked)
        self.waistIncrementButton.clicked.connect(self.waistIncrementClicked)
        self.shoulderIncrementButton.clicked.connect(self.shoulderIncrementClicked)
        self.elbowIncrementButton.clicked.connect(self.elbowIncrementClicked)
        self.twistIncrementButton.clicked.connect(self.twistIncrementClicked)
        self.pitchIncrementButton.clicked.connect(self.pitchIncrementClicked)
        self.rollIncrementButton.clicked.connect(self.rollIncrementClicked)
        self.waistDecrementButton.clicked.connect(self.waistDecrementClicked)
        self.shoulderDecrementButton.clicked.connect(self.shoulderDecrementClicked)
        self.elbowDecrementButton.clicked.connect(self.elbowDecrementClicked)
        self.twistDecrementButton.clicked.connect(self.twistDecrementClicked)
        self.pitchDecrementButton.clicked.connect(self.pitchDecrementClicked)
        self.rollDecrementButton.clicked.connect(self.rollDecrementClicked)
        self.IncreaseApushButton.clicked.connect(self.IncreaseAClicked)
        self.IncreaseBpushButton.clicked.connect(self.IncreaseBClicked)
        self.IncreaseCpushButton.clicked.connect(self.IncreaseCClicked)
        self.IncreaseXpushButton.clicked.connect(self.IncreaseXClicked)
        self.IncreaseYpushButton.clicked.connect(self.IncreaseYClicked)
        self.IncreaseZpushButton.clicked.connect(self.IncreaseZClicked)
        self.DecreaseApushButton.clicked.connect(self.DecreaseAClicked)
        self.DecreaseBpushButton.clicked.connect(self.DecreaseBClicked)
        self.DecreaseCpushButton.clicked.connect(self.DecreaseCClicked)
        self.DecreaseXpushButton.clicked.connect(self.DecreaseXClicked)
        self.DecreaseYpushButton.clicked.connect(self.DecreaseYClicked)
        self.DecreaseZpushButton.clicked.connect(self.DecreaseZClicked)
        self.XyzJogradioButton.clicked.connect(self.XyzJogChecked)
        self.JointJogradioButton.clicked.connect(self.JointJogChecked)




        self.sendButton2.clicked.connect(self.send2Clicked)
        self.commandList.clicked.connect(self.getCommand)
        self.jogSpeedSlider.valueChanged.connect(self.jogSpeedValue)
        self.jogSpeedSlider.sliderReleased.connect(self.sendjogSpeedValue)
        self.jogIncrementSlider.valueChanged.connect(self.jogIncrementValue)
        self.addPositionButton.clicked.connect(self.addPosition)
        self.toPositionListButton.clicked.connect(self.addPositionFromCurrent)




    def onConnect(self):
        self.actionJogOperation.triggered.connect(lambda: self.stackedWidget.setCurrentWidget(self.jogPage))
        self.actionCommandTool.triggered.connect(lambda: self.stackedWidget.setCurrentWidget(self.commandPage))
        self.actionCommunication.triggered.connect(lambda: self.stackedWidget.setCurrentWidget(self.communicationPage))
        self.actionPositionTool.triggered.connect(lambda: self.stackedWidget.setCurrentWidget(self.positionPage))
        #self.actionXYZJogTool.triggered.connect(lambda: self.stackedWidget.setCurrentWidget(self.XYZJogTool))