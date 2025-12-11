#  WAP to Convert distant given in feet and inches into meter and centimeter.
#  take inputs 
ft = float(input("Enter distance in feets :"))
inches = float(input("Enter distance in inches: "))

# convert ft to inches
inc = ft * 12 


#  convert into meter and centimeter
m = inc // 0.0254
cm = inches // 2.54

#  display results
print(f'The distance {ft}ft and {inches} in is {m} meter and {cm} centimeter')