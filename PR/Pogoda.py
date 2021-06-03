import pyowm
owm = pyowm.OWM('31f9b342c3a37938fdb4e96d053e78e4')
mgr = owm.weather_manager()
place = input('Введите место: ')
observation = mgr.weather_at_place(place)
w = observation.weather
print(w)