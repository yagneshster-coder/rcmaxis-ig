from PIL import Image, ImageDraw, ImageFont
import os
D="/home/user/ig"
def f(w,s): return ImageFont.truetype(f"{D}/fonts/m{w}.woff",s)
NAVY="#0B1F3A"; BLUE="#2F7FF0"; LB="#5FA3FF"; WHITE="#FFFFFF"; BG="#F4F7FB"; GREY="#5B6B82"; INK="#0B1F3A"; GHOST="#12305A"
W,H=1080,1350; M=96
OUT=f"{D}/out"; os.makedirs(OUT,exist_ok=True)

def wrap(d,text,font,maxw):
    lines=[]
    for para in text.split("\n"):
        cur=""
        for w in para.split(" "):
            t=(cur+" "+w).strip()
            if d.textlength(t,font=font)<=maxw: cur=t
            else: lines.append(cur); cur=w
        lines.append(cur)
    return lines
def block(d,xy,text,font,fill,maxw,lh=1.25):
    x,y=xy
    for ln in wrap(d,text,font,maxw):
        d.text((x,y),ln,font=font,fill=fill); y+=int(font.size*lh)
    return y
def chevron(d,x,y,s,col):
    pts=[(0,0),(35,-72.8),(70,0),(47.65,0),(35,-26.32),(22.35,0)]
    d.polygon([(x+px*s/70,y+py*s/70) for px,py in pts],fill=col)
def canvas(dark=True):
    im=Image.new("RGB",(W,H),NAVY if dark else BG); return im,ImageDraw.Draw(im)
def kicker(d,y,t,dark=True):
    fo=f(800,30); tw=d.textlength(t,font=fo)
    d.rounded_rectangle((M,y,M+tw+42,y+56),radius=28,fill=BLUE)
    d.text((M+21,y+12),t,font=fo,fill=WHITE)
def footer(d,dark=True,page=None):
    chevron(d,M,H-80,30,LB if dark else BLUE)
    d.text((M+44,H-92),"RCMAXIS",font=f(800,32),fill=WHITE if dark else INK)
    if page:
        d.text((W//2-70,H-92),"@rcm.axis",font=f(500,28),fill=LB if dark else BLUE)
        d.text((W-M-40,H-92),page,font=f(500,28),fill=LB if dark else BLUE)
    else:
        tw=d.textlength("@rcm.axis",font=f(500,28)); d.text((W-M-tw,H-92),"@rcm.axis",font=f(500,28),fill=LB if dark else BLUE)

def single(name,k,title,sub,body=None,big=None,src=None):
    im,d=canvas(True); y=330
    if not big: chevron(d,W-M-240,H-150,280,GHOST)
    kicker(d,200,k)
    if big:
        d.text((M,y),big,font=f(800,190),fill=LB); y+=250
    y=block(d,(M,y),title,f(800,88 if not big else 60),WHITE,W-2*M,1.12)+40
    y=block(d,(M,y),sub,f(500,46),LB,W-2*M,1.3)+60
    if body: block(d,(M,y),body,f(700,40),WHITE,W-2*M-80,1.4)
    if src: d.text((M,H-160),src,font=f(400,24),fill=GREY)
    footer(d); im.save(f"{OUT}/{name}.jpg",quality=95)

def list_single(name,k,title,items,note=None):
    im,d=canvas(True); kicker(d,150,k)
    y=block(d,(M,240),title,f(800,62),WHITE,W-2*M,1.15)+50
    for a,b in items:
        n=len(wrap(d,b,f(500,34),W-2*M-72)); hh=110+n*42
        d.rounded_rectangle((M,y,W-M,y+hh),radius=22,fill=GHOST)
        d.text((M+36,y+28),a,font=f(800,42),fill=LB)
        block(d,(M+36,y+88),b,f(500,34),WHITE,W-2*M-72,1.2)
        y+=hh+22
    if note: block(d,(M,y+24),note,f(700,36),WHITE,W-2*M,1.3)
    footer(d); im.save(f"{OUT}/{name}.jpg",quality=95)

def cover(name,k,title,sub,page):
    im,d=canvas(True); chevron(d,W-M-300,H-150,360,GHOST)
    kicker(d,200,k); y=block(d,(M,310),title,f(800,84),WHITE,W-2*M,1.12)+30
    block(d,(M,y),sub,f(500,40),LB,W-2*M-100,1.3)
    d.text((M,H-220),"Swipe",font=f(800,36),fill=WHITE)
    d.line((M+125,H-198,M+185,H-198),fill=WHITE,width=5); d.polygon([(M+185,H-210),(M+205,H-198),(M+185,H-186)],fill=WHITE)
    footer(d,True,page); im.save(f"{OUT}/{name}.jpg",quality=95)

def point(name,n,title,body,fix,page):
    im,d=canvas(False)
    d.text((M,170),n,font=f(800,150),fill=BLUE)
    y=block(d,(M,380),title,f(800,62),INK,W-2*M,1.15)+30
    y=block(d,(M,y),body,f(500,40),GREY,W-2*M,1.4)+50
    d.rounded_rectangle((M,y,W-M,y+230),radius=24,fill=WHITE,outline="#D9E3F0",width=3)
    d.text((M+36,y+30),"THE FIX",font=f(800,28),fill=BLUE)
    block(d,(M+36,y+80),fix,f(700,34),INK,W-2*M-72,1.3)
    footer(d,False,page); im.save(f"{OUT}/{name}.jpg",quality=95)

def cta(name,title,sub,page):
    im,d=canvas(True); chevron(d,W//2-110,780,220,BLUE)
    y=block(d,(M,880),title,f(800,62),WHITE,W-2*M,1.15)+20
    block(d,(M,y),sub,f(500,38),LB,W-2*M,1.35)
    footer(d,True,page); im.save(f"{OUT}/{name}.jpg",quality=95)

# 18 Nov - Welcome
single("1118","WELCOME","New here? This is RCMAXIS.",
  "We help US practices get paid for the care they deliver.",
  "Follow for practical posts on denials, AR, coding, billing and credentialing, plus RCM career tips and openings.")
# 19 Nov - Timely filing
list_single("1119","DEADLINES","Timely filing: the deadline that turns a claim into a write-off",
  [("Medicare","12 months from the date of service"),
   ("Medicaid","Set by each state. Check your state's manual"),
   ("Commercial payers","Set by contract. Often 90 to 180 days, sometimes shorter")],
  "Miss it and the claim is usually denied with no appeal. Track it per payer, per claim.")
# 20 Nov - carousel front desk errors
cover("1120_s1","FRONT DESK","5 front-desk errors that cause denials","Small typos at check-in become denied claims weeks later.","1/4")
point("1120_s2","1-2","Name or date of birth mismatch","If the patient's details don't match the payer's file exactly, the claim can reject before it is even reviewed.","Copy details from the insurance card and confirm them with the patient at every visit.","2/4")
point("1120_s3","3-5","Wrong ID, subscriber or plan","An old member ID, the wrong policyholder, or a plan that changed in January all lead to coverage denials.","Scan the card at each visit and run an eligibility check before the appointment.","3/4")
cta("1120_s4","Clean data in = clean claims out","Save this for your front-desk team.","4/4")
# 21 Nov - code sets
list_single("1121","CODING 101","CPT vs ICD-10 vs HCPCS",
  [("CPT","What was done: visits, procedures, tests"),
   ("ICD-10-CM","Why it was done: the diagnosis"),
   ("HCPCS Level II","Supplies, drugs, equipment and some services")],
  "Every claim needs the what and the why to line up. When they don't, expect a medical-necessity denial.")
# 22 Nov - AR aging
list_single("1122","AR","Why the 90+ day bucket matters",
  [("0-30 days","Normal. Most clean claims are paid here"),
   ("31-60 / 61-90 days","Follow up now: status, missing info, rework"),
   ("90+ days","Hardest to collect. Filing and appeal deadlines are closing in")],
  "The older a claim gets, the less likely it is to be paid. Work the oldest money first.")
print(sorted(os.listdir(OUT)))
