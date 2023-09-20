# 데이터 가공 연습
from konlpy.tag import Kkma
import collections
Kkma = Kkma()

list_sentence = [
    "열 길 물속은 알아도 한 길 사람 속은 모른다.", # ['길', '물', '물속', '속', '사람']
    "호랑이 그리려다 고양이 그린다.", # ['호랑이', '고양이']
    "호랑이도 제 말하면 온다.", # ['호랑이', '저', '말']
    "단단한 땅에 물이 괸다.", # ['땅', '물']
    "사촌이 땅을 사면 배가 아프다.", # ['사촌', '땅', '배']
    "물이 깊어야 고기가 모인다.", # ['물', '고기']
    "개구리 올챙이 적 생각 못 한다." # ['개구리', '올챙이', '적', '생각']
]

#for i in list_sentence:
#    print(i)

list_result = []

for i in list_sentence:
    #print(Kkma.nouns(i))
    list_result = list_result + Kkma.nouns(i)
    #print(list_result)

print(list_result)

print(collections.Counter(list_result))

print(collections.Counter(list_result).most_common(3))