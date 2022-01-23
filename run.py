from func import *
import func


@app.route('/', methods=['POST', 'GET'])
@app.route('/index', methods=['POST', 'GET'])
def index():
    return func.index()

@app.route('/view_users')
def view_users():
    return func.view_users()


if __name__ == '__main__':
    app.run(debug=True)
