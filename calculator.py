
# write your code here
import re

varDict={}

while True:
    ipt=input().strip()

    if len(ipt)==0:
        continue
    if ipt=='/exit':
        print('Bye!')
        break
    elif ipt=='/help':
        print('The program calculates the sum of numbers')
        continue
    elif ipt.count('=')>1:
        print('Invalid assignment')
        continue
    elif re.match('\/[\w]+',ipt):
        print("Unknown command")
        continue

    try:
        if '=' in ipt:
            varsl=ipt.split('=')
            strlist=[var.strip() for var in varsl]
            if strlist[0].isalpha():
                if strlist[1].isalpha():
                    if strlist[1] in varDict.keys():
                        varDict[strlist[0]]=varDict[strlist[1]]
                    else:
                        print('Unknown variable')
                        continue
                elif strlist[1].isnumeric():
                    varDict[strlist[0]]=int(strlist[1])
                else:
                    print('Invalid identifier')
            else:
                print('Invalid identifier')
        else:

            operators=re.findall(r'[+-]+',ipt)

# convert all valid + and - into simple operators
            if operators:
                nop=[]
                for op in operators:
                    if op.count('-')%2:
                        nop.append('-')
                    else:
                        nop.append('+')
                for np,op in zip(nop,operators):
                    ipt=ipt.replace(op,np,1)

            # print(ipt)

# process the clean version of input
            if ipt.isalpha():
                if ipt in varDict.keys():
                    print(varDict[ipt])
                    continue
                else:
                    print('Unknown variable')
                    continue

            elif ipt[0] in '+-':
                if ipt[1:].isnumeric():
                    print(ipt)

            elif ipt.isnumeric():
                print(ipt)

# convert to RPN postfix notation

            else:
                strlist=re.findall(r'[\w]+|[\+\-\/\*\(\)]',ipt)
                postfix=[]
                operators=[]

# set up a start index for decompose input into operands and operators
                index=0

                if strlist[0] == '-':
                    index=2
                    if strlist[1].isapha():
                        if strlist[1] in varDict.keys():
                            postfix.append(varDict[strlist[1]])
                        else:
                            print('Unknown variable')
                            continue
                    elif strlist[1].isnumeric():
                        postfix.append(-int(strlist[1]))

                for str in strlist[index:]:

                    # deal with operands
                    if str.isalpha():
                        if str in varDict.keys():
                            postfix.append(varDict[str])
                        else:
                            print('Unknown variable')
                            continue
                    elif str.isnumeric():
                        postfix.append(int(str))

                    # deal with opeartors
                    if str in '*/+-()':
                        if not operators:
                            operators.append(str)
                        elif operators[-1]=='(':
                            operators.append(str)

                        elif str in '*/' and operators[-1] in '+-':
                            operators.append(str)
# treat low or equal precedence
                        elif str in '+-' or (str in '*/' and operators[-1] in '*/'):
                            while(operators):
                                if operators[-1]!='(':
                                    postfix.append(operators.pop())
                                else:
                                    break
                            operators.append(str)
# treat right parethesis
                        elif str=='(':
                            operators.append('(')

                        elif str == ')':
                            if len(operators)==1 and operators[0]!='(':
                                print('Invalid expression')
                                break

                            while(operators):
                                operator = operators.pop()
                                if operator!='(':
                                    postfix.append(operator)
                                elif operator == '(':
                                    break

# pop all remaining operators
                while(operators):
                    operator=operators.pop()
                    if operator not in '()':
                        postfix.append(operator)
                    else:
                        print('Invalid expression')
                        break
            # print(postfix)

# calculate the result
            result=[]

            for ele in postfix:
                if isinstance(ele, int):
                    result.append(ele)
                else:
                    b=result.pop()
                    a=result.pop()

                    if ele=='+':
                        interim=a+b
                    elif ele=='-':
                        interim=a-b
                    elif ele=='*':
                        interim=a*b
                    else:
                        interim=a/b
                    result.append(interim)
            final=int(result[-1])
            print(final)


                #
                #     for str in strlist:
                #         if str in varDict.keys():
                #             nums.append(int(varDict[str]))
                #         elif str.isnumeric():
                #             nums.append(int(str))
                #         elif '+' in str:
                #             ops.append('+')
                #         elif '-' in str:
                #             minuscount=str.count('-')
                #             if minuscount%2:
                #                 ops.append('-')
                #             else:
                #                 ops.append('+')
                #         else:
                #             print('Unknown variable')
                #
                # if len(nums)==len(ops)+1:
                #     result=nums[0]
                #     for num,op in zip(nums[1:],ops):
                #         if op=='+':
                #             result+=num
                #         elif op=='-':
                #             result-=num
                #     print(result)
                # else:
                #     print("Invalid expression")
                #     continue

    except Exception:
        print('Invalid expression')
