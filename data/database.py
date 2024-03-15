import aiosqlite
import os

# class Database:
#     def __init__(self, db_name):
#         self.connections = aiosqlite.connect(db_name)
db_name = os.getenv('DB_NAME')


async def get_quiz_index(user_id):
    # Подключаемся к базе данных
    async with aiosqlite.connect(db_name) as db:
        # Получаем запись для заданного пользователя
        async with db.execute('SELECT question_index FROM quiz_state WHERE user_id = (?)', (user_id, )) as cursor:
            # Возвращаем результат
            results = await cursor.fetchone()
            if results is not None:
                return results[0]
            else:
                return 0


async def create_table():
    # Создаем соединение с базой данных (если она не существует, она будет создана)
    async with aiosqlite.connect(db_name) as db:
        # Создаем таблицу
        await db.execute('''CREATE TABLE IF NOT EXISTS quiz_state (user_id INTEGER PRIMARY KEY, question_index INTEGER)''')
        await db.execute('''CREATE TABLE IF NOT EXISTS users (user_id INTEGER PRIMARY KEY, score INTEGER)''')
        # Сохраняем изменения
        await db.commit()


async def get_user_score(user_id):
    async with aiosqlite.connect(db_name) as db:
        async with db.execute('SELECT score FROM users WHERE user_id = ?', (user_id,)) as cursor:
            results = await cursor.fetchone()
            if results is not None:
                return results[0]
            else:
                return 0


async def update_quiz_index(user_id, index):
    # Создаем соединение с базой данных (если она не существует, она будет создана)
    async with aiosqlite.connect(db_name) as db:
        # Вставляем новую запись или заменяем ее, если с данным user_id уже существует
        await db.execute('INSERT OR REPLACE INTO quiz_state (user_id, question_index) VALUES (?, ?)', (user_id, index))
        # Сохраняем изменения
        await db.commit()


async def update_user_score(user_id, new_score):
    async with aiosqlite.connect(db_name) as db:
        await db.execute('INSERT INTO users (user_id, score) VALUES (?, ?) ON CONFLICT(user_id) DO UPDATE SET score = excluded.score', (user_id, new_score))
        await db.commit()

