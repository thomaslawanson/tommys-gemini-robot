# it should ask user for their name so it can use their name✅
# it should be able to tell the date of the day✅
# it should know the user's age✅
# it should be able to count from any start to any end with any steps✅
# it should be able to calculate the year that i was born✅

# it should be able  to know when my computer was turned on
# it should be able to know the operating system of my computer ✅
# should be able to draw anything we will input what do you want to draw? hot dog for example it draws a hot dog
# Date should be printed as Monday, 2024-11-10✅
# Anything that has content inside of it (a header), should have a colon at the end like this:

import winreg
from datetime import datetime, date

import requests
# Requests handles communication with websites, getting the full data
from bs4 import BeautifulSoup as bs

# Beautiful Soup formats & selects specific parts of the data
# aria-level="3" role="heading"
# Websites are written in HTML (Hyper Text Markup Language)
# We need to use HTML to communicate with websites and get specific data
import hangman

HEADERS = {
    "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
    "accept-encoding": "gzip, deflate",
    "accept-language": "en-US,en;q=0.9",
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36",
}


def print_options(users_name):
    print('Welcome,', users_name, '!')
    print('(1) Change your information.')
    print('(2) Count from and to with step.')
    print('(3) Get current date.')
    print('(4) Calculate the year I was born.')
    print('(5) Calculate your (Body Mass Index) Also know as BMI.')
    print("(6) Get the time in any location.")
    print("(7) Get the temp in any location.")
    print("(8) Get our main browser.")
    print('(9) Play hangman.')
    print('(10) Exit.')
    option = input('> ')
    return option


def request_time(location):
    req = requests.get(f'https://www.google.com/search?q=time+in+{location}', headers=HEADERS)
    # We use HEADERS to identify our request so it doesn't look empty & suspicious
    # in other words, we make the website think we're humans not a robot
    soup = bs(req.text, 'html.parser')
    # So, we use a parser/formatter called html.parser from BeautifulSoup to format the content/text of the response.

    time_element = soup.find('div', {'aria-level': "3", "role": "heading"})

    try:
        return time_element.text
    except AttributeError:
        return "NOT FOUND"


def request_temp(location):
    req = requests.get(f"https://www.google.com/search?q=temperature+in+{location}", headers=HEADERS)
    soup = bs(req.text, "html.parser")

    temp_element = soup.find("span",{'id': 'wob_tm'})
    try:
        return temp_element.text
    except AttributeError:
        return "location not found"


def ask_for_input():
    name = input("I'm Gemini, what's your name please? Thanks! ")
    age = int(input("I'm wondering about your age? "))

    return name, age


def count_to(start, end, step):
    for i in range(start, end + 1, step):
        print(i)


def get_def_browser():
    try:
        with (winreg.HKEY_CURRENT_USER,
                    r"Software\Microsoft\Windows\Shell\Associations\UrlAssociations\http\UserChoice") as key:
            prog_id, _ = winreg.QueryValueEx(key, "ProgId")
            return prog_id  # This is the identifiers for the default browser
    except FileNotFoundError:
        return "Default browser not found"


def get_date():
    full_date = datetime.now()
    current_date = full_date.strftime("%Y-%m-%d")
    day_name = full_date.strftime("%A")
    print(day_name, current_date)


def calculate_year_born(user_age):
    current_year = date.today().year
    return (current_year - user_age)


def calculate_bmi(weight_kg, height_m):
    bmi = weight_kg / (height_m * height_m)
    classify = ''
    '''
    under 18.5 – This is described as underweight
    between 18.5 and 24.9 – This is described as the 'healthy range'.
    between 25 and 29.9 – This is described as overweight.
    between 30 and 39.9 – This is described as obesity.
    40 or over – This is described as severe obesity.
    '''
    if bmi < 18.5:  # wair very fair
        classify = "underweighted"
    elif 18.5 <= bmi <= 24.9:
        classify = "healthy"
    elif 25 <= bmi <= 29.9:
        classify = "fat"
    elif 30 <= bmi <= 39.9:
        classify = "really fat"
    elif 40 <= bmi:
        classify = "explodingly fatty"

    return bmi, classify


# The function content ends at the next fully un-indented line
# The function execution ends at the closest return or if there is no return, then at the end of the content

# This is called multi-assignment, where 1st gets assigned to 1st variable & 2nd gets assigned to 2nd variable
users_name, users_age = ask_for_input()

while True:
    selected_option = print_options(users_name)

    if selected_option == '1':
        users_name, users_age = ask_for_input()

    elif selected_option == '2':
        start_input = int(input("Start: "))
        end_input = int(input("end: "))
        step_input = int(input("step: "))
        print("Here's the count:")
        count_to(start_input, end_input, step_input)

    elif selected_option == '3':
        print("Current Date:")
        get_date()

        # if: different variables
        # elif: same variable

    elif selected_option == '4':
        print('The year you were born is:')
        print(calculate_year_born(users_age))

    elif selected_option == '5':
        users_gender = input("Are you a male (M) or a female (F)? ")
        users_weight = float(input("What's your weight in kg? "))
        users_height = float(input("What's your height in meters? "))

        users_bmi, users_classification = calculate_bmi(users_weight, users_height)

        print('Your BMI is:', users_bmi)
        print('Your classification is....', users_classification)


    elif selected_option == '6':
        user_location = input("Write the location you want the time in: ")
        output_time = request_time(user_location)
        print(f"The time in {user_location} is: {output_time}")
    elif selected_option == '7':
        user_location = input("Write the location you want the temperature in: ")
        # °F = °C × (9/5) + 32
        output_temperature_c = int(request_temp(user_location))
        output_temperature_f = output_temperature_c * (9/5) + 32
        print(f"The temperature in {user_location} is: {output_temperature_c} C | {output_temperature_f} F")
    elif selected_option == '8':
       user_browser = get_def_browser()
       print(f"Your browser is: {user_browser}")
    elif selected_option == "9":
        hangman.play_hangman()

    elif selected_option == "10":

        break
    else:
        print("Invalid option - pick a corect option ")

    print()


# git config --global user.email "you@example.com" git config --global user.name "Your Name" to set your account's default identity
