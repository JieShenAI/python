## dict2json

字典类型转换为json，并保存到本地文件



```python
def write_dict2json(d,folder,filename):
    """
    d: 字典类型
    folder: 父文件夹的路径
    filename: 文件的名字
    eg:
        write_dict2json(d,'.',"sqlnames.json")
    """
    import json
    json_data = json.dumps(d)
    from pathlib import Path
    p = Path(folder)
    p.mkdir(exist_ok=True)    
    v = p.joinpath(filename)
    v.write_text(json_data)
```



读取本地json文件

```python
import json
from pathlib import Path
s = Path("./sqlnames.json").read_text()
data = json.loads(s)
```
