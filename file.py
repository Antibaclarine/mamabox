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