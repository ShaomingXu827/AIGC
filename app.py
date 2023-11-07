from flask import Flask, request, render_template_string
import openai
from openai import OpenAI

client = OpenAI()

app = Flask(__name__)

HTML_TEMPLATE = """
<!doctype html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <title>ChatGPT Flask App</title>
</head>
<body>
  <h1>Ask ChatGPT</h1>
  <form action="/" method="post">
    <input type="text" name="question" placeholder="Ask something..." />
    <input type="submit" value="Submit">
  </form>
  <p>{{ response }}</p>
</body>
</html>
"""

@app.route('/', methods=['GET', 'POST'])
def index():
    response = ""
    if request.method == 'POST':
        question = request.form['question']
        response = ask_openai(question)
    return render_template_string(HTML_TEMPLATE, response=response)

def ask_openai(question):
    try:
        response = client.completions.create(
            model="text-davinci-003",
            prompt=question,
            max_tokens = 150
        )
        return response.choices[0].text.strip()
    except Exception as e:
        return str(e)

if __name__ == '__main__':
    app.run(debug=True)