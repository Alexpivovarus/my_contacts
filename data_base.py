from json import dumps, loads

FILE_NAME = "db.json"
PEOPLES_DATA = ["first name", "last name", "phone number"]
PEOPLES_EXTRA_DATA = [
    "birthday", "address", "hair color", "eye color", "place of study",
    "place of work", "studying for", "profession",
    "height", "weight", "favorite color", "favorite number", "is married",
    "have girlfriend", "have children", "have you been convicted",
    "how many divorced"]
PEOPLES_DATA_RUSSIAN_DICT = {
    "first name": "имя", "last name": "фамилия", "phone number": "номер телефона",
    "birthday": "дата рождения", "address": "адрес", "hair color": "цвет волос",
    "eye color": "цвет глаз", "place of study": "место учёбы",
    "place of work": "место работы", "studying for": "на кого учится",
    "profession": "профессия", "height": "рост", "weight": "вес",
    "favorite color": "любимый цвет", "favorite number": "любимое число",
    "is married": "находится в браке","have girlfriend": "находтся в отношениях",
    "have children": "есть ли дети", "have you been convicted": "судим ли",
    "how many divorced": "сколько раз разводился"}
def read_data_base():
    with open(FILE_NAME, "r") as file:
        data_base = loads(file.read())
    return data_base


def write_data_base(data_base):
    with open(FILE_NAME, "w") as file:
        file.write(dumps(data_base))


def add_people():
    this_people_data = {}
    peoples = read_data_base()
    for peoples_id in peoples.keys():
        new_id = int(peoples_id) + 1
    for data in PEOPLES_DATA:
        this_people_data[data] = input(f"Введите {PEOPLES_DATA_RUSSIAN_DICT[data]}:")
    peoples[new_id] = this_people_data
    write_data_base(peoples)
    return new_id


def find_people():
    parameters_dict = {}
    found_ids = []
    data_base = read_data_base()
    search_by = None
    i = 0
    for parameter in PEOPLES_DATA:
        i += 1
        parameters_dict[i] = parameter
        #{1: "first", 2: "last"}
    for keys in parameters_dict:
        print(f"Введите {keys} если хотите ввести {PEOPLES_DATA_RUSSIAN_DICT[parameters_dict[keys]]}")

    search_parameter = int(input(": "))
    search_by = input(f"Введите {PEOPLES_DATA_RUSSIAN_DICT[parameters_dict[search_parameter]]}: ")

    for id in data_base.keys():
        if search_by == data_base[id][parameters_dict[search_parameter]]:
            found_ids.append(id)
    return found_ids


def add_extra_information():
    pass


def change_people_information():
    pass


def change_extra_information():
    pass


def delete_people():
    pass


def show_people_information():
    pass


def show_all_people_information():  # with extra information
    pass


if __name__ == '__main__':
    print(read_data_base())
    print(find_people())