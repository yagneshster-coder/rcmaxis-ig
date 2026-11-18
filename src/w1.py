exec(open(MAKE).read().split("# 18 Nov")[0])

def steps(name,title,items,page):
    im,d=canvas(False)
    y=block(d,(M,190),title,f(800,66),INK,W-2*M,1.15)+70
    for n,(t,desc) in items:
        d.ellipse((M,y,M+92,y+92),fill=BLUE)
        tw=d.textlength(str(n),font=f(800,44)); d.text((M+46-tw/2,y+20),str(n),font=f(800,44),fill=WHITE)
        d.text((M+136,y+2),t,font=f(700,46),fill=INK)
        y=block(d,(M+136,y+66),desc,f(500,36),GREY,W-2*M-136,1.35)+70
    footer(d,False,page); im.save(f"{OUT}/{name}.jpg",quality=95)

def code(name,c,title,move,page):
    im,d=canvas(False)
    d.text((M,220),c,font=f(800,170),fill=BLUE)
    y=block(d,(M,460),title,f(700,58),INK,W-2*M,1.2)+50
    d.rounded_rectangle((M,y,W-M,y+400),radius=24,fill=WHITE,outline="#D9E3F0",width=3)
    d.text((M+42,y+40),"NEXT MOVE",font=f(800,28),fill=BLUE)
    block(d,(M+42,y+100),move,f(500,42),INK,W-2*M-84,1.4)
    footer(d,False,page); im.save(f"{OUT}/{name}.jpg",quality=95)

def bullets(name,title,items,page,top=260):
    im,d=canvas(False)
    y=block(d,(M,top),title,f(800,66),INK,W-2*M,1.15)+80
    for t in items:
        chevron(d,M,y+46,34,BLUE)
        y=block(d,(M+64,y),t,f(500,46),INK,W-2*M-64,1.35)+50
    footer(d,False,page); im.save(f"{OUT}/{name}.jpg",quality=95)

def endcard(name,title,sub,page):
    im,d=canvas(True); chevron(d,W//2-120,560,240,BLUE)
    y=block(d,(M,640),title,f(800,62),WHITE,W-2*M,1.15)+40
    block(d,(M,y),sub,f(500,38),LB,W-2*M,1.35)
    footer(d,True,page); im.save(f"{OUT}/{name}.jpg",quality=95)

# Mon 23
