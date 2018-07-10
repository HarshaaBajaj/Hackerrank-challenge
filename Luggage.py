def  luggage(weights):
    answer = ""
    b=[] ; final =[]
    for i in [map(int(x),weights.split(','))][::-1]:
        if len(b) < 3 :
            b.append(i)
        if len(b) == 3 :
            final.append(b[::-1])
            b=[]
    answer = ','.join(str(j) for i in final for j in i)
    return answer

if __name__ == '__main__':
	weights = input('Please enter the luggage ids separated by comma \n') or '1,2,3,4,5,6'
	print('Unloading order \n',luggage(weights))
