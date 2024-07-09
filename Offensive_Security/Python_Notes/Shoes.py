class Shoes:
        def __init__(self, name, price):
                self.name = name
                self.price = float(price)
        
        def budget_check(self, budget):
                if not isinstance(budget, (int, float)): #This is checking to see if the value is either int or float and checked against type                                                                      entered for budget
                        print('Invalid entry. Please enter a number.')
                        exit()                
                    
        def change(self, budget):
                return (budget - self.price)
        
        def buy(self, budget):
                self.budget_check(budget)               
                            
                if budget >= self.price:
                        print(f'You can cop some {self.name}')
                        
                        if budget == self.price:
                                print('You have exactly enough money for these shoes.')
                        else:
                                print(f'You can buy these shoes and have ${self.change(budget)} left over')

                        exit('Thanks for using our shoe budget app!')
