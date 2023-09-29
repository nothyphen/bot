#!/usr/bin/python

class Validator():
    def weather(name):
        if name in ('Sun', 'Sunny', 'Clear', 'Clear with periodic clouds'):
            return "☀️ افتابی"
        
        elif name in ('Rain', 'Chance of Rain', 'Light Rain', 'Showers', 'Scattered Showers', 'Rain and Snow', 'Hail'):
            return "🌧️ بارانی"

        elif name in ('Scattered Thunderstorms', 'Chance of Storm', 'Storm', 'Thunderstorm', 'Chance of TStorm'):
            return "⛈️ رعد و برق"

        elif name in ('Mist','Dust','Fog','Smoke','Haze','Flurries'):
            return "🌫️ مه آلود"

        elif name in ('Freezing Drizzle', 'Chance of Snow', 'Sleet', 'Snow', 'Icy','Snow Showers'):
            return "🌨️ برفی"
        
        elif name in ('Partly sunny', 'Mostly sunny', 'Partly cloudy', 'Mostly cloudy', 'Cloudy', 'Overcast') :
            return "⛅ افتابی"

    def date(day):
        s1 = day.split(" ")

        if s1[0] in ('Saturday'):
            return "شنبه"+" "+s1[1]
        elif s1[0] in ('Sunday'):
            return "یکشنبه"+" "+s1[1]
        elif s1[0] in ('Monday'):
            return "دوشنبه"+" "+s1[1]
        elif s1[0] in ('Tuesday'):
            return "سه شنبه"+" "+s1[1]
        elif s1[0] in ('Wednesday'):
            return "چهارشنبه"+" "+s1[1]
        elif s1[0] in ('Thursday'):
            return "پنجشنبه"+" "+s1[1]