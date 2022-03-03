import json
import reg
import re
import random
import dbfunc

#aname=None
#bname=None

def load_file(file):
    with open(file) as responses:
        #print("file opened successfully")
        return json.load(responses)

#if re.search(reg.patterns["greet"],"hi"):
    #print("yes")
#print(responses["greet"])
def match_intent(message):
    #print(message)
    matched_intent = None
    
    for intent,pattern in reg.patterns.items():
        #print(intent)
        if re.search(pattern,message.lower()):
            matched_intent=intent
    #print(matched_intent)
    return matched_intent

def respond(message):
    intent=match_intent(message)
    key='default'
    global bname
    global aname
    responses=load_file("response.json")
    if intent in responses:
        key=intent
    if key=="add_books":
        return(dbfunc.add_books())
    if key=="view_books":
        return(dbfunc.view_books())
    #if key=="buy_books":
        #buy_book=message.split("^")[1]
        #return(dbfunc.buy_books())
    if key=="add_bookname":
        bname=message.split("^")[1]
        #dbfunc.add_bname(bname)
    #print(name)
    if key=="buy_bookname":
        buybook=message.split("^")[1]
        return dbfunc.buy_books(buybook)
    if key=="add_authorname":
        aname=message.split("^")[1]
        #dbfunc.add_aname(name)
        #print(bname)
        #print(aname)
        dbfunc.add_record(bname,aname)
    return random.choice(responses[key])

def send_message(message):
    res=respond(message)
    return res

def take_input():
    s=input("")
    return s
while(True):
    p=take_input()
    if p!="Quit":
        print("Bot: "+send_message(p))
    else:
        print("Thanku fro talking to me!!")
        break
#print(reg.dict_syn)