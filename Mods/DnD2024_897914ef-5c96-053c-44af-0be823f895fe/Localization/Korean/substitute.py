import re

# 치환할 단어 목록 정의
replacements = {
    r" 검사": " 판정",
    r"Arcana": "비전",
    r"Arcana와": "비전과",
    r"Bludgeoning": "타격",
    r"Cantrips": "소마법",
    r"Critical Hit": "치명타",
    r"Long Rest": "긴 휴식",
    r"Religion": "종교",
    r"Short Rest": "짧은 휴식",
    r"Temporary Hit Points": "임시 생명력",
    r"곤충 역병": "곤충 떼",
    r"공격 굴림": "명중 굴림",
    r"괴사": "사령",
    r"구원 굴림": "내성 굴림",
    r"구원": "내성",
    r"굴림를": "굴림을",
    r"기 포인트": "기력",
    r"기회 공격": "허점 공격",
    r"능력치 판정": "능력 판정",
    r"데미지": "피해",
    r"드래곤": "용",
    r"레이디언트": "광휘",
    r"레이지": "격노",
    r"맹목 싸움": "맹안 전투술",
    r"메타매직": "변형 마법",
    r"면역성": "면역",
    r"무거운 갑옷": "중갑",
    r"민첩성": "민첩",
    r"밀려납니다[1]": "[1] 밀려납니다",
    r"바인딩": "결속",
    r"반응": "대응",
    r"방어력": "방어도",
    r"병의 광선": "독 광선",
    r"보너스 액션": "보조 행동",
    r"불리함을 부과": "불리 보정을 부여",
    r"불이익": "불리 보정",
    r"브레스": "숨결",
    r"빛의 피해": "광휘 피해",
    r"사이오닉": "초능력",
    r"산성 비말": "산성 거품",
    r"성기사": "팔라딘",
    r"성직자": "클레릭",
    r"세이브": "내성 굴림",
    r"세이빙 스로우": "내성 굴림",
    r"수정치": "보정치",
    r"숙련도 보너스": "숙련 보너스",
    r"스마이트": "강타",
    r"스피어": "창",
    r"아드레날린 러시": "아드레날린 질주",
    r"아치페이": "대요정",
    r"악취 나는 구름": "악취 구름",
    r"액션": "행동",
    r"야만인": "바바리안",
    r"어드밴티지": "유리 보정",
    r"엎드린": "넘어진",
    r"엘드리치": "비술",
    r"웨폰": "무기",
    r"유리하며": "유리 보정을 받으며",
    r"유리한 상황": "유리 보정",
    r"유리한 상황": "유리 보정",
    r"이동 속도": "이동속도",
    r"이점": "유리 보정",
    r"익스텐드": "연장",
    r"저주": "주술",
    r"저항력": "저항",
    r"점프": "도약",
    r"주도권": "선제권",
    r"주문 세이브 DC": "주문 내성 난이도",
    r"주손": "주 손",
    r"지도력과": "인도와",
    r"채널 디비니티": "신성력 전달",
    r"채널 맹세": "맹세 권능",
    r"체력 구원": "건강 내성",
    r"체력 세이브": "건강 내성",
    r"체력 포인트": "생명력",
    r"체크": "판정정",
    r"초점 포인트": "기력",
    r"카리스마": "매력",
    r"칸트립": "소마법",
    r"캔트립": "소마법",
    r"크로매틱 오브": "오색 보주",
    r"크로매틱": "오색",
    r"크리티컬": "치명타",
    r"타겟": "대상",
    r"탄약": "화살",
    r"팩트 무기": "계약 무기",
    r"페이 방랑자": "요정 방랑자",
    r"푸시": "밀기",
    r"피어싱": "관통",
    r"해산 주문": "해제 주문",
    r"행동 범위": "사정거리리",
    r"헥스": "주술",
    r"힘 검사": "근력 판정",
    r"힘과 민첩": "근력과 민첩",
    r"력력": "력",
    r"AC와": "방어도와",
    r"힘 판정": "근력 판정",
    r"도이": "도가",
    r"야생 형태": "야생 형상",
    r"주문 내성 굴림 DC": "주문 내성 난이도",
    r"갑갑": "갑",
    r"숙련도": "숙련",
    r"련가": "련이",
    r"어뎁트": "숙련",
    r"Origin Feat": "기원 재주",
    r"기원 특성": "기원 재주",
    r"입문자": "입문",
    r"Magic Initiate": "마법 입문",
    r"Wizard": "위저드",
    r"Skilled": "숙련됨",
    r"Tavern Brawler": "술집 싸움꾼",
    r"Tough": "강골",
    r"Alert": "경계",
    r"Healer": "치유사",
    r"Savage Attacker": "맹렬한 공격자",
    r"협약 무기": "계약 무기",
    r"수도사": "몽크",
    r"마법 포인트": "소서리 포인트",
    r"어려운 지형": "험지",
    r"워록": "워락",
    r"인보케이션": "영창",
    r"비술 인보케이션": "섬뜩한 영창",
    r"스터닝 스트라이크": "기절의 일격",
    r"텔레키네틱": "염동력",
    r"온대 지방": "온대",
    r"Feywild": "페이와일드",
    r"기스제라이": "기스저라이",
    r"저장 DC": "내성 난이도",
    r"Feat": "재주",
    r"트로피컬 랜드": "열대",
    r"트루 스트라이크": "진실의 일격",
    r"비무장 파업": "비무장 공격",
    r"Radiant": "광휘",
    r"몰래 공격": "암습",
    r"치명타 히트": "치명타",
    r"Ki-Points": "기력",
    r"방어도 클래스": "방어도",
    r"동맹군": "아군",
    r"이니셔티브": "선제권",
    r"Enchantment": "환혹술",
    r"Illusion": "환영술",
    r"DC ": "난이도 ",
    r"건조": "사막",
    r"유리한 입장": "유리 보정",
    r"Strength": "근력",
    r"Dexterity": "민첩",
    r"Unarmed Strike": "비무장 공격",
    r"Offhand": "보조 무기",
    r"Bardic Inspiration": "바드의 영감",
    r"중갑옷": "중갑",
    r"경갑옷": "경갑",
    r"놀라지 않습니다.": "기습당하지 않습니다",
    r"힘이나 민첩": "근력이나 민첩",
    r"Mechanus": "메카누스",
    r"Performance": "공연",
    r"숙련도를": "숙련을",
    r"아르카나": "비전",
    r"통찰력": "통찰",
    r"조사력과": "조사와",
    r"조사력": "조사",
    r"통찰력": "통찰",
    r"맹시력": "암시야",
    r"블라인드사이트": "암시야",
    r"Radiant": "광휘",
    r"피해해": "피해",
    r"Disengage": "철수",
    r"Dexterity": "민첩",
    r"은밀함": "은신",
    r"능숙해집니다": "숙련됩니다",
    r"Second Wind": "재기의 바람",
    r"람를": "람을",
    r"오프핸드": "보조 무기",
    r"유리합니다": "유리 보정을 받습니다",
    r"멀티버스": "다중 우주",
    r"Fire": "화염",
    r"판정정": "판정",
    r"무술 무기": "군용 무기",
    r"체질 내성": "건강 내성",
    r"Warding Flare": "수호의 섬광",
    r"평면": "차원",
    r"생명점": "생명력",
    r"전투술 스타일": "전투 방식",
    r"유리한 점": "유리 보정",
    r"전문성": "통달",
    r"행동 서지": "행동 폭증",
    r"찌르기": "관통",
    r"극지방": "극지",
    r"추위": "냉기",
    r"Tides of Chaos": "혼돈의 물결",
    r"결를": "결을",
    r"Sorcerer": "소서러",
    r"방어구를": "갑옷을",
    r"Psionic Spells": "정신 주문",
    r"섀도우": "그림자",
    r"스텝": "걸음",
    r"힘 기반": "근력 기반",
    r"5피트": "1.5m",
    r"10피트": "3m",
    r"30피트": "9m",
    r"60피트": "18m",
    r"판정정": "판정",
    r"문라이트": "달빛",
    r"샷": "사격격",
    r"라이프 드링커": "죽음을 먹는 자",
    r"기동을": "전투기법",
    r"트립": "넘어뜨리기",
    r"불 볼트": "화염살",
    r"불타는 손": "불타는 손길",
    r"불덩어리": "화염구",
    r"흐릿함": "잔상",
    r"병충해": "역병",
    r"돌담": "바위의 벽",
    r"병병": "병",
    r"페이 원더러": "페이 방랑자",
    r"요정의 불": "요정불",
    r"거짓된 삶": "거짓 생명",
    r"체력 내성": "건강 내성",
    r"힘, 사령, 초능력, 광휘": "역장, 사령, 정신, 광휘",
    r"저장 굴림": "내성 굴림",
    r"저장에 실패하면": "내성 굴림에 실패하면",
    r"파파": "파",
    r"클로즈 쿼터 슈터": "영거리 사격수",
    r"땅땅": "땅",
    r"길길": "길",
    r"사악한 조롱": "신랄한 조롱",
    r"열 금속": "상처 유발",
    r"사람을 붙잡기": "인간형 포박",
    r"상처 입히기": "상처 유발",
    r"흉측한 웃음": "끔찍한 웃음",
    r"마인드 슬리버": "정신 파편",
    r"모바일": "기동",
    r"사령, 초능력, 광휘": "사령, 정신, 광휘",
    r"Advantage": "유리 보정",
    r"정를": "정을",
    r"Lucky": "행운",
    r"Performer": "공연가",
    r"도을": "도를",
    r"보호하세요": "보호합니다",
    r"펀치를": "주먹을",
    r"날리세요": "날립니다",
    r"문문": "문",
    r"음음": "음",
    r"로빙": "배회",
    r"에임": "조준",
    r"환상 주문": "환영술",
    r"소환 페이": "페이 소환",
    r"Shadowfell": "섀도펠",
    r"Shadow Step": "그림자 걸음",
    r"Ki-Point": "기력",
    r"민첩를": "민첩을",
    r"Invisible": "투명",
    r"롱 레스트": "긴 휴식",
    r"Nature": "자연",
    r"능숙하며": "숙련되며",
    r"인식력": "포착",
    r"은밀": "은신",
    r"능숙한": "숙련된",
    r"지각력": "포착",
    r"가벼운 갑옷": "경갑",
    r"기원 특기": "기원 재주",
    r"차저": "돌격자",
    r"능숙해지고": "숙련되고",
    r"대시": "달리기",
    r"약물 판정": "의학 판정",
    r"신성한 타격": "신성한 강타",
    r"결결": "결",
    r"야수 형태": "야수 형상",
    r"증를": "증을",
    r"워딩 플레어": "수호의 섬광",
    r"귀하의": "당신의",
    r"힘 대신 민첩": "근력 대신 민첩",
    r"비술 나이트": "비술 기사",
    r"1단계": "1레벨",
    r"콜드": "냉기",
    r"썬더": "천둥",
    r"사람 붙잡기": "인간형 포박",
    r"실드 배시": "방패 밀어치기",
    r"무장하지 않은 공격": "비무장 공격",
    r"Short": "짧은",
    r"능숙합니다": "숙련됩니다",
    r"암흑 시야": "암시야",
    r"체력 보정치": "건강 보정치",
    r"석궁": "쇠뇌",
    r"Two-Weapon Fighting": "쌍수 전투술",
    r"Two Handed": "양손",
    r"Two-Handed": "양손",
    r"와일드 셰이프": "야생 형상",
    r"상를": "상을",
    r"공격 롤": "명중 굴림",
    r"유리한 위치를 차지합니다": "유리 보정을 얻습니다",
    r"포스": "역장",
    r"Concentration": "집중",
    r"Channel Divinity": "신성력 전달",
    r"달를": "달을",
    r"특기": "재주",
    r" AC ": " 방어도 ",
    r"Charmed": "매혹",
    r"Frightened": "겁에 질림",
    r"Command": "명령",
    r"령를": "령을",
    r"Charisma": "매력",
    r"체력 점수": "건강 점수",
    r"광채": "광휘",
    r"불,": "화염",
    r"힘 내성 굴림": "근력 내성 굴림",
    r"Cunning Strike": "교활한 일격",
    r"세컨드 윈드": "재기의 바람",
    r"람를": "람을",
    r"Hand of Harm": "해악의 손길",
    r"Hand of Healing": "치유의 손길",
    r"독 복용량": "독소",
    r"인챈트먼트": "환혹술",
    r"일루전": "환영술",
    r"스트라이크": "일격",
    r"피어서": "관통자",
    r"꿰뚫는 사람": "관통자",
    r"전투방식": "전투 방식",
    r"련를": "련을",
    r"실드 참격": "방패 밀어치기",
    r"비무장 타격": "비무장 공격",
    r"불리한 상황을 부과": "불리 보정을 부여",
    r"딘와": "딘과",
    r"능숙해질": "숙련될",
    r"Piercing": "관통",
    r"Slashing": "참격",
    r"힘 보정치": "근력 보정치",
    r"느림": "늦추기",
    r"소환하세요": "소환합니다",
    r"싸우게 하세요": "싸우게 합니다",
    r"관전자": "스펙테이터",
    r"환상": "환영",
    r"애니메이션": "움직이는",
    r"마인드플레이어": "정신 침탈자",
    r"마인드 플레이어": "정신 침탈자",
    r"소환 구조물": "구조물 소환",
    r"소환의 괴수": "이형체 소환",
    r"파업": "일격",
    r"엎드리게": "넘어지게",
    r"성공해야 하며, 실패하면": "실패하면",
    r"냉전": "냉기",
    r"화재": "화염",
    r"Find Familiar": "소환수 찾기",
    r"Flurry of Blows": "연속 타격",
    r"전투술꾼": "싸움꾼",
    r"얻으려면": "얻기 위해",
    r"회복하세요": "회복합니다",
    r"활성화하세요": "활성화합니다",
    r"터치하고": "만지고",
    r"마스터합니다": "단련합니다",
    r"술를": "술을",
    r"Charm Person": "인간형 매혹",
    r"Mirror Image": "거울 분신",
    r"강타을": "강타를",
    r"계약무기": "계약 무기",
    r"Elemental Fury": "원소 분노",
    r"": "",
    r"": "",
    r"": "",
    r"": "",
    r"": "",
    r"": "",
    r"": "",
    r"": "",
    r"": "",
    r"": "",
}

# 파일 경로 설정
input_file = "d24_korean.xml"  # 원본 파일
output_file = "d24_korean.xml"  # 수정된 결과를 저장할 파일

# 파일 읽기
with open(input_file, "r", encoding="utf-8") as file:
    content = file.read()

# 치환 작업
for pattern, replacement in replacements.items():
    content = re.sub(pattern, replacement, content)

# 수정된 내용 저장
with open(output_file, "w", encoding="utf-8") as file:
    file.write(content)

print(f"치환 작업 완료: {output_file}에 저장됨")
