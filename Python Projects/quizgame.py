print("Welcome to my computer program quiz!")
playing = input("Do you want to play? ")

if playing.lower() != "yes":
    quit()
    
print("Okay! Let's play :)")
score = 0

answer = input("Q1. What does CPU stand for? ")
if answer.lower() == "central processing unit":
    print("correct!")
    score += 1
else:
    print("Incorrect!")
    
answer = input("Q2. What does GPU stand for? ")
if answer.lower() == "graphical processing unit":
    print("correct!")
    score += 1
else:
    print("Incorrect!")
    
answer = input("Q3. What does RAM stand for? ")
if answer.lower() == "random access memory":
    print("correct!")
    score += 1
else:
    print("Incorrect!")
    
    
print(f"your score is {score} congrast!")
print(f"your score in percentage is {(score/3)*100}")