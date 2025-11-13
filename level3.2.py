# 3.2
# Теперь у воинов есть 2 метода. Защищаться и атаковать. Есть очки
# здоровья, очки брони и очки выносливости.
# На каждом шаге каждый воин атакует или защищается. Когда
# воин атакует, он теряет 10 очков выносливости. Когда воин
# защищается, а его атакуют, он теряет очки здоровья(random(0, 20))
# и очки брони(random(0, 10)).Когда оба воина атакуют, они оба
# теряют очки здоровья(random(10, 30)) и выносливости. Если оба
# воина защищаются, они не теряют очков. Когда очки брони кончаются, защищающийся воин
# теряет только очки здоровья(random(10, 30)). Когда очки выносливости
# закончатся, воин наносит меньше урона random(0, 10).
# На каждом ходе решение защищаться или атаковать принимается случайным образом.
# Проигрывает тот воин, у которого первым осталось 10 единиц здоровья.
# Тогда(как в Колизее) у пользователя спрашивают убить его, или (нет.polliceverso)
# Пример: health = 100
# у обоих
# health_1 - здоровье первого
# health_2 - здоровье второго
# endurance = 100 - выносливость
# у обоих
# end_1- выносливость первого
# end_2 - выносливость второго
# armor = 100 - броня
# у обоих armor_1-броня у первого
# armor_2-броня у второго
# 1: атака
# 2: атака
# health_1 -= random(10, 30)
# health_2 -= random(10, 30)
# end_1 -= 10
# end_2 -= 10
# 1: атака
# 2: защита
# end_1 -= 10
# health_2 -= random(0, 20)
# armor_2 -= random(0, 10)
import random


class Warrior:
    def __init__(self, name):
        self.name = name
        self.health = 100
        self.endurance = 100
        self.armor = 100

    def take_damage(self, damage):
        """Получает урон"""
        self.health -= damage
        if self.health < 0:
            self.health = 0
        print(f"{self.name} получил удар. Осталось здоровья: {self.health}")

    def lose_endurance(self, amount):
        """Тратит выносливость"""
        self.endurance -= amount
        if self.endurance < 0:
            self.endurance = 0
        print(f"{self.name} потерял выносливость. Осталось выносливости: {self.endurance}")

    def lose_armor(self, amount):
        """Потеря брони"""
        self.armor -= amount
        if self.armor < 0:
            self.armor = 0
        print(f"{self.name} потерял броню. Осталось брони: {self.armor}")

    def restore_stats(self):
        """Частичное восстановление характеристик каждый раунд"""
        self.endurance = min(100, self.endurance + 5)

    def make_decision(self):
        """Решает атаковать или защищаться"""
        # Проверяем, может ли воин действовать
        if self.health <= 0:
            return "defend"  # Мертвые не атакуют

        decision = random.choice(["attack", "defend"])
        print(f"{self.name} решил {'атаковать' if decision == 'attack' else 'защититься'}.")
        return decision


class BattleManager:
    def __init__(self, warriors):
        self.warriors = warriors

    def simulate_round(self):
        actions = {}
        for warrior in self.warriors:
            actions[warrior] = warrior.make_decision()

        # Восстанавливаем немного выносливости каждому воину
        for warrior in self.warriors:
            warrior.restore_stats()

        # Анализируем действия
        attacker = None
        defender = None
        for warrior, action in actions.items():
            if action == "attack":
                attacker = warrior
            else:
                defender = warrior

        # Разбор ситуации
        if attacker is not None and defender is not None:
            # Атакующий тратит выносливость
            attacker.lose_endurance(10)

            # Защитник получает урон и потерю брони
            health_damage = random.randint(0, 20)
            armor_damage = random.randint(0, 10)
            defender.take_damage(health_damage)
            defender.lose_armor(armor_damage)

        elif attacker is not None and defender is None:
            # Оба атакуют
            damage = random.randint(10, 30)
            for warrior in self.warriors:
                warrior.take_damage(damage)
                warrior.lose_endurance(10)

        # Завершаем раунд
        print("-" * 30)

    def check_game_over(self):
        losers = []
        for warrior in self.warriors:
            if warrior.health <= 0:  # Изменено с <=10 на <=0
                losers.append(warrior)
        return losers

    def run_battle(self):
        round_number = 1
        while True:
            print(f"\nРаунд №{round_number}")

            # Показываем текущее состояние бойцов
            for warrior in self.warriors:
                print(
                    f"{warrior.name}: Здоровье={warrior.health}, Выносливость={warrior.endurance}, Броня={warrior.armor}")

            self.simulate_round()
            losers = self.check_game_over()
            if losers:
                break
            round_number += 1

        # Кто проиграл?
        loser = losers[0]
        print(f"\nВоин {loser.name} достиг критического уровня здоровья!\n")

        # Просим зрителя принять решение
        print("Зритель решает судьбу:")
        print("1 - Казнить проигравшего")
        print("2 - Помиловать и отпустить")
        choice = input("Ваш выбор (1 или 2): ")

        # Добавляем проверку ввода
        while choice not in ['1', '2']:
            print("Пожалуйста, введите 1 или 2")
            choice = input("Ваш выбор (1 или 2): ")

        if choice == "1":
            print(f"Толпа кричит: \"Казнь!\". Воин {loser.name} убит.")
        else:
            print(f"Милосердие возобладало. Воин {loser.name} спасён.")


# Запускаем игру
warriors = [Warrior("Спартак"), Warrior("Максимус")]
manager = BattleManager(warriors)
manager.run_battle()





