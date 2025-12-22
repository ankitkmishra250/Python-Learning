n = 3;

for i in range(1,11):
    if i == 5:
        print(f"{i} is skipped");
        continue;
    print(f"{n} * {i} = {n*i}");