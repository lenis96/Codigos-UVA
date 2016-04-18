# Problema UVA 10063	Knuth's Permutation
from sys import stdin
def solve(cad,n):
	if(n==len(cad)):
		print("".join(cad))
	else:
		for i in range(n+1):
			cad.insert(i,cad.pop(n))
			solve(cad,n+1)
			cad.insert(n,cad.pop(i))
	
def main():
	line=stdin.readline().strip()
	while (len(line)!=0):
		solve(list(line),1)
		line=stdin.readline().strip()
		if(len(line)!=0):print("")
main()