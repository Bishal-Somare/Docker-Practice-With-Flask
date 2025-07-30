from flask import Flask, request, render_template_string

app = Flask(__name__)

# HTML template to show form and output
HTML_TEMPLATE = '''
<!doctype html>
<title>Multiplication Table</title>
<h2>Enter a number to see its multiplication table</h2>
<form method="get">
  <input type="number" name="number" required>
  <input type="submit" value="Show Table">
</form>

{% if table %}
  <h3>Multiplication Table of {{ number }}</h3>
  <ul>
    {% for row in table %}
      <li>{{ row }}</li>
    {% endfor %}
  </ul>
{% endif %}
'''

@app.route('/', methods=['GET'])
def table():
    number = request.args.get('number', type=int)
    table = None
    if number is not None:
        table = [f"{number} x {i} = {number * i}" for i in range(1, 11)]
    return render_template_string(HTML_TEMPLATE, number=number, table=table)

if __name__ == '__main__':
     app.run(host='0.0.0.0', port=5000)
