import turtle
turtle.bgpic('bg.gif')
score = input('输入分数:')
score = int(score)
if score >= 85:
    turtle.write('A', font=('arial',100,'bold'))
elif score >= 75:
    turtle.write('B', font=('arial',100,'bold'))
elif score >= 60:
    turtle.write('C', font=('arial',100,'bold'))
elif score >= 0:
    turtle.write('D', font=('arial',100,'bold'))
else:
    turtle.bgpic('bg2.gif')
turtle.hideturtle()
turtle.done

