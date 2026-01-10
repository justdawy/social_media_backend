from flask import Flask, render_template_string

def create_app():
    app = Flask(__name__)
    
    @app.route('/hello')
    def hello_world():
        return render_template_string('<h1>Hello, World!</h1>')
    
    return app