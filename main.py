'''
Author: ar3s93
Version: 0.1b
Email: manuelr@tutanota.com
'''
import fut

#importing config file
import config

#Building a Menu
#Print the Menu

print_menu = """
1. Trade Contracts (Gold) - Best Choose
2. Trade Player
3. Trade Club Objects
4. Trade Staff
5. Exit
"""

print(print_menu)
menu=input("Enter your choice [1-5]: ")
   
if menu==1:
        print("Trade Contracts")
        #Link to connection for Trade Contracts (Not available yet)    
elif menu==2:
        print("Trade Player")        
        #Link to connection for Trade Player (Not available yet)    
elif menu==3:
        print("Trade Club Objects")        
        #Link to connection for Trade Club Objects (Not available yet)    
elif menu==4:
        print("Trade Staff")        
        #Link to connection for Trade Staff (Not available yet)        
elif menu==5:
        exit()
else:  
    # Any integer inputs other than values 1-5 we print an error message
    raw_input("Wrong option selection. Enter any key to try again..")