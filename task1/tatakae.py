class titandex:
    def __init__(self,name,height,strength_titan,winning_streak):
        self.name=name
        self.height=height
        self.strength_titan=strength_titan
        self.winning_streak=winning_streak
        winning_streak=0

    def titanvsscout(self,name_of_scout,strength_of_scout):

        if self.strength_titan>strength_of_scout:
            self.winning_streak+=1
            print("The winner is ** "+self.name.upper()+" **"+"\twinning streak of titan is "+str(self.winning_streak))
        elif self.strength_titan<strength_of_scout:
            self.winning_streak = 0
            print("The winner is ** "+name_of_scout.upper() +" **"+ "\twinning streak of titan is " + str(self.winning_streak))
        else:
            self.winning_streak = 0
            print("It's a DRAW\t" + "winning streak of titan is " + str(self.winning_streak))

    def titanvstitan(self,titan):
        winning_streak_of_second_titan=0
        if self.name==titan.name:
            return print("Can't fight the same titan")
        elif self.strength_titan>titan.strength_titan:
            self.winning_streak+=1
            winning_streak_of_second_titan=0
            print("The winner is ** "+self.name.upper()+" **"+"\twinning streak of titan is "+str(self.winning_streak))
        elif self.strength_titan<titan.strength_titan:
            self.winning_streak = 0
            titan.winning_streak=1
            print("The winner is ** "+titan.name.upper() +" **" + "\twinning streak of second titan is " + str(titan.winning_streak))
        else:
            self.winning_streak = 0
            titan.winning_streak= 0
            print("It's a DRAW\t" + "\twinning streak of titan is " + str(self.winning_streak)+"\twinning streak of the second titan is "+str(titan.winning_streak))

titan1=titandex("founding titan",13,350,0)
titan2=titandex("colossal titan",60,300,0)
titan3=titandex("Beast titan",17,450,0)
titan4=titandex("armoured titan",13,250,0)


titan1.titanvsscout("levi",300)
titan1.titanvsscout("hange",230)
titan1.titanvsscout("Mikasa",375)


titan1.titanvstitan(titan2)
titan1.titanvstitan(titan3)
titan1.titanvstitan(titan4)
titan1.titanvstitan(titan1)

