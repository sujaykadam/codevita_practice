import itertools
tc=int(input())
for i in range(tc):
	flag=0
	n=int(input())
	arr = [int(x) for x in input().split()]
	combo=list(itertools.combinations(arr,2))
	for j in combo:
		if((j[0]+j[1]%3!=0)):
			flag=1
			break
	if(flag==1):
		print("Yes")
	else:
		print("No")