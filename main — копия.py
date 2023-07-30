import telebot
from telebot import types
import random
token=""
bot=telebot.TeleBot(token)
hp=dmg=0
ras={"elf":{"hp":50,"dmg":70},
     "gnom":{"hp":75,"dmg":40},
     "hobbit":{"hp":100,"dmg":125},
     "org":{"hp":110,"dmg":170}}
prof={"warrior":{"hp":60,"dmg":80},
      "medical":{"hp":100,"dmg":35},
      "mag":{"hp":90,"dmg":130},
      "archer":{"hp":45,"dmg":60}}
monsters=["robot","alien","ghost","zombie","vampire"]
def race_menu():
    keyboard=types.ReplyKeyboardMarkup(resize_keyboard=True)
    for race in ras.keys():
        keyboard.add(types.KeyboardButton(text=race))
    return keyboard
def proff_menu():
    keyboard=types.ReplyKeyboardMarkup(resize_keyboard=True)
    for proff in prof.keys():
        keyboard.add(types.KeyboardButton(text=proff))
    return keyboard
def create_monster():
    rndname=random.choice(monsters)
    rndhp=random.randint(45,110)
    rnddmg=random.randint(30,170)
    return[rndname,rndhp,rnddmg]
@bot.message_handler(commands=["start"])
def start(message):
    keyboard=types.ReplyKeyBoardMarkup(resize_keyboard=True)
    btn1=types.KeyboardButton("play")
    btn2=types.KeyboardButton("info")
    keyboard.add(btn1,btn2)
    bot.send_message(message.chat.id,"Do you wanna play?",reply_markup=keyboard)
def quest():
    keyboard=types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn3=types.KeyboardButton("go")
    btn4=types.KeyboardButton("back")
    keyboard.add(btn3,btn4)
    return keyboard
@bot.message_handler(content_types=["text"])
def main(message):
    global hp,dmg
    victim=create_monster()
    if message.text=="play":
        bot.send_message(message.chat.id,"Выберете расу",reply_markup=race_menu())
    if message.text=="elf":
        hp+=ras["elf"]["hp"]
        dmg+=ras["elf"]["dmg"]
        bot.send_message(message.chat.id,f"Вы выбрали эльфа, у вас столько здоровья {hp}, у вас столько урона {dmg}",reply_markup=proff_menu())
        image=open("5cd8c777035969f08488dd2aac1d8ebe--elves-fantasy-fantasy-rpg.jpg","rb")
        bot.send_photo(message.chat.id,image)
    if message.text=="gnom":
        hp+=ras["gnom"]["hp"]
        dmg+=ras["gnom"]["dmg"]
        bot.send_message(message.chat.id,f"Вы выбрали гнома у вас столько здоровья {hp}, у вас столько урона {dmg}",reply_markup=proff_menu())
        image=open("1663292575_10-phonoteka-org-p-gnom-art-krasivo-10.jpg","rb")
        bot.send_photo(message.chat.id,image)
    if message.text=="hobbit":
        hp+=ras["hobbit"]["hp"]
        dmg+=ras["hobbit"]["dmg"]
        bot.send_message(message.chat.id,f"Вы выбрали хоббита у вас столько здоровья {hp}, у вас столько урона {dmg}",reply_markup=proff_menu())
        image=open("1645247048_1-adonius-club-p-khobbit-art-1.jpg","rb")
        bot.send_photo(message.chat.id,image)
    if message.text=="org":
        hp+=ras["org"]["hp"]
        dmg+=ras["org"]["dmg"]
        bot.send_message(message.chat.id,f"Вы выбрали орга у вас столько здоровья {hp}, у вас столько урона {dmg}",reply_markup=proff_menu())
        image=open("ab950a3e504b83c244eac37bfdefed36.jpg","rb")
        bot.send_photo(message.chat.id,image)
    if message.text=="warrior":
        hp+=ras["warrior"]["hp"]
        dmg+=ras["warrior"]["dmg"]
        bot.send_message(message.chat.id,f"Вы выбрали воина у вас столько здоровья {hp}, у вас столько урона {dmg}",reply_markup=quest())
        image=open("voin-80-foto-8.jpg","rb")
        bot.send_photo(message.chat.id,image)
    if message.text=="medical":
        hp+=ras["medical"]["hp"]
        dmg+=ras["medical"]["dmg"]
        bot.send_message(message.chat.id,f"Вы выбрали лечащий у вас столько здоровья {hp}, у вас столько урона {dmg}",reply_markup=quest())
        image=open("tony-foti-heal-scaled.jpg","rb")
        bot.send_photo(message.chat.id,image)
    if message.text=="mag":
        hp+=ras["mag"]["hp"]
        dmg+=ras["mag"]["dmg"]
        bot.send_message(message.chat.id,f"Вы выбрали мага у вас столько здоровья {hp}, у вас столько урона {dmg}",reply_markup=quest())
        image=open("2dfbd347f0ac5fa946a11adc2acaac88.png","rb")
        bot.send_photo(message.chat.id,image)
    if message.text=="archer":
        hp+=ras["archer"]["hp"]
        dmg+=ras["archer"]["dmg"]
        bot.send_message(message.chat.id,f"Вы выбрали лучника у вас столько здоровья {hp}, у вас столько урона {dmg}",reply_markup=quest())
        image=open("devushka-ryzhaia-fantasticheskii-art-art-luchnitsa-grud-zele.jpg","rb")
        bot.send_photo(message.chat.id,image)
    if message.text=="go":
        event=random.randint(1,4)
        if event==1 or event==2 or event==3:
            keyboard=types.ReplyKeyboardMarkup(resize_keyboard=True)
            btn3=types.KeyboardButton("go")
            btn4=types.KeyboardButton("back")
            keyboard.add(btn3,btn4)
            bot.send_message(message.chat.id,"Вам никто не встретился. Хотите ли вы ещё играть?",reply_markup=keyboard)
        elif event==4:
            keyboard=types.ReplyKeyboardMarkup(resize_keyboard=True)
            btn5=types.KeyboardButton("attack")
            btn6=types.KeyboardButton("escape")
            btn7=types.KeyboardButton("back")
            keyboard.add(btn5,btn6,btn7)
            bot.send_message(message.chat.id,f"Вам встретился {victim[0]}. У вас столько {hp} здоровья и столько {dmg} урона. У вашего врага столько {victim[1]} и столько {victim[2]} Хотите ли вы драться?",reply_markup=keyboard)
    if message.text=="attack":
        victim[1]-=dmg
        if victim[1]<=0:
            hp+=20
            dmg+=45
            bot.send_message(message.chat.id,f"У вас столько {hp} и столько {dmg}",reply_markup=quest())
        elif victim[1]>0:
            hp-=victim[2]
            bot.send_message(message.chat.id,f"Вас атакуют!")
            if hp<=0:
                keyboard=types.ReplyKeyboardMarkup(resize_keyboard=True)
                btn7=types.KeyboardButton("back")
                keyboard.add(btn7)
                bot.send_message(message.chat.id,f"Вы умерли. Хотите ли вы заново начать?",reply_markup=keyboard)
    
bot.polling(non_stop=True)