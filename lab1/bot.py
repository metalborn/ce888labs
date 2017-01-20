from sopel import module
from emo.wdemotions import EmotionDetector

emo = EmotionDetector()
total_list= [0]*6
@module.rule('')
def hi(bot, trigger):
    #print(trigger, trigger.nick)
    #bot.say('Hi, ' + trigger.nick)
    str(trigger)
    global total_list
    list=emo.detect_emotion_in_raw_np(trigger)
    for i in range (0,5):
        total_list[i]=total_list[i]+list[i]

    print (total_list)