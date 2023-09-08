import PySimpleGUI as sg

# Initialize the cart list
cart = []

# Define the window layout
layout = [
    [sg.Button("Add to Cart"), sg.Button("Calculate Total"), sg.Button("Exit")],
    [sg.Multiline("", key="receipt", size=(40, 10))]
]

# Create the window
window = sg.Window("Cash Register", layout)

# Main loop
while True:
    event, values = window.read()

    if event == sg.WIN_CLOSED or event == "Exit":
        break

    if event == "Add to Cart":
        product_name = values["product_name"]
        quantity = int(values["quantity"])
        price = float(values["price"])

        cart.append((product_name, quantity, price))
        window["receipt"].print(f"{product_name} x{quantity} - ${price:.2f} added to cart")

    if event == "Calculate Total":
        total = sum(quantity * price for _, quantity, price in cart)
        window["receipt"].print(f"Total: ${total:.2f}\n")

# Close the window
window.close()
