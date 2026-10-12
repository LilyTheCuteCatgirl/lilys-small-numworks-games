from kandinsky import fill_rect as FR,draw_string as DS
from ion import keydown as KD,KEY_UP,KEY_DOWN,KEY_LEFT,KEY_RIGHT,KEY_OK,KEY_EXE,KEY_SHIFT
from time import sleep as SL
from random import randint as RI
W=12;H=9;MINES=18
WHITE=(255,255,255)
BLACK=(0,0,0)
GRAY=(160,165,175)
BLUE=(25,75,210)
RED=(210,35,35)
def neighbors(p):
 x=p%W;y=p//W
 return[b*W+a for b in range(max(0,y-1),min(H,y+2))for a in range(max(0,x-1),min(W,x+2))if(a,b)!=(x,y)]
def count(p):return sum(mines[q]for q in neighbors(p))
def tile(p):
 x=34+21*(p%W);y=22+21*(p//W)
 c=WHITE if opened[p]else GRAY
 FR(x,y,20,20,c)
 if opened[p]:
  if mines[p]:DS('*',x+5,y+1,RED,c)
  else:
   n=count(p)
   if n:DS(str(n),x+5,y+1,(0,0,200)if n<3 else RED,c)
 elif flags[p]:DS('F',x+5,y+1,RED,c)
 if p==cursor:
  FR(x,y,20,1,BLUE)
  FR(x,y+19,20,1,BLUE)
  FR(x,y,1,20,BLUE)
  FR(x+19,y,1,20,BLUE)
def header(text=''):
 FR(0,0,320,20,WHITE)
 DS(text or'MINES '+str(MINES)+' FLAGS '+str(sum(flags)),4,0,BLACK,WHITE)
def setup():
 global mines,opened,flags,cursor,first,won
 mines=[0]*(W*H);opened=[0]*(W*H);flags=[0]*(W*H)
 cursor=0;first=True;won=False
 FR(0,0,320,222,WHITE)
 for p in range(W*H):tile(p)
 header()
def place(p):
 forbidden=neighbors(p)+[p]
 n=0
 while n<MINES:
  q=RI(0,W*H-1)
  if q not in forbidden and not mines[q]:mines[q]=1;n+=1
def reveal(p):
 todo=[p]
 while todo:
  q=todo.pop()
  if opened[q]or flags[q]:continue
  opened[q]=1
  tile(q)
  if count(q)==0 and not mines[q]:
   for z in neighbors(q):
    if not opened[z]and not flags[z]:todo.append(z)
def play():
 global cursor,first,won
 setup()
 keys=(KEY_UP,KEY_DOWN,KEY_LEFT,KEY_RIGHT,KEY_OK,KEY_EXE,KEY_SHIFT)
 while True:
  k=-1
  for i,key in enumerate(keys):
   if KD(key):k=i;break
  if k<0:SL(.04);continue
  old=cursor
  x=cursor%W;y=cursor//W
  if k==0 and y>0:cursor-=W
  if k==1 and y<H-1:cursor+=W
  if k==2 and x>0:cursor-=1
  if k==3 and x<W-1:cursor+=1
  if k==6 and not opened[cursor]:
   flags[cursor]=1-flags[cursor]
   header()
  if k in(4,5)and not flags[cursor]and not opened[cursor]:
   if first:place(cursor);first=False
   if mines[cursor]:
    for p in range(W*H):
     if mines[p]:opened[p]=1;tile(p)
    header('BOOM! OK TO RESTART')
    break
   reveal(cursor)
   if sum(opened)==W*H-MINES:
    won=True;header('YOU WIN! OK TO RESTART');break
  tile(old);tile(cursor)
  while KD(keys[k]):SL(.035)
 while KD(KEY_OK)or KD(KEY_EXE):SL(.05)
 while not(KD(KEY_OK)or KD(KEY_EXE)):SL(.05)
 while KD(KEY_OK)or KD(KEY_EXE):SL(.05)
while True:play()