import inspirobot  # Import the libary
flow = inspirobot.flow()  # Generate a flow object
for quote in flow:
    print(quote.text)
