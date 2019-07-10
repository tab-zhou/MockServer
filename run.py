# coding:utf-8
from app import app
from app.user import user
from app.test import test

app.config.update(DEBUG=True)
app.config.update(ENV="development")

app.register_blueprint(user, url_prefix='/user')
app.register_blueprint(test, url_prefix='/test')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=7777, debug=True)

