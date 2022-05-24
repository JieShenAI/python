
## dataclass
参考: https://www.bilibili.com/video/BV1D34y1a7Hz

```python
from dataclasses import dataclass, field

@dataclass(order=True)
class BX:
    id: int
    title: str = None
    province: str = None
    description: str = field(default=None, repr=False)
```
