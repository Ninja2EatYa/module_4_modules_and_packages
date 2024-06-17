#  Наверное это едиcтвенный корректный способ вызвать inner_function ВНЕ функции test_function, т.к. другие варианты вызова в принципе нарушают правила оформления кода. В данном варианте вызова test_fucntion просто не видит результата работы вложенной функции.

def test_function():
    def inner_function():
        print('Я в области видимости функции test_function')
        return inner_function()


test_function()

#  Корректный вызов:
def test_function():
    def inner_function():
        print('Я в области видимости функции test_function')

    return inner_function()


test_function()
