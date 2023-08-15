#Demonstration of using logical operation
p = True
q = False
r = True

#task_1
a = p or q  #True
aa = a and r  #True
b = p and r  #True
c = q and r  #False

ans_1 = aa or b or c  #True 
print(ans_1)


#task_2
d = not (p and q)  #True
e = q and (not r)  #False

ans_2 = d or e  #True
print(ans_2)