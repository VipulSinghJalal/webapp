from app import app

@app.route('/')
@app.route('/home')
def home():
    return "basic page check"
