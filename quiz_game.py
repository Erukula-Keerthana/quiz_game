print("Welcome to computer quiz! ")
playing=input("Do you want to play? ")
if playing.lower() !="yes": #here lower convert all letters into lower case
    quit()
print("okay let's play:")
score=0
answer=input("what does CPU stands for? ")
if answer.lower()=="central processing unit":
    print("Corret")
    score=score+1
else:
    print("Incorrect")
answer=input("what does GPU stands for? ")
if answer.lower()=="graphics processing unit":
    print("Corret")
    score=score+1
else:
    print("Incorrect")
answer=input("what does RAM stands for? ")
if answer.lower()=="random access memory":
    print("Corret")
    score=score+1
else:
    print("Incorrect")
answer=input("what does PSU stands for? ")
if answer.lower()=="power supply unit":
    print("Corret")
    score=score+1
else:
    print("Incorrect")
print("you got "+ str(score) + "questions correct")
print("you got "+ str((score/4)*100) + "%")
## i can modify this questions by using score and increasing questions




