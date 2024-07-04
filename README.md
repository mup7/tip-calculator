# Tip Calculator

Welcome to the Tip Calculator! This is a simple Tkinter-based application that helps you calculate how much each person should pay based on the total bill, tip percentage, and number of people splitting the bill.

## Features

- User-friendly graphical interface
- Input fields for bill amount, tip percentage, and number of people
- Calculates the amount per person
- Error handling for invalid input

## Prerequisites

- Python 3.x
- Tkinter (usually included with Python)

## Installation

1. **Clone the repository:**
   ```bash
   git clone https://github.com/mup7/tip-calculator.git
   cd tip-calculator
   ```

## Usage

1. **Run the application:**
   ```bash
   python main.py
   ```

2. **Use the application:**
   - Enter the total bill amount in dollars.
   - Enter the desired tip percentage (e.g., 10 for 10%).
   - Enter the number of people splitting the bill.
   - Click on the "Calculate" button.
   - The calculated amount each person should pay will be displayed.

## Code Overview

**main.py**  
This file serves as the entry point of the application. It imports the **'Root'** class from **'root.py'** and initializes it to start the Tkinter application.

**root.py**  
This file contains the **'Root'** class, which handles the creation and management of the Tkinter root window and its widgets.

- **'__init__' method**: Initializes the root window and widgets (labels, entry fields, and button).
- **'calculate_bill_per_person' method**: Calculates and displays the amount each person should pay based on user inputs.

**Detailed Code Comments**  
The code is thoroughly commented to explain each part of the GUI setup and the logic for calculating the bill per person.

## License

This project is licensed under the MIT License. See the [LICENSE](https://github.com/mup7/tip-calculator/blob/main/LICENSE) file for details.

## Contributing

Contributions are welcome! Please fork the repository and submit a pull request with your changes.

## Acknowledgements

- The Tkinter documentation and community for their helpful resources.

## Contact

For any questions or feedback, please contact [mupdlv@gmail.com](mailto:mupdlv@gmail.com).
