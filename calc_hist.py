HISTORY_FILE = "history.txt"

def show_history():
    file = open(HISTORY_FILE, "r")
    lines =file.readlines()
    if len(lines) == 0:
        print("No history available.")
    else:
        print("Calculation History:")
        for line in lines:
            print(line.strip())
    file.close()

def clear_history():
    file = open(HISTORY_FILE, "w")
    file.close()
    print("History cleared.")

def add_to_history(equation, result):
    file = open(HISTORY_FILE, "a")
    file.write(f"{equation} = {result}\n")
    file.close()
    print("Result added to history.")

def calculate(user_input):
    parts = user_input.split()
    if len(parts) != 3:
        print("Invalid input. Please enter in the format: <number1> <operator> <number2>")
        return None
    
    num1 = float(parts[0])
    operator = parts[1]
    num2 = float(parts[2])

    if operator == '+':
        result = num1 + num2
    elif operator == '-':
        result = num1 - num2
    elif operator == '*':
        result = num1 * num2
    elif operator == '/':
        if num2 == 0:
            print("Error: Division by zero.")
            return None
        result = num1 / num2
    else:
        print("Invalid operator. Please use +, -, *, or /.")
        return None
    
    if int(result) == result:
        result = int(result)
    print(f"Result: {result}")
    add_to_history(user_input, result)
    return result
 
def main():
    print("Welcome to the Calculator!")
    while True:
        user_input = input("Enter calculation (or 'history' to view history, 'clear' to clear history, 'exit' to quit): ")
        if user_input.lower() == 'exit':
            print("Exiting calculator. Goodbye!")
            break
        elif user_input.lower() == 'history':
            show_history()
        elif user_input.lower() == 'clear':
            clear_history()
        else:
            calculate(user_input)

main()
