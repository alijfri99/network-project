def calcsum(msg):
	sum = 0
	for i in msg:
		sum = sum + i
	sum = format(sum,"b")
	if(len(sum)<8):
		while(len(sum)!=8):
			sum = "0" + sum
	elif(len(sum)>8):
		while(len(sum)!=8):
			sum = int(sum[0],2) + int(sum[1:len(sum)],2)
			sum = format(sum,"b")
	return(sum)

def complement(input):
	result = ""
	for i in input:
		if(i=="0"):
			result = result + "1"
		elif(i=="1"):
			result = result + "0"
	return(result)

print(complement(calcsum([255,255])))