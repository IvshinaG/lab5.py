def one(n):
    n=int(input("Введите число: "))
    m=[2,4,5,3,7]
    if n in m:
        s=str(m)+"\n"+str(n)+"\nПоздравляю, Вы угадали число!"
    else:
        s=str(m) + "\n" + str(n) + "\nНет такого числа"
    return s
def two(n):
    m=[]
    for i in range (len(n)-1):
        if n[i] in n[i+1:]:
            m.append(n[i])
    set(m)
    return m
def three(n):
    if n>7:
        return "Дней в неделе 7"
    else:
        dn=("Понедельник", "Вторник","Среда","Четверг","Пятница","Суббота","Воскресенье")
        m=list(dn)
        vd=m[7-n:7]
        rd=m[0:7-n]
        s="Ваши выходные дни:"+str(vd)+"\nВаши рабочие дни:"+str(rd)
        return s
def four(n):
    c1=["Ившина","Ефлютина","Сидоров"]
    c2=["Фатькин","Яковлева","Иванов"]
    ck=[]
    ck.append(c1[2])
    ck.append(c2[2])
    ck=tuple(ck)
    print("Список 1 класса:",c1,"\nСписок 2 класса:", c2)
    print("Спортивная команда:", ck)
    print("Количество участников спрот команды:",len(ck))
    ck2=tuple(sorted(ck))
    print("Отсортированный список спорт. команды:",ck2)
    k=ck.count("Иванов")
    return ("Кол-во повторений фамилии Иванов", k)

print(one(4))

n=[2,4,6,2,4,3,5]
print("Повторяющиеся значения в списке",n,two(n))

n=int(input("Cколько выходных вы хотите?"))
print(three(n))

print(four(1))

