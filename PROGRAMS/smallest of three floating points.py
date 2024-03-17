
flota = []
flota += input("input a var\n")
flota += input("input another var\n")
flota += input("input one more var\n")


def var_hunter(arb_var):
    
     arb_var.sort()
     print(arb_var[0])
     return

var_hunter(flota)
print(var_hunter)


#takes in strings and prints out first array position
#how can we use min method?