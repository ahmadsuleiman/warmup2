def string_times(str, n):
  return str*n
  
def front_times(str, n):
  if len(str)>=3:
    return str[0:3]*n
  return str[0:len(str)]*n

def string_bits(str):
  s=""
  for t in range(0,len(str),2):
    s=s+str[t]
  return s

def string_splosion(str):
  s=""
  for i in range (0,len(str)):
    s=s+str[0:i+1]
  return s
  
def last2(str):
  s=str[-2:]
  cnt=0
  for i in range (0,len(str)-2):
    if str[i:i+2]==s:
      cnt=cnt+1
  return cnt
  
def array_count9(nums):
  d=0
  for i in nums:
    if i==9:
      d=d+1
  return d
  
def array_front9(nums):
  if len(nums)>=4:
    for i in range(4):
      if nums[i]==9:
        return True
  if len(nums)<4:
    for i in nums:
      if i==9:
        return True
  return False
  
def array123(nums):
  for i in range(0,len(nums)):
    if nums[i]==1 and i+2<len(nums) and nums[i+1]==2 and nums[i+2]==3:
      return True
  return False
  
def string_match(a, b):
  cnt=0
  ls=[""]
  for i in range (0,len(a)-1):
    for t in range(0,len(b)-1):
      if a[i:i+2]==b[t:t+2]:
        if a[i:i+2] not in ls:
          ls.append(a[i:i+2])
          cnt=cnt+1
  return cnt