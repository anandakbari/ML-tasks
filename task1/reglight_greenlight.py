creepy_doll = ['red_light', 'green_light', 'red_light', 'you_got_shot', 'green_light', 'you_got_shot',
'you_got_shot', 'green_light', 'you_ got_shot', 'red_light', 'green_light', 'red_light', 'you_got_shot',
'green_light','red_light', 'red_light', 'green_light', 'you_got_shot','red_light', 'you_got_shot']

n=len(creepy_doll)
next_game=[]

'''for index in range(n):
    if creepy_doll[index].count("green_light")>0:
        next_game.append(creepy_doll[index:index+1])'''
next_game.append(creepy_doll[1:n-1:3])




print(next_game)

