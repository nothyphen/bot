#!/usr/bin/python

from aiogram import Bot, Dispatcher, executor, types
from Pkg.searcher import Models
from Pkg.chatGPT import ModelsBot
from Pkg.weather import ModelsWeather
from Pkg.validator import Validator
from Pkg.information import Information
from Pkg.translator import Translate
from Pkg.trip import Trip
from Pkg.usd import Dollor

API_TOKEN = '6616867385:AAErvY2hPqKeavUrTgfq1Zk8LAEpr4RZ9DI'

bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)

@dp.message_handler(content_types=['text'])
async def give(message: types.Message):
    #msg = message.text.lower().replace(' ', '')
    msg = message.text

    if "علی" in msg :
         await message.answer("چونکه علی یه کونیه :)")
    
    users = []
    count = 0
    if msg == 'TAG' :
        admins = await bot.get_chat_administrators(chat_id=message.chat.id)
        count += await bot.get_chat_members_count(chat_id=message.chat.id)
        print(count)
        for i in range(count):
                print(i)
                try :
                    users.append("<a href='"+"tg://user?id="+str(admins[i]['user']['id'])+"' >"+ str(admins[i]['user']['username']) +"</a>")
                except IndexError :
                     pass
                eslah = str(users).replace("[", "").replace("]", "").replace('"', "")

        await message.answer(text=eslah, parse_mode="HTML", disable_notification=False)

    if "CHOICE" in msg :
        choices = []
        text = msg.replace("choice", "")
        line = text.splitlines()
        for i in range(len(line) - 1):
            choices.append(line[i+1])
        
        await message.answer_poll(question="انتخاب شما ؟ ", options=choices)
    if msg == "PIN" :
        await bot.pin_chat_message(chat_id=message.chat.id, message_id=message["reply_to_message"]["message_id"], disable_notification=False)
    
    if msg == "UNPIN" :
        await bot.unpin_chat_message(chat_id=message.chat.id, message_id=message["reply_to_message"]["message_id"])

    if msg == "HELP":
        result = Information.info()
        await message.reply(result)

    if "SEARCH" in msg :
        marker = "%"
        info = Models.search(msg)
        reply = []
        temp = []
        for i in info:
            if marker in i:
                temp.append(i)
                reply.append(temp)
                temp = []
            else:
                temp.append(i)
        reply.append(temp)
        
        for i in reply:
            new_msg = f"Product Name : {i[0]} \n\n Product Price : {i[1]} \n\n\n Product Link : {i[2]}"
            await message.answer(new_msg)
    
    if "AI" in msg :
        result = ModelsBot.chatbot(msg)
        await message.reply(result)

    if "WEATHER" in msg :
        result = ModelsWeather.get_weather(msg)
        if result['ok'] == 'no':
            await message.reply("متاسفانه شهر شما یافت نشد")

        persian_weather = Validator.weather(result['weather'])
        persian_time = Validator.date(result['time'])
        new_msg = f"  🌡️ دما  : {result['celsion']} \n 🌬️ سرعت باد  : {result['wind']} \n 💧 رطوبت  : {result['humidity']} \n 🕟 زمان  : {persian_time} \n ☁️ هوا  : {persian_weather}"

        if result['weather'] in ('Sun', 'Sunny', 'Clear', 'Clear with periodic clouds'):
            await message.reply_photo(photo='https://media.istockphoto.com/id/1007768414/photo/blue-sky-with-bright-sun-and-clouds.webp?b=1&s=170667a&w=0&k=20&c=rHd7W8nOPEdKEnuMgpSnfC2OC9B_rwMe1HS7k_d-ORc=', caption=new_msg)

        elif result['weather'] in ('Partly sunny', 'Mostly sunny', 'Partly cloudy', 'Mostly cloudy', 'Cloudy', 'Overcast') :
            await message.reply_photo(photo="https://media.istockphoto.com/id/598222542/photo/sky-background.jpg?s=612x612&w=0&k=20&c=WBAiCExAztT4SzWh4hIgmQwTG7VMJ5o9oObXHszmm8A=", caption=new_msg)

        elif result['weather'] in ('Rain', 'Chance of Rain', 'Light Rain', 'Showers', 'Scattered Showers', 'Rain and Snow', 'Hail'):
            await message.reply_photo(photo='https://media.istockphoto.com/id/1257951336/photo/transparent-umbrella-under-rain-against-water-drops-splash-background-rainy-weather-concept.jpg?b=1&s=612x612&w=0&k=20&c=NqRbz72ha40NZ0TiMzc4cLE2T0frsRsf-AlSOOLgwZ8=', caption=new_msg)

        elif result['weather'] in ('Scattered Thunderstorms', 'Chance of Storm', 'Storm', 'Thunderstorm', 'Chance of TStorm'):
            await message.reply_photo(photo='https://images.pexels.com/photos/1118869/pexels-photo-1118869.jpeg?cs=srgb&dl=pexels-johannes-plenio-1118869.jpg&fm=jpg', caption=new_msg)

        elif result['weather'] in ('Mist','Dust','Fog','Smoke','Haze','Flurries'):
            await message.reply_photo(photo='https://images.pexels.com/photos/45222/forest-fog-nature-winter-45222.jpeg?cs=srgb&dl=pexels-pixabay-45222.jpg&fm=jpg', caption=new_msg)

        elif result['weather'] in ('Freezing Drizzle', 'Chance of Snow', 'Sleet', 'Snow', 'Icy','Snow Showers'):
            await message.reply_photo(photo='https://wallpapercave.com/wp/9uTVIpA.jpg', caption=new_msg)


    if "MEAN" in msg:
        result = Translate.TranslaFarsi(msg)
        await message.reply(result)

    if "TRIP" in msg:
        result = Trip.space(msg)
        await message.reply(result+" کیلومتر")

    if msg == "ارز":
        result = Dollor.check()
        await message.reply(result)

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)