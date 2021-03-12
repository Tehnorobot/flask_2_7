from flask import Flask, render_template
from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileRequired
import json

app = Flask(__name__)

app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'

class LoginForm(FlaskForm):
    photo = FileField(validators=[FileRequired()])
    
@app.route('/member', methods=['GET', 'POST'])
def member():
    with open("templates/info.json", "rt", encoding="utf8") as f:
        news_list = json.loads(f.read())
    len_list = len(news_list['info'])
    return render_template('login_2.html', news=news_list, len_list=len_list)
    
    
if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')