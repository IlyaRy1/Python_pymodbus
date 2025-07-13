'''
Разные ID слэйвов при одном ip-адресе могут быть при использовании шлюза Modbus TCP <-> Modbus RTU/ASCII
Шлюз (Gateway) - устройство/ПО, обеспечивающее взаимодействие между разными сетями/протоколами
Прим.: устройства на rs-485 имеют свои адреса (1,2,3,...); шлюз имеет один ip, но перенаправляет запросы на нужный слэйв по ID
Ещё разные ID слэйвов могут быть при использовании нескольких виртуальных слэйвов на одном хосте

Для (всех):
Параметры в скобках - [(адрес, с которого начинаем считывать), опция_(число катушек к считыванию), опция_(ID слэйва)]

Для (катушек) и (дискретных входов):
При 1 <= count <= (X) формируется список из (Z) = (X) + (Y) элементов
(Y) - необходимое количество дополнительных элементов, необходимых до достижения количества элементов (Z) кратному восьми
Первые count элементов соответствуют регистрам слэйва
Остальные = False
При count > определяемого числа регистров формируется пустой список
Значение count должно быть от 1 до 2000, иначе ошибка ValueError

Для (удерживающих регистров) и (входных регистров):
При count = (Z) формируется список из (Z) элементов, соответствующих регистрам слэйва
При count > определяемого числа регистров формируется пустой список
Значение count должно быть от 1 до 125, иначе ошибка ValueError
Возможное значение регистров слэйва: от -32767 до 32767
Если значение регистра (Y) отрицательное, то оно считывается как (X)=65536+(Y)
'''
# Синхронный пример

print("Start of code") # Вывод в консоль сообщение о начале интерпретации

## Настройка, начало
from pymodbus.client import ModbusTcpClient # Подключение библиотеки pymodbus
clientIP = '127.0.0.1' # IP-адрес сервера
client = ModbusTcpClient(host = clientIP) # Создание клиента modbus tcp, параметр в скобках - [(хост, к которому подключаемся)]
client.connect() # Подключение к серверу modbus tcp
## Настройка, конец

## Операции modbus, начало
print("\nКатушки:") # Работа с coils
info_coils1 = client.read_coils(address = 0, count = 8, slave = 1) # Получение информации с сервера о регистрах coils
info_coils2 = client.read_coils(address = 2000, count = 10, slave = 1) # Получение информации с сервера о регистрах coils
print(info_coils1.bits) # Вывод сформированного списка 1 в консоль
print(info_coils2.bits) # Вывод сформированного списка 2 в консоль

print("\nДискретные входы:") # Работа с discrete inputs
info_discrete_inputs1 = client.read_discrete_inputs(address = 0, count = 8, slave = 1) # Получение информации с сервера о регистрах discrete inputs
info_discrete_inputs2 = client.read_discrete_inputs(address = 2000, count = 10, slave = 1) # Получение информации с сервера о регистрах discrete inputs
print(info_discrete_inputs1.bits) # Вывод сформированного списка в консоль
print(info_discrete_inputs2.bits) # Вывод сформированного списка в консоль

print("\nУдерживающие регистры:") # Работа с  регистрами holding registers
info_holding_registers1 = client.read_holding_registers(address = 0, count = 5, slave = 1) # Получение информации с сервера о регистрах holding registers
info_holding_registers2 = client.read_holding_registers(address = 125, count = 125, slave = 1) # Получение информации с сервера о регистрах holding registers
print(info_holding_registers1.registers) # Вывод сформированного списка в консоль
print(info_holding_registers2.registers) # Вывод сформированного списка в консоль

print("\nВходные регистры:") # Работа с регистрами input registers
info_input_registers1 = client.read_input_registers(address = 0, count = 5, slave = 1) # Получение информации о регистрах input registers
info_input_registers2 = client.read_input_registers(address = 125, count = 125, slave = 1) # Получение информации о регистрах input registers
print(info_input_registers2.registers) # Вывод сформированного списка в консоль
print(info_input_registers1.registers) # Вывод сформированного списка в консоль
## Операции modbus, конец

client.close() # Закрыть соединение

print("\nEnd of code") # Вывод в консоль сообщение о конце интерпретации
