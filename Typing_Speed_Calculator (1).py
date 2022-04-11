#Importing Libraries

from time import *
import random as r

#Calculating Errors

def errors(paratest,usertest):
    err=0
    for i in range(len(paratest)):
        try:
            if (paratest[i]!=usertest[i]):
                err=err+1
        except:
            continue
    return err

#Time calculation

def time_taken(stime,endtime,user):
    delay=endtime-stime
    exact_time=round(delay,2)
    speed=len(user)/exact_time
    return round(speed)

#User Input data

test=["Narrative paragraphs tell about a scene or event", "descriptive paragraphs give vivid descriptions of one subject"," expository paragraphs provide information","persuasive paragraphs try to convince the reader","The quick brown fox jumps over the lazy dog"]
test1=r.choice(test)
print("****Let's test the speed****")
print(test1)
print()
print()
stime=time()
user=input("Enter : ")
endtime=time()

#function calls

print("Your speed is",time_taken(stime,endtime,user),"words per sec (w/sec)")
print("Errors are ",errors(test1,user))