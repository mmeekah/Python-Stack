from flask import Flask
app=Flask(__name__)
@app.route('/')
def hello_world():
    return 'Hello World!'


# @app.route('/dojo')
# def say_dojo():
#     return 'Say Dojo!'


@app.route('/say/<name>')
def say(name):
    print (name)
    return 'Hi, '+name +'!'

@app.route('/repeat/<num>/<word>')
def say_n_times(num,word):
    return (word + " ") * int(num)


@app.errorhandler(404)
def page_not_found(e):
  return  "Sorry! No response. Try again."

if __name__=="__main__":   # Ensure this file is being run directly and not from a different module    
    app.run(debug=True)    # Run the app in debug mode.