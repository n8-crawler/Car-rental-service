import datetime
import json
class rental:
    car = {'Compact':[500,0],'Minivan':[1000,5],'Premium':[2000,3]}
    

class custmer(rental):
    def __init__(self,name,contact,car_type,Rent_date,Odo_reading):
        self.Name = name
        self.Contact = contact
        self.Car = car_type 
        self.Order_date = Rent_date
        self.Odo = Odo_reading

        
    def book(self):

        self.user_details = {
                    "name": self.Name,
                    "contact":self.Contact,
                    "car_type":self.Car,
                    "odo_reading1":self.Odo,
                    "odo_reading2":None,
                    "order_date" :self.Order_date,
                    "deliverrd_date":None

                }

        if self.Car == "Compact":
            if rental.car['Compact'][1]>0:
               
                with open (self.Contact+'.json','w') as f:
                    json.dump(self.user_details,f)


                rental.car['Compact'][1]-=1
                return 'Booked'
            else: return 'All {} cars are already booked'.format(self.Car)
            
        if self.Car == "Premium":
            if rental.car['Premium'][1]>0:
               
                with open (self.Contact+'.json','w') as f:
                    json.dump(self.user_details,f)


                rental.car['Premium'][1]-=1
                return 'Booked'
            else: return 'All {} cars are already booked'.format(self.Car)
        
        if self.Car == "Minivan":
            if rental.car['Minivan'][1]>0:
               
                with open (self.Contact+'.json','w') as f:
                    json.dump(self.user_details,f)


                rental.car['Minivan'][1]-=1
                return 'Booked'
            
            else: return 'All {} cars are already booked'.format(self.Car)


    def deliver (self,id,odo2,return_date,rent_days):
        with open(id+'.json','rb') as f:
            py_data = json.load(f)
            d2 = datetime.datetime.strptime(str(return_date).strip().replace('/','/'), '%Y/%m/%d')
            py_data['deliverrd_date'] = return_date
            py_data['odo_reading2'] = odo2
            py_data['rented_days'] = rent_days
        
        return self.rent(py_data)

    def rent(self,pydata):
        delta_odo = pydata['odo_reading2'] - pydata['odo_reading1']
        kilometerPrice = 10
        rented_days = pydata['rented_days']

        if pydata['car_type'] == 'Compact':
            price = rental.car[pydata['car_type']][0]*  rented_days

            rental.car['Compact'][1]+=1
            return price
        if pydata['car_type'] == 'Premium':
            
            price = rental.car[pydata['car_type']][0]*  rented_days * 1.2 + kilometerPrice * delta_odo
            rental.car['Premium'][1]+=1
            return price
        
        if pydata['car_type'] == 'Minivan':
            
            price = rental.car[pydata['car_type']][0]*  rented_days * 1.7 + kilometerPrice * delta_odo
            rental.car['Minivan'][1]+=1
            return price




