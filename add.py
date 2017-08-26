# coding: utf8

import io
import time
import codecs

print("Système d'intégration de Q/R à l'IA")
time.sleep(1)
title=input("Titre: ").replace('"', "''")
trigger=input("Quand l'IA détecte: ").replace('"', "''")
answer=input("Que doit répondre l'IA? ").replace('"', "''")
# options = input("Options? ") # r = regex, v = vars (r, v, rv, vr) (not working atm)

with codecs.open("chat.rc", "a+", "utf-8") as chatFile:
    chatFile.seek(0,0)
    if (chatFile.read().find("[\""+title+"\",")==-1) and (len(trigger) > 0) and (len(answer) > 0) and (len(title) > 0):
        # full = '"'+title+'": {"trigger": "'+trigger+'", "answer": "'+answer+'", "options": "'+options+'"}' + '\n'
         full = '"'+title+'": {"trigger": "'+trigger+'", "answer": "'+answer+'"}\n'
         chatFile.write(full)
time.sleep(1)
print("Merci à vous de participer au développement de l'IA")
