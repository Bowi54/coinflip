import random
class coinflip:
    def __init__(self):
        self.myscore = 0
        self.enemyscore = 0
    def flip(self):
        return random.choice(['орел', 'решка'])
    def winner(self,vibor ):
        result = self.flip()
        print(result)
        if vibor.lower()==result.lower():
             print('you win')
             self.myscore += 1
        else:
            print('you lose')
            self.enemyscore += 1
        print(self.myscore,self.enemyscore)
    def play(self):
        print('коинфлип')
        while True:
            userinput = input()
            if userinput == 'o':
                vibor = 'орел'
                self.winner(vibor)
            if userinput == 'r':
                vibor = 'решка'
                self.winner(vibor)
            if userinput == 'esc':
                break
            if userinput not in ['o', 'r', 'esc']:
                print('ты чорт')
                continue
if __name__ == "__main__":
    game = coinflip()
    game.play()
    
