def guess_game():
    low = 1
    high = 100
    tries = 0
    
    print("--- Number Guessing Game ---")
    print("Think of a number between 1 and 100.")
    print("Use H (High), L (Low), or C (Correct) for feedback.")
    print("-" * 30)

    while low <= high:
        tries += 1
        guess = (low + high) // 2 
        print(f"\nGuess #{tries}: {guess}")
        
        user_input = input("Your feedback (H/L/C): ").strip().upper()

        if user_input == "H":
            high = guess - 1
        
        elif user_input == "L":
            low = guess + 1
        
        elif user_input == "C":
            print("-" * 30)
            print(f"Computer guessed your number ({guess}) in {tries} tries!")
            print("-" * 30)
            return 
        
        else:
            print("Invalid input. Try again using H, L, or C.")
            tries -= 1 
            
    print("-" * 30)
    print("Error: The search failed. Please ensure your feedback was consistent.")
    print("-" * 30)

if __name__ == "__main__":
    guess_game()

