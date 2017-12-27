# coding: utf8

import io
import codecs
import json

print("Système d'intégration de Q/R à l'IA")
trigger=input("Quand l'IA détecte: ").replace('"', "''")
answer=input("Que doit répondre l'IA? ").replace('"', "''")

with codecs.open("chat.rc", "a+", "utf-8") as chatFile:
    chatFile.seek(0,0)
    if (chatFile.read().find("[\""+title+"\",")==-1) and (len(trigger) > 0) and (len(answer) > 0) and (len(title) > 0):
         full = json.dumps({'trigger': trigger, 'answer': answer})
         chatFile.write(full)
print("Merci à vous de participer au développement de l'IA")
