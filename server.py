"""Greeting Flask app."""

from random import choice

from flask import Flask, request

# "__name__" is a special Python variable for the name of the current module
# Flask wants to know this to know what any imported things are relative to.
app = Flask(__name__)

AWESOMENESS = [
    'awesome', 'terrific', 'fantastic', 'neato', 'fantabulous', 'wowza',
    'oh-so-not-meh', 'brilliant', 'ducky', 'coolio', 'incredible',
    'wonderful', 'smashing', 'lovely']


@app.route('/')
def start_here():
    """Home page."""

    #return "<!doctype html><html>Hi! This is the home page.</html>"
    return "<!doctype html><html>Hi! This is the home page. <a href='/hello'> Continue here.</a></html>"

@app.route('/hello')
def say_hello():
    """Say hello and prompt for user's name."""
    name = input("person")
    return """
    <!doctype html>
    <html>
      <head>
        <title>Hi There!</title>
      </head>
      <body>
        <h1>Hi There!</h1>
        <form action="/greet">
          What's your name? <input type="text" name="person"><br>
          Select a compliment:
          <select name="compliment">
            <option value="awesome">awesome</option>
            <option value="terrific">terrific</option>
            <option value="fantastic">fantastic</option>
            <option value="neato">neato</option>
            <input type="submit" value="Submit"> <br>
            </form>
        <form action="/diss">
        What's your name? <input type="text" name="person"><br>
          Select an insult:
          <select name="insult">
            <option value="rude">rude</option>
            <option value="mean">mean</option>
            <option value="stinky">stinky</option>
            <option value="dumb">dumb</option>
            <input type="submit" value="Submit">
        </form>
      </body>
    </html>
    """


@app.route('/greet')
def greet_person():
    """Get user by name."""

    player = request.args.get("person")

    # rand_compliment = choice(AWESOMENESS)
    compliment = request.args.get("compliment")

    return f"""
    <!doctype html>
    <html>
      <head>
        <title>A Compliment</title>
      </head>
      <body>
        Hi, {player}! I think you're {compliment}!
      </body>
    </html>
    """


@app.route('/diss')
def diss_person():
  """Insult user by name."""

  player = request.args.get("person")

  insult = request.args.get("insult")

  return f"""
    <!doctype html>
    <html>
      <head>
        <title>An Insult</title>
      </head>
      <body>
        Hi, {player}! I think you're {insult}!
      </body>
    </html>
    """

if __name__ == '__main__':
    # debug=True gives us error messages in the browser and also "reloads"
    # our web app if we change the code.
    app.run(debug=True, host="0.0.0.0", port=5001)
