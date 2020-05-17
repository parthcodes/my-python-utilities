vacation_poll=[]

continue_poll = True
while continue_poll:
  vacation_poll.append(input("Enter your favorite vacation place:").strip())
  print("Your selection is saved! Thanks for participating.")
  if(input("Enter 'q' to exit the survey! else keep helping!") == 'q'):
    continue_poll = False
print(vacation_poll)