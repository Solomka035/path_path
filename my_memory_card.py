from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (QApplication, QWidget, QHBoxLayout,
QVBoxLayout, QGroupBox, QRadioButton, QPushButton, QLabel, QButtonGroup)
from random import shuffle, randint
class Question():
    def __init__(self,question,right_answer,wrong1,wrong2,wrong3):
        self.question = question 
        self.right_answer = right_answer
        self.wrong1 = wrong1
        self.wrong2 = wrong2
        self.wrong3 = wrong3
question_list= []
question_list.append(Question('Сколько атрибутов есть в Доте?','3','2','4','1'))
question_list.append(Question('Какой основной атрибут у Пака?','Интелект','Сила','Ловкость','универсал'))
question_list.append(Question('Сколько человек в одной команде в Доте?','пять','три','четыре','шесть'))
question_list.append(Question('Какого персонажа нет в Доте?','бёрд самурай','пудж','лина','ан даинг'))
question_list.append(Question('В каком году Дота вышна на "Sourse 2"?','2013','2015','2020','2003'))
question_list.append(Question('В каком году в Доте появилась муэрта?','2023','2022','2020','2018'))
question_list.append(Question('В каком патче в Доте координально поменялась карта?','7.33','6.28','7.34','7.32е'))
question_list.append(Question('Сколько нейтральных лагерей с древними крипами в Доте на данный момент?','4','3','2','6'))
question_list.append(Question('Какая команда по Доте выйграва TI12?','Team Spirit','Gaiming Gladiators','BetBoom team','Evil Genius'))
question_list.append(Question('В каком году был проведён первый the international по Доте?','2011','2013','2020','2018'))

app = QApplication([])
window = QWidget()
window.setWindowTitle('Memo Card')
btn_OK = QPushButton('Ответить')
lb_question = QLabel('В каком году была основана Москва?')
RadioGroupBox = QGroupBox('Варианты ответов')
rbtn_1 = QRadioButton('1147')
rbtn_2 = QRadioButton('1242')
rbtn_3 = QRadioButton('1861')
rbtn_4 = QRadioButton('1943')
RadioGroup = QButtonGroup()
RadioGroup.addButton(rbtn_1)
RadioGroup.addButton(rbtn_2)
RadioGroup.addButton(rbtn_3)
RadioGroup.addButton(rbtn_4)
layout_ans1=QHBoxLayout()
layout_ans2=QVBoxLayout()
layout_ans3=QVBoxLayout()
layout_ans2.addWidget(rbtn_1)
layout_ans2.addWidget(rbtn_2)
layout_ans3.addWidget(rbtn_3)
layout_ans3.addWidget(rbtn_4)
layout_ans1.addLayout(layout_ans2)
layout_ans1.addLayout(layout_ans3)
RadioGroupBox.setLayout(layout_ans1)
AnsGroupBox = QGroupBox('Результат теста')
layout_line1=QHBoxLayout()
layout_line2=QHBoxLayout()
layout_line3=QHBoxLayout()
layout_line1.addWidget(lb_question, alignment = (Qt.AlignHCenter | Qt.AlignVCenter))
layout_line2.addWidget(RadioGroupBox)
layout_line2.addWidget(AnsGroupBox)
RadioGroupBox.hide()
layout_line3.addStretch(1)
layout_line3.addWidget(btn_OK, stretch = 2)
layout_line3.addStretch(1)
layout_card = QVBoxLayout()
layout_card.addLayout(layout_line1,stretch = 2)
layout_card.addLayout(layout_line2,stretch = 8)
layout_card.addStretch(1)
layout_card.addLayout(layout_line3,stretch = 1)
layout_card.addStretch(1)
layout_card.setSpacing(5)
def show_res():
    RadioGroupBox.hide()
    AnsGroupBox.show()
    btn_OK.setText('Следующий вопрос')
def show_ques():
    RadioGroupBox.show()
    AnsGroupBox.hide()
    btn_OK.setText('Ответить')
    RadioGroup.setExclusive(False)
    rbtn_1.setChecked(False)
    rbtn_2.setChecked(False)
    rbtn_3.setChecked(False)
    rbtn_4.setChecked(False)
    RadioGroup.setExclusive(True)
answers = [rbtn_1, rbtn_2, rbtn_3, rbtn_4]
def ask(q: Question):
    shuffle(answers)
    answers[0].setText(q.right_answer)
    answers[1].setText(q.wrong1)
    answers[2].setText(q.wrong2)
    answers[3].setText(q.wrong3)
    lb_question.setText(q.question)
    lb_Correct.setText(q.right_answer)
    show_ques()
def show_correct(res):
    lb_Result.setText(res)
    show_res()
def check_answer():
    if answers[0].isChecked():
        show_correct('Правильно!')
        window.score += 1
        print('Статистика \n -Всего вопросов:',window.total,'\n -Правильных ответов:',window.score)
        print('Рейтинг:',window.score/window.total*100,'%')
    else:
        if answers[1].isChecked() or answers[2].isChecked() or answers[3].isChecked():
            show_correct('Неверно!')
            print('Рейтинг:',window.score/window.total*100,'%')
def next_question():
    window.total += 1
    print('Статистика \n -Всего вопросов:',window.total,'\n -Правильных ответов:',window.score)
    cur_question = randint(0, len(question_list)-1)
    q = question_list[cur_question]
    ask(q)
def click_OK():
    if btn_OK.text() == 'Ответить':
        check_answer()
    else:
        next_question()
btn_OK.clicked.connect(click_OK)
next_question()
window.setLayout(layout_card)
window.show()
app.exec()
