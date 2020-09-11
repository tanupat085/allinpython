# Copy File
# Choose My Type file



# Choose Local Disk



# print(' Do you want to keep stealing files? ')
# print(' if you want to Choose [1]')
# print(" if you dont want to Choose [2]")

# T2 = str(input('Choose [1] or [2] : '))

# if ('1' or '[1]') in T2 :

#     B = str(input('Enter Local path files : '))
#     E = str(input('Enter Paste Local Disk : '))
#     T3 = str(input('Enter Type file : ')).lower()

#     path = r'{}'.format(B)
#     destination = '{}:\\'.format(E)

#     for f in allfile:
#         if f[-len(T3):] == T3 :
#             source = os.path.join(path,f)
#             dest = os.path.join(destination,f)
#             print(source)
#             print(dest)
#             shutil.move(source,dest)
#             print('----')
# else :
#     exit()

import os
import shutil
def main():
    A = str(input('Enter Local path files : '))
    P = str(input('Enter Paste Local Disk : '))
    T1 = str(input('Enter Type file : ')).lower()

    path = r'{}'.format(A)
    destination = '{}:\\'.format(P)

    allfile = os.listdir(path)

    for f in allfile:
        if f[-len(T1):] == T1 :
            source = os.path.join(path,f)
            dest = os.path.join(destination,f)
            print(source)
            print(dest)
            shutil.move(source,dest)
            print('----')
    print(te)

test = int(input('case  : '))

if test == 1 :
    main()
    
elif test != 1 :
    exit()


