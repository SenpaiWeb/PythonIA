import re
from codecs import open
from json import dumps

username = str
name = "Edward" # bot name
answers = open("chat.rc", "r", "utf-8").read() # scan file to do not have to re-open it for each operation
def getAnswer(trigger):
    try:
        # catch answer with trigger
        m = re.search('{"trigger": "'+re.escape(trigger)+'", "answer": "(.+)"}', answers)
        return name + ": " + m.group(1).replace("%n", username)
    except AttributeError:
            answer = input(name + ": Je ne comprends pas ce que vous me demandez, que dois-je répondre la prochaine fois? ")
            addAnswer(trigger, answer)

def getTrigger(answer):
    m = re.search('{"trigger": "(.+)", "answer": "'+answer+'"}', answers)
    return m.group(1)

def addAnswer(trigger, answer):
    open("chat.rc", "a+", "utf-8").write(json.dumps({'trigger':trigger, 'answer':answer}))

print(getAnswer("__firstcontact__"))
try:
    username = input("<Entrez votre nom> ")
    while(True):
        print(getAnswer(input("$ ")))
except KeyboardInterrupt:
            print("\nBye!")
            exit(1)
