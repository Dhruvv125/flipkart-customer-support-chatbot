import random

# ==============================
# Flipkart Chatbot Questions
# ==============================

chatbot = {

    # Greetings
    ("hi", "hello", "hey", "hii", "good morning", "good evening"): [
        "Hello! Welcome to Flipkart. 😊",
        "Hi! How can I help you today?",
        "Hey! Welcome to Flipkart Customer Support.",
        "Welcome! What can I do for you?"
    ],

    # Order Status
    ("order", "track order", "where is my order", "order status", "my order"): [
        "Please enter your Order ID to track your order.",
        "You can check your order status from the 'My Orders' section.",
        "Your order is being processed. Please check your Order ID.",
        "You can track your order anytime from your Flipkart account."
    ],

    # Delivery
    ("delivery", "delivery date", "late delivery", "when will my order arrive"): [
        "Your expected delivery date is shown in 'My Orders'.",
        "Delivery usually takes 2-7 business days.",
        "We're sorry for the delay. Your order will arrive soon.",
        "Please track your shipment for the latest updates."
    ],

    # Return
    ("return", "replace", "return product", "replacement"): [
        "You can return eligible products within 7 days.",
        "Go to 'My Orders' and click Return/Replace.",
        "Your return request will be reviewed shortly.",
        "Replacement is available for eligible products."
    ],

    # Refund
    ("refund", "money back", "refund status"): [
        "Refunds are usually processed within 3-7 business days.",
        "Your refund will be credited to your original payment method.",
        "You can check your refund status in 'My Orders'.",
        "Your refund request is being processed."
    ],

    # Payment
    ("payment", "payment failed", "upi", "card payment", "net banking"): [
        "Please try the payment again after a few minutes.",
        "If money was deducted, it will be refunded automatically.",
        "Flipkart supports UPI, Cards, Net Banking and Wallets.",
        "Please check your bank account for the latest payment status."
    ],

    # Cancel Order
    ("cancel order", "cancel my order", "order cancel"): [
        "You can cancel your order from the 'My Orders' section.",
        "Cancellation is available before the product is shipped.",
        "Your cancellation request has been received."
    ],

    # Customer Support
    ("help", "support", "customer care", "contact support"): [
        "Our customer support team is available 24×7.",
        "Please tell me your issue. I'll try my best to help.",
        "How may I assist you today?"
    ],

    # Exit
    ("bye", "exit", "quit"): [
        "Thank you for contacting Flipkart. Have a great day! 👋",
        "Goodbye! Visit Flipkart again. 😊",
        "See you soon. Happy Shopping!"
    ]
}


# ==============================
# Chatbot Function
# ==============================

def get_response(user_message):

    user_message = user_message.lower().strip()

    for questions, answers in chatbot.items():

        if user_message in questions:
            return random.choice(answers)

    return random.choice([
        "Sorry, I didn't understand your question.",
        "Can you please rephrase your question?",
        "I can help with Orders, Delivery, Refund, Returns and Payments.",
        "Please ask a Flipkart-related question."
    ])