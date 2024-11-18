# for i in range(1,6):
#     print("*"*i)
# for j in range(4,0,-1):
#     print("*"*j)
step=5
tot_step=step*2
for i in range(1,tot_step):
    if i<=step:
        num_star=i
    else:
        num_star=tot_step-i
    for j in range(num_star):
        print("*",end="")
    print()