def  luggage(weights):
    answer = ""
    b=[] ; final =[]
    for i in list(map(lambda x : int(x),weights.split(',')))[::-1]:
        if len(b) < 3 :
            b.append(i)
        if len(b) == 3 :
            final.append(b[::-1])
            b=[]
    answer = ','.join(str(j) for i in final for j in i)
    return answer
