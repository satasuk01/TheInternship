import sys

listOfCat=["Fruit","Country"]
wordArr = []
max_score=0

def createWordsArray():
    for catI in listOfCat:
        arr = []
        file = open(catI+".txt",'r')
        line = 0
        for line in file:
            arr.append(line.strip())
        wordArr.append(arr)
        file.close()

def play(playWord, answer, hint, score, wrongGuessed, life):#score
    print('Hint:','"',hint,'"')
    while True:
        if(life<=0):
            print("You Lose!")
            input()
            sys.exit()
        if(''.join(playWord) == answer):
            print(answer)
            global max_score
            max_score = score+max_score
            print("You Won! \tmax score:",max_score,"\n")
            break
        print(' '.join(playWord), "\tscore", score,",", "remaining guess",life,',',"wrong guessed:",' '.join(wrongGuessed) )
        char = input()[0]
        if char not in answer and char not in wrongGuessed:
            wrongGuessed.append(char)
            life=life-1
            score=score-1
        elif char in answer and char not in playWord:
            score=score+5
            for i in range(len(answer)):
                if char == answer[i]:
                    playWord[i]=char
        #print(wrongGuessed, life, playWord)
        
createWordsArray()

while True:
    print("Select Category:")
    for i in range(len(listOfCat)):
        print(str(i)+": "+listOfCat[i])
        
    selectedCat = int(input())
    while True:
        if selectedCat>=0 and selectedCat<len(listOfCat):
           break
        selectedCat = int(input("Please input valid number"))

    for i in range(len(wordArr[selectedCat])):
        if i%2 == 1:
            continue     #skip hint
        playWord=['_']*len(wordArr[selectedCat][i])
        wrongGuessed = []
        score=0
        life=10
        #print(playWord,wordArr[selectedCat][i])
        play(playWord, wordArr[selectedCat][i], wordArr[selectedCat][i+1], score, wrongGuessed, life)
    print("You've cleared this category\n")
