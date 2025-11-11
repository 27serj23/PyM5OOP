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


class Model:
    def save(self, filename='data.json'):
        # Собираем все атрибуты объекта (кроме тех, что начинаются с "_")
        data = {}

        # Используя dir(self), фильтруем атрибуты, отбрасывая системные
        attributes = list(filter(lambda attr: not attr.startswith('_'), dir(self)))

        # Сохраняем каждое найденное свойство
        for attr in attributes:
            value = getattr(self, attr)
            data[attr] = str(value)  # Приведение к строке

        # Записываем данные в JSON-файл
        with open(filename, 'w', encoding='utf-8') as file:
            json.dump(data, file, ensure_ascii=False, indent=4)

        print(f"Сохранен объект в файл {filename}: {data}")

class Post(Model):
    def __init__(self, title, content, date_posted, author):
        self.title = title
        self.content = content
        self.date_posted = date_posted
        self.author = author

    def _str_(self):
        return self.title

post = Post(
    title="Мой первый пост",
    content="Это мой первый пост!",
    date_posted="2023-10-01T12:00:00Z",
    author="Игорь Иванов"
)
# Вызываем метод сохранения
post.save()