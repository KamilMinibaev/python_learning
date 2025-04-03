import csv

MENU_TEXT = '''
Меню:
    1 - Иерархия команд
    2 - Сводный отчёт
    3 - Сохранить сводный отчет в файл
    0 - Выход
'''

def read_data(filename: str):
    """
    читаю файл по названию
    """

    try:
        with open(filename) as file:
            csv_reader = csv.DictReader(file, delimiter=';')
            data = [row for row in csv_reader]

            return data

    except FileNotFoundError:
        print('Нет такого файла')

    except Exception as e:
        print(e)


def team_hierarchy(filename: str) -> None:
    """
    вывожу список отделов, которые находятся в департаменте
    """

    # словарь для хранения
    departments_teams = {}

    data = read_data(filename)

    for row in data:
        department = row['Департамент']
        team = row['Отдел']

        # + департамент, если не было
        if department not in departments_teams:
            departments_teams[department]= set()
        # + команда, если не было
        departments_teams[department].add(team)

    for dep, teams in departments_teams.items():
        print(f'Департамент: {dep}')
        for team in teams:
            print(f'Команда: {team}')


def count_stats(data) -> {}:

    departments = {}

    for row in data:
        department = row['Департамент']
        salary = float(row['Оклад'])

        if department not in departments:
            departments[department] = {
                'count': 0,
                'sum_salary': 0.0,
                'min_salary': salary,
                'max_salary': salary
            }

        departments[department]['count'] += 1
        departments[department]['sum_salary'] += salary

        if salary < departments[department]['min_salary']:
            departments[department]['min_salary'] = salary

        if salary > departments[department]['max_salary']:
            departments[department]['max_salary'] = salary

    return departments



def dept_summary(filename) -> None:
    """
    вывожу информацию о каждом департаменте: численность, вилка ЗП, средняя ЗП
    """

    data = read_data(filename)

    departments = count_stats(data)

    print('Департамент | Численность | Зарплата (мин – макс) | Средняя зарплата')
    for dep, data in departments.items():
        count = data['count']
        avg_salary = round(data['sum_salary'] / count, 2)
        min_salary = round(data['min_salary'], 2)
        max_salary = round(data['max_salary'], 2)
        print(f'{dep} | {count} | {min_salary} – {max_salary} | {avg_salary}')




def save_summary(filename):
    """
    сохраняю в файл информацию о каждом департаменте
    """
    output_file = input("Напишите имя сохраняемого файла в формате .csv: ")

    data = read_data(filename)

    departments = count_stats(data)

    summary_list = []

    for dep, data in departments.items():
        count = data['count']
        avg_salary = round(data['sum_salary'] / count, 2)
        summary_list.append({
            'Департамент': dep,
            'Численность': count,
            'Min оклад': round(data['min_salary'], 2),
            'Max оклад': round(data['max_salary'], 2),
            'Avg оклад': avg_salary
        })

    fieldnames = ['Департамент', 'Численность', 'Min оклад', 'Max оклад', 'Avg оклад']

    with open(output_file, 'w', newline='', encoding='utf-8') as file:
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        for row in summary_list:
            writer.writerow(row)



def menu():
    '''
    меню, которое позволяет выбрать любую из функций
    '''

    while True:
        filename = input("Введите имя файла для работы: ")
        try:
            with open(filename, "r", encoding="utf-8") as file:
                break

        except FileNotFoundError:
            print(f"Файла '{filename}' нет, давай по новой")

        except Exception as e:
            print(e)

    while True:
        print(MENU_TEXT)

        choice = input("Введите номер пункта: ")

        match choice:
            case '1':
                team_hierarchy(filename)
            case '2':
                dept_summary(filename)
            case '3':
                save_summary(filename)
            case '0':
                print("Выходим)")
                break
            case _:
                print("Такую функцию еще не придумали, попробуйте снова")


if __name__ == '__main__':
    menu()
