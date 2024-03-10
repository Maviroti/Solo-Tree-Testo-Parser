
# ======================================
# Тестовые входные данные
# ======================================
dict_struct_test = {("Test1", "Test2"): {"Test3": [{"Test5": ["Test7","Test8","Test9"]}, {"Test6": "Test10"}]}, "Test2": {"Test4": "Test11"}}

list_struct_test = [{"Test1": []}, {"Test2": []}, {"Test3": ["Test1", "Test2"]}, {"Test4": ["Test2"]}, {"Test5": ["Test3"]}, {"Test6": ["Test3"]}, {"Test7": ["Test5"]}, 
                    {"Test8": ["Test5"]}, {"Test9": ["Test5"]}, {"Test10": ["Test6"]}, {"Test11": ["Test4"]}]

tests_list_test = ["Test1", "Test2", "Test3", "Test4", "Test5", "Test6", "Test7", "Test8", "Test9", "Test10", "Test11"]

list_struct_test2 = [{"Test1": []}, {"Test2": []}, {"Test3": []}, {"Test4": []}, {"Test5": []}, {"Test6": ["Test1", "Test2"]}, {"Test7": ["Test3"]}, 
                    {"Test8": ["Test4","Test5"]}, {"Test9": ["Test6", "Test7"]}, {"Test10": ["Test8"]}, {"Test11": ["Test9","Test10"]}]

list_struct_test3 = [{"Test1": []}, {"Test2": []}, {"Test3": []}, {"Test4": []}, {"Test5": []}, {"Test6": ["Test1", "Test2"]}, {"Test7": ["Test3"]}, 
                     {"Test9": ["Test6", "Test7"]}, {"Test10": ["Test4","Test5"]}, {"Test11": ["Test9","Test10"]}]


# ======================================
# Параметры для argparser
# ======================================
main_name = "Solo Tree Testo Parser"
main_description = "Скрипт выводит дерево зависимостей тестов для заданного теста"
main_copyright = "(С) 2024 М0твей"
main_version = "0.1"
