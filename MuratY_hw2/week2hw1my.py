n=int(input("Pls enter an integer to find Lucky Numbers: "))
numbers=[x+1 for x in range(n)]
freq=2
while freq < len(numbers):
    del numbers[freq-1::freq]
    freq += 1
    #print(numbers)
print("Lucky Numbers :",numbers)
    