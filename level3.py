# Уровень 3.
# Очень объемное задание. Выполнение по желанию.
# 3.1 Напишите программу по следующему описанию. Есть класс
# "Воин". От него создаются два экземпляра - юнита. Каждому
# устанавливается здоровье в 100 очков. В случайном порядке
# они бьют друг друга. Тот, кто бьет, здоровья не теряет. У того, кого бьют,
# оно уменьшается на 20 очков от одного удара. После
# каждого удара надо выводить сообщение, какой юнит атаковал, и
# сколько у противника осталось здоровья. Как только у кого - то заканчивается
# ресурс здоровья, программа завершается сообщением о том, кто одержал победу.
import random

class Warrior:
    def __init__(self, name):
        self.name = name
        self.health = 100

    def attack(self, opponent):
        damage = 20
        opponent.health -= damage
        print(f"{self.name} нанес удар {opponent.name}. Осталось здоровья: {opponent.health}")

warriors = [Warrior("Воин Андрей"), Warrior("Воин Борис")]

while all(warrior.health > 0 for warrior in warriors):
    attacker = random.choice(warriors)
    defender = next(warrior for warrior in warriors if warrior != attacker)
    attacker.attack(defender)

winner = next((w for w in warriors if w.health > 0))
loser = next((w for w in warriors if w.health <= 0))

print(f"\nПобедитель: {winner.name}\nПроигравший: {loser.name}")




