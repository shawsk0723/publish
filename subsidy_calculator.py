"""
https://shawsk.tistory.com/

subsidy calculator
"""



from tkinter import *            # tkinter 라이브러리에 모든 함수를 사용

def calculate(card_amount):
    print("calculate card amount to use~")
    result = 100000*10 + int(card_amount) * 1.03
    return result

window = Tk()                              # 창을 생성
window.geometry("600x400")                 # 창 크기설정
window.title("소비상생지원금 계산기 - 쌀사비파")           # 창 제목설정
window.option_add("*Font","맑은고딕 25")    # 폰트설정
window.resizable(False, False)             # x, y 창 크기 변경 불가

def btnpress():                            # 함수 btnpress() 정의
    card_amount = ent.get()
    result = calculate(card_amount)
    label.configure(text = '사용해야 할 금액: ' + str(result))

message = Label(window, text = '2분기 평균 카드 사용액 입력', height=3)
message.pack()

ent = Entry(window)                        # window라는 창에 입력창 생성
ent.pack()                                 # 입력창 배치

btn = Button(window)                       # window라는 창에 버튼 생성
btn.config(text= "계산하기")               # 버튼 내용 
btn.config(width=10)                      # 버튼 크기
btn.config(command=btnpress)               # 버튼 기능 (btnpree() 함수 호출)
btn.pack()                                 # 버튼 배치

label = Label(window, text = '결과 :', height=3)
label.pack()


window.mainloop()
