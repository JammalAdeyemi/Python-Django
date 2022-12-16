class Ticket:
    def __init__(self, ticketNumber, ticketPrice):
        self.ticketNumber = ticketNumber
        self.ticketPrice = ticketPrice
    def getNumber(self):
        return self.ticketNumber
    def getPrice(self):
        return self.ticketPrice
    def toString(self):
        return f"Number: {self.ticketNumber}, Price: {self.ticketPrice}"

class StudentTicket(Ticket):
    def __init__(self, ticketNumber, ticketPrice, name):
        super().__init__(ticketNumber, ticketPrice)
        self.name = name
    def getName(self):
        return self.name
    def getPrice(self):
        return super(StudentTicket, self).getPrice() / 2
    def toString(self):
        return f"Number: {self.ticketNumber}, Price: {self.ticketPrice}, ID required for {self.name}"