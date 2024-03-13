# Author: Cameron F. Abrams, <cfa22@drexel.edu>

import argparse as ap
def rbd(I:int):
    """Recursive binary decomposition of an integer I"""
    n=0
    while I%2==0:
        I//=2
        n+=1
    if I==1:
        return [n]
    return [n]+rbd(I-1)

def dbr(L):
    n=len(L)
    sum=0
    for i in range(n):
        x=0
        for j in range(i+1):
            x+=L[j]
        sum+=2**x
    return sum

if __name__=='__main__':
    parser=ap.ArgumentParser()
    parser.add_argument('I',type=int)
    # parser.add_argument('J',type=int)
    parser.add_argument('p',type=int,default=1)
    args=parser.parse_args()

    sumcounts={}

    for I in range(1,args.I):
        II=I**args.p
        L=rbd(II)
        J=dbr(L)
        s=sum(L)
        if not s in sumcounts:
            sumcounts[s]=0
        sumcounts[s]+=1
        print(f'{I:>10d} {II:>12d} {len(L):>4d} {s:>4d} {J:>12d} {L}')
    print('Sumcounts:')
    for k,v in sumcounts.items():
        print(f'{k}: {v}')
    # I=args.I 
    # L=rbd(I)
    # II=dbr(L)
    # print(f'I   {I:>12d} {len(L):>4d} {sum(L):>4d} {II:>12d} {L}')
    # J=args.J 
    # M=rbd(J)
    # JJ=dbr(M)
    # print(f'J   {J:>12d} {len(M):>4d} {sum(M):>4d} {JJ:>12d} {M}')
    # IJ=I+J
    # LM=rbd(IJ)
    # IIJJ=dbr(LM)
    # print(f'I+J {IJ:>12d} {len(LM):>4d} {sum(LM):>4d} {IIJJ:>12d} {LM}')
          

