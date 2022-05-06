s={1:['gopi','male','MPCS','pass'],2:['raju','male','MPCS','pass'],3:['hari','male','MPCS','pass'],4:['rani','male','MPCS','pass'],5:['ravi','male','MPES','fail']}
x=int(input('enter rollno:'))
print('sno:',x)
print('sname:',s[x][0])
print('gender:',s[x][1])
print('group:',s[x][2])
print('result:',s[x][3])

output:
enter rollno:3
sno: 3
sname: hari
gender: male
group: MPCS
result: pass
