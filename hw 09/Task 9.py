numbers = [23,56,44,345,237,89,5789]
def stop_237(numbers):
    for i in numbers:
        if i%2 == 0:
            if i == 237:
                break
            print(i)

stop_237(numbers)