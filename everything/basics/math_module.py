import math

exponential = pow(2,3) # 2^3
log = math.log(10, 10)
round_above = math.ceil(4.2)
round_bellow = math.floor(4.2)
square = math.sqrt(16)
mod = math.fmod(16,4)
mod2 = math.fmod(3, 2)
only_log_10 = math.log10(1000000000000000000000000000000000000000000000000)
only_log_2 = math.log2(42948294)
only_integer = math.trunc(17.3234)
print(f"2^3 is {exponential}")
print(f"4.2 became {round_above} using ceil (ceiling)") # 5
print(f"4.2 became {round_bellow} using floor") # 4
print(f"mod 16/4 is {mod}") # 0
print(f"mod 3/2 is {mod2}") # 1
print(f"i had 17.3234 and it's became {only_integer}")
print(f"{only_log_10} lol (its very easy actually)")
print(f"{only_log_2} no so easy now")
