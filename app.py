from flask import Flask
from functools import reduce

app = Flask(__name__)


@app.route("/")
def hello_world():
    return "<h1>Portfolio-App</h1>"


@app.route("/A1G", methods=['GET'])
def A1G():
    list_1 = [1, 2, 3, 4, 5, 6]

    def sum_of_list(list_obj):
        return sum(list_obj)

    result = sum_of_list(list_1)
    return f'the sum is: {result}'


@app.route("/A1F", methods=['GET'])
def A1F():
    NUMBER_1 = 7
    tuple_1 = (1, 2, 3, 4, 5, 6)

    def add_item_to_tuple(tuple_obj, number):
        try:
            tuple_obj += number
        except Exception as error:
            return f'{error}'

    result = add_item_to_tuple(tuple_1, NUMBER_1)

    return f'{result}'


@app.route("/A1E", methods=['GET'])
def A1E():
    list_1 = [1, 2, 4, 6, 7]

    def funktional(list_obj):
        return sum(list_obj)

    def prozedual(list_obj):
        summe = 0
        for i in list_obj:
            summe += i
        return summe

    return f'{funktional(list_1)}'


@app.route("/B1G", methods=["GET"])
def B1G():
    def bubblesort(arr):
        n = len(arr)
        for i in range(n):
            for j in range(0, n - i - 1):
                if arr[j] > arr[j + 1]:
                    arr[j], arr[j + 1] = arr[j + 1], arr[j]

    nums_bef = [24, 577, 124, 55, 34, 21, 666]
    nums = [24, 577, 124, 55, 34, 21, 666]
    bubblesort(nums)
    return f"Before: {nums_bef} <br>After: {nums}"


@app.route("/B1F", methods=["GET"])
def B1F():
    def bubble_pass(lst):
        if len(lst) <= 1:
            return lst
        if lst[0] > lst[1]:
            return [lst[1]] + bubble_pass([lst[0]] + lst[2:])
        return [lst[0]] + bubble_pass(lst[1:])

    def sorting(lst, n=None):
        if n is None:
            n = len(lst)
        if n == 1:
            return lst
        lst = bubble_pass(lst)
        return sorting(lst, n - 1)

    nums = [245, 555, 1343, 5745, 2, 21, 333]

    sorted_list = sorting(nums)

    return f"Before: {nums} After: {sorted_list}"


@app.route("/B1E", methods=["GET"])
def B1E():
    def new_squares(lst):
        result_nums = list(filter(lambda x: x % 2 == 0, map(lambda x: x ** 2, lst)))
        return result_nums

    numbers = [0, 3, 5, 6, 7]
    new_numbers = new_squares(numbers)

    return f"Even squares: {new_numbers}"


@app.route("/B2G", methods=["GET"])
def B2G():
    def square(x):
        return x ** 2

    square_of_number = square

    result = square_of_number(10)
    return f"{result}"


@app.route("/B2F", methods=["GET"])
def B2F():
    def doubler(x):
        return x * 2

    def minus_double(number, func):
        return number - func(number)

    return f"{minus_double(5, doubler)}"


@app.route("/B2E", methods=["GET"])
def B2E():
    def power(exp):
        def number_by_power(number):
            return number ** exp

        return number_by_power

    power_of_5 = power(5)

    return f"{power_of_5(10)}"


@app.route("/B3G", methods=["GET"])
def B3G():
    string = "abfdjsfkdsfe fefdsf efes"

    def uppercase(text):
        to_upper = lambda x: x.upper()
        return to_upper(text)

    return f"lower: {string} upper: {uppercase(string)}"


@app.route("/B3F", methods=["GET"])
def B3F():
    def multiply_pairs(number1, number2):
        new_number = lambda x, y: x * y
        return new_number(number1, number2)

    return f"result: {multiply_pairs(5, 255)}"


@app.route("/B3E", methods=['GET'])
def B3E():
    numbers = [1, 2, 3, 4]

    def showcase(numbers_list):
        if sum(map(lambda x: x ** 2, numbers_list)) > sum(numbers_list):
            return 'bigger'
        else:
            return 'smaller'

    return showcase(numbers)


@app.route("/B4G", methods=['GET'])
def B4G():
    numbers = [1, 2, 3, 4]

    def map_funk(numbers_list):
        square = map(lambda x: x ** 2, numbers_list)
        return square

    def filter_funk(numbers_list):
        even = filter(lambda x: x % 2 == 0, numbers_list)
        return even

    def reduce_funk(numbers_list):
        number_sum = reduce(lambda x, y: x + y, numbers_list)
        return number_sum

    return f'Map: {list(map_funk(numbers))}\nFilter:{list(filter_funk(numbers))}\nReduce:{reduce_funk(numbers)}'


@app.route("/B4F", methods=['GET'])
def B4F():
    numbers = [1, 2, 3, 4]

    def combined_funk(numbers_list):
        square_even_sum = reduce(lambda x, y: x + y, filter(lambda x: x % 2 == 0, map(lambda x: x ** 2, numbers_list)))
        return square_even_sum

    return f'Combined: {combined_funk(numbers)}'


@app.route("/B4E", methods=['GET'])
def B4E():
    test_json = [
        {
            "name": "Alice",
            "grade": 4.0
        },
        {
            "name": "Bob",
            "grade": 3.5
        },
        {
            "name": "Charlie",
            "grade": 4.25
        },
        {
            "name": "David",
            "grade": 5.5
        },
        {
            "name": "Manuel",
            "grade": 3.75
        }
    ]

    def complex_funk(json):
        updated_students = list(filter(lambda student: student["grade"] > 4.5,
                                       map(lambda student: {**student, "grade": student["grade"] + 1}, json)))
        return updated_students

    return complex_funk(test_json)


@app.route("/C1G", methods=['GET'])
def C1G():
    def args_sum_all(*args):
        return sum(args)

    def kwargs_print_info(**kwargs):
        for key, value in kwargs.items():
            return f"{key}: {value}"

    def closure_outer_function(x):
        def closure_inner_function(y):
            return x + y

        return closure_inner_function

    closure_add_five = closure_outer_function(5)
    closure_add_five(3)

    kwargs_print_info(name="Alice", age=30)
    args_sum_all(1, 2, 3, 4)

    return str(args_sum_all(1, 2, 3, 4))


@app.route("/C1F", methods=['GET'])
def C1F():
    def sum_all(x, y, z):
        return x + y + z

    def refactored_sum_all(*args):
        return sum(args)

    return str(refactored_sum_all(1, 2, 3, 4, 5))


@app.route("/C1E", methods=['GET'])
def C1E():
    def sum_all(x, y, z):
        return x + y + z

    def refactored_sum_all(*args):
        return sum(args)

    return str(refactored_sum_all(1, 2, 3)) if refactored_sum_all(1, 2, 3) == sum_all(1, 2, 3) else str('Test failed')


if __name__ == '__main__':
    app.run(debug=True)
