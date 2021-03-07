from flask import Flask, request 

app = Flask(__name__)

@app.route('/')
def home():
    return 'Hello home'

@app.route('/query_example')
def query_example():
    language = request.args.get('language')
    framework = request.args.get('framework')
    library = request.args.get('library')

    result1 = "{0} is the language from the query string.".format(language)
    result2 = "{0} is the framework from the query string.".format(framework)
    result3 = "{0} is the library from the query string.".format(library)

    return """
            <h1>{0}</h1>
            <h1>{1}</h1>
            <h1>{2}</h1>,
    """ .format(result1, result2, result3)

@app.route('/form_example', methods=['GET', 'POST'])
def form_example():
    if request.method == 'POST':
        framework = request.form.get('framework')
        language = request.form.get('language')

        return """
                <h1>{0} is from the framework form</h1>
                <h1>{1} is from the language form</h1>""".format(framework, language)

    return '''
              <form method="POST">
                  <div><label>Language: <input type="text" name="language"></label></div>
                  <div><label>Framework: <input type="text" name="framework"></label></div>
                  <input type="submit" value="Submit">
              </form>'''

@app.route('/json_example')
def json_example():
    return 'json example'



if __name__ == '__main__':
    app.run(debug=True)