#1
first_name = "Виталий"
last_name = "Красилов"
new_account = last_name[:5]
temp_password = last_name[2:6]
print(temp_password)
print(new_account)


#2
def account_generator(first_name, last_name):
    account_name = first_name[:3] + last_name[:3]
    return account_name

# Данные нового сотрудника
first_name = "Виталий"
last_name = "Красилов"

# Генерация имени учетной записи с помощью функции
new_account = account_generator(first_name, last_name)

# Вывод результатов
print("Данные сотрудника:")
print(f"Имя: {first_name}")
print(f"Фамилия: {last_name}")
print(f"Новое имя учетной записи: {new_account}")

# Дополнительные примеры для тестирования
print("Тестирование функции с другими сотрудниками:")
print()

# Сотрудники с одинаковой фамилией
employee1_account = account_generator("Иван", "Красилов")
employee2_account = account_generator("Мария", "Красилов")
employee3_account = account_generator("Петр", "Красилов")

print(f"Иван Красилов: {employee1_account}")
print(f"Мария Красилов: {employee2_account}")
print(f"Петр Красилов: {employee3_account}")

#3
def password_generator(first_name, last_name):
    # Берем последние три буквы имени и фамилии
    password = first_name[-3:] + last_name[-3:]
    return password

temp_password = password_generator("Иван", "Петров")
print(temp_password)

#4

company_motto = "Мечты сбываются"

# Находим предпоследний символ
second_to_last = company_motto[-2]
print(f"Предпоследний символ: '{second_to_last}'")

#  Создаем срез из последних 4 символов
final_word = company_motto[-4:]
print(f"Последние 4 символа: '{final_word}'")