port telebot
from random import choice


name = 'Капибара'
energy = 70
satiety = 10
happiness = 100
bot = telebot.TeleBot("5623563303:AAG1mUPGVFGdGAUh_u0ruz-xG-cyWjmP77s")
stickers = ['CAACAgIAAxkBAAEI3ZlkVRJiMUf_aUkGhPDLS8JPUDN2xAACGyAAAu3pqErpL8JlA9wlRS8E', 'CAACAgIAAxkBAAEI3aJkVRLRZW0uwbGGqsmnIH9Ik2T3LwACRCEAAqHmqUo-nP7mtSkC6S8E', 'CAACAgIAAxkBAAEI3aRkVRMDWXedwbHNWQzeJ8qfAZSHewACdRMAAgzg8Eu-uLkEJBHvxi8E']

def feed():
    global satiety, energy
    satiety += 10
    energy += 5

def play():
    global satiety, happiness
    satiety -= 5
    energy -= 10
    happiness += 10

def sleep():
    global satiety, happiness
    satiety -= 5
    happiness -= 5
    energy = 70


def check():
    global satiety, energy, happiness
    if satiety <= 0:
        bot.send_message(message.chat.id, f'{name} умер от голода. Не забывайте кормить своего питомца!')

    elif satiety >= 10:
        bot.send_message(message.chat.id, f'{name} наелся и счастлив.')
    if happiness < 0:
        bot.send_message(message.chat.id, f'{name} умер от тоски. С питомцем нужно чаще играть!')
    elif happiness > 100:
        bot.send_message(message.chat.id, f'{name} счастлив как никогда.')
    if energy < 70:
        bot.send_message(message.chat.id, f'{name} умер от истощения.')
    elif energy > 70:
        bot.send_message(message.chat.id, f'{name} полон сил и энергии!')

@bot.message_handler(commands=['feed'])
def feed_handler(message):
    feed()
    bot.send_message(message.chat.id, f'{name} вкусно покушал и теперь его голод составляет {satiety}!')
    check()

@bot.message_handler(commands=['play'])
def play_handler(message):
    play()
    bot.send_message(message.chat.id, f'{name} славно поиграл и теперь его счастье составляет {happiness}!')
    check()

@bot.message_handler(commands=['sleep'])
def sleep_handler(message):
    sleep()
    bot.send_message(message.chat.id, f'{name} выспался и его энергия равна {energy}!')
    check()

@bot.message_handler(commands=['стикер'])
def sticker_handler(message):
    global happiness
    if happiness < 20:
        bot.send_message(message.chat.id, 'Мне скучно, поиграй со мной!')
        bot.send_sticker(message.chat.id, 'CAACAgIAAxkBAAEI3XxkVQs1e632dNpuOqbhtUUcdie5hgACDCEAAvKkyUhwuUsR4bLTSS8E')
    elif happiness > 20:
        bot.send_message(message.chat.id, 'ыфвфыаываввпырпыварвапырврвыпвпрвпаыр')
        bot.send_sticker(message.chat.id, 'CAACAgIAAxkBAAEI3X5kVQvUaCxXi7i7FZKedGl9Lzsc9gACoxYAAlHtkUiboLBaPJUQ2S8E')
@bot.message_handler()
def random_sticker_handler(message):
    if message.text == "Отправь рандомный стикер":
        bot.send_sticker(message.chat.id, choice(stickers))
bot.polling()


