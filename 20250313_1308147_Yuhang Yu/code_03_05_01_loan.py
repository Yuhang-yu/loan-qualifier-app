# you have to write a program that determine whether you will accept loan application or reject. You will determine acceptance based on annual salary and year of work. Acceptance standard is annual salary >500,000 yuan and > 5 year of work in current work
annual_salary = int(input('Enter your annual salary:'))
year_work = int(input('Enter your year of work:'))
if annual_salary >= 500000 and year_work >= 5:
    print('Your application is accepted')
else:
     print('Sorry your application has been rejected')