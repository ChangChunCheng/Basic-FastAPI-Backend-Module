from src.configs.psql import DB_Config
import psycopg2
from passlib.context import CryptContext
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


def get_password_hash(password):
    return pwd_context.hash(password)


conn = psycopg2.connect(
    host=DB_Config().host,
    port=DB_Config().port,
    database=DB_Config().db,
    user=DB_Config().user,
    password=DB_Config().password
)

cur = conn.cursor()
cur.execute('''
    INSERT INTO Principal 
        (ID, Account, Password, Name, Disable, CreateAt, UpdateAt) 
    VALUES 
        (gen_random_uuid(), 'jacky850509@gmail.com', \' ''' + get_password_hash('aaa') + ''' \' , '張浚誠', FALSE, now(), now())
''')

cur.execute('''
    INSERT INTO Principal 
        (ID, Account, Password, Name, Disable, CreateAt, UpdateAt) 
    VALUES 
        (gen_random_uuid(), 'asd831222@gmail.com', \' ''' + get_password_hash('aaa') + ''' \' , '陳雲山', FALSE, now(), now())
''')

cur.execute('''
    INSERT INTO Principal 
        (ID, Account, Password, Name, Disable, CreateAt, UpdateAt) 
    VALUES 
        (gen_random_uuid(), 'wisdom8559@gmail.com', \' ''' + get_password_hash('aaa') + ''' \' , '張浚誠', FALSE, now(), now())
''')
conn.commit()


cur = conn.cursor()

cur.execute('select * from principal')
rows = cur.fetchall()
for row in rows:
    print(row)
