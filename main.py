from getpass import getpass as input
print("***THE MOST EPIC \U0001F5FB vs \U0001F4C4 vs \U00002702 BATTLE OF ALL TIME!***")
print("Type R, P or S to make your move! Winner of 3 rounds wins the lot!")
print()
ps1 = 0
ps2 = 0
while True:
# Player 1
  p1 = input("Player 1: ")

# Player 2 
  p2 = input("Player 2: ")

  if p1 == p2:
      print("You both tied!")
  elif (p1 == "R" or p1 == "r") and (p2 == "P" or p2 == "p"):
      print("AH! Congrats Player 2! Paper covers rock!")
      ps2 += 1
  elif (p1 == "P" or p1 == "p") and (p2 == "R" or p2 == "r"):
      print("AH! Congrats Player 1! Paper covers rock! \U0001F389")
      ps1 +=1
  elif (p1 == "S" or p1 == "s") and (p2 == "R" or p2 == "r"):
      print("Congrats Player 2! Rock breaks your scissors! \U0001F389")
      ps2 += 1
  elif p1 == ("R" or p1 == "r") and (p2 == "S" or p2 == "s"):
      print("Congrats Player 1! Rock breaks your scissors! \U0001F389")
      ps1 += 1
  elif (p1 == "P" or p1 == "p") and (p2 == "S" or p2 == "s"):
      print("Congrats Player 2! Scissors cuts paper! \U0001F389")
      ps2 += 1
  elif (p1 == "S" or p1 == "s") and (p2 == "P" or p2 == "p"):
      print("Congrats Player 1! Scissors cuts paper! \U0001F389") 
      ps1 += 1

  if  ps1 ==3:
    print('Thanks for playing! Player 1 Wins!')
  elif ps2 ==3:
    print('Thanks for playing! Player 2 Wins!')
    exit()
  else:
    continue


