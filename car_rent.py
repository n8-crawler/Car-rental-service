from datetime import date
import datetime
import time
import customer
while True:
    car_type = None
    days_rent = None


    #customer details

    choice = int(input("Enter input \n press 1 for rent \n press 2 for return\n  press 3 for Exit \n"))
    if choice ==3:
        print('Thanks for using Car rental services')
        
        break


    print("Welcome user to our renting portal\n please provide your details \n")
    name = input('Name: ')
    contact = input('Mobile_No: ')
    car_choice = int(input("Enter input \n press 1 for compact \n press 2 for premium \n press 3 for mini\n"))
    if car_choice==1:
        car_type = 'Compact'
    elif car_choice ==2:
        car_type = 'Premium'
    else: car_type = 'Minivan' 
    Rent_date = input("enter date in 2010/04/15: ")
    Odo_reading1 = int(input('Enter total km reading: '))
    try:
        d1 = datetime.datetime.strptime(str(Rent_date).strip().replace('/','/'), '%Y/%m/%d')

    except:            
    
        print('Enter valid Date')


    if choice ==2:
        Odo_reading2 = input('enter your odo reading: ')
        Return_date = input("enter date in 2010/04/15: ")
        cust_obj = customer.custmer(name,contact,car_type,Rent_date,Odo_reading1)

        d2 = datetime.datetime.strptime(str(Return_date).strip().replace('/','/'), '%Y/%m/%d')

        if (d2-d1).days>0:
            days_rent = (d2-d1).days


            temp = cust_obj.deliver(contact,Odo_reading2,Return_date,days_rent)
            print('total rent: ',temp)
            print('Thanku for Choosing our Services')
            break
        
        print('Your Return date is previous to Booking date')


    print('''Thank You for providing all these Details \n
            Name:{}\n
            contact:{}\n
            car_type:{}\n
            rent_date:{}\n
            odo_reading{}\n
            PROCESSING...'''.format(name,contact,car_type,Rent_date,Odo_reading1))
    time.sleep(5)

    cust_obj = customer.custmer(name,contact,car_type,Rent_date,Odo_reading1)
    
    temp = cust_obj.book()
    print(temp)
        
    

