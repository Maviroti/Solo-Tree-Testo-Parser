import os
import re

# OLD
# =====================================


def del_repetitive_obj(obj_list: list):
    result_list = []
    for obj in obj_list:
        if isinstance(obj, tuple):
            obj = list(obj)
            for obj_2 in obj:
                if obj_2 not in result_list:
                    result_list.append(obj_2)
        else:
            if obj not in result_list:
                result_list.append(obj)
    return (result_list)


def lvl_qualifier(list_struct: list):
    result_list = []  # Итоговый список, который содержит списки тестов. Каждый список это уровень в структуре
    intermediate_list = []  # промежуточный или вспомогательный список

    # if not result_list:
    for obj in list_struct:
        if not list(obj.values())[0]:
            intermediate_list.append(list(obj.keys())[0])
            # list_struct.remove(obj)
    result_list.append(intermediate_list)
    intermediate_list = []
    # else:

    flag_append = 1  # Проверяем что был найден хоть один родительский тест

    while flag_append == 1:
        flag_append = 0
        # список, который содержит последний список из результируещего. для проверки связей с предыдущем уровнем
        up_list = result_list[len(result_list) - 1]
        for up_obj in up_list:
            for obj in list_struct:
                # Список родителей для объекта
                list_parent_for_obj = list(obj.values())[0]
                if up_obj in list_parent_for_obj:
                    flag_append = 1
                    obj_name = list(obj.keys())[0]
                    if obj_name not in intermediate_list:
                        intermediate_list.append(obj_name)
        if flag_append == 1:
            result_list.append(intermediate_list)
        intermediate_list = []

    return (result_list)
# =====================================


def lvl_qualifier_for_solo(test_name: str, list_struct: list):
    result_list = []  # Итоговый список, который содержит списки тестов. Каждый список это уровень в структуре
    intermediate_list = []  # промежуточный или вспомогательный список
    up_list = []  # лист на уровень выше
    flag_test_found = 0  # Проверка на то что тест вообще существует

    for obj in list_struct:
        obj_keys = list(obj.keys())[0]
        if obj_keys == test_name:
            flag_test_found = 1
            obj_value = list(obj.values())[0]
            intermediate_list = obj_value
            result_list.append([test_name])
            break

    if flag_test_found == 0:
        exit("Имя теста не найдено")

    flag_parent = 0  # Проверяем что был найден хоть один родительский тест
    flag_append = 1  # Проверяем что в ходе итерации цикла был найден родитель

    while flag_append == 1:
        flag_append = 0
        for test in intermediate_list:
            for obj in list_struct:
                key_obj = list(obj.keys())[0]
                if key_obj == test:
                    flag_parent = 1
                    flag_append = 1
                    list_value_obg = list(obj.values())
                    up_list = up_list + list_value_obg[0]
        if flag_append == 1:
            result_list.append(intermediate_list)
            intermediate_list = up_list
            up_list = []

    if flag_parent == 0:
        exit(f"{test_name} - Скрипт не смог найти ни одного родителя для этого теста")

    result_list.reverse()
    return (result_list)


def find_parent(test_name: str, list_struct: list):
    for obj in list_struct:
        obj_key = list(obj.keys())[0]
        if obj_key == test_name:
            list_parent = list(obj.values())[0]
            return (list_parent)


def space_add(list_lvl: list, list_struct: list):
    list_lvl_bak = list_lvl.copy()
    up_list_bak = list_lvl_bak[0]
    up_list = list_lvl[0].copy()
    list_res = []

    for num_lvl in range(1, len(list_lvl)):
        list_obj = list_lvl[num_lvl].copy()
        for ind_obj, obj in enumerate(list_obj):
            list_parent = find_parent(obj, list_struct)
            if list_parent:
                list_parent_index = []
                for parent in list_parent:
                    list_parent_index.append(up_list_bak.index(parent))

                len_obj = len(obj)
                # Присвиваем кол-во пробелов между родителями
                len_parent = len(list_parent) - 1
                for index in list_parent_index:
                    len_parent = len_parent + len(up_list[index])

                if len_obj > len_parent:
                    diff = len_obj - len_parent
                    up_list[list_parent_index[-1]] = up_list[list_parent_index[-1]] + " " * diff
                elif len_obj < len_parent:
                    diff = len_parent - len_obj
                    list_obj[ind_obj] = obj + " " * diff

                # переносим родителя и объект в начало своих списков
                # newind = 0
                # for ind in list_parent_index:                        
                #     up_list.insert(newind, up_list.pop(ind))
                #     newind += 1
                # list_obj.insert(0, list_obj.pop(ind_obj))

        list_res.append(up_list)
        up_list = list_obj
        up_list_bak = list_lvl_bak[num_lvl]

    list_res.append(up_list)
    return (list_res)


def drow_line(list_lvl: list, list_with_space: list, list_struct: list):
    result_list = []
    for num_lvl in range(0, len(list_lvl) - 1):
        line_str = "  "
        up_lvl = list_lvl[num_lvl]
        down_list = list_lvl[num_lvl + 1]
        for test in down_list:
            parent_list = find_parent(test, list_struct)
            if parent_list:
                parent_index_list = []
                for parent in parent_list:
                    parent_index_list.append(up_lvl.index(parent))

                if len(parent_index_list) == 1:
                    len_parent = len(
                        list_with_space[num_lvl][parent_index_list[0]])
                    line_str = line_str + "|" + " " * (len_parent)
                else:
                    line_str = line_str + "├"
                    for enum, index in enumerate(parent_index_list):
                        len_parent = len(list_with_space[num_lvl][index])
                        last_paren = list_with_space[num_lvl][parent_index_list[-1]]
                        if enum != len(parent_index_list) - 2:
                            line_str = line_str + "─" * (len_parent) + "┴"
                        else:
                            line_str = line_str + "─" * \
                                (len_parent) + "┘" + " " * len(last_paren)
                            break

        result_list.append(list_with_space[num_lvl])
        result_list.append([line_str])
    result_list.append(down_list)
    return (result_list)


def del_last_space(list_with_line: list):
    result_list = list_with_line
    for list_obj in result_list:
        list_obj[-1] = list_obj[-1].rstrip()
    return (result_list)


def testo_test_file(path_tests: str):
    """
    Находит все файлы с расширением .testo
    :param path_tests (str): Путь до папки в которой происходит поиск файлов .testo
    :return List: Список со всеми относительными путями до файлов .testo
    """
    testo_tests_path_list = []
    list_tree = os.listdir(path_tests)

    for filename in list_tree:
        if os.path.isfile(f'{path_tests}/{filename}') and filename.endswith('.testo'):
            testo_tests_path_list.append(f'{path_tests}/{filename}')

        if os.path.isdir(f'{path_tests}/{filename}'):
            testo_tests_path_list = testo_tests_path_list + \
                testo_test_file(f'{path_tests}/{filename}/')

    return (testo_tests_path_list)


def testo_parser(test_path_list: list):
    """
    Парсит зависимости всех тестов
    :param test_path_list (list): Список со всеми путями до файлов .testo
    :return List: Списки со словарями вида {"test_name": ["parent1", "parent2"...]. Если родителей нет, то в значении словаря будет пустой список}
    """
    list_struct_result = []

    for path_file in test_path_list:
        with open(path_file, 'r', encoding='utf-8') as file:
            lines = file.readlines()

            for line in lines:
                line = re.sub(r'#.*', "", line)
                line = re.sub(r'/\*.*\*/', "", line)
                test_struct_line = re.findall(r'test (.*):(.*)', line) # Вернёт либо [], либо [('test name', 'all parents')]
                if len(test_struct_line) == 0:
                    test_struct_line = re.findall(r'test (.*)', line) # Вернёт либо [], либо ['test name']

                if len(test_struct_line) != 0:
                    if isinstance(test_struct_line[0], tuple):
                        test_struct_line = list(test_struct_line[0])
                    elif not isinstance(test_struct_line[0], str):
                        exit("Неправильный тип данных")

                if len(test_struct_line) == 1:
                    test_name = test_struct_line[0]
                    test_name = test_name.replace("{", "").strip()

                    list_struct_result.append({test_name: []})

                if len(test_struct_line) != 2:
                    continue

                if len(test_struct_line) == 2:
                  # очищаем первую и вторую строку
                  test_name = test_struct_line[0].strip()
                  parent_str = test_struct_line[1].replace("{", "")
                  parent_list = parent_str.split(",")

                  # очищаем родителей
                  for enum, paren in enumerate(parent_list):
                      parent_list[enum] = paren.strip()

                  # Добавляем в результат
                  list_struct_result.append({test_name: parent_list})

    return (list_struct_result)


def list_struct_with_bracket(list_struct: list):
    for enum, struct in enumerate(list_struct):
        struct_keys = list(struct.keys())[0]
        struct_keys = "[" + struct_keys + "]"

        list_value_struct = list(struct.values())[0]
        for enum2, value_struct in enumerate(list_value_struct):
            value_struct = "[" + value_struct + "]"
            list_value_struct[enum2] = value_struct

        list_struct[enum] = {struct_keys: list_value_struct}

    return (list_struct)


def name_and_path(test_path_list: str):
    name_and_path_dict_result = {}

    for path_file in test_path_list:
        with open(path_file, 'r', encoding='utf-8') as file:
            lines = file.readlines()

            for line in lines:
                line = re.sub(r'#.*', "", line)
                line = re.sub(r'/\*.*\*/', "", line)
                test_name_list = re.findall(r"test (.*)", line)
                if len(test_name_list) == 1:
                    test_name = test_name_list[0]
                    test_name = re.sub(r":(.*)", "", test_name)
                    test_name = test_name.replace("{", "")
                    test_name = test_name.strip()
                    if test_name in name_and_path_dict_result:
                        name_and_path_dict_result[test_name].append(path_file)
                    else:
                        name_and_path_dict_result[test_name] = [path_file]

    return (name_and_path_dict_result)
