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
from typing import List, Tuple

class Warrior:
    def __init__(self, name: str, health: int = 100, endurance: int = 100, armor: int = 100):# инициализируем имя итд
        self.name = name
        self.health = health
        self.endurance = endurance
        self.armor = armor
        self._is_defending = False

    def is_alive(self) -> bool: # возвращаем True, пока здоровье больше 10
        return self.health > 10

    def attack(self) -> Tuple[bool, int, str]: # осуществляем атаку, генерируя случайный урон и снижая собственную выносливость
        if self.endurance < 10:
            damage = random.randint(0, 10)
            return True, damage, f"{self.name} атакует с пониженным уроном из-за усталости (урон: {damage})"
        self.endurance -= 10 # Защита
        damage = self.get_attack_damage()
        return True, damage, f"{self.name} атаковал (урон: {damage})"

    def defend(self) -> str: # активирует режим защиты, предотвращая максимальный ущерб
        self._is_defending = True
        return f"{self.name} переходит в режим защиты"

    def take_damage(self, damage: int, attacker_action: str) -> str:# вычисляет фактический наносимый урон
        health_damage = 0
        armor_damage = 0
        if attacker_action == 'attack':
            if self._is_defending:
                if self.armor > 0:
                    health_damage = random.randint(0, 20)
                    armor_damage = random.randint(0, 10)
                    self.armor -= armor_damage
                    if self.armor < 0:
                        self.armor = 0
                else:
                    health_damage = random.randint(10, 30)
            else:
                health_damage = random.randint(10, 30)
        else:
            health_damage = damage

        self.health -= health_damage
        if armor_damage > 0:
            return f"получил {health_damage} урона по здоровью (броня поглотила {armor_damage})"
        else:
            return f"получил {health_damage} урона по здоровью"
# вспомогательные методы
    def get_attack_damage(self) -> int: # расчет урона в зависимости от выносливости
        if self.endurance <= 0:
            return random.randint(0, 10)
        return random.randint(10, 30)

    def reset_defense(self):# сброс защиты
        self._is_defending = False

    def is_defending(self) -> bool:# проверка состояния защиты
        return self._is_defending
# строковое представление
    def __str__(self) -> str:# статус воина с форматированием
        status = ""
        if self.health <= 10:
            status = " [НА ПОРОГЕ СОБСТВЕННОЙ СМЕРТИ]"
        return f"{self.name}{status}:\n\t• Здоровье: {self.health}\n\t• Броня: {self.armor}\n\t• Выносливость: {self.endurance}"

class Battle:
    def __init__(self, warriors: List[Warrior]):
        if len(warriors) < 2:
            raise ValueError("Нужно минимум 2 воина для боя")
        self.warriors = warriors

    def _select_actions(self) -> List[Tuple[Warrior, str]]:
        return [(warrior, random.choice(['attack', 'defend'])) for warrior in self.warriors]

    def _resolve_interaction(self, attacker: Warrior, defender: Warrior,
                             attacker_action: str, defender_action: str) -> str:
        attack_success, damage, attack_msg = attacker.attack()

        if not attack_success and 'не может атаковать' in attack_msg:
            return attack_msg

        def_msg = defender.take_damage(damage, attacker_action)

        if defender_action == 'defend':
            return f"{attack_msg}: {def_msg}. {defender.name} защищался"
        else:
            return f"{attack_msg}: {def_msg}"

    def _execute_turn(self, actions: List[Tuple[Warrior, str]]) -> List[str]:
        messages = []

        for warrior, action in actions:
            if action == 'defend':
                msg = warrior.defend()
                messages.append(msg)

        alive_warriors = self._get_alive_warriors()
        warrior_actions = {w: a for w, a in actions}

        for attacker, attacker_action in actions:
            if attacker_action != 'attack' or not attacker.is_alive():
                continue

            possible_targets = [w for w in alive_warriors if w != attacker and w.is_alive()]

            if not possible_targets:
                messages.append(f"{attacker.name} не нашел цели для атаки")
                continue

            defender = random.choice(possible_targets)
            defender_action = warrior_actions[defender]

            msg = self._resolve_interaction(attacker, defender, attacker_action, defender_action)
            messages.append(msg)

        return messages

    def _cleanup_defense(self):
        for warrior in self.warriors:
            warrior.reset_defense()

    def _get_alive_warriors(self) -> List[Warrior]:
        return [w for w in self.warriors if w.is_alive()]

    def run(self):
        turn = 1

        print("🚀 ⚔ 🚀 \nНачало боя!")
        for warrior in self.warriors:
            print(f"➕ {warrior}")

        while len(self._get_alive_warriors()) > 1:
            print(f"\n\n------ ХОД #{turn} ------")

            actions = self._select_actions()
            print("✉ ДЕЙСТВИЯ:\n")
            for warrior, action in actions:
                print(f"— {warrior.name}: {action.capitalize()}")

            messages = self._execute_turn(actions)
            print("\n🔥 РЕЗУЛЬТАТЫ ЭТОГО ХОДА:\n")
            for msg in messages:
                print(f"— {msg}")

            print("\n📋 ТЕКУЩЕЕ СОСТОЯНИЕ ВОИНОВ:\n")
            for warrior in self.warriors:
                if warrior.is_alive():
                    print(f"☘ {warrior}")
                else:
                    print(f"✨ {warrior.name} ранен")

            self._cleanup_defense()
            turn += 1

        alive = self._get_alive_warriors()
        dead = [w for w in self.warriors if not w.is_alive()]

        if alive and dead:
            winner = alive[0]
            loser = dead[0]
            print(f"\n🥊 {loser.name.upper()} проиграл (его здоровье упало ниже допустимой нормы)! ⬇")

            # Пользовательский выбор убийства
            while True:
                choice = input("Хотите казнить проигравшего? (1 — Да / 2 — Нет): ").strip()
                if choice == "1":
                    print(f"🔫 {loser.name.upper()} был казнён по воле толпы!")
                    break
                elif choice == "2":
                    print(f"🌟 {loser.name.upper()} помилован зрителями и продолжает жить!")
                    break
                else:
                    print("Введите 1 или 2.")

            print(f"🥈 ПОБЕДИЛ: {winner.name.upper()}!")
        else:
            print("🌵 Бой завершён вничью!")

if __name__ == "__main__":
    warrior1 = Warrior("Ахиллес", health=120, armor=80)
    warrior2 = Warrior("Гектор", endurance=120)

    battle = Battle([warrior1, warrior2])
    battle.run()




