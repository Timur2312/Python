from datetime import datetime as dt

def temperature_logger(data):
    time = dt.now().strftime('%H:%M')
    with open('log.txt','a') as file:
        file.write(f'{time};temperature;{data}\n')

def preassure_logger(data):
    time = dt.now().strftime('%H:%M')
    with open('log.txt','a') as file:
        file.write(f'{time};pressure;{data}\n')

def wind_speed_logger(data):
    time = dt.now().strftime('%H:%M')
    with open('log.txt','a') as file:
        file.write(f'{time};wind_speed;{data}\n')