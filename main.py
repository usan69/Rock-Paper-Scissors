import random



rock='''
" _______
---   ____)
      (_____)
      (_____)
      (____)
---.__(___)
""")'''


paper='''

 _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
""")'''


scissors='''

   _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
""")'''



game_image=[rock,paper,scissors]

user_choice=int(input("What do you choose? 0 type for rock , 1 type for paper , 2  type for scissors!\n"))
print(game_image[user_choice])

computer_choice=random.randint(0,2)

print("computer choose :")
print(game_image[computer_choice])


if user_choice==0 and computer_choice==2:
  print("user wins!")
elif user_choice >=3 or user_choice < 0 :
  print("You typed an invalid number. you lose")
elif computer_choice==0 and user_choice==2:
  print("You lose")
elif computer_choice > user_choice :
  print("Computer wins!")
elif user_choice< computer_choice:
  print("You win")
elif computer_choice==user_choice:
  print("it's a draw")
