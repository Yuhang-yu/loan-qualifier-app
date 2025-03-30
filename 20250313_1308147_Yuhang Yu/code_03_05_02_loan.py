# you have to write a program that determine whether you will accept loan application or reject. You will determine acceptance based on annual salary and year of work. Acceptance standard is annual salary >500,000 yuan and > 5 year of work in current work
# But this time ,you have to tell them why their application has been rejected and tell them how much salary or year of work or both salary and year of work needed more
annual_salary = int(input('Enter your annual salary:'))
base_salary = 500000
base_year = 5
year_work = int(input('Enter your year of work:'))
if annual_salary >= base_salary and year_work >= base_year:
    print('Your application is accepted')
else:
      print('Sorry, your application has been rejected.')

if annual_salary < base_salary and year_work < base_year:
        print(f'You need at least {base_salary - annual_salary} more yuan in salary '
              f'and {base_year - year_work} more years of work.')
elif annual_salary < base_salary:
        print(f'You need at least {base_salary - annual_salary} more yuan in salary.')
else:
        print(f'You need at least {base_year - year_work} more years of work.')
