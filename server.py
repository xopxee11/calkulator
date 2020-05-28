from bottle import route, run, static_file, request, template
import numexpr as ne
import os


@route('/')
def send_index():
    return template('index', result=None)


@route('/style.css')
def send_css():
    return static_file('style.css', root='.')


@route('/icon.ico')
def send_icon():
    return static_file('icon.ico', root='.')


@route('/', method='POST')
def calculate():
    try:
        result = ne.evaluate(request.forms.get('expression'))
    except (KeyError, SyntaxError, TypeError):
        result = 'error'
    return template('index', result=result)


if os.environ.get('APP_LOCATION') == 'heroku':
    run(host="0.0.0.0", port=int(os.environ.get("PORT", 5000)))
else:
    run(host='localhost', port=8080)
