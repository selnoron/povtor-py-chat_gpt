from models import printf


## 1
def get_age() -> str:
    age: str = input()
    if not age.isnumeric():
        return "number"
    return f"I'm {age} yo"

printf(get_age())

## 2
def get_evodd() -> str:
    num: str = input()
    if not num.isnumeric():
        return "number"
    if int(num) % 2 == 0:
        return f"number {num} is even"
    else:
        return f"number {num} is odd"

printf(get_evodd()) 

## 3
def get_even_array() -> list:
    return [i for i in range(1, 11) if i % 2 == 0]

printf(get_even_array()) 

## 4
def get_sum_of_array() -> list:
    return sum([i for i in range(101)])

printf(get_sum_of_array()) 

## 5
age: str = input("age - ")
name: str = input("name - ")

def get_info(name: str, age: int) -> str:
    if not age.isnumeric():
        return "age must be number"
    return f"I'm {name}, I'm {age} yo"

printf(get_info(name, age))

## 6
num: str = input()

def check_num(num: str) -> str:
    try:
        return f"result - {round(float(num))}"
    except:
        return "input is not number"

printf(check_num(num))

## 7
# Это задание сделал мой chatGPT :D
def compare_numbers(num1: int, num2: int) -> str:
    """
    Compares two numbers and returns a message
    :param num1: first number
    :param num2: second number
    :return: message
    """
    if num1 > num2:
        return "Первое число больше второго"
    elif num1 < num2:
        return "Второе число больше первого"
    else:
        return "Числа равны"

num1 = int(input("Введите первое число: "))
num2 = int(input("Введите второе число: "))
printf(compare_numbers(num1, num2))

## 8
arr1: list[str] = ["HEllo", "GoodBYE"]
print(*arr1, sep="\n")
printf('')

## 9
num = int(input())
for i in range(1, int(((500 / 5) / 10) + 1)):
    print(f"{num} * {i} = {num * i}")
printf('')