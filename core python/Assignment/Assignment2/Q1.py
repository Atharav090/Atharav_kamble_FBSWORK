# WAP to Convert the time entered in hh,min and sec into seconds.

#  take inputs
hh = int(input("Enter the hours: "))
min = int(input("Enter the minutes: "))
sec = int(input("Enter the seconds: "))

#  convert hh and min into seconds 
temp1 = hh * 3600
temp2 = min * 60

total_sec = temp1 + temp2 + sec
#  Display results 
print(f'the total seconds into {hh} hours, {min} minutes and {sec} seconds is: {total_sec} seconds')

