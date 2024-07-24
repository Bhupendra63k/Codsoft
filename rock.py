import random
l=["rock","paper","scissors"]
('''
   "rock" vs "scisssors -> rock wins
   "rock" vs "papers" -> paper wins
    "paper" vs "scissors" ->scissors wins
 ''')
print("welcome to rock paper scissors game")
print("Are you want to play :")
print("press 1 for start game")
while True :
  user_choice=int(input("enter a value : "))
  ccount=0
  player_count=0
  if user_choice==1 :
    print("your game is start")
    for u in range(1,6):
     user_turn=int(input("enter your turn :"))
     print('''
    1 for 'rock'
    2 for 'paper'
    3 for 'scissors'
          ''')
     if user_turn ==1:
        player="rock"
     elif user_turn ==2:
        player="paper"
     elif user_turn==3:
        player ="scissors"
     else :
      print("invalid")
     computer=random.choice(l)
     if computer==player:
      print("match draw")
      print(computer)
      print(player)
      ccount=ccount+1
      player_count=player_count+1
     elif (player=="rock" and computer=="scissors") or  (player=="scissors" and computer=="paper") or (player=="paper"and computer=="rock"):
      print("player win")
      print(computer)
      print(player)
      player_count=player_count+1
    else :
     print("computer win")
     print(computer)
     print(player)
     ccount=ccount+1
     print("computer score :",ccount)
     print("player score :",player_count)
    if ccount>player_count:
      print("you lose")
    elif ccount<player_count :
      print("you win")
    else :
      print("match draw")
      while False:
        break