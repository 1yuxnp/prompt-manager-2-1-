categories = [
    "텍스트 생성",
    "이미지 생성",
    "영상 생성",
    "페르소나",
    "자동화",
    "기타"
]
prompts = [
    {
        "title": "Term Cafe UI 생성",
        "content": "모바일 카페 주문 앱의 깔끔한 UI 화면을 생성해주세요.",
        "category": "이미지 생성",
        "favorite": False
    },
    {
        "title": "COOL SPOT 광고 이미지",
        "content": "여름 테크니컬 스트릿 패션 브랜드의 시원하고 미래적인 광고 이미지를 생성해주세요.",
        "category": "이미지 생성",
        "favorite": False
    },
    {
        "title": "ExamPilot 학습 계획",
        "content": "시험 기간과 과목별 중요도를 고려하여 효율적인 학습 계획을 작성해주세요.",
        "category": "텍스트 생성",
        "favorite": False
    }
]
def add_prompt():
    print()
    print("=== 프롬프트 추가 ===")

    while True:
        title = input("제목: ").strip()

        if title:
            break

        print("제목은 비워둘 수 없습니다.")

    while True:
        content = input("내용: ").strip()

        if content:
            break

        print("내용은 비워둘 수 없습니다.")

    print()
    print("카테고리 선택:")

    for i, category in enumerate(categories, start=1):
        print(f"{i}) {category}")

    while True:
        choice = input("선택: ").strip()

        if choice.isdigit() and 1 <= int(choice) <= len(categories):
            category = categories[int(choice) - 1]
            break

        print("올바른 카테고리 번호를 입력해주세요.")

    new_prompt = {
        "title": title,
        "content": content,
        "category": category,
        "favorite": False
    }

    prompts.append(new_prompt)

    print()
    print("프롬프트가 추가되었습니다!")
def show_list():
    print()
    print("=== 프롬프트 목록 ===")

    if len(prompts) == 0:
        print("등록된 프롬프트가 없습니다.")
        return

    for i, prompt in enumerate(prompts, start=1):
        favorite = " ⭐" if prompt["favorite"] else ""
        print(f'{i}. [{prompt["category"]}] {prompt["title"]}{favorite}')

    print()
    print(f"총 {len(prompts)}개의 프롬프트")
def show_category():
    print()
    print("=== 카테고리별 조회 ===")

    for i, category in enumerate(categories, start=1):
        print(f"{i}) {category}")

    while True:
        choice = input("선택: ").strip()

        if choice.isdigit() and 1 <= int(choice) <= len(categories):
            category = categories[int(choice) - 1]
            break

        print("올바른 카테고리 번호를 입력해주세요.")

    print()
    print(f"[{category}] 카테고리 프롬프트:")

    count = 0

    for i, prompt in enumerate(prompts, start=1):
        if prompt["category"] == category:
            favorite = " ⭐" if prompt["favorite"] else ""
            print(f'{i}. {prompt["title"]}{favorite}')
            count += 1

    if count == 0:
        print("해당 카테고리에 프롬프트가 없습니다.")
    else:
        print()
        print(f"총 {count}개의 프롬프트")
def show_menu():
    print()
    print("=== 나만의 프롬프트 관리 ===")
    print("1. 프롬프트 추가")
    print("2. 프롬프트 목록")
    print("3. 카테고리별 조회")
    print("4. 프롬프트 검색")
    print("5. 프롬프트 상세 보기")
    print("6. 즐겨찾기 관리")
    print("7. 즐겨찾기 목록")
    print("0. 종료")


while True:
    show_menu()

    choice = input("선택: ")

    if choice == "0":
       print("프로그램을 종료합니다.")
       break
    elif choice == "1":
         add_prompt()
    elif choice == "2":
         show_list()
    elif choice == "3":
         show_category()
    else:
         print("아직 준비 중인 기능입니다.")