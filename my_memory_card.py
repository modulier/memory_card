#создай приложение для запоминания информации
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import*
from random import*

class Question():
    def __init__(self, question, right_answer,wrong1, wrong2, wrong3):
        self.question = question
        self.right_answer = right_answer
        self.wrong1 = wrong1
        self.wrong2 = wrong2
        self.wrong3 = wrong3

questions_list = []
questions_list.append(
    Question('Государственный язык Бразилии', 'Португальский', 'Бразильский', 'Испанский', 'Итальянсий'))

questions_list.append(
    Question('Кто такой нос', 'Владик', 'Сеня', 'Максон', 'Сквадрий'))

questions_list.append(
    Question('На чем расседает барыль', 'Кугач', 'Блаблакар', 'Самоходный пень', 'Вагонетка'))

questions_list.append(
    Question('Кто такая колготница', 'Полина', 'Кегля', 'Лерачка', 'Карбонара'))

questions_list.append(
    Question('Столица Болгарии', 'София', 'Рим', 'Нигерия', 'Могилёв'))

questions_list.append(
    Question('Моя любимая игра', 'Роблокс', 'Fortnite', 'Бравл с моей бести', 'Покемоны'))

app = QApplication([])
window = QWidget()
window.setWindowTitle('memo card')
window.resize(400,200)
window.move(100,100)

lb_Question = QLabel('Ваш вопрос')#вопрос
btn_OK = QPushButton('Ответить')

RadioGroupBox = QGroupBox('вырианты ответов')
rbtn_1 = QRadioButton('Ответ1')
rbtn_2 = QRadioButton('Ответ2')
rbtn_3 = QRadioButton('Ответ3')
rbtn_4 = QRadioButton('Ответ4')

RadioGroup = QButtonGroup()
RadioGroup.addButton(rbtn_1)
RadioGroup.addButton(rbtn_2)
RadioGroup.addButton(rbtn_3)
RadioGroup.addButton(rbtn_4)

layout_ans1 = QHBoxLayout()
layout_ans2 = QVBoxLayout()
layout_ans3 = QVBoxLayout()

layout_ans2.addWidget(rbtn_1)
layout_ans2.addWidget(rbtn_2)
layout_ans3.addWidget(rbtn_3)
layout_ans3.addWidget(rbtn_4)

layout_ans1.addLayout(layout_ans2)
layout_ans1.addLayout(layout_ans3)
RadioGroupBox.setLayout(layout_ans1)

# окно результата
AnsGroupBox = QGroupBox("Результаты теста")
lb_Result = QLabel('Правильно\Неправильно')
lb_Correct = QLabel('Правильный ответ')

layout_res = QVBoxLayout()
layout_res.addWidget(lb_Result, alignment=(Qt.AlignLeft | Qt.AlignTop))
layout_res.addWidget(lb_Correct, alignment=Qt.AlignHCenter)
AnsGroupBox.setLayout(layout_res) #конец окна результата

layout_line1 = QHBoxLayout()
layout_line2 = QHBoxLayout()
layout_line3 = QHBoxLayout()

layout_line1.addWidget(lb_Question, alignment = (Qt.AlignHCenter | Qt.AlignVCenter))

layout_line2.addWidget(RadioGroupBox)
layout_line2.addWidget(AnsGroupBox)
RadioGroupBox.hide()

layout_line3.addStretch(1)
layout_line3.addWidget(btn_OK, stretch = 3)
layout_line3.addStretch(1)
layout_card = QVBoxLayout()
layout_card.addLayout(layout_line1)
layout_card.addLayout(layout_line2)
layout_card.addLayout(layout_line3)



def show_result():
#показать панель ответов
    RadioGroupBox.hide()
    AnsGroupBox.show()
    btn_OK.setText('следующий вопрос')

def show_question():

    RadioGroupBox.show()
    AnsGroupBox.hide()

def show_question():
    RadioGroupBox.show()
    AnsGroupBox.hide()
    btn_OK.setText('Ответить')
    RadioGroup.setExclusive(False)
    rbtn_1.setChecked(False)
    rbtn_2.setChecked(False)
    rbtn_3.setChecked(False)
    rbtn_4.setChecked(False)
    RadioGroup.setExclusive(True)

answer = [rbtn_1,rbtn_2,rbtn_3,rbtn_4]

def ask(q:Question):
    shuffle(answer)
    answer[0].setText(q.right_answer)
    answer[1].setText(q.wrong1)
    answer[2].setText(q.wrong2)
    answer[3].setText(q.wrong3)
    lb_Question.setText(q.question)
    lb_Correct.setText(q.right_answer)
    show_question()

def show_correct(res):
    lb_Result.setText(res)
    show_result()

def check_answer():
    if answer[0].isChecked():
        show_correct('Правильно!')
        window.score += 1
        print('Статистика\n-Всего вопросов: ', window.total, '\n-Правильных ответов', window.score)
        print('Рейтинг: ',window.score/window.total*100, '%')
    else:
        if answer[1].isChecked() or answer[2].isChecked() or answer[3].isChecked():
            show_correct('Неверно!')

def next_question():

    window.total += 1
    print('Статистика\n-Всего вопросов: ', window.total, '\n-Правильных ответов', window.score)
    cur_question = randint(0 ,len(questions_list) - 1)
    q = questions_list[cur_question]
    ask(q)

def click_OK():
    if btn_OK.text() == 'Ответить':
        check_answer()
    else:
        next_question()

window.setLayout(layout_card)

window.cur_question = -1
btn_OK.clicked.connect(click_OK)
window.total = 0
window.score = 0
next_question()
window.show()
app.exec()