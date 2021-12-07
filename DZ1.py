def angle(a,b,c): #Считает косинус угла, лежащего напротив большей стороны
    maxstorona=max(a,b,c)
    minstorona=min(a,b,c)
    sredsotona=0
    if a>=minstorona and a<=maxstorona:
        sredstorona=a
    if b>=minstorona and b<=maxstorona:
        sredstorona=b
    if c>=minstorona and c<=maxstorona:
        sredstorona=c
    cos=(minstorona+sredstorona-maxstorona)/(2*sredstorona*minstorona)
    return cos

a=int(input('Введите сторону треугольника: '))
b=int(input('Введите сторону треугольника: '))
c=int(input('Введите сторону треугольника: '))

if a+b>c and a+c>b and c+b>a:
    if a==b and b==c:
        print('Треугольник равносторонний')
    elif a==b or b==c or a==c:
        print('Треугольник равнобедренный')
    else:
        print('Треугольник произвольный')

    if angle(a,b,c) > 0:
        print('Треугольник остроугольный')
    elif angle(a,b,c) == 0:
        print('Треугольник прямоугольный')
    else:
        print('Треугольник тупоугольный')
else:
    print('Нельзя построить треугольник')
    
