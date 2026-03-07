word=input("Enter word:");
if any(letter in "a,e,i,o,u" for letter in word):
    print("Word contains vowels");
else:
    print("Word not contain vowels");

