import schoolId
import schoolnmae


def handle(my_Temp):
    for i in iter(my_Temp):
        print(i)
    return len(my_Temp)
    

cnt = 0
for i in range(28):
    schoolListStr = schoolId.GetSchoolId(i)
    Temp =schoolnmae.GetName(schoolListStr)
    cnt = cnt + handle(Temp)
    
    
print("一共有" + str(cnt) + "个学校")