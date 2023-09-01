# Point 클래스 선언
- Point 클래스는 2차원 평면의 점 or 2차원 벡터를 나타내는 클래스
- 필요한 멤버는 점의 x좌표, y좌표
```python
class Hello:
  def __init__(self, x =0, y =0):
    self.x = x
    self.y = y
  def __str__(self):
    return f"({self.x}, {self.y})"

p = Hello(1,2)
print(p)
```