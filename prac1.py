# %%
length = float(input())
width  = float(input())
height = float(input())

total_length = length + width + height

if total_length <= 80:
    fee = 50000
elif total_length <= 100:
    fee = 80000
elif total_length <= 120:
    fee = 100000
elif total_length <= 160:
    fee = 130000
else:
    fee = 1000000000000000
