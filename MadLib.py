#MadLib.py
#Name:Dillan Klug
#Date:8/28/2024
#Assignment:Lab 1

def main():
  print("Madlib")
  #Ask user for words
  onomatopoeia = input("Onomatopoeia (Sound) - ")
  verb = input("Past Tense Verb (Action) - ")
  adjective = input("Adjective (Description) - ")
  animal = input ("Favorite Animal - ")
  emotion = input ("Emotion - ")
  number = input ("Number - ")
  #Print the story with the user supplied words.
  print("Here is your Madlib!")
  print()
  print(onomatopoeia + "!,", "he said as he", verb, "away from the", adjective, animal + ". He had never felt so", emotion, "in his", number, "years of life!" )


#Call the main function if this is the file being run.
if __name__ == '__main__':
    main()
