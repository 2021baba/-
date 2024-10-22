ZM = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
NUM = [1,2,3,4,5,6,7,8,9,10]
for i in ZM:
    for j in NUM:
        print(f'{i}- {j}')
        print('{}- {}'.format(i,j))
        print('%s- %d'%(i,j))