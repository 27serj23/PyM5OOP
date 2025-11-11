# Уровень 1.
# Создайте класс StringVar для работы со строковым типом данных,
# содержащий методы set() и get().
# Метод set() служит для изменения содержимого строки,
# get() – для получения содержимого строки.
# Создайте объект типа StringVar и протестируйте его методы.
class StringVar:
    def __init__(self, initial_value=""):
        self._value = initial_value # закрытый атрибут, будет содержать строковое значение

    def set(self, new_value): # метод set(), позволит установить новое значение строки
        self._value = new_value

    def get(self): # get(), возвращает текущее значение строки
        return self._value
# тестируем класс
my_string_var = StringVar("Hello")
print(my_string_var.get())

my_string_var.set("World")
print(my_string_var.get())
# Вывод:
# Hello
# World

