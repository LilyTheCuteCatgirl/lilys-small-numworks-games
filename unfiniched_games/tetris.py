from kandinsky import fill_rect as FR,draw_string as DS
from ion import keydown as KD,KEY_UP,KEY_DOWN,KEY_LEFT,KEY_RIGHT,KEY_OK,KEY_EXE
from time import sleep as SL,monotonic as MT
from random import randint as RI
SHAPES=('4567','1256','1456','1245','0156','0456','2456')
COLORS=((20,20,20),(0,210,220),(255,225,40),(190,80,225),(70,215,85),(245,70,70),(65,100,255),(255,150,55))
WHITE=(255,255,255)
def blocks(n,r,x,y):
 for ch in SHAPES[n]:
  k=int(ch,16);a=k%4;b=k//4
  if n!=1:
   for _ in range(r):a,b=3-b,a
  yield x+a,y+b
def fits(n,r,x,y):
 for a,b in blocks(n,r,x,y):
  if a<0 or a>=10 or b>=20 or b>=0 and board[b][a]:return False
 return True
def paint(x,y,c):
 if y>=0:FR(82+10*x,20+10*y,9,9,COLORS[c])
def draw():
 FR(78,16,104,204,(90,90,90))
 FR(81,19,100,200,COLORS[0])
 for j in range(20):
  for i in range(10):
   if board[j][i]:paint(i,j,board[j][i])
 for a,b in blocks(piece,rot,px,py):paint(a,b,piece+1)
 FR(194,0,126,122,WHITE)
 DS('TETRIS',204,8)
 DS('SCORE',204,38)
 DS(str(score),204,58)
 DS('LINES '+str(lines),204,84)
 DS('LV '+str(level),204,104)
def next_piece():
 global piece,rot,px,py,bag
 if not bag:bag=list(range(7))
 piece=bag.pop(RI(0,len(bag)-1))
 rot=0;px=3;py=-1
 return fits(piece,rot,px,py)
def lock_piece():
 global board,score,lines,level
 for x,y in blocks(piece,rot,px,py):
  if y<0:return False
  board[y][x]=piece+1
 remaining=[row for row in board if 0 in row]
 cleared=20-len(remaining)
 board=[[0]*10 for _ in range(cleared)]+remaining
 lines+=cleared
 level=1+lines//10
 score+=(0,100,300,500,800)[cleared]*level
 return next_piece()
def play():
 global board,piece,rot,px,py,bag,score,lines,level
 board=[[0]*10 for _ in range(20)]
 bag=[];score=0;lines=0;level=1
 next_piece()
 FR(0,0,320,222,WHITE)
 DS('ROTATE',0,20)
 DS('MOVE',0,50)
 DS('FALL',0,80)
 DS('DROP',0,110)
 DS('TETRIS',0,185)
 last=MT();repeat=last;held=False;dropheld=False
 draw()
 while True:
  now=MT();changed=False
  up=KD(KEY_UP)
  if up and not held:
   nr=(rot+1)%4
   for step in(0,-1,1,-2,2):
    if fits(piece,nr,px+step,py):rot=nr;px+=step;changed=True;break
  held=up
  left=KD(KEY_LEFT);right=KD(KEY_RIGHT)
  if left or right:
   if now>=repeat:
    xx=px+right-left
    if fits(piece,rot,xx,py):px=xx;changed=True
    repeat=now+.12
  else:repeat=now
  hard=KD(KEY_OK)or KD(KEY_EXE)
  if hard and not dropheld:
   while fits(piece,rot,px,py+1):py+=1;score+=1
   if not lock_piece():break
   changed=True;last=now
  dropheld=hard
  interval=max(.10,.68-.045*(level-1))
  if now-last>=(.065 if KD(KEY_DOWN)else interval):
   if fits(piece,rot,px,py+1):py+=1
   elif not lock_piece():break
   changed=True;last=now
  if changed:draw()
  SL(.025)
 FR(72,90,156,50,WHITE)
 DS('GAME OVER',86,98)
 DS('OK RESTART',82,118)
 while KD(KEY_OK)or KD(KEY_EXE):SL(.05)
 while not(KD(KEY_OK)or KD(KEY_EXE)):SL(.05)
 while KD(KEY_OK)or KD(KEY_EXE):SL(.05)
while True:play()