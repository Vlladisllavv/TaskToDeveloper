import sqlite3

db = sqlite3.connect('first.db')
cur = db.cursor()


def make_db():
    cur.execute("CREATE TABLE IF NOT EXISTS profile(user_id text primary key)")
    db.commit()


def edit_profile(user_id):
    res = cur.execute("SELECT * FROM profile WHERE user_id = ?", (user_id,)).fetchall()
    print(res)
    if res:
        print('Ты есть в БД')
    else:
        cur.execute("INSERT INTO profile ('user_id') VALUES(?)", (user_id,))
        db.commit()
