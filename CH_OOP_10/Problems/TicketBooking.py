class Train:
    #Designing a train ticket booking system using OOP concepts
    def __init__(self, name, fare, seats):
        self.name = name
        self.fare = fare
        self.seats = seats
#Instance methods
    def getStatus(self):
        print(f"The name of the train is {self.name}")
        print(f"The seats available in the train are {self.seats}")

    def bookTicket(self):
        if (self.seats > 0):
            print(f"Your ticket has been booked! Your seat number is {self.seats}")
            self.seats = self.seats - 1
        else:
            print("Sorry, No seats available")

    def cancelTicket(self):
        print("Your ticket has been cancelled")
        self.seats = self.seats + 1
    def getFare(self):
        print(f"The fare of the ticket is {self.fare}")
        
        #Create an object of the Train class
intercity = Train("Intercity Express", 90, 3)


#Run the  function, but use the data (name, fare, seats) from the intercity object."
intercity.getStatus()
intercity.bookTicket()
intercity.getFare()
intercity.cancelTicket()