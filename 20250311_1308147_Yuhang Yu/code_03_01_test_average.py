#this program gets three test scores and display their ave
# if score is greater than high score, then provide congratulation message

#set high score
high_score = 90
#get test1 score
test1 = int(input('Enter your score for test 1: '))
#get test2 score
test2 = int(input('Enter your score for test 2: '))
#get test3 score
test3 = int(input('Enter your score for test 3: '))
#caluculate the ave of the 3 score
average = (test1 + test2 + test3) / 3
#test the ave score is greater than high_score
print(f'The average score is {average:.2f}.')
#if ave score is greater than high_score
  #display "conguatulation" message with user's ave score
if average >= high_score:
    print('Congratulation!')
    print('That is a great average!')


   
#end program