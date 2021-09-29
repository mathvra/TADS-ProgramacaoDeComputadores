while True:
	N = int(input())

	if (N == 0):
		break

	jogadas = list(map(int,input().split()))
	maryWin = 0
	johnWin = 0
	for v in jogadas:
		if(v == 0):
			maryWin += 1
		else:
			johnWin += 1
	print("Mary won {} times and John won {} times" .format(maryWin,johnWin))