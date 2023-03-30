import pandas as pd
import numpy as np

df1= pd.read_csv('demo.csv')
df1.head()

t_count = df1[df1.target=='True'].target.count()
f_count = df1[df1.target=='False'].target.count()
# t_count, f_count

def getProbability(value, columnName):
  df2 = df1[df1[columnName] == value]
  count_t = df2[df2.target == "True"].target.count()
  count_f = df2[df2.target == "False"].target.count()
  return (count_t/t_count , count_f/f_count)

c1 = input()
c2 = input()
c3 = int(input())

# c1 = "JEE101"
# c2 = "Q4"
# c3 = 50

ans1y , ans1N = getProbability(c1, "categoryid")
ans2y , ans2N = getProbability(c2,  "quarter")
ans3y, ans3N = getProbability(c3,  "discount")
yes = ans1y*ans2y*ans3y*(t_count/(t_count+f_count))
no = ans1N*ans2N*ans3N*(f_count/(t_count+f_count))

if(yes > no):
  print("Student enrolled is more than 1000")
else:
  print("Student enrolled is less than 1000")