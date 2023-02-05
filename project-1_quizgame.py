q1='''who is the best player in cricket?
a.Dhoni
b.Virat
c.Rohit sharma
d.pandya'''
q2='''what are you studying?
a.BBA
b.B.sc
c.B.tech
d.MBBS'''
q3='''which branch is tough in engineering?
a.ECE
b.EEE
c.Mech
d.CSE'''
q4='''what is the capital of INDIA?
a.Delhi
b.Andhra Pradesh
c.Kerala
d.Bihar'''
q5='''what is the easiest programming language?
a.python
b.C language
c.java
d.HTML"'''

questions={q1:"a",q2:"c",q3:"a",q4:"a",q5:"a"}

name=input("Enter name:")
print("Hello",name,"Welcome to the quiz")
score=0
for i in questions:
    print()
    print(i)
    flag1=input("Do you want to skip this question(yes/no)")
    if  flag1=="Yes":
                continue
    ans=input("Enter your answer")
    if ans==questions[i]:
        print("Wow! you got one point")
        score=score+1
        print("Your current score is :",score)
    else:
        print("Wrong answer,u lost 1 mark")
        print("Correct answer:",questions[i])
        score=score-1
        print("Your current score is:",score)
    flag2=input("Do you want to quit? type(yes/no)")
    if flag2=="Yes":
                break
            
print("Your total score:",score)      
             
             
