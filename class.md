
## dataclass
参考: https://www.bilibili.com/video/BV1D34y1a7Hz

```python
from dataclasses import dataclass, field
import datetime


@dataclass(order=True)
class BX:
    id: int = None
    title: str = None
    time: datetime = None
    purchaser: str = None
    agency: str = None
    announce_type: str = None
    province: str = None
    link: str = None
    features: list[int] = field(default_factory=list, repr=False, hash=False)


if __name__ == '__main__':
    bx1 = BX(1)
    bx2 = BX(2)
    print(bx1 < bx2)
    print(inspect.getmembers(BX, inspect.isfunction))
```

@dataclass(order=True)
增加了大于、小于等比较大小的方法

@dataclass(frozen=True)
设为不允许修改值，可hash

使用`print(inspect.getmembers(BX, inspect.isfunction))`,看到这个数据类型所有的方法
