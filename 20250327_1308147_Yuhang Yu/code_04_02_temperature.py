# This program assists a techinician in the process of checking a substance's temperature.

# Set the maximum temperature ( 100 )
max_tem = 100
# Get the substance's tempereture
temperature = float(input("Enter the current substance's temperature:" ))
# As long as necessery, give instruct the user to adjust the tempe. 
# IF THE TEM IS TOO HIGH(max temp>) and less than 5 mins, display the messege 
while temperature > max_tem:
   #Instruction is display the following messege
   #Turn the tem down and wait 5 minutes
   print("Turn the thermostat down and wait 5 minutes")
   #Then take the tem again and enter it
   print("Then take the temperature again and enter it")
   #ask the current temm
   temperature = float(input('Enter the new temperature:'))
# Display 'all tem is in normal parameter
print("All temperature is in normal parameter")