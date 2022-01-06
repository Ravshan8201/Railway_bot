import sqlite3
conn = sqlite3.connect('user_list.sqlite')
cur = conn.cursor()
cur.execute('''
CREATE TABLE IF NOT EXISTS Nnn(
TG_ID INTEGER ,
STAS INTEGER 
)
''')
first_insertd = '''
INSERT INTO Nnn VALUES ('{}','{}')
'''
upd_stas = '''
UPDATE Nnn 
SET STAS = '{}' 
WHERE TG_ID = '{}'
'''
select_stas = '''
SELECT STAS
From Nnn
WHERE TG_ID = '{}'
'''

upd_tg = '''
UPDATE Nnn 
SET TG_ID = '{}' 
WHERE TG_ID = '{}'
'''
select_tg = '''
SELECT TG_ID
From Nnn
WHERE TG_ID = '{}'
'''
