from django.test import TestCase

# Create your tests here.
# when2 = {desk: [k for k, v in fts.items() if v == desk] for desk in set(fts.values())}
# print(when2)
class CountFromBy:
    def __init__(self, v: int, i: int) -> None:
        self.val = v
        self.incr = i
        
    def increase(self) -> None:
        self.val +=self.incr