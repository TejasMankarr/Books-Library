from flask import Flask, request, jsonify
import sqlite3
import json

app = Flask(__name__)

def db_connection():
    conn = None
    try:
        conn = sqlite3.connect('books.sqlite')
    except sqlite3.error as e:
        print(e)
    return conn

@app.route('/books', methods=['GET','POST'])
def books():
    conn = db_connection()
    cursor = conn.cursor()

    if request.method == 'GET':
        cursor = conn.execute("SELECT * FROM books")
        books = [
            dict(id=row[0],author=row[1], title=row[2])
            for row in cursor.fetchall()
        ]
        if books is not None:
            return jsonify(books)
    
    if request.method == 'POST':
        new_author = request.form['author']
        new_title = request.form['title']
        sql = """
                INSERT INTO books (author,title) VALUES (?,?)
        """
        cursor = cursor.execute(sql, (new_author,new_title))
        conn.commit()

        return f'Book with the id: {cursor.lastrowid} created successfully'
        
# @app.route('/books/<int:id>', methods=['GET','PUT','DELETE'])
# def single_book(id):
#     if request.method == 'GET':
#         for book in book_list:
#             if book['id'] == id:
#                 return jsonify(book_list[id])
#             pass
#     if request.method == 'PUT':
#         for book in book_list:
#             if book['id'] == id:
#                 book['author'] = request.form['author']
#                 book['language'] = request.form['language']
#                 book['title'] = request.form['title']
#                 update_book = {
#                     'id': id,
#                     'author': book['author'],
#                     'language': book['language'],
#                     'title': book['title']
#                 }
#                 return jsonify(update_book)
#     if request.method == 'DELETE':
#         for index, book in enumerate(book_list):
#             if book['id'] == id:
#                 book_list.pop(index)
#                 return jsonify(book_list)

if __name__ == '__main__':
    app.run(debug=True)