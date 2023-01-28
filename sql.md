# python连接mysql



### 防泄露数据库密码

```python
from pathlib import Path
import json
def load_sql_info(filename):
    """
    mysite.json
    :param filename:
    :return:
    """
    p = Path()
    p = p.home().joinpath(".jiejie/mysql").joinpath(filename)
    return json.loads(p.read_text())
```

在 `C:\Users\用户名\.jiejie\mysql` 目录下，添加`sql.json`文件

将数据库的相关配置填写在`sql.json`文件中:

```json
{
    "db":"dbname",
    "user":"xxxx",
    "pwd":"xxx",
    "host":"xxxx",
    "port":3306
}
```

此后便可以在python中，来获取到数据库的配置。因为这样无需将数据库的配置填写到代码中，从而保护了数据的安全。

```python
sql_json = load_sql_info("sql.json")
db = sql_json.get("db")
user = sql_json.get("user")
sql_pwd = sql_json.get("pwd")
port = sql_json.get("port")
host = sql_json.get("host")
```



以下提供了，根据不同平台导入不同json配置信息的方法

```python
def load_static():
    import platform
    _ = Path().home().joinpath(".jiejie/statics")
    if platform.system().lower() == 'windows':
        p = _.joinpath("win.json")
    elif platform.system().lower() == 'linux':
        p = _.joinpath("linux.json")
    # 其他平台 ，暂不支持，直接报错 Permission denied
    return json.loads(p.read_text())
```



## 连接数据库

```python
import pymysql
def get_cursor():
    conn = pymysql.connect(host=host, port=port,
                           user=user, passwd=sql_pwd, charset='utf8', db=db)
    cursor = conn.cursor(cursor=pymysql.cursors.DictCursor)
    return conn, cursor

# 释放数据库连接
def close(conn, cursor):
    try:
        cursor.close()
    except Exception as e:
        print(e.args)
    try:
        conn.close()
    except Exception as e:
        print(e.args)
```



通过sql查询语句，从数据库中拿到返回的结果,

比如这里的sql语句为: `select * from xxxTable`

```python
def _select(sql):
    conn, cursor = get_cursor()
    res = []
    try:
        cursor.execute(sql)
        res = cursor.fetchall()
    except Exception as e:
        print(e.args)
    close(conn, cursor)
    return list(res)
```

