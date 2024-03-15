
import argparse
from helpers import lvl_qualifier_for_solo, space_add, drow_line, del_last_space, testo_parser, testo_test_file, \
                    list_struct_with_bracket, name_and_path

import config


def createParser():  
  parser_root = argparse.ArgumentParser(prog=config.main_name, description=config.main_description, epilog=config.main_copyright, add_help=False)         
  root_group = parser_root.add_argument_group(title='Параметры')

  root_group.add_argument ('-h', '--help', action="help", help='Справка')
  root_group.add_argument ('--version', action='version', help='Версия скрипта', version='Script %(prog)s version {}'.format(config.main_version))


  subparsers = parser_root.add_subparsers (dest='command',
                                      title = 'Возможные команды')

  tree_parser = subparsers.add_parser("tree", add_help = False, help = 'Запуск в режиме вывода дерева зависимостей')  
  tree_group = tree_parser.add_argument_group (title='Параметры')
  tree_group.add_argument ('-tp', '--tests_path', required=True, type=str, help='Путь до папки с тестами', metavar='')
  tree_group.add_argument ('-tn', '--test_name', required=True, type=str, help='Название теста', metavar='')   
  tree_group.add_argument ('--test', action='store_const', const=True, default=False, help='Тестовый запуск', metavar='')
  tree_group.add_argument ('--debug', action='store_const', const=True, default=False, help='Сохранение дебажной информации в debug.log', metavar='')
  tree_group.add_argument ('-h', '--help', action="help", help='Справка')

  dublicate_parser = subparsers.add_parser("dubcheck", add_help = False, help = 'Запуск в режиме поиска дубликатов в именах тестов')
  dublicate_group = dublicate_parser.add_argument_group (title='Параметры')
  dublicate_group.add_argument ('-tp', '--tests_path', required=True, type=str, help='Путь до папки с тестами', metavar='')
  dublicate_group.add_argument ('--debug', action='store_const', const=True, default=False, 
                                 help='Сохранение дебажной информации в debug.log', metavar='')
  dublicate_group.add_argument ('-h', '--help', action="help", help='Справка')
       
  return parser_root


def main():
  parser = createParser()
  namespace = parser.parse_args() 
  if namespace.debug:
    print(namespace)
  
  if namespace.command == "tree":
    namespace.test_name = '[' + namespace.test_name + ']'

    if namespace.test:
      namespace.test_name = "Test11"
      

    test_path_list = testo_test_file(namespace.tests_path)
    if namespace.debug:
      with open("./debug.log", 'w', encoding='utf-8') as file:
        file.write("\nTEST PATH LIST\n")
        for i in test_path_list:
          file.write(i+"\n")


    if namespace.test:
      list_struct = config.list_struct_test3
    else:
      list_struct = testo_parser(test_path_list)
      list_struct = list_struct_with_bracket(list_struct)
    if namespace.debug:
      with open("./debug.log", 'a', encoding='utf-8') as file:
        file.write("\nLIST_STRUCT\n")
        for i in list_struct:
          file.write(str(i)+"\n")
    
    

    list_lvl = lvl_qualifier_for_solo(namespace.test_name, list_struct)
    if namespace.debug:
      with open("./debug.log", 'a', encoding='utf-8') as file:
        file.write("\nLVL\n")
        for i in list_lvl:
          file.write(str(i)+"\n")


    list_with_space = space_add(list_lvl, list_struct)
    if namespace.debug:
      with open("./debug.log", 'a', encoding='utf-8') as file:
        file.write("\nSPACE\n")
        for i in list_with_space:
          file.write(str(i)+"\n")


    list_with_line = drow_line(list_lvl, list_with_space, list_struct )
    if namespace.debug:
      with open("./debug.log", 'a', encoding='utf-8') as file:
        file.write("\nLINE\n")
        for i in list_with_line:
          file.write(str(i)+"\n")

    list_with_line_NICE = del_last_space(list_with_line)
    if namespace.debug:
        with open("./debug.log", 'a', encoding='utf-8') as file:
          file.write("\nLINE_NICE\n")
          for i in list_with_line_NICE:
            file.write(str(i)+"\n")


    print("\nRESULT")
    for line in list_with_line_NICE:
      for obj in line:
        print(obj, end=" ")
      print()

  if namespace.command == "dubcheck":
    test_path_list = testo_test_file(namespace.tests_path)
    if namespace.debug:
      with open("./debug.log", 'w', encoding='utf-8') as file:
        file.write("\nTEST_PATH_LIST\n")
        for i in test_path_list:
          file.write(i+"\n")


    name_and_path_dict = name_and_path(test_path_list)
    if namespace.debug:
      
      with open("./debug.log", 'w', encoding='utf-8') as file:
        file.write("\nNAME_AND_PATH_DICT\n")
        for key, value in name_and_path_dict.items():          
          file.write(str(key) + " -- " + str(value) + "\n")

    print("\nRESULT")
    flag_have_dublicate = 0 # Проверка на нахождение хотя-бы одного дубликата
    for name in name_and_path_dict:
      if len(name_and_path_dict[name]) > 1:
        flag_have_dublicate = 1
        print()
        print(name)
        for enum,path in enumerate(name_and_path_dict[name]):
          if enum != len(name_and_path_dict[name]) - 1:
            print("  ├", path)
          else:
            print("  └", path)
    
    if flag_have_dublicate == 0:
      print("Дубликатов не найдено!")
            
          

if __name__ == "__main__":
  main()