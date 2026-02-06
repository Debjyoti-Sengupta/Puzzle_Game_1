import os
import random
import sys
input_path=sys.argv[1]
output_path=sys.argv[2]
fin=open(input_path,'r')
size=int(fin.readline())
farm=fin.readlines()
hays=0; ponds=0; hpos_list=[]; ppos_list=[]; Cows=[]
for i in range(size):
    hays+=farm[i].count('@')
    ponds+=farm[i].count('#')
    if (farm[i].count('@')!=0):
        nxt1=0
        for j in range(farm[i].count('@')):
            hpos=farm[i].find('@',nxt1)
            hpos_list.append((i,hpos))
            nxt1=hpos+1
    if (farm[i].count('#')!=0):
        nxt2=0
        for j in range(farm[i].count('#')):
            ppos=farm[i].find('#',nxt2)
            ppos_list.append((i,ppos))
            nxt2=ppos+1
#print('Size:',size,'Haystacks:',hays,'Ponds:',ponds,'HayPos:',hpos_list,'PondPos:',ppos_list)
while len(Cows)!=hays:
    CowPos=(random.randint(0,size-1),random.randint(0,size-1))
    if (CowPos not in hpos_list) and (CowPos not in ppos_list) and (CowPos not in Cows):
        Cows.append(CowPos)
#print(Cows)
fout=open(output_path,'w')
fout.write(str(size)+'\n')
farmout=[]
for i in range(size):
    farmout.append([])
for i in range(size):
    for j in range(size):
        farmout[i].append(0)

for i in range(size):
    for j in range(size):
        if (i,j) in Cows:
            farmout[i][j]='C'
        elif (i,j) in hpos_list:
            farmout[i][j]='@'
        elif (i,j) in ppos_list:
            farmout[i][j]='#'
        else:
            farmout[i][j]='.'
    farmout[i].append('\n')
farmwc=[]
for i in range(size):
    str1=''
    str1=str1.join(farmout[i])
    farmwc.append(str1)
fout.writelines(farmwc)
totalsc=0
for (i,j) in Cows:
    nhay=0; npond=0; ncow=0; cowsc=0;
    if i!=0 and j!=0 and i!=(size-1) and j!=(size-1):
        for k in [j-1,j,j+1]:
            if farmout[i-1][k]=='@' and k==j:
                nhay+=1
            elif farmout[i-1][k]=='#' and k==j:
                npond+=1
            elif farmout[i-1][k]=='C':
                ncow+=1
        for k in [j-1,j+1]:
            if farmout[i][k]=='@':
                nhay+=1
            elif farmout[i][k]=='#':
                npond+=1
            elif farmout[i][k]=='C':
                ncow+=1
        for k in [j-1,j,j+1]:
            if farmout[i+1][k]=='@' and k==j:
                nhay+=1
            elif farmout[i+1][k]=='#' and k==j:
                npond+=1
            elif farmout[i+1][k]=='C':
                ncow+=1
    if i==0 and j==0:
        for k in [j+1]:
            if farmout[i][k]=='@':
                nhay+=1
            elif farmout[i][k]=='#':
                npond+=1
            elif farmout[i][k]=='C':
                ncow+=1
        for k in [j,j+1]:
            if farmout[i+1][k]=='@' and k==j:
                nhay+=1
            elif farmout[i+1][k]=='#' and k==j:
                npond+=1
            elif farmout[i+1][k]=='C':
                ncow+=1
    if i==0 and j==size-1:
        for k in [j-1]:
            if farmout[i][k]=='@':
                nhay+=1
            elif farmout[i][k]=='#':
                npond+=1
            elif farmout[i][k]=='C':
                ncow+=1
        for k in [j-1,j]:
            if farmout[i+1][k]=='@' and k==j:
                nhay+=1
            elif farmout[i+1][k]=='#' and k==j:
                npond+=1
            elif farmout[i+1][k]=='C':
                ncow+=1
    if i==size-1 and j==0:
        for k in [j,j+1]:
            if farmout[i-1][k]=='@' and k==j:
                nhay+=1
            elif farmout[i-1][k]=='#' and k==j:
                npond+=1
            elif farmout[i-1][k]=='C':
                ncow+=1
        for k in [j+1]:
            if farmout[i][k]=='@':
                nhay+=1
            elif farmout[i][k]=='#':
                npond+=1
            elif farmout[i][k]=='C':
                ncow+=1
    if i==size-1 and j==size-1:
        for k in [j-1,j]:
            if farmout[i-1][k]=='@' and k==j:
                nhay+=1
            elif farmout[i-1][k]=='#' and k==j:
                npond+=1
            elif farmout[i-1][k]=='C':
                ncow+=1
        for k in [j-1]:
            if farmout[i][k]=='@':
                nhay+=1
            elif farmout[i][k]=='#':
                npond+=1
            elif farmout[i][k]=='C':
                ncow+=1
    if i==0 and j!=0 and j!=size-1:
        for k in [j-1,j+1]:
            if farmout[i][k]=='@':
                nhay+=1
            elif farmout[i][k]=='#':
                npond+=1
            elif farmout[i][k]=='C':
                ncow+=1
        for k in [j-1,j,j+1]:
            if farmout[i+1][k]=='@' and k==j:
                nhay+=1
            elif farmout[i+1][k]=='#' and k==j:
                npond+=1
            elif farmout[i+1][k]=='C':
                ncow+=1
    if i==size-1 and j!=0 and j!=size-1:
        for k in [j-1,j,j+1]:
            if farmout[i-1][k]=='@' and k==j:
                nhay+=1
            elif farmout[i-1][k]=='#' and k==j:
                npond+=1
            elif farmout[i-1][k]=='C':
                ncow+=1
        for k in [j-1,j+1]:
            if farmout[i][k]=='@':
                nhay+=1
            elif farmout[i][k]=='#':
                npond+=1
            elif farmout[i][k]=='C':
                ncow+=1
    if j==0 and i!=0 and i!=size-1:
        for k in [j,j+1]:
            if farmout[i-1][k]=='@' and k==j:
                nhay+=1
            elif farmout[i-1][k]=='#' and k==j:
                npond+=1
            elif farmout[i-1][k]=='C':
                ncow+=1
        for k in [j+1]:
            if farmout[i][k]=='@':
                nhay+=1
            elif farmout[i][k]=='#':
                npond+=1
            elif farmout[i][k]=='C':
                ncow+=1
        for k in [j,j+1]:
            if farmout[i+1][k]=='@' and k==j:
                nhay+=1
            elif farmout[i+1][k]=='#' and k==j:
                npond+=1
            elif farmout[i+1][k]=='C':
                ncow+=1
    if j==size-1 and i!=0 and i!=size-1:
        for k in [j-1,j]:
            if farmout[i-1][k]=='@' and k==j:
                nhay+=1
            elif farmout[i-1][k]=='#' and k==j:
                npond+=1
            elif farmout[i-1][k]=='C':
                ncow+=1
        for k in [j-1]:
            if farmout[i][k]=='@':
                nhay+=1
            elif farmout[i][k]=='#':
                npond+=1
            elif farmout[i][k]=='C':
                ncow+=1
        for k in [j-1,j]:
            if farmout[i+1][k]=='@' and k==j:
                nhay+=1
            elif farmout[i+1][k]=='#' and k==j:
                npond+=1
            elif farmout[i+1][k]=='C':
                ncow+=1
    if nhay!=0:
        cowsc+=1
    if nhay!=0 and npond!=0:
        cowsc+=2
    if ncow!=0:
        cowsc-=3
    totalsc+=cowsc
fout.write(str(totalsc))
fout.write('\n')
fin.close()
fout.close()

