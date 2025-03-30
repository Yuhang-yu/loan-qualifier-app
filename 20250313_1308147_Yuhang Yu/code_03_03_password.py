# this program compares 2 strings and if the pair of the string is match then show greeting otherwise kick out
# set password
password = "Yulia"
# get input of password
inp_password = input('please enter your password:')
# if the inputed password is same wo password that you set then show greeting message
if inp_password == password:
    print('Hello')
# otherwise shows byebye message
else:
    print('Sorry,wrong password. please try again.')