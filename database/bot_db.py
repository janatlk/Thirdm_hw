import sqlite3


def sql_create():
    global db, cursor
    db = sqlite3.connect("bot.sqlite3")
    cursor = db.cursor()

    if db:
        print("База данных подключена!")
    db.execute("CREATE TABLE IF NOT EXISTS menu"
               "(photo TEXT, name TEXT PRIMARY KEY,"
               "description TEXT, price TEXT)"
               )
    db.commit()

async def sql_command_insert(state):
    # try:
    async with state.proxy() as data:
        cursor.execute("INSERT INTO menu VALUES "
                       "(?, ?, ?, ?)", tuple(data.values()))
        db.commit()
    # except:
    #     print("Ошибка отправки данных!")

async def sql_command_all():
    return cursor.execute("SELECT * FROM menu").fetchall()

async def sql_command_delete(name):
    cursor.execute("DELETE FROM menu WHERE name == ?", (name,))
    db.commit()