deposit = float(input())
first_year = (deposit*0.04)+deposit
second_year = (first_year*0.04)+first_year
third_year = (second_year*0.04)+second_year
print("The amount of savings in the first year:", round(first_year,2),"in the second:", round(second_year,2), "in the third:", round(third_year,2))