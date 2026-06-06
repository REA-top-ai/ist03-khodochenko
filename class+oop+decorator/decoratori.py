import functools
import time

def is_alive(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        c = args[0]
        if c.health <= 0:
            print(f"{c.name} мертв и не может действовать!")
            return None
        return func(*args, **kwargs)
    return wrapper

def log_action(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        print(f"[LOG] Начало действия: {func.__name__}")
        res = func(*args, **kwargs)
        print(f"[LOG] Действие завершено")
        return res
    return wrapper

def easter_event_stats(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        c = args[0]
        oldt_h = c.health
        oldt_m = c.mana
        c.health *= 2
        c.mana = int(c.mana * 1.5)
        res = func(*args, **kwargs)
        c.health = oldt_h
        c.mana = oldt_m
        return res
    return wrapper

def holy_staff_bonus(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        c = args[0]
        bonus = 0
        if c.hero_class == "волшебник":
            bonus = 5
            c.mana += bonus
            c.items["Священный посох"] = {"мана": 5}
        res = func(*args, **kwargs)
        if bonus > 0:
            c.mana -= bonus
            c.items.pop("Священный посох", None)
        return res
    return wrapper

def validate_mana(func):
    # Проверяет наличие маны перед использованием заклинания
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        c = args[0]
        s_name = args[1] if len(args) > 1 else kwargs.get("spell_name")
        if s_name in c.spells_names:
            cost = c.spells_names[s_name].get("mana_cost", 0)
            if c.mana < cost:
                print(f"Недостаточно маны для {s_name}!")
                return None
        return func(*args, **kwargs)
    return wrapper

class Hero:
    def __init__(self, name, hero_class):
        self.name = name
        self.hero_class = hero_class
        self.spells_names = {}
        self.items = {}
        
        if hero_class == "волшебник":
            self.health = 60
            self.mana = 50
        else:
            self.health = 100
            self.mana = 10
            
    @is_alive
    def attack(self, damage):
        print(f"Герой нанес урон: {damage}")

    @log_action
    def heal(self, amount):
        self.health += amount
        print(f"{self.name} восстановил {amount} здоровья. Текущее: {self.health}")

    @is_alive
    @validate_mana
    def cast_spell(self, spell_name):
        if spell_name in self.spells_names:
            self.mana -= self.spells_names[spell_name]["mana_cost"]
            print(f"Заклинание: {spell_name}")

    def add_spell(self, spell_name, mana_cost, attack_damage=0, health_increase=0):
        self.spells_names[spell_name] = {
            "mana_cost": mana_cost,
            "attack_damage": attack_damage,
            "health_increase": health_increase
        }

    def add_item(self, item_name, param, value):
        if len(self.items) < 6:
            self.items[item_name] = {param: value}
            if param == "здоровье":
                self.health += value
            elif param == "мана":
                self.mana += value

    @easter_event_stats
    @holy_staff_bonus
    def perform_event_action(self):
        print(f"Праздничные статы {self.name}: HP={self.health}, MP={self.mana}, Предметы: {list(self.items.keys())}")
