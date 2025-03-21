from flask import Flask, render_template,request, redirect
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

app = Flask(__name__)
# Configure SQLAlchemy
app.config['SQLALCHEMY_DATABASE_URI'] ='mysql+pymysql://root:Jjsh5371@localhost/flaskdemo'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
migrate = Migrate(app, db)

class Book(db.Model):
   id = db.Column(db.Integer, primary_key=True, autoincrement=True)
   title = db.Column(db.String(100), unique=True)
   author = db.Column(db.String(100))
   price = db.Column(db.Integer())


@app.route('/')
def home():
   obj = Book.query.all()
   return render_template('home.html', book=obj)

@app.route('/add_book/', methods=['GET','POST'])
def add_book():
   if request.method == 'POST':
      obj = Book()
      obj.title = request.form['title']
      obj.author = request.form['author']
      obj.price = request.form['price']
      db.session.add(obj)
      db.session.commit()
      return redirect('/')
   return render_template('add_book.html')

@app.route('/delete/<int:id>/')
def delete_book(id):
   obj = Book.query.get_or_404(id)
   db.session.delete(obj)
   db.session.commit()
   return redirect('/')

@app.route('/update/<int:id>/', methods=['GET', 'POST'])
def update_book(id):
   obj = Book.query.get_or_404(id)
   if request.method == 'POST':
      obj.title = request.form['title']
      obj.author = request.form['author']
      obj.price = request.form['price']
      db.session.commit()
      return redirect('/')
   return render_template('update_book.html', book=obj)



if __name__ == '__main__':
   app.run(debug=True)