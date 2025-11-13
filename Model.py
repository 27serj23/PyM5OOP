# from email.policy import default
#
# class Post(models.Model):
#     title = models.CharField(max_lenght=100)
#     content = models.TextField()
#     date_posted = models.DateTimeField(default=timezone.now)
#     author = models.ForeignKey(User, on_delete=moels.CASCADE)
#
#     def __str__(self):
#         return self.title
# В Django есть класс Models, от которого наследуются все модели, которые
# вы создаете. В классе models есть метод save, который создает соответствующую
# таблицу в базе данных и сохраняет туда объекты.
# С базами данных вы пока не умеете работать, но умеете работать с json.
# Ваша задача:
# Создайте класс Model, в котором будет метод save. Метод save
# должен создавать словарь со всеми значениями атрибутов класса и записывать его в файл json.
# В данном примере это выглядит так: {'title': 'Какой-то заголовок', ..., 'author': 'какой-то автор'}.
# Все атрибуты класса можно получить следующим образом:
# Out[2]:
# ['_class_',
#  '_delattr_',
#  '_dict_',
#  '_dir_',
#  '_doc_',
#  '_eq_',
#  '_format_',
#  '_ge_',
#  '_getattribute_',
#  '_gt_',
#  '_hash_',
#  '_init_',
#  '_init_subclass_',
#
#  '_le_',
#  '_lt_',
#  '_module_',
#  '_ne_',
#  '_new_',
#  '_reduce_',
#  '_reduce_ex_',
#  '_repr_',
#  '_setattr_',
#  '_sizeof_',
#  '_str_',
#  '_subclasshook_',
#  '_weakref_',
#  'author',
#  'text',
#  'title']
# Или сразу так, получая только пользовательские атрибуты:
# In[5]: list(filter (lambda x : not x.startswith('_'), dir(C1 )))
# Out[5]: ['author', 'text', 'title']
import json
import os


class Model:
    def save(self, filename='data.json'): # метод для сохранения объектов в файл
        try:
            # Проверяем, существует ли файл и не пустой ли он
            if os.path.exists(filename) and os.path.getsize(filename) > 0:
                with open(filename, 'r', encoding='utf-8') as file:
                    existing_data = json.load(file)
            else:
                existing_data = []
        except (FileNotFoundError, json.JSONDecodeError):
            # Если файл отсутствует или его содержание не является допустимым JSON
            existing_data = []

        # Формируем словарь со свойствами текущего объекта (только атрибуты экземпляра)
        data = {}
        for attr in dir(self): # перебираем все атрибуты объекта

            if attr.startswith('_'):# Пропускаем приватные атрибуты и методы
                continue
            value = getattr(self, attr)# получаем значение атрибута
            # Пропускаем callable объекты (методы)
            if not callable(value):
                data[attr] = value

        existing_data.append(data)# Добавляем новую запись в конец списка

        with open(filename, 'w', encoding='utf-8') as file:  # Перезаписываем файл данными
            json.dump(existing_data, file, ensure_ascii=False, indent=4)# сохраняем данные в формате json

        print(f"Сохранён объект в файл {filename}. Всего записей: {len(existing_data)}")


class Post(Model):
    def __init__(self, title, content, date_posted, author): # конструктор, который создает объект с параметрами
        self.title = title # каждый параметр становиться атрибутом объекта
        self.content = content
        self.date_posted = date_posted
        self.author = author

    def __str__(self):
        return f"{self.title}"


# Первый пост
first_post = Post(title="Мой первый пост", content="Это мой первый пост!", date_posted="2023-10-01T12:00:00Z",
                  author="Игорь Иванов")
first_post.save()

# Второй пост
second_post = Post(title="Второй пост", content="Ещё один замечательный день.", date_posted="2023-10-02T16:30:00Z",
                   author="Иван Петров")
second_post.save()
