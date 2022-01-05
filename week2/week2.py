# 第一題
def calculate(min, max):
    sum=0
    for n in range(min,max+1,1):
        sum=sum+n
    print(sum)
calculate(1,3)  # 你的程式要能夠計算 1+2+3，最後印出 6
calculate(4,8)  # 你的程式要能夠計算 4+5+6+7+8，最後印出 30

# 第二題
def avg(data):
    sum=0
    n=data["count"] # 員工人數 
    salarytable=data["employees"] #薪資表
    for i in range(n):
        table=salarytable[i] #list變成dic格式
        salary=table["salary"]
        sum+=salary
    result=sum/n
    print(result)
# 請用你的程式補完這個函式的區塊
avg({"count":3,"employees":[
{"name":"John","salary":30000},
{"name":"Bob","salary":60000},
{"name":"Jenny","salary":50000}]}) 


# 第三題
def maxProduct(nums):
    after=[]
    for i in nums:
        for j in nums:
            if i!=j:
                after.append(i*j)
    print(max(after))
   
maxProduct([5, 20, 2, 6]) # 得到 120
maxProduct([10, -20, 0, 3]) # 得到 30
maxProduct([-1, 2]) # 得到 -2
maxProduct([-1, 0, 2]) # 得到 0
maxProduct([-1, -2, 0]) # 得到 2

# 第四題
def twoSum(nums, target):
    after=[] #相加結果列表
    for i in nums:
        for j in nums:
            if i!=j:
                x=i+j
                if x==target:
                    return [nums.index(i),nums.index(j)]                    
result=twoSum([2, 11, 7, 15], 9)
print(result) # show [0, 2] because nums[0]+nums[2] is 9

# Optional
def maxZeros(nums):
    max_time=0  # 已知最大連續出現次數初始為0
    cur_time=0  # 紀錄當前元素是第幾次連續出現
    pre_element=None    #紀錄上一個元素是什麼
    for i in nums:
        if i == 0:  # 如果當前元素和上個元素相同，連續出現次數+1，並更新最大值
            cur_time += 1
            max_time = max((cur_time, max_time))
        else:
            pre_element = 0
            cur_time = 0
    print(max_time)
maxZeros([0, 1, 0, 0]) # 得到 2
maxZeros([1, 0, 0, 0, 0, 1, 0, 1, 0, 0]) # 得到 4
maxZeros([1, 1, 1, 1, 1]) # 得到 0
maxZeros([0, 0, 0, 1, 1]) # 得到 3