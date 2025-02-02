from flask import Flask, render_template

app = Flask(__name__)

# Criamos uma rota ( Página incial do site)
@app.route('/')
def home():
    return render_template('index.html')

# Running server when we run the file
if __name__ == '__main__':
    app.run(debug=True) # the debug=true update the site automatic

