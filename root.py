import tkinter

TITLE_FONT = ("Arial", 15, "normal")

class Root:
    """
    This class creates a Tkinter window for a Tip Calculator application.
    """

    def __init__(self):
        """
        Initializes the Tkinter window and its widgets.
        """
        self.root = tkinter.Tk()
        self.root.config(padx=25, pady=25)
        self.root.title("Tip Calculator")
        self.root.iconbitmap("logo.ico")

        # Welcome label
        self.label1 = tkinter.Label(text="Welcome to the Tip Calculator!", font=TITLE_FONT)
        self.label1.pack()

        # Bill amount input
        self.label2 = tkinter.Label(text="What was the total bill cost? ($)")
        self.label2.pack()
        self.bill = tkinter.Entry()
        self.bill.pack()
        self.bill.focus()  # Set focus to the bill input field

        # Tip percentage input
        self.label3 = tkinter.Label(text="How much would you like to tip? (%)")
        self.label3.pack()
        self.tip = tkinter.Entry()
        self.tip.pack()

        # Number of people input
        self.label4 = tkinter.Label(text="How many people to split the bill?")
        self.label4.pack()
        self.people = tkinter.Entry()
        self.people.pack()

        # Calculate button
        self.submit_button = tkinter.Button(text="Calculate", command=self.calculate_bill_per_person)
        self.submit_button.pack()

        # Result label
        self.result_label = tkinter.Label(text="")
        self.result_label.pack()

        # Start the Tkinter event loop
        self.root.mainloop()

    def calculate_bill_per_person(self):
        """
        Calculates the amount each person should pay based on the total bill,
        the tip percentage, and the number of people. Updates the result label
        with the calculated amount.
        """
        try:
            # Retrieve and convert input values
            tip_as_decimal = float(self.tip.get()) / 100
            total_bill = float(self.bill.get()) * (1 + tip_as_decimal)
            total_bill_per_person = round(total_bill / int(self.people.get()), 2)

            # Update result label with the calculated amount
            self.result_label.config(text=f"Each person should pay: ${total_bill_per_person:.2f}")
        except ValueError:
            # Handle invalid input
            self.result_label.config(text="Please, enter numbers to calculate.")
