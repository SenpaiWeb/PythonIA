import io
import time
import random
import re
import codecs

username = str
name = "Jacquie" # bot name
answers = codecs.open("chat.rc", "r", "utf-8").read() # scan file to do not have to re-open it for each operation
def getAnswer(trigger):
    try:
        # catch answer with trigger
        m = re.search('{"trigger": "'+re.escape(trigger)+'", "answer": "(.+)"}', answers)
        return name + ": " + m.group(1).replace("%n", username)
    except AttributeError:
            return "Je ne comprends pas ce que vous me demandez."

def getTrigger(answer):
    m = re.search('{"trigger": "(.+)", "answer": "'+answer+'"}', answers)
    return m.group(1)

def getAll(title):
    insideArray = {}
    m = re.search('"'+title+'": {"trigger": "(.+)", "answer": "(.+)"}', answers)
    insideArray["trigger"] = m.group(1)
    insideArray["answer"] = name + ": " + m.group(2)
    return insideArray

print(getAll("__welcome__")["answer"])
try:
    username = input("<Entrez votre nom> ")
    while(True):
        print(getAnswer(input("$ ")))
except KeyboardInterrupt:
            print("\nBye!")
            exit(1)
