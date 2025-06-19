from circular_linked_list import CircularLinkedList
from array_list import ArrayList

def print_menu():
    print("\nМеню:")
    print("1. Додати елемент")
    print("2. Вставити елемент за індексом")
    print("3. Отримати елемент за індексом")
    print("4. Видалити елемент за індексом")
    print("5. Видалити всі елементи зі значенням")
    print("6. Знайти перший індекс значення")
    print("7. Знайти останній індекс значення")
    print("8. Перевернути список")
    print("9. Клонувати список")
    print("10. Розширити іншим списком")
    print("11. Очистити список")
    print("12. Вивести довжину")
    print("13. Вивести весь список")
    print("14. Вийти")

def print_full_list(lst):
    try:
        values = [lst.get(i) for i in range(lst.length())]
        print("Список:", values)
    except:
        print("Список: []")

def interactive_mode(lst):
    print("\nВведіть початкові елементи списку через пробіл:")
    initial_input = input("> ")
    for ch in initial_input.strip().split():
        lst.append(ch)
    print_full_list(lst)

    while True:
        print_menu()
        choice = input("Оберіть опцію: ")

        try:
            if choice == '1':
                val = input("Введіть символ: ")
                lst.append(val)
            elif choice == '2':
                val = input("Символ: ")
                idx = int(input("Індекс: "))
                lst.insert(val, idx)
            elif choice == '3':
                idx = int(input("Індекс: "))
                print("Елемент:", lst.get(idx))
            elif choice == '4':
                idx = int(input("Індекс: "))
                print("Видалено:", lst.delete(idx))
            elif choice == '5':
                val = input("Значення: ")
                lst.deleteAll(val)
            elif choice == '6':
                val = input("Значення: ")
                print("Перший індекс:", lst.findFirst(val))
            elif choice == '7':
                val = input("Значення: ")
                print("Останній індекс:", lst.findLast(val))
            elif choice == '8':
                lst.reverse()
            elif choice == '9':
                clone = lst.clone()
                print("Клоновано. Довжина клону:", clone.length())
            elif choice == '10':
                print("Додавання ['x','y','z']")
                ext = CircularLinkedList() if isinstance(lst, CircularLinkedList) else ArrayList()
                for ch in ['x', 'y', 'z']:
                    ext.append(ch)
                lst.extend(ext)
            elif choice == '11':
                lst.clear()
            elif choice == '12':
                print("Довжина:", lst.length())
            elif choice == '13':
                print_full_list(lst)
            elif choice == '14':
                break
            else:
                print("Невідома команда")
        except Exception as e:
            print("Помилка:", e)

        print_full_list(lst)

if __name__ == "__main__":
    print("Оберіть тип списку:")
    print("1. Однозв'язний кільцевий список")
    print("2. Список на масиві")
    t = input("Ваш вибір: ")
    if t == '1':
        structure = CircularLinkedList()
    else:
        structure = ArrayList()

    interactive_mode(structure)

