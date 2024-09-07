def add(num1, num2):
    max_len = max(len(num1), len(num2))+1
    num1 = num1.zfill(max_len)
    num2 = num2.zfill(max_len)
    
    carry = 0
    result = []
    
    for i in range(max_len - 1, 0, -1):
        total = int(num1[i]) + int(num2[i]) + carry
        if total == 0:
            result.append('0')
            carry = 0
        elif total == 1:
            result.append('1')
            carry = 0
        elif total == 2:
            result.append('0')
            carry = 1
        elif total == 3:
            result.append('1')
            carry = 1
    
    if carry:
        result.append('1')
    
    return ''.join(result[::-1])

def subtractor(que1, que2):
    
    util = ''.join('1' if i == '0' else '0' for i in que2)
    one = '1'
    a = add(util, one)
    

    result = add(a, que1)
    
    result = result.lstrip('0')
    if(len(result)>max(len(que1) , len(que2))):
        return result if result else '0'
    else:
        result=''.join('1' if i == '0' else '0' for i in result)
        a = add(result,one)
        return a
    
    
    


print(subtractor( "10011","11"))  
