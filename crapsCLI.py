#! /usr/bin/env python3
__author__ = "rafael daveiga"

from die import *


class CrapsCLI(object):
    def __init__(self):
        self.die1 = Die()
        self.die2 = Die()
        self.currentBet = 0
        self.rollValue = 0
        self.startingBank = 2000
        self.currentBank = self.startingBank
        self.firstRoll = True
        self.firstRollValue = 0
        self.numberOfWins = 0
        self.numberOFLoses = 0
        self.payouts = {4: 2, 5: 1.5, 6: 1.2, 8: 1.2, 9: 1.5, 10: 1.2}

    def __str__(self):
        return "FirstRoll: {0} RollValue: {1} Bank: {2} Wins: {3} Losses: {4}".format(self.firstRoll, self.rollValue,
                                                                                      self.currentBank,
                                                                                      self.numberOfWins,
                                                                                      self.numberOFLoses)

    # setters getters later

    def getRollValue(self):
        return self.rollValue

    def getBetValue(self):
        return 50

    def playRoll(self):
        self.placeBet()
        self.rollValue = self.die1.roll() + self.die2.roll()
        print("Rolled a {0}".format(self.getRollValue()))
        if self.firstRoll:
            if self.rollValue in (7, 11):
                self.settleWin()
            elif self.rollValue in (2, 3, 12):
                self.settleLoss()
            else:
                self.firstRoll = False
                self.firstRollValue = self.rollValue
        else:  # play second roll
            if self.rollValue == self.firstRollValue:
                self.settleWin()
            else:
                self.settleLoss()
            self.firstRoll = True
        print(gameObject)
        return

    def settleWin(self):
        self.numberOfWins += 1
        self.settleBet(True, self.rollValue, self.firstRoll, self.currentBet)
        print("win")

    def settleLoss(self):
        self.numberOFLoses += 1
        self.settleBet(False, self.rollValue, self.firstRoll, self.currentBet)
        print("loss")

    def placeBet(self):
        self.currentBet = 50

    def settleBet(self, wonGame, firstRollValue, firstRoll, betValue):
        if firstRoll:
            if wonGame:
                self.currentBank += betValue
            else:
                self.currentBank += betValue
        else:
            if wonGame:
                self.currentBank += betValue * self.payouts[firstRollValue]
            else:
                self.currentBank += betValue * self.payouts[firstRollValue]

    def quitGame(self, event):
        if self.guitCounter == 0:
            self.quitCounter += 1
            self.quitMessage = "Are You Sure You Want To Quit"


gameObject = CrapsCLI()
for number in range(0, 10):
    gameObject.playRoll()
    print("First Roll: {0} Rolled a {1}".format(gameObject.getRollValue(), gameObject.getRollValue()))
    print(gameObject)
