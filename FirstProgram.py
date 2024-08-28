#FirstProgram.py
#Name:Dillan Klug
#Date:8/28/2024
#Assignment:Lab 1

def main():
  print("First Program")
  #Say hello
  print("Hello user")
  #Ask for the user's name
  name = input("What is your name? ")
  #Use the user's name in the program.
  print("Nice to meet you", name)
  #Ask the user for their age.
  age = input("How old are you? ")
  #Tell the user what year they were born in.
  #Assume that they have not had their birthday yet this year.
  birthY = 2024 - int(age)
  print("That means you were born around", birthY)

#Call the main function if this is the file being run.
if __name__ == '__main__':
    main()
