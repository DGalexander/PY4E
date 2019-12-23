hrs = input("Enter Hours:")
pay = input("Enter Pay:")
try:
    h = float(hrs)
    p = float(pay)
except:
    print("Error, please eneter numeric input")
    quit()
if h <= 40 :
    print(h * p)
else :
    h_extra = h - 40
    h_normal = h - h_extra
    print(h_extra * p * 1.5 + h_normal * p)
