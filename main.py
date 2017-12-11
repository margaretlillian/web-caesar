from flask import Flask, request
from caesar import alphabet, rotate_string

app = Flask(__name__)
app.config['DEBUG'] = True

form = """<!DOCTYPE html>
<html>
    <head>
    <title>Caesar Cipher</title>
    <style type="text/css">
    body {{
        background: #f9f9f9;
        color: #666;
        font: lighter 1.5em arial, sans-serif;
    }}
    p, input {{
        font-size: 0.75em;
    }}
    h1 {{
        text-align: center;
        text-transform: uppercase;
        font-weight: lighter;
        padding-bottom: 0;
        margin-bottom: 0;
    }}       

    form {{ 
        margin: 10px auto;
        width: 540px;
        border-radius: 10px;
        background-color: #ced9db;
        padding: 20px;
                }}
            input, textarea {{
                background: #edf9fc;
                border: 1px solid #0e82a0;
                color: #33535b;
            }}
            textarea {{
                margin: 10px 0;
                width: 500px;
                height: 120px;
                font: 1em arial, sans-serif;
            }}
    </style>
    </head>

    <body>
        <div>
        <h1>Caesar Cipher</h1>
        
        <form method="post">
            <p>The Caesar Cipher iterates over each character in the message, rotating each letter x number of times.
            For example, a rotation of 1 would make the word "thing" become "uijoh". 
            Enter a message you want to encrypt and how many times to rotate the characters. </p>
            <label>
            Rotate by: <input type="text" name="rot">
            </label>

            <label>
            <br><br>Enter the message to encrypt.<br>
            <textarea name="text">{0}
            </textarea>
            </label>
            
            <input type="submit" value="Encrypt">
        </form>
        </div>
    </body>
</html>"""

@app.route("/")

def index():
    return form.format("")

@app.route("/", methods=['POST'])

def encrypt():
    #request.form(name-of-thing-being-requested)
    rot = request.form["rot"]
    text = request.form["text"]
    new_text = rotate_string(text, int(rot))
    return form.format(new_text)
app.run()