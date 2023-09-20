# 단어 숫자 세기 연습
import collections
print(collections.Counter(['가','나','다','라','마','바','가','나']))
print(collections.Counter(['가','나','다','라','마','바','가','나','나나','가','다','바']))

# 딕셔너리(dictionary)는 items()함수를 사용하면 딕셔너리에 있는 키와 값들의 쌍을 얻을 수 있다.
for k, v in collections.Counter(['가','나','다','라','마','바','가','나','나나','가','다','바']).items():
    print(k, ":", v)

list_a = ['가','나','다','라','마','가','나']
list_b = ['가','나','다','라','마','가','나','사','다','바']
list_c = list_a + list_b
print(list_c) # ['가', '나', '다', '라', '마', '가', '나', '가', '나', '다', '라', '마', '가', '나', '사', '다', '바']

print(collections.Counter(list_c)) # Counter({'가': 4, '나': 4, '다': 3, '라': 2, '마': 2, '사': 1, '바': 1})
print(collections.Counter(list_c).most_common(3)) # [('가', 4), ('나', 4), ('다', 3)]