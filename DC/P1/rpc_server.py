from xmlrpc.server import SimpleXMLRPCServer
import threading

def factorial(n):
    print(f"Calling Factorial:{n}")
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)

def shutdown():
    print("Shutting down the server...")
    threading.Thread(target=server.shutdown).start()
    return "Server is shutting down."

server = SimpleXMLRPCServer(("localhost", 8000), allow_none=True)
print("Server is listening on port 8000...")

server.register_function(factorial, "factorial")
server.register_function(shutdown, "shutdown")

server.serve_forever()
