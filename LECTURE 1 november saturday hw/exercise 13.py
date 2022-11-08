loaf_of_bread = 3.49
day_old_bread = loaf_of_bread*0.6
number_of_loaves = int(input())
print("Price for the loaves:", round(loaf_of_bread*number_of_loaves,2))
print("Price for the day old loaves:", round(day_old_bread*number_of_loaves,2))
print("total:", round(loaf_of_bread*number_of_loaves-(day_old_bread*number_of_loaves),2))