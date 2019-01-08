def sum_multiples(end_num):
    solution = []
    for num in range(1, end_num):
        if num % 3 == 0 or num % 5 == 0:
            solution.append(num)

    return sum(solution)

print(sum_multiples(1000))
