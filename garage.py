class Garage():
    def __init__(self):
        self.tickets = [1, 2, 3, 4]
        self.parkingSpaces = [1, 2, 3, 4]
        self.currentTicket = {
            'ticket_id': 0,
            'assigned_space': 0,
            'paid' : False,
            'payment': ''
        }

    def takeTicket(self):
        ticket_id = self.tickets.pop()
        parking_space = self.parkingSpaces.pop()
        self.currentTicket = {
            'id': ticket_id,
            'assigned_space': parking_space,
            'paid': False,
            'payment': ''
        }
        print('Thank you for choosing this garage for all your parking needs')

    def payForParking(self):
        if self.currentTicket['payment'] == '':
            amount = ''
            while amount == '':
                amount = input('Please enter payment amount >> ')
                if amount == '':
                    print('no payment specified, please try again')
                else:
                    self.currentTicket['payment'] = amount
                    self.currentTicket['paid'] = True
        else:
            print('Ticket has already been paid. You have 15 mins to leave.')

    def leaveGarage(self):
        if not self.currentTicket['paid']:
            self.payForParking()

        print('Thank You, have a nice day')
        self.parkingSpaces.append(self.currentTicket['assigned_space'])
        self.tickets.append(self.currentTicket['id'])

garage = Garage()
garage.takeTicket()
garage.leaveGarage()