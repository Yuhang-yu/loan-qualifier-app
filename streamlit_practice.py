import streamlit as st
st.title("My first webapp")

# you have to write a program that
# determine whether you will accept loan
# application or reject. You will
# determine acceptance based on annual
# salary and year of work. Acceptance
# standard is annual salary >500,000 yuan
# and > 5 year of work in current work

annual_salary = st.number_input('Enter your annual salary:')

year_work = st.number_input('Enter your year of work:')

if st.button('submit'):
    
    if annual_salary >= 500000 and year_work >= 5:
        st.write('Your application is accepted')
    
    else:
        st.write('Sorry your application has been rejected')
