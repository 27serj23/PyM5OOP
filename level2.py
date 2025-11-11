# Уровень 2.
# Создайте класс точка Point, позволяющий работать с
# координатами (x, y). Добавьте необходимые методы класса.
class Point:
    def __init__(self, x=0, y=0): # параметры x, y, задают координаты точки
        self.x = x
        self.y = y
    # методы для изменения координат
    def set_x(self, new_x):
        self.x = new_x

    def set_y(self, new_y):
        self.y = new_y
    # методы для отдельного извлечения текущих координат
    def get_x(self):
        return self.x

    def get_y(self):
        return self.y
    # метод, который выводит полную информацию о точке
    def info(self):
        return f"Point(x={self.x}, y={self.y})"
# точка с заданными координатами
point = Point(3, 4)

print(point.info())
# меняем координаты
point.set_x(-1)
point.set_y(7)

print(point.info())
# проверяем получение отдельных координат
print("X:", point.get_x())
print("Y:", point.get_y())



