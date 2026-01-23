class flashcard:
    def __init__(self, word, meaning):
        self.words = word
        self. meanings =  meaning
    def __str__(self):
        return self.word +' ('+self.meaning+')'
    flash=[]
    print("Welcome to Flashcard Ennterprises Ltd")
    while True:
        word = input("Enter the name you want to add to our prenium set of flashcards!")
        meaning = input("Enter the meaning of the word you are adding!")
        flash.append(flashcard(word, meaning))
option = int(input("Enter yes , if you want to add another flashcard. Otherwise enter no. Thank you for using Flashcard Ennterprises Ltd   : "))
if(option):
     break
print("\nYour flashcards")
for i in flash:
 print(">", i)