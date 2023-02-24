a = ['s', 'u', 'f', 't', 'z', 'w']
a.sort(reverse=True)

for i , j in enumerate(a):
    row = f"{i+1}.{j.capitalize()}"
    print(row)
