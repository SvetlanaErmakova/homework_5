import os #для проверки на пустоту файла
import math

def find_min_square(points):
    min_s=-1
    S=-1
    coord=[]
    f=len(points)
    for i in range(0, f-4, 2):
        for j in range(2, f-2,2):
            for k in range(4, f,2):
                S=square(points[i],points[i+1],points[j],points[j+1],points[k],points[k+1])

                if(S>0 and min_s<0): #первый раз точки не лежащие на одной прямой => инициализировать min_s
                  min_s=S

                if(S>0 and min_s>=S ):
                    min_s=S
                    coord=[points[i], points[i+1], points[j], points[j+1], points[k], points[k+1] ] 

    return min_s, coord 

def square(x1, y1, x2, y2, x3, y3):#если точки на одной прямой возвращает -1
    a=[x1-x2, y1-y2]
    b=[x3-x2, y3-y2]
    c=[x1-x3, y1-y3]
    m_a=math.sqrt(a[0]**2+a[1]**2)
    m_b=math.sqrt(b[0]**2+b[1]**2)
    m_c=math.sqrt(c[0]**2+c[1]**2)
    p=(m_a+m_b+m_c)/2

    if(a[0]*b[1]-a[1]*b[0]==0): #векторы коллиниарны, определитель=0
        return -1
    else:
        return math.sqrt(p*(p-m_a)*(p-m_b)*(p-m_c)) #площадь треугольника
# автотест
def autotest():
    #1ый
    points_s1 = read_file("autotest1.txt")#массив координат точек
    points1=[]
    for elt in points_s1:
        points1.append(int(elt))
    rez1=find_min_square(points1)

    #2ой
    points_s2 = read_file("autotest2.txt")#массив координат точек
    points2=[]
    for elt in points_s2:
        points2.append(int(elt))
    rez2=find_min_square(points2)


    return (round(rez1[0],3) ==  0.5 and round(rez2[0],3) == 4.5) 

def read_file(filename):
    try:
        file=open(filename)
    except OSError:
        return 'er'

    if(os.stat(filename).st_size == 0): #проверка на пустоту файла
         return 'er2'

    return file.read().split(',') 

if autotest():
    print("Autotest are succesfully completed!")

    filename=input("Input file name: \n")
    #filename="data.txt"
    points_s = read_file(filename)#массив координат точек
    points=[]
    for elt in points_s:
        points.append(int(elt))
    
    if(points_s=='er'):
        print("Error! Cannot open file! ")
    elif(points_s=='er2'):
        print("Error! Empty file! ")
    elif(len(points)%2!=0):
        print("Error! Odd number of coordinates! ")#если нечетное число координат точек
    elif(len(points)/2 <3):
        print("Error! For a triangle you need at least 3 points! ")
    else:
        rez=find_min_square(points)
        print("Triangle with a minimum square:{0} is formed by points: {1}".format(round(rez[0],2), rez[1])) 
    
else:
    print("Autotest failed")  # автотесты не прошли


