class dice:
    diceTypes = ["", "000010000", "100000001", "100010001", "101000101","101010101","101101101"]

    def renderDice(self, number):
        dot = "o"
        counter = 0
        for h in range(4):
            if h == 0 or h==9:
                print ' ',
            else:
                print '-',
        print '\n',
        for x in self.diceTypes[number]:
            if counter % 3 == 0:
                print '|',
            counter += 1
            if int(x) == 1:
                print dot,
            else:
                print ' ',
            if counter % 3 == 0:
                print '|\n',
        for h in range(4):
            if h == 0 or h==9:
                print ' ',
            else:
                print '-',
        print '\n',