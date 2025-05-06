 
import xmlrpc.client 
 
proxy = xmlrpc.client.ServerProxy("http://localhost:8000/") 
 
while True: 
    user_input = input("Enter a number to compute its factorial (or type 'exit' to quit): ").strip()
 
    if user_input.lower() == 'exit': 
        try: 
            print(proxy.shutdown()) 
        except: 
            print("Server already shut down.") 
        break 
 
    try: 
        num = int(user_input) 
        result = proxy.factorial(num) 
        print(f"Factorial of {num} is {result}") 
    except ValueError: 
        print("Please enter a valid integer or 'exit'.")