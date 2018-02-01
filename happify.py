number = str(input('What number would you like to \'Hapify\': '))
number = list(number)

happy = 0

for i in range(len(number)):
    happy = happy + (int(number[i])*int(number[i]))

print(happy)
