def welcome():
    print(' \t\t\t ++=>WELCOME TO 2048<=++')
    print(''' Rules: \n1. Press "w" to move the row up.\n2. Press "d" to move the row right.\n3. Press "s" to move the row down.\n4. Press "a" to move the row left.''')
    print('==================================')

def startup():
    global arr
    arr=[[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0]]
    import random
    cho=[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,2,0,0,0,2,0,0,0,0,0,4,0,0]
    global arr2
    arr2=[]
    for key in arr:
        l=[]
        for ele in key:
            s=random.randint(0,len(cho)-1)
            ele=cho[s]
            l.append(ele)
        arr2.append(l)
    if arr2==[[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0]]:
        startup()

def interface():
    
    print('\t===============')
    print('\n',end='')
    for key in arr2:
        print('\t',end='')
        for ele in key:
            if ele!=0:
                print('[{}]'.format(ele),end=' ')
            else:
                print('[ ]',end=' ')
                
        print('\n')
    print('\t===============')
    print('\t===============')

def get_value():
    global user_value
    user_value=input('Choose:')
    if user_value not in ['a','A','s','S','d','D','w','W']:
        user_value=None
        print('wrong input')
        get_value()
'''
def logic():
    if user_value in ['w','W']:
'''




startup()
welcome()
interface()
#get_value()
#logic()