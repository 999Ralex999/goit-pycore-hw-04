def get_cats_info(path):
    cats = []
    try:
        with open(path, 'r', encoding='utf-8') as file:
            for line in file:
                parts = line.strip().split(',')
                if len(parts) != 3:
                    print("Ошибка: Некорректный формат данных.")
                    return []

                id, name, age = parts
                try:
                    age = int(age)  
                except ValueError:
                    print(f"Ошибка: Некорректный формат возраста для кота {name}.")
                    return []

                cats.append({'id': id, 'name': name, 'age': age})

        return cats

    except FileNotFoundError:
        print(f"Ошибка: Файл '{path}' не найден.")
        return []
    except Exception as e:
        print(f"Ошибка при чтении файла: {e}")
        return []

cats_info = get_cats_info("cats_file.txt")
print(cats_info)
