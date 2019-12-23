hrs = input("Enter Hours:")
h = float(hrs)
pay = input("Enter Pay:")
p = float(pay)

if h <= 40 :
    print(h * p)
else :
    h_extra = h - 40
    h_normal = h - h_extra
print(h_extra * p * 1.5 + h_normal * p)



# else h > 40 :
# print(h_extra * p * 1.5 + h_normal * p)

#else :
#    h_extra = h - 40
#    h_normal = h - h_extra
#    h_extra = h_extra * p * 1.5
#    h_normal = h_normal * p
#    print(h_extra + h_normal)
#print('All Done!')
