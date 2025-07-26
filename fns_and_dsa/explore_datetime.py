from datetime import datetime

def display_current_datetime():
    current_date = datetime.datetime.now()
    #Format and print the current date and time in a readable format, such as “YYYY-MM-DD HH:MM:SS”.
    current_date.strftime("%Y-%m-%d %H:%M:%S")
    print(f"Current date and time: {current_date}")
display_current_datetime()


future_day = int(input("Enter the number of days to add to the current date: "))
def calculate_future_date():
    global future_day
    future_date = ""
    today = datetime.datetime.now()
    future_date = today + datetime.timedelta(days=future_day)
    #Print the future date in a format like “YYYY-MM-DD”.

    print(f"Future date: {future_date.strftime("%Y-%m-%d")}")

calculate_future_date()
