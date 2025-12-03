num = int(input())
max_val = num
while num != 0:
  if num > max_val:
    max_val = num
  num = int(input())
print(max_val)
