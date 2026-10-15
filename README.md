
# Flipkart Customer Support Chatbot

A simple web-based customer support chatbot built using Python and Flask. It provides predefined responses to common customer questions related to orders, delivery, product returns, refunds, payments and cancellations.

## Features

- Interactive chatbot interface
- Order status and delivery guidance
- Return and replacement guidance
- Refund and payment assistance
- Order cancellation information
- Simple and responsive web interface

## Technologies Used

- Python
- Flask
- HTML
- CSS
- JavaScript

## Project Structure

```text
flipkart-customer-support-chatbot/
├── app.py
├── chatbot.py
├── requirements.txt
├── README.md
├── .gitignore
├── templates/
│   └── index.html
└── static/
    ├── style.css
    └── script.js
```

## Installation and Setup

1. Install Python and Git.
2. Clone or download this repository.
3. Open the project folder in VS Code.
4. Create a virtual environment:

   ```bash
   python -m venv .venv
   ```

5. Activate the environment in Windows PowerShell:

   ```powershell
   .\.venv\Scripts\Activate.ps1
   ```

6. Install the dependencies:

   ```bash
   python -m pip install -r requirements.txt
   ```

7. Start the application:

   ```bash
   python app.py
   ```

8. Open http://127.0.0.1:5000 in your browser.

## Example Questions

- Hello
- Track order
- Delivery
- Return
- Refund status
- Payment
- Cancel order
- Help

## How It Works

The Flask application serves the chatbot webpage and receives messages from the frontend. The chatbot module matches the user's message against predefined phrases and returns a corresponding response.

## Limitations

This is an educational, rule-based chatbot prototype. It does not connect to Flipkart's official systems and cannot retrieve actual orders, payment records or refund status.

## Future Improvements

- Add a database for conversation history.
- Improve natural-language understanding.
- Add automated chatbot testing.
- Integrate an authorized customer support API if available.

## Disclaimer

This project is intended for educational purposes. It is not an official Flipkart product or service.
