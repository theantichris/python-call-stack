def sum_to_one(n):
    result = 1
    call_stack = []

    while n is not 1:
        execution_context = {"n_value": n}
        call_stack.append(execution_context)
        n -= 1
        print(call_stack)

    print("BASE CASE REACHED")

    while len(call_stack) is not 0:
        return_value = call_stack.pop()
        print(call_stack)

    return result, call_stack

sum_to_one(4)