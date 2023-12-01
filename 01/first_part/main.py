import re

result = 0

with open('data.txt') as file:
    lines = file.readlines()
    for line in lines:
        numbers = re.findall(r'\d+', line)

        if len(numbers) > 1:
            first = numbers[0][0]
            second = numbers[-1][-1]
            line_result = first + second
        elif len(numbers[0]) > 1:
            line_result = numbers[0][0] + numbers[0][-1]
        else:
            line_result = numbers[0][0] + numbers[0][0]

        result = result + int(line_result)

print(f"Result : {result}")
