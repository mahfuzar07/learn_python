value = input().split(" ")
a, b, c = value

greatest = (int(a) + int(b) + abs(int(a) - int(b)))  / 2
result = (int(greatest) + int(c) + abs(int(greatest) - int(c)))/2

print(f"{result:.0f} eh o maior")