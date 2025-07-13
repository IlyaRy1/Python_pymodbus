print("Начинается настройка подключения к modbus tcp slave device") # Вывод в консоль сообщение о начале интерпретации
from pymodbus.client import ModbusTcpClient # Подключение библиотеки pymodbus
clientIP = '127.0.0.1' # IP-адрес сервера
client = ModbusTcpClient(host = clientIP) # Создание клиента modbus tcp, параметр в скобках - [(хост, к которому подключаемся)]
client.connect() # Подключение к серверу modbus tcp
print("Подключение установлено")

## Операции modbus, начало
print("Запись coil начинается")
client.write_coil(address = 0, value = True, slave = 1)
client.write_coil(address = 5, value = True, slave = 1)
print("Запись coil выполнена успешно")

print("Запись holding register начинается")
client.write_register(address = 0, value = 12, slave = 1)
client.write_register(address = 5, value = 606, slave = 1)
print("Запись holding register выполнена успешно")

## Операции modbus, конец

client.close() # Закрыть соединение

print("Соединение успешно отключено") # Вывод в консоль сообщение о конце интерпретации