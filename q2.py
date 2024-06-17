def stringCheck(input):
    string_list=input
    result = []
    for string in string_list:
        anslist = []
        stack = []
        for i,char in enumerate(string):
            if char=='(':
                stack.append(i)
                anslist.append(' ')
            elif char==')':
                if len(stack)!=0:
                    stack.pop()
                    anslist.append(' ')
                else:
                    anslist.append('?')
            else:
                anslist.append(' ')
        while len(stack)!=0:
            anslist[stack.pop()]='x'
        result.append(string)
        result.append(''.join(anslist))
    return result

input=['bge)))))))))', '((IIII))))))', '()()()()(uuu', '))))UUUU((()']
ans = stringCheck(input)
for result in ans:
    print(result)