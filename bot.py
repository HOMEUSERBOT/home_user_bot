from pyrogram import Client, filters, idle
from pyrogram.errors import FloodWait
from pyrogram.types import ChatPermissions, Message, InlineKeyboardMarkup, InlineKeyboardButton, ReplyKeyboardMarkup
from time import sleep, perf_counter
from pyrogram.handlers import MessageHandler
from covid import Covid
import time, random, datetime, asyncio, sys, wikipedia, requests, os

# Для логов уберите знак "#"  ниже
import logging
 
app = Client("my_account")

print("""
██╗░░██╗░█████╗░███╗░░░███╗███████╗  
██║░░██║██╔══██╗████╗░████║██╔════╝  
███████║██║░░██║██╔████╔██║█████╗░░  
██╔══██║██║░░██║██║╚██╔╝██║██╔══╝░░  
██║░░██║╚█████╔╝██║░╚═╝░██║███████╗  
╚═╝░░╚═╝░╚════╝░╚═╝░░░░░╚═╝╚══════╝  

██╗░░░██╗░██████╗███████╗██████╗░  ██████╗░░█████╗░████████╗
██║░░░██║██╔════╝██╔════╝██╔══██╗  ██╔══██╗██╔══██╗╚══██╔══╝
██║░░░██║╚█████╗░█████╗░░██████╔╝  ██████╦╝██║░░██║░░░██║░░░
██║░░░██║░╚═══██╗██╔══╝░░██╔══██╗  ██╔══██╗██║░░██║░░░██║░░░
╚██████╔╝██████╔╝███████╗██║░░██║  ██████╦╝╚█████╔╝░░░██║░░░
░╚═════╝░╚═════╝░╚══════╝╚═╝░░╚═╝  ╚═════╝░░╚════╝░░░░╚═╝░░░
Telegram Канал - @homeland_restored
Помощь - @klarlex
Логи:""")

# Команда type
@app.on_message(filters.command("type", prefixes=".") & filters.me)
def type(_, msg):
    orig_text = msg.text.split(".type ", maxsplit=1)[1]
    text = orig_text
    tbp = "" # to be printed
    typing_symbol = "▒"
 
    while(tbp != orig_text):
        try:
            msg.edit(tbp + typing_symbol)
            sleep(0.05) # 50 ms
 
            tbp = tbp + text[0]
            text = text[1:]
 
            msg.edit(tbp)
            sleep(0.05)
 
        except FloodWait as e:
            sleep(e.x)
    # Помощь
@app.on_message(filters.command("help" , prefixes=".") & filters.me)
def hack(_, msg):
    msg.edit("""home userbot!
КОММАНДЫ
Основные:
.help - Помощь
.covid [Страна] - Статистика заражения вирусом covid-19 [Коронавирус]
.weather погода!
.ping - пинг
Процент загрузки:
.hack - Взлом Пентагонна
.jopa - Взлом жопы
Плюшки:
.type - Эффект Печати
Если нужна помощь, пиши @klarlex""")
 
# Команда взлома пентагона
@app.on_message(filters.command("hack", prefixes=".") & filters.me)
def hack(_, msg):
    perc = 0
 
    while(perc < 100):
        try:
            text = "👮‍ Взлом пентагона в процессе ..." + str(perc) + "%"
            msg.edit(text)
 
            perc += random.randint(1, 3)
            sleep(0.1)
 
        except FloodWait as e:
            sleep(e.x)
 
    msg.edit("🟢 Пентагон успешно взломан!")
    sleep(3)
 
    msg.edit("👽 Поиск секретных данных об НЛО ...")
    perc = 0
 
    while(perc < 100):
        try:
            text = "👽 Поиск секретных данных об НЛО ..." + str(perc) + "%"
            msg.edit(text)
 
            perc += random.randint(1, 5)
            sleep(0.15)
 
        except FloodWait as e:
            sleep(e.x)
 
    msg.edit("🦖 Найдены данные о существовании динозавров на земле!")
 
@app.on_message(filters.command("thanos", prefixes=".") & filters.me)
def thanos(_, msg):
    chat = msg.text.split(".thanos ", maxsplit=1)[1]
 
    members = [
        x
        for x in app.iter_chat_members(chat)
        if x.status not in ("administrator", "creator")
    ]
 
    random.shuffle(members)
 
    app.send_message(chat, "Щелчок Таноса ... *щёлк*")
 
    for i in range(len(members) // 2):
        try:
            app.restrict_chat_member(
                chat_id=chat,
                user_id=members[i].user.id,
                permissions=ChatPermissions(),
                until_date=int(time.time() + 86400),
            )
            app.send_message(chat, "Исчез " + members[i].user.first_name)
        except FloodWait as e:
            print("> waiting", e.x, "seconds.")
            time.sleep(e.x)
 
    app.send_message(chat, "Но какой ценой?")
  
# Covid
@app.on_message(filters.command("covid", prefixes=".") & filters.me)
async def covid_local(client: Client, message: Message):
    region = ' '.join(message.command[1:])
    await message.edit('<code>Загрузка...</code>')
    covid = Covid(source="worldometers")
    try:
        local_status = covid.get_status_by_country_name(region)
        await message.edit("<b>=======🦠 COVID-19 STATUS 🦠=======</b>\n" +
                           f"<b>Регион [Страна]</b>: <code>{local_status['country']}</code>\n" +
                           "<b>====================================</b>\n" +
                           f"<b>🤧 Новые заражения</b>: <code>{local_status['new_cases']}</code>\n" +
                           f"<b>😷 Новые смерти</b>: <code>{local_status['new_deaths']}</code>\n" +
                           "<b>====================================</b>\n" +
                           f"<b>😷 Подтверждённые</b>: <code>{local_status['confirmed']}</code>\n" +
                           f"<b>❗️ Активные [Заражённые]:</b> <code>{local_status['active']}</code>\n" +
                           f"<b>⚠️ Критически</b>: <code>{local_status['critical']}</code>\n" +
                           f"<b>💀 Смертей</b>: <code>{local_status['deaths']}</code>\n" +
                           f"<b>🚑 Спасенно [Вылеченно]</b>: <code>{local_status['recovered']}</code>\n")
    except ValueError:
        await message.edit(f'<code>There is no region called "{region}"</code>')
      
# Информация про бота
@app.on_message(filters.command("info" , prefixes=".") & filters.me)
def hack(_, msg):
    msg.edit("home userbot\nVersion 0.0.0.0\nCreator @klarlex")
  
@app.on_message(filters.command("ping", prefixes=".") & filters.me)
async def ping(client: Client, message: Message):
    start = perf_counter()
    await message.edit('Pong')
    end = perf_counter()
    ping = end - start
    await message.edit(f'<b>🏓 Понг \n📶</b><code> {round(ping, 3)}МС</code>')
    
    # Погода
def get_pic(city):
    file_name = f'{city}.png'
    with open(file_name, 'wb') as pic:
        response = requests.get('http://wttr.in/{citys}_2&lang=rus.png', stream=True)

        if not response.ok:
            print(response)

        for block in response.iter_content(1024):
            if not block:
                break

            pic.write(block)
        return file_name

@app.on_message(filters.command("weather", prefixes=".") & filters.me)
async def weather(client: Client, message: Message):
    city = message.command[1]
    await message.edit("```Processing the request...```")
    r = requests.get(f"https://wttr.in/{city}?m?M?0?q?T&lang=en")
    await message.edit(f"```City: {r.text}```")
    await client.send_document(chat_id=message.chat.id, document=get_pic(city), reply_to_message_id=message.message_id)
    os.remove(f'{city}.png')
                
app.run()
