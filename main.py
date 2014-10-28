from Seller import Seller
from Buyer import Buyer
from Item import Item
from transaction import Transaction

def main(self):
    x = input("What would you like to do? (b)id or (s)ell")
    if (x=='b'):
        print("*****Auction*****")
        i=1
        for y in auctions:
            print(i+". "+y.getname()+"\t"+y.getstart()+"\t"+y.getseller())
        z=0
        while (z==0):
            try:
                
                x = input("Enter the number of the auction you would like to bid on: ")
                auction = auctions[x-1]
                z=1
            except:
                print("Please enter the number of the auction you would like to bid on: ")

        bname = input("Enter your name: ")
        bid = input("Enter your bid: ")
        auction.submitBid(Buyer(bname),bid)
        main()
            
    else if (x=='s'):
        sname = input("Enter your name: ")
        item = input ("What item are you wanting to sell? ")
        sbid = input( "Enter starting bid: ")
        auctions.append(Transaction(Item(item,sbid,Seller(sname))))
        main()
        
        
        
    else:
        print("Please enter 'b' for buy or 's' for sell.")
        main()

auctions = []

auctions.append(Transaction(Item('Bear',200.00,Seller('Bob'))))
auctions.append(Trnasaction(Item('Cat',20.00,Seller('George'))))
auctions.append(Transaction(Item('Dog',40.00,Seller('Fred'))))
auctions.append(Transaction(Item('Elephant',4000.00,Seller('Billy'))))
auctions.append(Transaction(Item('Giraffe',2000.00,Seller('Jill'))))

main()
