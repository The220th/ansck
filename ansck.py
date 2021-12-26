# -*- coding: utf-8 -*-

from typing import List
import sys

def letter2num(a : List[int]) -> str:
	'''
	Переводит число `a` в представлении листа (см. dec2sn) в число в этой системе счисления.

	Например:
	letter2num([15, 12, 8, 2]) вернёт "29CF"

	Если "букв" больше не "осталось", то вернёт None
	'''
	res = ""
	for i in range(len(a)):
		if(a[i] < 10):
			res += str(a[i])
		elif(a[i] < 36):
			res += chr(a[i] + 55)
		else:
			return None
	return res[::-1]

def num2letter(a : str) -> List[int]:
	'''
	Переводит число `a`, записанное в определённой системе счисления в число в виде листа (см. sn2dec).
	Такое число съест функция sn2dec

	Например:
	num2letter("29CF") вернёт [15, 12, 8, 2]
	'''
	res = []
	for c in a:
		if(48 <= ord(c) <= 57):
			res.append(int(c))
		else:
			res.append(ord(c)-55)
	return res[::-1]

def sn2dec(suf : int, a : List[int]) -> int:
	'''
	Переводит число `a` из системы счисления `suf` в число в десятичной системе счисления.

	Например:
	sn2dec(2, [1, 0, 0, 1, 1]) вернёт 25
	sn2dec(3, [1, 0, 1, 1]) вернёт 37
	sn2dec(123, [1, 16, 0, 15]) вернёт 27914974
	sn2dec(10, [7, 5, 3]) вернёт 357

	В аргументе `a` на позиции a[0] стоит самый младший разряд.
	'''
	res = 0
	for i in range(len(a)):
		res += int(a[i]*(suf**i))
	return res

def dec2sn(suf : int, a : int) -> List[int]:
	'''
	Переводит число `a` из десятичной системы счисления в число в системе счисления `suf`.

	Например:
	dec2sn(2, 25) вернёт [1, 0, 0, 1, 1]
	dec2sn(3, 37) вернёт [1, 0, 1, 1]
	dec2sn(123, 27914974) вернёт [1, 16, 0, 15]
	dec2sn(10, 357) вернёт [7, 5, 3]

	В возвращаемом числе (листе) на позиции 0 находится самый младший разряд.
	'''
	res = []
	while(a // suf != 0):
		res.append(a % suf)
		a = a // suf
	res.append(a % suf)
	return res

def syntaxErrorMsg() -> str:
	res = "Syntax error. Check README.md: "
	res += "https://github.com/The220th/ansck/blob/main/README.md"
	return res

def process(suf1 : int, sn : List[int], suf2 : int) -> None:
	global NORMALFORM
	if(NORMALFORM == 1):
		origNum = letter2num(sn)
	else:
		origNum = sn[::-1]
	print(f"Entered original number \"{origNum}\" in this numeral system \"{suf1}\"")
	
	decOrigNum = sn2dec(suf1, sn)
	print(f"{origNum}_{suf1} = {decOrigNum}_{10}")

	secondNum_sn = dec2sn(suf2, decOrigNum)

	print("")

	marked1, marked2 = "", ""
	if(NORMALFORM == 1):
		marked1 = "    <------"
	else:
		marked2 = "    <------"

	print(f"{letter2num(sn)}_{suf1} = {letter2num(secondNum_sn)}_{suf2} {marked1}")
	#print("")
	print(f"{sn[::-1]}_{suf1} = {secondNum_sn[::-1]}_{suf2} {marked2}")

#python snk.py num_suf 2suf

if __name__ == '__main__':
	if(len(sys.argv) != 3):
		print(syntaxErrorMsg())
		exit()
	if(sys.argv[1].find("_") == -1):
		print(syntaxErrorMsg())
		exit()
	suf1 = int(  sys.argv[1][sys.argv[1].find("_")+1:]  )
	withoutSuf = sys.argv[1][:sys.argv[1].find("_")]
	suf2 = int(sys.argv[2])

	if(suf1 < 2 or suf2 < 2):
		print(f"({suf1} or {suf2}) less than 2")
		exit()

	NORMALFORM = 0

	initNum = None
	if(withoutSuf.find("[") == -1):
		initNum = num2letter(withoutSuf)
		NORMALFORM = 1
	else:
		if(withoutSuf.find("]") == -1):
			print("Cannot find \"]\"")
			print(syntaxErrorMsg())
			exit()
		initNum = withoutSuf[withoutSuf.find("[")+1:withoutSuf.find("]")]
		initNum = initNum.replace(",", "")
		initNum = list(map(int, initNum.split()))
		initNum = initNum[::-1]

	if(max(initNum) >= suf1):
		print(f"{withoutSuf} cannot be in this numeral system: {suf1}. Because {max(initNum)} >= {suf1}")
		exit()

	process(suf1, initNum, suf2)