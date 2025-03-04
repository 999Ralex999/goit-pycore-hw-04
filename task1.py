def total_salary(path):
    salaries = []
    try:
        with open(path, 'r', encoding='utf-8') as file:
            for line in file:
                try:
                    _, salary = line.split(",")
                    salaries.append(int(salary.strip()))
                except ValueError:
                    print("Ошибка: Некорректный формат данных в файле.")
                    return (0, 0)
        
        if salaries:
            return (sum(salaries), sum(salaries) / len(salaries))
        else:
            print("Файл пуст или не содержит корректных данных.")
            return (0, 0)
            
    except FileNotFoundError:
        print(f"Ошибка: Файл '{path}' не найден.")
        return (0, 0)
    except Exception as e:
        print(f"Ошибка при чтении файла: {e}")
        return (0, 0)

total, average = total_salary("salary_file.txt")
print(f"Общая сумма заработной платы: {total}, Средняя заработная плата: {average}")

