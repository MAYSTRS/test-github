#Блок загрузки модулей
from tkinter import *
from time import strftime #Импортируем из модуля time->strftime

#Блок определения функций
def raschet():
    if(not vozrast.get()) or(not rost.get()) or (not ves.get()):
        callorii['text']='Одно из полей не заполнено!'
        callorii['fg']='red'
    else:
        print('Возраст %s, рост %s, вес %s'
            %(vozrast.get(),rost.get(),ves.get()))
        if  pol_val.get() == 1: #Мужчина
            cal = (10 * int(ves.get()) + 6.25 * int(rost.get()) - 5 \
              * int(vozrast.get()) +5)* act_val.get()
        elif  pol_val.get() == 2: #Женщина
            cal = (10 * int(ves.get()) + 6.25 * int(rost.get)) - 5 \
              * int(vozrast.get()) -161* act_val.get()
            
        callorii['text']=cal
        #print('Ваша норма %s кКаллорий в день!' %cal)  
    

#Основная программа
window=Tk()#Создаём главное окно
window['bg']='white'
window.title('Расчёт калорий')
#window.iconbitmap(r'time_clock.ico')

#window.geometry('20000x900')
#relief= FLAT, GROOVE, RIDGE, SUNKEN, RAISED
#блок создания виджетов
vozrast = Entry(window, width=10,relief=SUNKEN,
              bd=5,font='Arial 24')
rost = Entry(window, width=10,relief=SUNKEN,
              bd=5,font='Arial 24')
ves = Entry(window, width=10,relief=SUNKEN,
            bd=5,font='Arial 24')
lab_voz = Label(window, text='Ваш возраст:',
             font='Arial 20',bg='white',fg='plum3')
lab_rost = Label(window, text='Ваш рост:',
             font='Arial 20',bg='white',fg='plum3')
lab_ves = Label(window, text='Ваш вес:',
             font='Arial 20',bg='white',fg='plum3')


#блок размещения виджетов
lab_voz.grid(row=0,column=0,padx=10,pady=10,sticky=W)
vozrast.grid(row=0,column=1,padx=10,pady=10)

lab_rost.grid(row=1,column=0,padx=10,pady=10,sticky=W)
rost.grid(row=1,column=1,padx=10,pady=10)

lab_ves.grid(row=2,column=0,padx=10,pady=10,sticky=W)
ves.grid(row=2,column=1,padx=10,pady=10)

Button(window, text='Расчёт:',font='Arial 24',bg='gray77',fg='cyan4',
       relief=FLAT,bd=5,command=raschet
       ).grid(row=6,column=0,padx=10,pady=10)

callorii=Label(window, text='',font='Arial 24',bg='white',fg='pink'
      )
callorii.grid(row=6,column=2,padx=10,pady=10,sticky=W)

Label(window, text='Ваш пол:',font='Arial 20',bg='white',fg='maroon4'
      ).grid(row=3,column=0,padx=10,pady=10,sticky=W)
pol_val=IntVar()
pol_val.set(0)
Radiobutton(window, text='Мужской',font='Arial 20',bg='white',fg='cyan',
            variable=pol_val,value=1).grid(row=4,column=0,padx=10,pady=10)
Radiobutton(window, text='Женский',font='Arial 20',bg='white',fg='hotpink',
            variable=pol_val,value=2).grid(row=5,column=0,padx=10,pady=10)

#Блок радио кнопок для выбора физ. активности
act_val=DoubleVar() #Создаем переменную типо float
act_val.set(0.0) #Присвоили переменной начальное значение
#Создаём и размещаем радио кнопки для выбора физ.активности
Radiobutton(window, text='Практически полное отсутствие\
активности.\n\
Сюда относятся люди с сидячим образом жизни,\n\
не занимающиеся спортом.',
            font='Arial 14',bg='white',fg='navy',
            variable=act_val,value=1.2
            ).grid(row=0,column=2,
                   padx=10,pady=10,sticky=W)

Radiobutton(window, text='Слабая активность.\n\
Это либо сидячий образ жизни в купе\n\
с небольшими тренировками 1-3 раза\n\
в неделю, либо занятия, требующие регулярной\n\
длительной ходьбы.',
            font='Arial 14',bg='white',fg='blue',
            variable=act_val,value=1.375
            ).grid(row=1,column=2,
                   padx=10,pady=10,sticky=W)

Radiobutton(window, text='Средняя активность.\n\
Этот коэффициент выбирают те,кто занимается спортом\n\
3-4 раза в неделю по 30-60 минут.',
            font='Arial 14',bg='white',fg='royal blue',variable=act_val,value=1.55
            ).grid(row=2,column=2,
                   padx=10,pady=10,sticky=W)

Radiobutton(window, text='Высокая активность. Это ежедневные\n\
или практически ежедневные тренировки,\n\
либо занятость в сфере строительства, сельского\n\
хозяйства и т.д.',
            font='Arial 14',bg='white',fg='dodger blue',variable=act_val,value=1.
            ).grid(row=3,column=2,
                   padx=10,pady=10,sticky=W)

Radiobutton(window, text='Экстремальная активность. Сюда относятся\n\
спортсмены с ежедневными многоразовыми тренировками\n\
и люди с длительным рабочим днем, например,\n\
в угольных шахтах.',
            font='Arial 14',bg='white',fg='deep sky blue',variable=act_val,value=1.9
            ).grid(row=4,column=2,
                   padx=10,pady=10,sticky=W)

#window.after(500,time_clock)

window.mainloop()#Запускаем обработчик событий

