class SimpleCalculator:
    
    
    def add(self, n1, n2):
        return n1 + n2

    def subtract(self, n1, n2):
        return n1 - n2

    def multiply(self, n1, n2):
        return n1 * n2

    def divide(self, n1, n2):
        if n2 == 0:
            return "Error: Cannot divide by zero (0)."
        return n1 / n2
    

    def menu(self):
        print("\n--- Calculator Options ---")
        print("1. Add (+)")
        print("2. Subtract (-)")
        print("3. Multiply (*)")
        print("4. Divide (/)")
        print("5. Exit")
        print("--------------------------")
        
        

    def _get_valid_input(self, prompt):
        while True:
            user_input = input(prompt)
            try:
                return float(user_input)
            except ValueError:
                print(">>> Invalid Input. Please enter a proper number.")

    def run(self):
        print("Welcome to the Simple Menu-Driven Calculator!")
        

        while True:
            self.menu()
            
            choice = input("Enter your choice (1-5): ")
            

            if choice == '5':
                print("Calculator shut down. Goodbye!")
                break
            
            
            if choice in ('1', '2', '3', '4'):
                num1 = self._get_valid_input("Enter first number: ")
                num2 = self._get_valid_input("Enter second number: ")

                result = None
                operator = ''
                

                if choice == '1':
                    result = self.add(num1, num2)
                    operator = '+'
                elif choice == '2':
                    result = self.subtract(num1, num2)
                    operator = '-'
                elif choice == '3':
                    result = self.multiply(num1, num2)
                    operator = '*'
                elif choice == '4':
                    result = self.divide(num1, num2)
                    operator = '/'

                if isinstance(result, str):
                    print(result)
                else:
                    print(f"\nCalculation: {num1} {operator} {num2} = {result}")
            
            
            else:
                print(">>> Invalid Choice. Please select an option from the menu (1-5).")



if __name__ == "__main__":
    calc = SimpleCalculator()
    calc.run()
    
    