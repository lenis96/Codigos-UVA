# Problema UVA 11085    Back to the 8-Queens
from sys import stdin
board=[None for i in range(8)]
t=[]
def safe(n,i):
        j,ans=0,True
        while(j<n and ans):
                if(board[j]==i):
                        ans=False
                if((n+i)-j<8 and board[j]==(n+i)-j):
                        ans=False
                if(j-(n-i)>=0 and board[j]==j-(n-i)):
                        ans=False
                j+=1
        return ans
def gen(n):
	global t
	if(n!=8):
		for i in range(8):
			if(safe(n,i)):
				board[n]=i
				gen(n+1)
	else:
		t.append(list(board))
def solve():
        global t
        diferencias=7
        for i in t:
                d=0
                j=0
                while j<8 and d<diferencias:
                        if(i[j]!=board[j]):d+=1
                        j+=1
                diferencias=min(d,diferencias)
        return diferencias
def main():
        global board
        line=stdin.readline()
        board=[int(i)-1 for i in line.split()]
        j=1
        while len(board)!=0:
                print("Case "+str(j)+": "+str(solve()))
                line=stdin.readline()
                board=[int(i)-1 for i in line.split()]
                j+=1
gen(0)
main()
