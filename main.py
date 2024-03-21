from flask import Flask
from random import randint

app = Flask(__name__)# Import the Flask class from the flask module
from flask import Flask
from random import randint

# Create an instance of the Flask class with the name of the current module as the argument
app = Flask(__name__)

# Generate a random number between 0 and 9 (inclusive)
correct_number = randint(0, 9)

# Decorator function to center content on the page
def center(function):
    def wrapper():
        # Wraps the content returned by the decorated function in a div element
        return '<div style="position:absolute;left:50%;top:50%;transform:translate(-50%, -60%);">' + function() \
            + "</div>"
    return wrapper

# Route decorator for the home page ("/")
@app.route("/")
# Apply the center decorator to the home_page function
@center
def home_page():
    # Prints the correct number in the console for debugging purposes
    print(correct_number)
    # Return HTML content for the home page, including an h1 heading and an iframe displaying a GIF
    return '<div style="position:absolute;left:50%;top:50%;transform:translate(-50%, -60%);text-align:center;">' \
           '<h1>Guess a number between 0 and 9!</h1>' \
           '<iframe src="https://giphy.com/embed/2x0VePimPaFJDpGZ7H" width="480" height="480" frameBorder="0" ' \
           'class="giphy-embed" allowFullScreen></iframe>' \
           '</div>'

# Route decorator for handling guesses ("/<int:guess>")
@app.route("/<int:guess>")
def guess_check(guess):
    if guess < correct_number:
        # If the guess is too low, return HTML content indicating it's too low and display a corresponding GIF
        result = '<div style="position:absolute;left:50%;top:50%;transform:translate(-50%, -50%);text-align:center;">' \
                 '<h1 style="text-align:top;">Too Low!</h1>' \
                 '<iframe src="https://giphy.com/embed/WUPmjKEKREEBq" width="480" height="363" frameBorder="0" ' \
                 'class="giphy-embed" allowFullScreen></iframe>' \
                 '</div>'
        return result
    elif guess > correct_number:
        # If the guess is too high, return HTML content indicating it's too high and display a corresponding GIF
        result = '<div style="position:absolute;left:50%;top:50%;transform:translate(-50%, -60%);">' \
                 '<h1 style="text-align:center;">Too High!</h1>' \
                 '<iframe src="https://giphy.com/embed/6lv7cWsF5CP96" width="480" height="245" frameBorder="0" ' \
                 'class="giphy-embed" allowFullScreen></iframe>' \
                 '</div>'
    else:
        # If the guess is correct, return HTML content indicating it's correct and display a corresponding GIF
        result = '<div style="position:absolute;left:50%;top:50%;transform:translate(-50%, -60%);">' \
                 '<h1 style="text-align:center;">You Got It!</h1>' \
                 '<iframe src="https://giphy.com/embed/lzRfMOmHgPmxy" width="480" height="480" frameBorder="0" ' \
                 'class="giphy-embed" allowFullScreen></iframe>' \
                 '</div>'
    return result

# To start the Flask server from the terminal, use the command: flask --app <filename> run
# To start the Flask server using code, execute the following block when this script is directly executed
if __name__ == "__main__":
    # Run the Flask app in debug mode
    app.run(debug=True)

correct_number = randint(0, 9)


def center(function):
    def wrapper():
        return '<div style="position:absolute;left:50%;top:50%;transform:translate(-50%, -60%);">' + function() \
            + "</div>"
    return wrapper


@app.route("/")
@center
def home_page():
    # Prints the correct number in the console for debugging purposes
    print(correct_number)
    return '<div style="position:absolute;left:50%;top:50%;transform:translate(-50%, -60%);text-align:center;">' \
           '<h1>Guess a number between 0 and 9!</h1>' \
           '<iframe src="https://giphy.com/embed/2x0VePimPaFJDpGZ7H" width="480" height="480" frameBorder="0" ' \
           'class="giphy-embed" allowFullScreen></iframe>' \
           '</div>'




@app.route("/<int:guess>")
def guess_check(guess):
    if guess < correct_number:
        # If the guess is too low, display a message and a corresponding GIF
        result = '<div style="position:absolute;left:50%;top:50%;transform:translate(-50%, -50%);text-align:center;">' \
                 '<h1 style="text-align:top;">Too Low!</h1>' \
                 '<iframe src="https://giphy.com/embed/WUPmjKEKREEBq" width="480" height="363" frameBorder="0" ' \
           'class="giphy-embed" allowFullScreen></iframe>' \
           '</div>'
        return result


    elif guess > correct_number:
        # If the guess is too high, display a message and a corresponding GIF
        result = '<div style="position:absolute;left:50%;top:50%;transform:translate(-50%, -60%);">' \
                 '<h1 style="text-align:center;">Too High!</h1>' \
                 '<iframe src="https://giphy.com/embed/6lv7cWsF5CP96" width="480" height="245" frameBorder="0" ' \
                 'class="giphy-embed" allowFullScreen></iframe>' \
                 '</div>'
    else:
        # If the guess is correct, display a message and a corresponding GIF
        result = '<div style="position:absolute;left:50%;top:50%;transform:translate(-50%, -60%);">' \
                 '<h1 style="text-align:center;">You Got It!</h1>' \
                 '<iframe src="https://giphy.com/embed/lzRfMOmHgPmxy" width="480" height="480" frameBorder="0" ' \
                 'class="giphy-embed" allowFullScreen></iframe>' \
                 '</div>'
    return result


# To start server (in terminal):
# flask --app <filename> run
# To start server (using code):
if __name__ == "__main__":
    # Run the Flask app in debug mode
    app.run(debug=False)
