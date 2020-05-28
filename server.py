# python3 -m venv calc --> sourse bin/activate --> deactivate

from bottle import route, run, static_file, request, template
import numexpr as ne


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


if __name__ == '__main__':
    run(host='localhost', port=8080)
# jjhmmmhm