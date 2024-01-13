import aiogram
import os
import random
from aiogram import types
from aiogram.dispatcher.filters import Command
from stt import speak
from answersall import answers


# подключение ключей к опенаи и телеге
# dp = Dispatcher(bot)
bot = aiogram.Bot('5901628369:AAHvKAuDi0s0Y03uWbRyzinMHI2u400So40')
dp = aiogram.Dispatcher(bot)


# функция для получения цитаты из текстового файла

def generate_quote1(filename):
    # открываем файл
    with open('ucheniedx.txt', encoding='utf-8') as f:
        # считываем весь текст
        text = f.read()
        # разбиваем текст на предложения
        sentences = text.split('.')
        # выбираем случайное число предложений из текста"
        n = random.randint(1, 15)
        # выбираем случайное место в тексте
        start = random.randint(0, len(sentences) - n - 1)
        # выбираем n предложений из текста, начиная с выбранного места
        quote = '.'.join(sentences[start:start + n])
        return quote


def generate_quote2(filename):
    # открываем файл
    with open('serap.txt', encoding='utf-8') as f:
        # считываем весь текст
        text = f.read()
        # разбиваем текст на предложения
        sentences = text.split('.')
        # выбираем случайное число предложений из текста
        n = random.randint(1, 15)
        # выбираем случайное место в тексте
        start = random.randint(0, len(sentences) - n - 1)
        # выбираем n предложений из текста, начиная с выбранного места
        quote = '.'.join(sentences[start:start + n])
        return quote


def generate_quote3(filename):
    # открываем файл
    with open('xtlan.txt', encoding='utf-8') as f:
        # считываем весь текст
        text = f.read()
        # разбиваем текст на предложения
        sentences = text.split('.')
        # выбираем случайное число предложений из текста
        n = random.randint(1, 15)
        # выбираем случайное место в тексте
        start = random.randint(0, len(sentences) - n - 1)
        # выбираем n предложений из текста, начиная с выбранного места
        quote = '.'.join(sentences[start:start + n])
        return quote


def generate_quote4(filename):
    # открываем файл
    with open('skazkiosile.txt', encoding='utf-8') as f:
        # считываем весь текст
        text = f.read()
        # разбиваем текст на предложения
        sentences = text.split('.')
        # выбираем случайное число предложений из текста
        n = random.randint(1, 15)
        # выбираем случайное место в тексте
        start = random.randint(0, len(sentences) - n - 1)
        # выбираем n предложений из текста, начиная с выбранного места
        quote = '.'.join(sentences[start:start + n])
        return quote


def generate_quote5(filename):
    # открываем файл
    with open('2ring.txt', encoding='utf-8') as f:
        # считываем весь текст
        text = f.read()
        # разбиваем текст на предложения
        sentences = text.split('.')
        # выбираем случайное число предложений из текста
        n = random.randint(1, 15)
        # выбираем случайное место в тексте
        start = random.randint(0, len(sentences) - n - 1)
        # выбираем n предложений из текста, начиная с выбранного места
        quote = '.'.join(sentences[start:start + n])
        return quote


def generate_quote6(filename):
    # открываем файл
    with open('darorla.txt', encoding='utf-8') as f:
        # считываем весь текст
        text = f.read()
        # разбиваем текст на предложения
        sentences = text.split('.')
        # выбираем случайное число предложений из текста
        n = random.randint(1, 15)
        # выбираем случайное место в тексте
        start = random.randint(0, len(sentences) - n - 1)
        # выбираем n предложений из текста, начиная с выбранного места
        quote = '.'.join(sentences[start:start + n])
        return quote

def generate_quote7(filename):
    # открываем файл
    with open('firewithin.txt', encoding='utf-8') as f2:
        # считываем весь текст
        text = f2.read()
        # разбиваем текст на предложения
        sentences = text.split('.')
        # выбираем случайное число предложений из текста
        n = random.randint(1, 15)
        # выбираем случайное место в тексте
        start = random.randint(0, len(sentences) - n - 1)
        # выбираем n предложений из текста, начиная с выбранного места
        quote = '.'.join(sentences[start:start + n])
        return quote


def generate_quote8(filename):
    # открываем файл
    with open('bezmolvie.txt', encoding='utf-8') as f:
        # считываем весь текст
        text = f.read()
        # разбиваем текст на предложения
        sentences = text.split('.')
        # выбираем случайное число предложений из текста
        n = random.randint(1, 15)
        # выбираем случайное место в тексте
        start = random.randint(0, len(sentences) - n - 1)
        # выбираем n предложений из текста, начиная с выбранного места
        quote = '.'.join(sentences[start:start + n])
        return quote


def generate_quote9(filename):
    # открываем файл
    with open('artofdream.txt', encoding='utf-8') as f:
        # считываем весь текст
        text = f.read()
        # разбиваем текст на предложения
        sentences = text.split('.')
        # выбираем случайное число предложений из текста
        n = random.randint(1, 15)
        # выбираем случайное место в тексте
        start = random.randint(0, len(sentences) - n - 1)
        # выбираем n предложений из текста, начиная с выбранного места
        quote = '.'.join(sentences[start:start + n])
        return quote


def generate_quote10(filename):
    # открываем файл
    with open('activeside.txt', encoding='utf-8') as f:
        # считываем весь текст
        text = f.read()
        # разбиваем текст на предложения
        sentences = text.split('.')
        # выбираем случайное число предложений из текста
        n = random.randint(1, 15)
        # выбираем случайное место в тексте
        start = random.randint(0, len(sentences) - n - 1)
        # выбираем n предложений из текста, начиная с выбранного места
        quote = '.'.join(sentences[start:start + n])
        return quote


def generate_quote11(filename):
    # открываем файл
    with open('koleso.txt', encoding='utf-8') as f:
        # считываем весь текст
        text = f.read()
        # разбиваем текст на предложения
        sentences = text.split('.')
        # выбираем случайное число предложений из текста
        n = random.randint(1, 15)
        # выбираем случайное место в тексте
        start = random.randint(0, len(sentences) - n - 1)
        # выбираем n предложений из текста, начиная с выбранного места
        quote = '.'.join(sentences[start:start + n])
        return quote


def generate_quote12(filename):
    # открываем файл
    with open('passii.txt', encoding='utf-8') as f:
        # считываем весь текст
        text = f.read()
        # разбиваем текст на предложения
        sentences = text.split('.')
        # выбираем случайное число предложений из текста
        n = random.randint(1, 15)
        # выбираем случайное место в тексте
        start = random.randint(0, len(sentences) - n - 1)
        # выбираем n предложений из текста, начиная с выбранного места
        quote = '.'.join(sentences[start:start + n])
        return quote

def generate_quote13(filename):
    # открываем файл
    with open('randomjaunteaching.txt', encoding='utf-8') as f:
        # считываем весь текст
        text = f.read()
        # разбиваем текст на предложения
        sentences = text.split('.')
        # выбираем случайное число предложений из текста
        n = random.randint(1, 17)
        # выбираем случайное место в тексте
        start = random.randint(0, len(sentences) - n - 1)
        # выбираем n предложений из текста, начиная с выбранного места
        quote = '.'.join(sentences[start:start + n])
        return quote


async def magic_ball(message: types.Message):
    answer = random.choice(answers)
    speak(answer)
    with open('hello.mp3', 'rb') as f:  
      await bot.send_voice(message.chat.id, f)

async def magic_ball2(message: types.Message):
  answer = random.choice(answers)
  await  message.answer(f'Ответ Духа: {answer}.\n p.s.\nИщи руки во сне!')
    

# Привязываем функцию к команде '/magic_ball'
dp.register_message_handler(magic_ball, Command("0"))
dp.register_message_handler(magic_ball2, Command("?"))  


@dp.message_handler(commands=["start"])
async def start_command(message: types.Message):
    await message.reply("Привет! Я бот-цитатник по книгам Карлоса Кастанеды.\n Я могу отправлять случайные фрагменты из книг:\
    \n 1968г. — Учение дона Хуана - /1 \
    \n 1971г. — Отдельная реальность - /2 \
    \n 1972г. — Путешествие в Икстлан - /3 \
    \n 1974г. — Сказки о силе - /4 \
    \n 1977г. — Второе кольцо силы - /5 \
    \n 1981г. — Дар Орла - /6 \
    \n 1984г. — Огонь изнутри - /7 \
    \n 1987г. — Сила безмолвия - /8 \
    \n 1993г. — Искусство сновидения - /9 \
    \n 1997г. — Активная сторона бесконечности - /10 \
    \n 1998г. — Колесо времени - /11 \
    \n 1998г. — Магические пассы - /12 \
    \n___________________________________\
    \n Абсолютный рандом поробуй сам угадать откуда - /13 \
    \n___________________________________\
    \n Напиши /1-/13 чтобы получить свою цитату от Духа.\
    \n___________________________________\
    \n Чтобы получить совет от духа, задай вопрос, а затем напиши /0 либо /?.")

    # обработчик команды /q

@dp.message_handler(commands=['1'])
async def send_quote1(message: aiogram.types.Message):
    # получаем случайную цитату из текстового файла
    quote = generate_quote1('text.txt')
    # отправляем цитату пользователю
    await message.answer(f'Вот тебе случайная цитата из книги "Учения Дона Хуана" воин:\n"{quote}. \n p.s.\nИщи руки во сне!"')


@dp.message_handler(commands=['2'])
async def send_quote2(message: aiogram.types.Message):
    # получаем случайную цитату из текстового файла
    quote = generate_quote2('text.txt')
    # отправляем цитату пользователю
    await message.answer(f'Вот тебе случайная цитата из книги "Отдельная реальность" воин:\n"{quote}.\n p.s.\nИщи руки во сне!"')


@dp.message_handler(commands=['3'])
async def send_quote3(message: aiogram.types.Message):
    # получаем случайную цитату из текстового файла
    quote = generate_quote3('text.txt')
    # отправляем цитату пользователю
    await message.answer(f'Вот тебе случайная цитата из книги "Путешествие в Икстлан" воин:\n"{quote}. \n p.s.\nИщи руки во сне!"')


@dp.message_handler(commands=['4'])
async def send_quote4(message: aiogram.types.Message):
    # получаем случайную цитату из текстового файла
    quote = generate_quote4('text.txt')
    # отправляем цитату пользователю
    await message.answer(f'Вот тебе случайная цитата из книги "Сказки силе" воин:\n"{quote}. \n p.s.\nИщи руки во сне!"')


@dp.message_handler(commands=['5'])
async def send_quote5(message: aiogram.types.Message):
    # получаем случайную цитату из текстового файла
    quote = generate_quote5('text.txt')
    # отправляем цитату пользователю
    await message.answer(f'Вот тебе случайная цитата из книги "Второе кольцо силы" воин:\n"{quote}. \n p.s.\nИщи руки во сне!"')


@dp.message_handler(commands=['6'])
async def send_quote6(message: aiogram.types.Message):
    # получаем случайную цитату из текстового файла
    quote = generate_quote6('text.txt')
    # отправляем цитату пользователю
    await message.answer(f'Вот тебе случайная цитата из книги "Дар орла" воин:\n"{quote}. \n p.s.\nИщи руки во сне!"')


@dp.message_handler(commands=['7'])
async def send_quote7(message: aiogram.types.Message):
    # получаем случайную цитату из текстового файла
    quote = generate_quote7('text.txt')
    # отправляем цитату пользователю
    await message.answer(f'Вот тебе случайная цитата из книги "Огонь изнутри" воин:\n"{quote}. \n p.s.\nИщи руки во сне!"')


@dp.message_handler(commands=['8'])
async def send_quote8(message: aiogram.types.Message):
    # получаем случайную цитату из текстового файла
    quote = generate_quote8('text.txt')
    # отправляем цитату пользователю
    await message.answer(f'Вот тебе случайная цитата из книги "Сила безмолвия" воин:\n"{quote}.\n p.s.\nИщи руки во сне!"')

@dp.message_handler(commands=['9'])
async def send_quote9(message: aiogram.types.Message):
    # получаем случайную цитату из текстового файла
    quote = generate_quote9('text.txt')
    # отправляем цитату пользователю
    await message.answer(f'Вот тебе случайная цитата из книги "Искусство сновидения" воин:\n"{quote}. \n p.s.\nИщи руки во сне!"')


@dp.message_handler(commands=['10'])
async def send_quote10(message: aiogram.types.Message):
    # получаем случайную цитату из текстового файла
    quote = generate_quote10('text.txt')
    # отправляем цитату пользователю
    await message.answer(f'Вот тебе случайная цитата из книги "Активная сторона бесконечности" воин:\n"{quote}. \n p.s.\n Ищи руки во сне!"')


@dp.message_handler(commands=['11'])
async def send_quote11(message: aiogram.types.Message):
    # получаем случайную цитату из текстового файла
    quote = generate_quote11('text.txt')
    # отправляем цитату пользователю
    await message.answer(f'Вот тебе случайная цитата из книги "Колесо времени" воин:\n"{quote}. \n p.s.\nИщи руки во сне!"')


@dp.message_handler(commands=['12'])
async def send_quote12(message: aiogram.types.Message):
    # получаем случайную цитату из текстового файла
    quote = generate_quote12('text.txt')
    # отправляем цитату пользователю
    await message.answer(f'Вот тебе случайная цитата из книги "Магические пассы" воин:\n"{quote}. \n p.s.\nИщи руки во сне!"')

@dp.message_handler(commands=['13'])
async def send_quote13(message: aiogram.types.Message):
    # получаем случайную цитату из текстового файла
    quote = generate_quote13('text.txt')
    # отправляем цитату пользователю
    await message.answer(f'Вот тебе абсолютли рандомная цитата от Кастанеды, попытайся сам понять откуда она взята, воин:\n"{quote}. \n p.s.\nИщи руки во сне!"')



# запускаем бота
if __name__ == '__main__':
    aiogram.executor.start_polling(dp, skip_updates=True)

bot.polling(non_stop=True, interval=0)  # запуск бота