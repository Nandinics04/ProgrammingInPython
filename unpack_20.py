
#detailing of unpacking 
# def total(galliones, sickles, knuts):
#     return (galliones*17+sickles)*29 + knuts

# coins=[100,50,25]
# print(total(*coins), "Knuts")

# print(total(galliones=100,sickles=50,knuts=25), "knuts")
# coins={ "galliones": 100, "sickles":50, 'knuts':25}
# print(total(coins["galliones"],coins["sickles"],coins["knuts"]), "knuts")
# print(total(**coins), "knuts")



def f(*args, **kwargs):
    print(f"Positional: {args}")
    print(f"Named Arguments: {kwargs}")

f([100,50,25,5])
f(galliones=100,snikles=50,knuts=25)

# def print(*objects,sep=' ',end='\n'): our print using this positional arguments and all 

