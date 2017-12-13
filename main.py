from flask import Flask, request
from caesar import rotate_string

app = Flask(__name__)
app.config['DEBUG'] = True

header = """<!DOCTYPE html>
<html>
    <head>
    <title>Caesar Cipher</title>
    <style type="text/css">
    body {
        background: #f9f9f9;
        color: #666;
        font: lighter 1.5em arial, sans-serif;
    }
    a{
        color: #117a9e;
        font-weight: bold;
        text-decoration: none;
        border-bottom: 1px solid #536870;
    }
    p, input {
        font-size: 0.75em;
    }
    h1 {
        text-align: center;
        text-transform: uppercase;
        font-weight: lighter;
        padding-bottom: 0;
        margin-bottom: 0;
    }       
    h2 {
        font-weight: lighter;
    }
    div {
        margin: 10px auto;
        width: 540px;
        border-radius: 10px;
        background-color: #ced9db;
        padding: 20px;
                }
            input, textarea {
                background: #edf9fc;
                border: 1px solid #0e82a0;
                color: #33535b;
            }
            textarea {
                margin: 10px 0;
                width: 500px;
                height: 120px;
                font: 1em arial, sans-serif;
            }
    </style>
    </head>

    <body>
        
        <h1>Caesar Cipher</h1>
        <div>"""
footer = """
        </div>
    </body>
</html>"""

form = """{HEADER}
        <form method="post">
            <p>The Caesar Cipher rotates each character in the message x number of times.
            For example, a rotation of 1 would make the word "thing" become "uijoh". 
            Enter a message you want to encrypt and how many times to rotate the characters. </p>
            <label>
            Rotate by: <input type="text" name="rot">
            </label>

            <label>
            <br><br>Enter the message to encrypt.<br>
            <textarea name="text">{TEXT}
 </textarea>
            </label>
            
            <input type="submit" value="Encrypt">
        </form>
{FOOTER}"""


error = """{HEADER}
<h2>Error!</h2>
    <p>Please enter a valid number. Letters, punctuation (including commas in larger numbers), and decimals are not allowed.</p>
    <p><a href="/">Return back</a></p>

    {FOOTER}
    """

@app.route("/")

def index():
    return form.format(HEADER=header, TEXT="", FOOTER=footer)

@app.route("/", methods=['POST'])

def encrypt():
    #request.form(name-of-thing-being-requested)
    try:
        rot = request.form["rot"]
        text = request.form["text"]
        new_text = rotate_string(text, int(rot))
    except ValueError:
        return error.format(HEADER=header, FOOTER=footer)
    else:
        return form.format(HEADER=header, TEXT=new_text, FOOTER=footer)
app.run()