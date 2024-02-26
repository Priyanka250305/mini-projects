l1=['a','b','c'] 
l2=['d','e','f']
l3=['g','h','i']
z=[l1,l2,l3]
for i in range(1,10):
    if i in [1,3,5,7,9]:
        a=input('enter a,b:')
        a=a.split(' ')
        k=z[int(a[0])]
        k[int(a[1])]='X'
        for i in z:
            print(i)
        d1=[l1[0],l2[1],l3[2]]
        d2=[l1[2],l2[1],l3[0]]
        c1=[l1[0],l2[0],l3[0]]
        c2=[l1[1],l2[1],l3[1]]
        c3=[l1[2],l2[2],l3[2]]
        if l3[0]==l3[1] and l3[1]==l3[2] and l3[1]=='X':
            print("user1 won!")
            break
        elif l2[0]==l2[1]and l2[1]==l2[2] and l2[1]=='X':
            print("user1 won!")
            break
        elif l1[0]==l1[1] and l1[2]==l1[1] and l1[1]=='X':
            print("user1 won!")
            break
        elif d1[0]==d1[1] and d1[1]==d1[2] and d1[1]=='X':
            print("user1 won!")
            break
        elif d2[0]==d2[1]and d2[1]==d2[2] and d2[1]=='X':
            print("user1 won!")
            break
        elif c1[0]==c1[1] and c1[2]==c1[1] and c1[1]=='X':
            print("user1 won!")
            break
        elif c2[0]==c2[1] and c2[2]==c2[1] and c1[1]=='X':
            print("user1 won!")
            break
        elif c3[0]==c3[1] and c3[2]==c3[1] and l1[1]=='X':
            print("user1 won!")
            break
    else:
        a=input('enter a,b:')
        a=a.split(' ')
        k=z[int(a[0])]
        k[int(a[1])]='O'
        for i in z:
            print(i)
        d1=[l1[0],l2[1],l3[2]]
        d2=[l1[2],l2[1],l3[0]]
        c1=[l1[0],l2[0],l3[0]]
        c2=[l1[1],l2[1],l3[1]]
        c3=[l1[2],l2[2],l3[2]]
        if l3[0]==l3[1] and l3[1]==l3[2]:
            print("user2 won!")
            break
        if l2[0]==l2[1]and l2[1]==l2[2]:
            print("user2 won!")
            break
        if l1[0]==l1[1] and l1[2]==l1[1]:
            print("user2 won!")
            break
        if d1[0]==d1[1] and d1[1]==d1[2]:
            print("user2 won!")
            break
        if d2[0]==d2[1]and d2[1]==d2[2]:
            print("user2 won!")
            break
        if c1[0]==c1[1] and c1[2]==c1[1]:
            print("user2 won!")
            break
        if c2[0]==c2[1] and c2[2]==c2[1]:
            print("user2 won!")
            break
        if c3[0]==c3[1] and c3[2]==c3[1]:
            print("user2 won!")
            break