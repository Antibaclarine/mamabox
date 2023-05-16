class Products:
    def __init__(self,id,name,price):
        self.id=id
        self.name=name
        self.price=price

class Cart:
    def __init__(self):
        self.item=[]
         
    def add_item(self,item):
        #check if if item is in the cart
        for i in self.item:
            if i.product.id == item.product.id:
                # increase the item quantity
                i.quantity +=item.quantity
                break;
        else:
            #add item to the cart
            self.item.append(item)
            def remove_item(self,product_id):
                self.product_id=product_id
                for i in self.items:
                    if i.product.id ==product_id:
                            self.item.remove(i)
                            break

    def total(self):
        #get the total cost
        total=0
        for i in self.item:
            total +=i.product.price *i.quantity
        return total

class Cart_to_item:
    def __init__(self,product,quantity):
        self.product=product
        self.quantity=quantity
        # return cart.total

cart=Cart()
product=Products(2,'cabbage',50)
item=Cart_to_item(product,1)
cart.add_item(item)


class DeliveryService:
    def __init__(self, service_provider, delivery_areas, delivery_time, delivery_charges):
        self.service_provider = service_provider
        self.delivery_areas = delivery_areas
        self.delivery_time = delivery_time
        self.delivery_charges = delivery_charges
        
    def __str__(self):
        return f"Delivery service provider: {self.service_provider}\nDelivery areas: {self.delivery_areas}\nDelivery time: {self.delivery_time}\nDelivery charges: {self.delivery_charges}"
        
    def partner_with_service_provider(self, service_provider):
        # Partner with service provider
        pass
    
    def set_delivery_areas(self, delivery_areas):
        # Set delivery zones
        pass
    
    def delivery_time_and_charges(self, delivery_address):
        # Calculate delivery time and charges
        pass

# Create an instance of the DeliveryService class
ds1 = DeliveryService("Mboga-Mart", ["Local"], "1-2 days", 5.00)

# Print the details of the DeliveryService object
print(ds1)

#Customer class
class Customer:
    def __init__(self, name, email, phone_number, address, order_history):
        self.name = name
        self.email = email
        self.phone_number = phone_number
        self.address = address
        self.order_history = order_history
    def update_email(self, new_email):
        self.email = new_email
    def update_phone_number(self, new_phone_number):
        self.phone_number = new_phone_number
    def update_address(self, new_address):
        self.address = new_address
    def add_order_to_history(self, order):
        self.order_history.append(order)
    def __str__(self):
        return f"{self.name},{self.email},{self.phone_number},{self.address},{self.order_history}"


#//Customer class
c1 = Customer("Eunice Musenyia", "eunicemusenyia@gmail.com", "555-1234", "123 Main vt.")
#//Customer
print(c1)

#  //payment
class Payments:
    def __init__(self,customer,amount,phoneNumber):
        self.customer=customer
        self.amount=amount
        self.phoneNumber=phoneNumber
        #updating customers name in the payment 
    def update_customer(self, new_customer):
        self.customer = new_customer
        #updating amounts in the payment list 
    def update_amount(self, new_amount):
        self.amount = new_amount
        #updating phone Numbers in the payment list
    def update_phoneNumber(self, new_phoneNumber):
        self.phoneNumber= new_phoneNumber
    def __str__(self):
       return f"{self.customer}-{self.amount}-{self.phoneNumber}"

# //Payments
p2=Payments("Julius nyerere",1000,"07453233737")
print(p2)
# //Inventory class
class Inventory:
    def __init__(self, product_name, quantity, price, action):
        self.product_name = product_name
        self.quantity = quantity
        self.price=price
        self.action=action
#updating stock
    def new_stock_levels(self,new_product):
        self.product_name=new_product
# updating stock quanity
    def Quantity_products(self,new_quantity):
        self.quantity=new_quantity
# updating prices
    def pricing(self, new_price):
        self.price=new_price
    def update_action(self,needed_action):
       self.action=needed_action
    def __str__(self):
        return f"{self.product_name},{self.quantity},{self.price},{self.action}"

#//Inventory class
i1 = Inventory("Apple", 100,"sh.500", "add")

# //Inventory
print(i1)