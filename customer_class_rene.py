import random


class Customer:
    """
    a single customer that moves through the supermarket
    in a MCMC simulation
    """

    def __init__(self,name,state,budget=100):
        self.name = name
        self.state = state
        self.budget= budget

    def __repr__(self):
        return f'<Customer {self.name} in {self.state}>'

    def next_state(self):
        """
        propagates the customer to the next state , returns nothing
        :return: nothing
        """
        self.state = random.choice(['spices','drinks','fruit'])

cust1 = Customer('Jake','drinks',50)
cust2 = Customer('Margret','spices')



print(cust1.name,cust1.state)
print(cust2.name,cust2.budget)


cust1.next_state()
print('--------------------')
print(cust1.name,cust1.state)
