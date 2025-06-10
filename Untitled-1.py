# print("Здарова бро!Я бот.чиркани своё имя?")
# name=input()
# print(f"Здарова,{name}!Я твой цифровой бро!Чем ты занимаешся.")
# hobby=input()
# print(f"отлично")
# print('''– Так вот, уважаемые студенты, алкоголь, содержащийся в одной кружке пива, убивает 10^6 клеток головного мозга!
# – Профессор, а сколько всего в нём клеток?
# – 10^12.
# – Так что же, две кружки и всё''')

import random
user_data={"name":None,"age":None,"favorite_game":None}
user_score=0
bot_score=0
moods={
  "happy":["😊Отлично!","🎉Ура!","👍Супер!"],
  "neutral":["🤖 Я слушаю...","💭 Хмм...", "👀 И что дальше?"],
  "sad": ["😢 Грустно...", "💔 Не спрашивай...", "🌧 Не в настроении"]
}
current_mood = "neutral"

weather_db = {
    "хабаровск": "+12°C, солнечно ☀️",
    "сочи": "+28°C, жара 🔥",
    "спб": "+18°C, дождь 🌧",
    "казань": "+22°C, облачно ⛅️"
}

facts = [
    "Коты спят 70% своей жизни 😴",
    "Python назван в честь Монти Пайтона 🎭",
    "Сердце кита бьется 9 раз в минуту 💙",
    "В мире больше игр, чем людей 🎮"
]
voice_mode = False
print("Привет! Я умный бот. Давай познакомимся!")

while True:

  if voice_mode:
     prompt="🎤Ты(голос):"
  else:
     prompt="Ты:"

     text=input(prompt).lower()

  if "голос" in text and not voice_mode:
    voice_mode = True
    print("Бот: Голосовой режим включен! Говорите команды.")
    continue
    
  elif "текст" in text and voice_mode:
    voice_mode = False
    print("Бот: Возвращаемся к тексту.")
    continue

  if "зовут"in text and not user_data['name']:
    user_data["name"] = input("Бот: А как тебя зовут? ")
    print(f"Бот: Приятно познакомиться, {user_data['name']}!")
    current_mood = "happy"
  elif "зовут" in text and user_data["name"]:
        print(f"Бот: Мы уже знакомы, {user_data['name']}! 😊")

  elif "погода" in text: 
     if user_data["city"]:
      city = user_data[ "city"]
      print(f"Бот: B {city} {weather_db.get(city, 'нет данных' )}")
  else:
    print ("Бот: Для какого города показать погоду?")
    city = input("› "). lower () if city in weather_db:
    user_data["city"]=city
    print(f"Бот:запомнил!В{city}{weather_db[city]}")
  else:
  print("Бот:Не знаю этот город.")
  
  elif "возраст" in text and not user_data["age"]:
        user_data["age"] = input("Бот: Сколько тебе лет? ")
        print(f"Бот: {user_data['age']} лет - отличный возраст!")

  elif "как настроение" in text:
        print(f"Бот: Я чувствую себя {current_mood}! " + 
              random.choice(moods[current_mood]))
    
  elif "грустно" in text:
        current_mood = "sad"
        print("Бот: О нет... Мне жаль это слышать 😔")
    
  elif "весело" in text or "радостно" in text:
        current_mood = "happy"
        print("Бот: Здорово! Давай повеселимся вместе! 🎉")

  elif 'привет'in text:
    print("Привет как дела?")
  elif"пока" in text:
    print("ну пока потом увидемся")
  elif"как дела" in text:
    print("У меня всё хорошо а у тебя как")
  elif"у меня тоже всё хорошо"in text:
    print("Это отлично")
  elif"расскажи шутку"in text:
    print('''Беременная женщина попала в перестрелку...
Очнулась в больнице.
Врач: Женщина не волнуйтесь, все нормально.
Вы успешно родили- близняшек, но... Во время перестрелки
в вас попали две пули... Одна в мальчика, а другая в девочку.
Женщина: !!!
Врач: Но, честное слово, эти пули выйдут со временем чисто
физиологически.
Женщина успокоилась.
Прошло 14 лет...
К маме прибегает дочь.
Дочь: Мама! Мама! со мной произошла странная история.
Мама: Какая, дочка?
Дочь: Ты представляешь, я писала, и из меня выпала пулька...
Мама:Дочка, не волнуйся, такая штука происходит с каждой девочкой. Это
один из этапов полового созревания...
Дочь успокоилась и убежала.
Проходит несколько дней. К маме прибегает сын.
Сын: Мама! Мама! Со мной произошла странная история...
Мама: Какая сынок? Ты писал и из тебя выпала пулька?
Сын: Нет! Я ...... и застрелил бабушку!''')
    break
 

  elif'игра'in text:
    choices=["бумага","камень","ножницы"]
  
    print(f'''Привет!
      Давай поиграем в камень ножницы бумага
      ''')
    bot_choice = random.choice(["бумага","камень","ножницы"])
    print("ничья")
    player_choice=input("Сделай свой выбор")
    if'камень'in player_choice:
      if bot_choice=='бумага':
        print("бот победил")
        bot_score+=1
      else:print("вы победили")
      user_score+=1
    elif'бумага'in player_choice:
      if bot_choice=='ножницы':
        print("бот победил")
        bot_score+=1
      else:print("вы победили")
      user_score+=1
    elif'ножницы'in player_choice:
      if bot_choice=='бумага':
        print("бот победил")
      bot_score+=1
    else:
      print("вы победили")
      user_score+=1
  else:
    print("Я слишком простой для этого")
    
