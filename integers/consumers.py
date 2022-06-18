from channels.generic.websocket import WebsocketConsumer
import json
from random import randint, choice
from time import sleep

emo = ['[smile]','[happy]','[angry]','[cry]','[embarrassed]','[surprised]','[wronged]','[shout]','[flushed]','[yummy]','[complacent]','[drool]','[scream]','[weep]','[speechless]','[funnyface]','[laughwithtears]','[wicked]','[facewithrollingeyes]','[sulk]','[thinking]','[lovely]','[greedy]','[wow]','[joyful]','[hehe]','[slap]','[tears]','[stun]','[cute]','[blink]','[disdain]','[astonish]','[rage]','[cool]','[excited]','[proud]','[smileface]','[evil]','[angel]','[laugh]','[pride]','[nap]','[loveface]','[awkward]','[shock]']

class WSConsumer(WebsocketConsumer):
    def connect(self):
        self.accept()

        for i in range(1000):
            self.send(json.dumps({'message': choice(emo)}))
            sleep(0.1)