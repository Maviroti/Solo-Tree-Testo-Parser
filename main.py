
import argparse
from helpers import lvl_qualifier_for_solo, space_add, drow_line, del_last_space, testo_parser, testo_test_file
import config


def createParser():
  parser = argparse.ArgumentParser(prog=config.main_name, description=config.main_description, epilog=config.main_copyright, add_help=False)        
  parser.add_argument ('-h', '--help', action="help", help='Справка')
  parser.add_argument ('--version', action='version', help='Версия скрипта', version='Script %(prog)s version {}'.format(config.main_version))
  parser.add_argument ('--debug', action='store_const', const=True, default=False, help='Вывод дебажной информации', metavar='')
  parser.add_argument ('--test', action='store_const', const=True, default=False, help='Тестовый запуск', metavar='')
  parser.add_argument ('-tp', '--tests_path', required=True, type=str, help='Путь до папки с тестами', metavar='')
  parser.add_argument ('-tn', '--test_name', required=True, type=str, help='Название теста', metavar='')    
  return parser


def main():
  parser = createParser()
  namespace = parser.parse_args() 

  if namespace.test:
    namespace.test_name = "Test11"
    list_struct = config.list_struct_test3

  test_path_list = testo_test_file(namespace.tests_path)
  list_struct = testo_parser(test_path_list)
  list_lvl = lvl_qualifier_for_solo(namespace.test_name, list_struct)
  list_with_space = space_add(list_lvl, list_struct)
  list_with_line = drow_line(list_lvl,list_with_space, list_struct )
  list_with_line_NICE = del_last_space(list_with_line)

  if namespace.debug:
    print("debug info \n===================================")
    print("\nTEST PATH LIST")
    print(test_path_list)

    print("\nLIST_STRUCT")
    print(list_struct)

    print("\nLVL")
    print(list_lvl)

    print("\nSPACE")
    print(list_with_space)

    print("\nLINE")
    print(list_with_line)

    print("\nLINE_NICE\n")
    print(list_with_line_NICE)
    print("\n===================================")


  print("\nRESULT")
  for line in list_with_line_NICE:
    for obj in line:
      print(obj, end=" ")
    print()


if __name__ == "__main__":
  main()