from Seller import Seller
from buyer import Buyer
from Item import Item
from transaction import Transaction

def main():
    x = input("What would you like to do? (b)id, (s)ell, or (e)nd: ")
    if (x=='b'):
        print("*****Auction*****")
        i=1
        for y in auctions:
            print(i,". ",(y.getItem()).getname(),"\t",y.getHighBid(),"\t",(y.getSeller().getname()))
            i+=1
        x = int(input("Enter the number of the auction you would like to bid on: "))
        auction = auctions[x-1]
        bname = input("Enter your name: ")
        bid = float(input("Enter your bid: "))
        auction.submitBid(Buyer(bname),bid)
        main()
            
    elif (x=='s'):
        sname = input("Enter your name: ")
        item = input ("What item are you wanting to sell? ")
        sbid = float(input( "Enter starting bid: "))
        auctions.append(Transaction(Item(item,sbid,Seller(sname))))
        main()

    elif (x=='e'):
        print("*****Auction*****")
        i=1
        for y in auctions:
            print(i,". ",(y.getItem()).getname(),"\t",y.getHighBid(),"\t",(y.getSeller().getname()))
            i+=1
        x = int(input("Enter the number of the auction you would like to end: "))
        auction = auctions[x-1]
        print("The winner is",auction.getHighBidder().getname(),"who bid",auction.getHighBid())
        auctions.remove(auction)
        main()
        
        
    else:
        print("Please enter 'b' for buy or 's' for sell.")
        main()

auctions = []

auctions.append(Transaction(Item('Bear',200.00,Seller('Bob'))))
auctions.append(Transaction(Item('Cat',20.00,Seller('George'))))
auctions.append(Transaction(Item('Dog',40.00,Seller('Fred'))))
auctions.append(Transaction(Item('Elephant',4000.00,Seller('Billy'))))
auctions.append(Transaction(Item('Giraffe',2000.00,Seller('Jill'))))

main()
