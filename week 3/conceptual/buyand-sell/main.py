from company import*
from product import*
from user import*





def main():
   dharaz = Company("eshop")
   aslam = User('aslma',234,'helo@0')
   aslam.load_money(2000)
   aslam._creat_id(dharaz)
   monir = User('monir',388,'helo@0')
   monir._creat_id(dharaz)
   por1  = Product("cloth",'shirt',300)
   print(por1)
   monir.post_for_sell(por1,dharaz)
   monir.see_product(dharaz)
   aslam.buy_product(dharaz)
   print(aslam.wallate,monir.wallate,dharaz.total_deal,dharaz.profit)








if __name__ == "__main__":main()