import sqlite3
conn = sqlite3.connect(r"D:\w2\Suracha_python\projectโค้ด\date.db")
c = conn.cursor()
c.execute('''CREATE TABLE loan(
    Users   varchar(40)  NOT NULL,
    Pass    varchar(20)  NOT NULL,
    Name    varchar(20)  NOT NULL,
    Address varchar(120) NOT NULL,
    Year    int          NOT NULL,
    Month   int          NOT NULL,
    Day     int          NOT NULL,
    Money   int          NOT NULL,
    Tel     int          NOT NULL)''')
conn.commit()
conn.close()