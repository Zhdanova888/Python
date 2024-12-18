def counter():
    n = 5
    def coun():
        nonlocal n 
        n += 1
        print(n)

    return coun

count = counter()
count()
count()
count()



def add_tax(n):
    def input_add_tax(a):
        return n + a
    return input_add_tax

add_vat = add_tax(20) 
print(add_vat(100))   
print(add_vat(200))    



def multiplier(n):
    def input_multiplier(a):
        return n * a
    return input_multiplier

times_three = multiplier(3)
print(times_three(5))  
print(times_three(10))  