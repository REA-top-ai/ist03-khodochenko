#1
def f_to_c(f_temp):
    c_temp = (f_temp - 32) * 5/9
    return c_temp
f100_in_celsius = f_to_c(100)
print("100°F в Цельсиях:", f100_in_celsius)
def c_to_f(c_temp):
    f_temp = c_temp * (9/5) + 32  # Формула преобразования
    return f_temp
c0_in_fahrenheit = c_to_f(0)
print("0°C в Фаренгейтах:", c0_in_fahrenheit)
#2
def get_force(mass, acceleration):
    return mass * acceleration
train_mass = 22680
train_acceleration = 10
train_force = get_force(train_mass, train_acceleration)

print("train_force:", train_force)
print(f"Поезд GE поставляет {train_force} ньютонов силы")
def get_energy(mass, c=3*10**8):
    return mass * c**2
bomb_mass = 1
bomb_energy = get_energy(bomb_mass)
print(f"1 кг бомбы составляет {bomb_energy} Джоулей")
def get_work(mass, acceleration, distance):
    force = get_force(mass, acceleration)
    return force * distance
train_distance = 100
train_work = get_work(train_mass, train_acceleration, train_distance)
print(f"Поезд выполняет {train_work} Джоулей за {train_distance} метров.")
#3
clothes = "домашняя одежда"
def show_clothes():
    print("У меня большой гардероб")
    print(f"Утром лучше всего подходит {clothes}")
    print(f"Днём лучше всего подходит {clothes}")
    print(f"Вечером лучше всего подходит {clothes}")
    print(f"Ночью лучше всего подходит {clothes}")
show_clothes()
def show_meals(meal):
    print("мои предпочтения в еде")
    print(f"На завтрак лучше всего подходит {meal}")
    print(f"На обед лучше всего подходит {meal}")
    print(f"На ужин лучше всего подходит {meal}")
show_meals("домашняя еда")
#4
user_name = "Дмитрий"

msg_dmitriy = "Дмитрий, твое рабочее место находится в другой комнате. Отойди от чужого компьютера и займись работой!"

msg_welcome = "Добро пожаловать"

def check1(name):
    if name == "Дмитрий":
        print(msg_dmitriy)
    else:
        print(msg_welcome)

check1("Дмитрий")
check1("Ангелина")

def check2(name, arm):
    if name == "Дмитрий":
        if arm == 1:
            print("Добро пожаловать!")
        else:
            print(msg_dmitriy)
    elif name == "Ангелина" and arm == 2:
        print("Добро пожаловать!")
    elif name == "Василий" and arm == 3:
        print("Добро пожаловать!")
    elif name == "Екатерина" and arm == 4:
        print("Добро пожаловать!")
    else:
        print("Логин или пароль не верный")

check2("Дмитрий", 2)
check2("Ангелина", 2)
check2("Иван", 1)
#5
def check_grade(score):
    if score >= 4.0:
        print("A")
    elif score >= 3.0:
        print("B")
    elif score >= 2.0:
        print("C")
    elif score >= 1.0:
        print("D")
    else:
        print("F")

check_grade(4.2)  # A
check_grade(3.7)  # B
check_grade(2.1)  # C
check_grade(1.5)  # D
check_grade(0.3)  # F