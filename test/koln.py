# KoNLPy 연습

# KoNLPy : 파이썬 한국어 NLP. 한국어 자연어 처리를 해주는, 한국어 정보처리를 위한 파이썬 패키지이다.
# https://konlpy-ko.readthedocs.io/ko/v0.4.3/install/
# konlpy설치시 java jdk를 설치한뒤 환경변수 설정을 해줘야한다.
from konlpy.tag import Kkma
import os
Kkma = Kkma()
# print(os.environ.get('JAVA_HOME'))
print(Kkma.sentences("아버지가 가방에 들어가십니다.")) # ['아버지가 가방에 들어가십니다.']
print(Kkma.nouns("아버지가 가방에 들어가십니다.")) # ['아버지', '가방']