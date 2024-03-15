
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
main_name = "Solo_Tree_Testo_Parser"
main_description = "Многофункциональный скрипт для работы с большим количеством тестов, написанных на Testo leng"
main_copyright = "(С) 2024 М0твей"
main_version = "2.0"
