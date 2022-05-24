import random

# dobás
v=random.randint(1,2)
if v==1:
    e='I'
else:
    e='F'
print('1. feladat\nA pénzfeldobás eredménye:',e)

#2. feladat tipp bekérése
v=random.randint(1,2)
if v==1:
       e='I'
else:
    e='F'
t=input('2. feladat\nTippeljen! (F/I)= ')
print('A tipp ',t,', a dobás eredménye ',e,' volt.',sep='')
if e==t:
    print('Ön eltalálta!')
else:
    print('Ön nem találta el!')

#3.feladat hány dobásból állt a kísérlet
f=open('kiserlet.txt')
db=0
for i in f:
    db+=1
print('3. feladat\nA kísérlet',db,'dobásból állt.')

#4.feladat, relatív gyakoriság
f=open('kiserlet.txt')
dbF=0
for i in f:
    if i[0]=='F':
        dbF +=1
print('4. feladat\nA kísérlet során a fej relatív gyakorisága: ',round(dbF*100/db,2),'% volt.', sep='')
f.close()

#5.feladat: két fej egymás után
print('5. feladat')
f=open('kiserlet.txt')
dbFF=0
i=0
s1=s2=s3=s4=''

for sor in f:
    i+=1
    if i==1:
       s1=sor
    elif i==2:
        s2=sor
    elif i==3:
        s3=sor
    else:
        s4=sor
    if i==4:
        if s1=='I\n' and s2=='F\n' and s3=='F\n' and s4=='I\n':
            dbFF+=1
     
        s1=s2
        s2=s3
        s3=s4
        s4=''
        i=3

print('A kisérlet során', dbFF,'alkalommal dobtak pontosan két fejet egymás után.')
f.close
