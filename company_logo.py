from collections import Counter
n=list(input())
n.sort()
x=Counter(n)
for letter,count in (x.most_common(3)):
    print(letter,count)
