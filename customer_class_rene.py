import random
import pandas as pd


class Customer:
    """
    a single customer that moves through the supermarket
    in a MCMC simulation
    """

    def is_active(self):
        """Returns False if a customer has reached the checkout,other wise returns True """
        if self.state == 'checkout':
            return False
        else:
            return True

    def __init__(self, name, state, transition_probs=0, budget=100):
        self.name = name
        self.state = state
        self.budget = budget
        self.transition_probs = pd.read_csv('trans_prob.csv',index_col=0)

    def __repr__(self):
        return f'<Customer {self.name} in {self.state}>'

    def next_state(self):
        """
        propagates the customer to the next state , returns nothing
        :return: nothing
        """
        print(self.transition_probs.index)
        print('---------')
        print(self.transition_probs[self.state])
        self.state = random.choices(list(self.transition_probs.index), weights=self.transition_probs[self.state])[0]



cust1 = Customer('Jake', 'drinks', 50)
cust2 = Customer('Margret', 'spices')

print(cust1.name, cust1.state)
print(cust2.name, cust2.budget)

cust1.next_state()
print('--------------------')
print(cust1.name, cust1.state)
