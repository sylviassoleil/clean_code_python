''' non-local v.s. global '''
global counter
counter = 0
def update_counter():
    global counter
    counter+=1
    return counter

def update_counter_nonlocal():
    counter_nonlocal = 1
    def inner_count():
        nonlocal counter_nonlocal # inside the nested function
        counter_nonlocal+=1
        return counter_nonlocal
    while counter_nonlocal<5:
        inner_count()
        print(counter_nonlocal)

def mean():
    total = 0
    length = 0
    def _mean(number):
        nonlocal total, length # the variables are updated at each iteration
        print(id(total), id(length))
        total+=number
        length+=1
        return total/length
    return _mean


# Exception Variable Scope
lst = [1, 2, 3]
try:
    lst[4]
except Exception as err:
    print(err)
# this will raise the error: err is not defined
if __name__ == '__main__':
    pass
    update_counter() # 1
    counter = 5
    update_counter()  # counter 6

    current_mean = mean()
    current_mean(10) # 10
    current_mean(15)  # 12.5

