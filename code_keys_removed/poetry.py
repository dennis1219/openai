from api import GPT,Example
gpt = GPT(temperature=0.8, max_tokens=200)

gpt = GPT(temperature=0.8, max_tokens=600)

gpt.add_example(Example(
    "오백년 도읍지를",
    "오백년 도읍지를 필마로 도라드니\n산천은 의구되 인걸은 간듸업다.\n어즈버, 태평연월이 이런가 하노라. "))

gpt.add_example(Example(
    "심산에 밤이드니",
    "심산에 밤이드니 북풍이 더욱 차다\n옥루고 처에도 이바람 부는게오\n긴밤에 치우신가 북두비겨 바래로다"))

gpt.add_example(Example(
    "동창이 밝았느냐",
    "동창이 밝았느냐 노고지리 우지진다\n소치는 아이는 상기아니 일었느냐\n재너머 사래긴밭 언제갈려 하느니"))

gpt.add_example(Example(
    "오늘도 다새거다 ",
    "오늘도 다새거다 호미메고 가자스라\n내논다 매어든 네논좀 매어주마\n올길에 뽕따다가 누에먹여 보자스라"))


gpt.add_example(Example(
    "마음이 지척이면",
    "마음이 지척이면 천리라도 지척이오\n마음이 천리오면 지척도 천리로다\n우리각재 천리오나 지척인가 하노라. "))

prompt = "바람이 살랑이니"
output = gpt.submit_request(prompt)
output.choices[0]['text']