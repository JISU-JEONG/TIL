class Person:
    name = '홍길동'

    def greeting(self):
        return f'{self.name} : 방가방가~'
    
    # def __str__(self):
    #     return f'{self.name} str 입니다.'

    def __repr__(self):
        return 'string'

iu = Person()
iu.name = '아이유'
print(iu)
print(type(iu))
a = iu
print(a)