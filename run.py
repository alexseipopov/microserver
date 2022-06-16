from flask import Flask, request, send_from_directory


app = Flask(__name__)

login = 'Pavel'
password = 'password'
token = 'qwerty'

directory = 'your local directory'
filename = 'name of file to download'
HEADER = 'some header f.e. AUTHORIZATION'


@app.route('/', methods=['GET'])
def index():
    if request.method != 'GET':
        return 'not get'
    print(request.args.get('login'), request.args.get('password'))
    if login in request.headers:
        if request.headers.get(login) == password:
            return token
    return 'not match'


@app.route('/download', methods=["GET"])
def download():
    if request.headers.get(HEADER) != token:
        return 'dont have nessesary header'
    send_from_directory(directory, filename=filename)
    return 'ok'


if __name__ == '__main__':
    app.run(port=5012)
