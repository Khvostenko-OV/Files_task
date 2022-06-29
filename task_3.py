files_number = 3
files_names = ['1.txt', '2.txt', '3.txt']
data = []

for i in range(files_number):
    with open(files_names[i], encoding='utf-8') as file:
        lines = file.readlines()
    lines[-1] += '\n'
    data.append([files_names[i] + '\n', str(len(lines)) + '\n'] + lines)

data.sort(key=len)

with open('sorted_result.txt', 'w', encoding='utf-8') as file:
    for d in data:
        file.writelines(d)
