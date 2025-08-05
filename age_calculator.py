import datetime

birthdate_byuser= input("Enter your birth date (YY-MM-DD) :")

birthdate = datetime.datetime.strptime(birthdate_byuser,"%Y-%m-%d").date()

today = datetime.date.today()


age_days= (today - birthdate).days

years = age_days // 365
months =(age_days % 365) // 30
days = (age_days % 365) % 30

print(f"You are {years} years,{months} months and {days} days old")