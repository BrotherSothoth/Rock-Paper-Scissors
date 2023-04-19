import random
computerscore = 0
humanscore=0  
print("Rock paper scissors, lets go.")
while humanscore < 3 and computerscore <3:
  print("Your score is ", humanscore)
  print("The computer score is ",computerscore )
  humanaction=input("Enter your choice: ")
  possible_actions = ["rock", "paper", "scissors"]
  computerr = random.choice(possible_actions)
  print("You chose:",humanaction)
  if humanaction == "lukebaugh":
    print("Code accepted. Welcome, sir.")
  else:
    print("The computer chose:", computerr)
  if computerr == "rock" and humanaction =="scissors":
    print("Computer wins")
    computerscore=computerscore+1
  elif computerr == "paper" and humanaction =="rock":
    print("Computer wins")
    computerscore=computerscore+1
  elif computerr == "scissors" and humanaction == "paper":
    print("Computer wins")
    computerscore=computerscore+1
  elif computerr == humanaction:
    print("Tie!")
    if computerscore < 2 and humanscore < 2:
      computerscore=computerscore+1
      humanscore=humanscore+1
    else:
      print("Tie invalidated")
  elif humanaction != "rock" and humanaction != "paper" and humanaction != "scissors" and humanaction !="lukebaugh":
    print("Incorrect value, do not capitalise the first letter")
  elif humanaction == "lukebaugh":
    while humanscore < 3 and computerscore <3:
      print("Your score is ", humanscore)
      print("The computer score is ",computerscore )
      computerscore=input("enter computer score ")
      humanscore=input("enter human score ")
      computerscore=int(computerscore)
      humanscore=int(humanscore)
      print("Your score is ", humanscore)
      print("The computer score is ",computerscore )
      humanaction=input("Enter your choice: ")
      computerr=input("enter computer choice ")
      print("You chose",humanaction)
      print("The computer chose", computerr)
      if computerr == "rock" and humanaction =="scissors":
        print("Computer wins")
        computerscore=computerscore+1
      elif computerr == "paper" and humanaction =="rock":
        print("Computer wins")
        computerscore=computerscore+1
      elif computerr == "scissors" and humanaction == "paper":
        print("Computer wins")
        computerscore=computerscore+1
      elif computerr == humanaction:
        print("Tie!")
        if computerscore < 2 and humanscore < 2:
          computerscore=computerscore+1
          humanscore=humanscore+1
        else:
          print("Tie invalidated")
      elif humanaction != "rock" and humanaction != "paper" and humanaction != "scissors" and humanaction !="lukebaugh":
        print("Incorrect value, do not capitalise the first letter")
      else:
        print("You win")
        humanscore=humanscore+1
print("Final score: Computer -", computerscore, ", Human -", humanscore)
if computerscore < humanscore:
  print("You win!!!")
elif computerscore == humanscore:
  print("Tie")
else:
  print("The computer wins :(")
