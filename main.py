def print_order(*order, **info):
    print("Музыкальная библиотека №1\n")

    # Словарь 'infos' должен содержать ключи 'author' и 'birthday'
    for key, value in sorted(info.items()):
        print(key, ":", value)

    # Кортеж 'order' содержит все наименования произведений
    print("Вы выбрали:")
    for item in order:
        print(" -", item)

    print("\nПриходите ещё!")

print_order("Славянский марш", "Лебединое озеро", "Спящая красавица",
            "Пиковая дама", "Щелкунчик",
            author="П.И. Чайковский", birthday="07/05/1840")
