exec(open(MAKE).read().split("# 18 Nov")[0])
exec(open(W1F).read().split("# Mon 23")[0].split("\n",1)[1])
_cover,_bullets,_endcard=cover,bullets,endcard

def cover(name,k,title,sub,i,n): _cover(name,k,title,sub,f"{i}/{n}")
def bullets(name,title,items,i,n): _bullets(name,title,items,f"{i}/{n}")
def cta(name,title,sub,i,n): _endcard(name,title,sub,f"{i}/{n}")

def code(name,c,title,move,i,n):
    im,d=canvas(False); sz=170
    while d.textlength(c,font=f(800,sz))>W-2*M: sz-=10
    d.text((M,220+(170-sz)),c,font=f(800,sz),fill=BLUE)
    y=block(d,(M,460),title,f(700,58),INK,W-2*M,1.2)+50
    d.rounded_rectangle((M,y,W-M,y+400),radius=24,fill=WHITE,outline="#D9E3F0",width=3)
    d.text((M+42,y+40),"NEXT MOVE",font=f(800,28),fill=BLUE)
    block(d,(M+42,y+100),move,f(500,42),INK,W-2*M-84,1.4)
    footer(d,False,f"{i}/{n}"); im.save(f"{OUT}/{name}.jpg",quality=95)

def steps(name,title,items,i,n):
    im,d=canvas(False)
    y=block(d,(M,190),title,f(800,66),INK,W-2*M,1.15)+70
    for num,t,desc in items:
        d.ellipse((M,y,M+92,y+92),fill=BLUE)
        tw=d.textlength(str(num),font=f(800,44)); d.text((M+46-tw/2,y+20),str(num),font=f(800,44),fill=WHITE)
        d.text((M+136,y+2),t,font=f(700,46),fill=INK)
        y=block(d,(M+136,y+66),desc,f(500,36),GREY,W-2*M-136,1.35)+70
    footer(d,False,f"{i}/{n}"); im.save(f"{OUT}/{name}.jpg",quality=95)

def cards(name,k,title,items,foot=None):
    im,d=canvas(False); kicker(d,140,k)
    y=block(d,(M,240),title,f(800,66),INK,W-2*M,1.15)+40
    for t,desc in items:
        nl=len(wrap(d,desc,f(500,34),W-2*M-80)); hh=120+nl*44
        d.rounded_rectangle((M,y,W-M,y+hh),radius=22,fill=WHITE,outline="#D9E3F0",width=3)
        d.text((M+40,y+30),t,font=f(800,42),fill=BLUE)
        block(d,(M+40,y+92),desc,f(500,34),INK,W-2*M-80,1.3)
        y+=hh+30
    if foot: block(d,(M,y+20),foot,f(800,38),INK,W-2*M,1.3)
    footer(d,False); im.save(f"{OUT}/{name}.jpg",quality=95)

def single(name,k,title,body,dark=False,src=None,big=None):
    im,d=canvas(dark); c=WHITE if dark else INK; g=LB if dark else GREY
    if dark: chevron(d,W-M-240,H-150,280,GHOST)
    kicker(d,200,k); y=330
    if big:
        d.text((M,y),big,font=f(800,190),fill=LB if dark else BLUE); y+=250
    y=block(d,(M,y),title,f(800,80 if not big else 56),c,W-2*M,1.12)+60
    block(d,(M,y),body,f(500,44),g,W-2*M-(80 if dark else 0),1.45)
    if src: d.text((M,H-160),src,font=f(400,24),fill=GREY)
    footer(d,dark); im.save(f"{OUT}/{name}.jpg",quality=95)
