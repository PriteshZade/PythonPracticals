def decimal_subtraction(num1, num2):
    ans = ""
    max_len = max(len(num1), len(num2))
    num1 = num1.zfill(max_len)
    num2 = num2.zfill(max_len)
    
    carry = 0
    
    for i in range(max_len - 1, -1, -1):
        a = convert(num1[i])
        b = convert(num2[i]) + carry
        
        if a >= b:
            ans = str(a - b) + ans
            carry = 0
        else:
            ans = str(a + 10 - b) + ans
            carry = 1
    ans = ans.lstrip('0')
    if not ans:
        ans = '0'
    return string_to_int(ans)

def convert(digit):
    return ord(digit) - ord('0')

def string_to_int(s):
    result = 0
    for char in s:
        result = result * 10 + convert(char)
    return result


result = decimal_subtraction("2038", "528")
print(result) 
