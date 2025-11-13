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
    def __init__(self, name, health=100, damage=20):
        self.name = name
        self.health = health
        self.damage = damage

    def take_damage(self, damage):
        self.health -= damage
        if self.health < 0:  # Не даем здоровью уйти в минус
            self.health = 0
        print(f"{self.name} получил удар. Осталось здоровья: {self.health}")


warriors = [Warrior("Воин Андрей"), Warrior("Воин Борис")]

fight_is_over = False
round_count = 0  # Счетчик раундов

while not fight_is_over:
    round_count += 1
    print(f"\n--- Раунд {round_count} ---")

    attacker, defender = random.sample(warriors, 2)
    print(f"{attacker.name} атакует {defender.name}!")  # Показываем кто кого атакует

    defender.take_damage(attacker.damage)

    # Проверяем, закончился ли бой
    if any(warrior.health <= 0 for warrior in warriors):
        fight_is_over = True

# Определяем победителя и проигравшего
winner = None
loser = None

for warrior in warriors:
    if warrior.health > 0:
        winner = warrior
    else:
        loser = warrior

# Проверяем, что победитель определен (на случай ничьи)
if winner and loser:
    print(f"\nПобедитель: {winner.name}")
    print(f"Проигравший: {loser.name}")
else:
    print("\nБой закончился вничью!")





