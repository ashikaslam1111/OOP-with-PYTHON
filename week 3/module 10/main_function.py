from manu import*
from restu import*
from demo_project import*
from order import*


def main():
   menu = Menu()
   # add pizza to the meanu
   pizza1 = Pizza('suttci pizza',300,'large',['sutci','piaz','lobon'],5)
   pizza2 = Pizza('alo borta',300,'large',['alo','piaz','lobon'],5)
   pizza3 = Pizza('dhal',300,'large',['dhal','piaz','lobon'],5)
   menu.add_manu_item('pizza',pizza1)
   menu.add_manu_item('pizza',pizza2)
   menu.add_manu_item('pizza',pizza3)
   # add burger to the meanu
   burger1 = Burger('naga',400,'murgii',['bread','murgi','morich'])
   menu.add_manu_item('burger',burger1)
   
   menu.show_menu()

   ## creating a resturent
   khiajan=Restrurent("Ashen Bosen Khan",1000,menu)
   ## add employes
   mangerr1 = Manager("monir",'017***',"hello@.com",'kagmare',3000,'management','1/1/1',59843)
   khiajan.add_employ("manager",mangerr1)

   chef1 = Chef('pappu',3333,'heooo@','kodalia',4000,'serv','5/4',5959,'khichuri')
   khiajan.add_employ("chef",chef1)

   serv1 = Server('raju','444','emr','tangail',6000,'cok','6/6',47943)
   khiajan.add_employ("server",serv1)
   khiajan.show_employ()

   ## creating customer 
   shakip  = Customer('shkip','0190000','em2@','nurala',2000)

   ## creating order 

   order = Order(shakip,[pizza1,burger1])
   ##print(order.total)
   shakip.place_order(order)
   khiajan.add_orders(order)


   # customer will pay for the order
   khiajan.recive_payment(2000,shakip,order)

   print(khiajan.revenue)










if __name__ == '__main__':main()#call the main fun