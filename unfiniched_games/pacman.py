from kandinsky import fill_rect as FR,draw_string as DS
from ion import keydown as KD,KEY_UP,KEY_DOWN,KEY_LEFT,KEY_RIGHT,KEY_OK
from time import sleep as SL,monotonic as MT
from random import randint as RI
ROWS=('#################','#o.....#.......o#','#.###..#..###.#.#','#......#........#','#.###.....###.#.#','#...#..#..#.....#','###.#.....#.###.#','#......#........#','#.###.....###.#.#','#...#..#..#...#.#','#.#....#....#...#','#o.............o#','#################')
D=((0,-1),(0,1),(-1,0),(1,0))
K=(KEY_UP,KEY_DOWN,KEY_LEFT,KEY_RIGHT)
BLACK=(0,0,0)
BLUE=(20,50,190)
WHITE=(255,255,255)
YELLOW=(255,220,0)
GHOST=((255,60,80),(0,220,230),(250,100,230))
def cell(x,y):
 c=maze[y][x];a=41+14*x;b=22+14*y
 FR(a,b,14,14,BLUE if c=='#'else BLACK)
 if c=='.':FR(a+6,b+6,2,2,WHITE)
 if c=='o':FR(a+4,b+4,6,6,YELLOW)
def actor(x,y,c):
 a=41+14*x;b=22+14*y
 FR(a+2,b+2,10,10,c)
 if c!=YELLOW:
  FR(a+4,b+4,2,2,WHITE)
  FR(a+8,b+4,2,2,WHITE)
def hud():
 FR(0,0,320,20,BLACK)
 DS('PAC-MAN '+str(score)+'  LIVES '+str(lives),1,0,YELLOW,BLACK)
def ready(text):
 FR(32,91,256,38,BLACK)
 DS(text,36,100,YELLOW,BLACK)
 while KD(KEY_OK):SL(.06)
 while not KD(KEY_OK):SL(.06)
 while KD(KEY_OK):SL(.06)
def reset():
 global px,py,gs,turn
 px,py=8,11
 gs=[[8,6],[8,3],[3,5]]
 turn=0
def free(x,y):
 return 0<=y<len(maze)and 0<=x<17 and maze[y][x]!='#'
def hit():
 global lives,score,power
 for i,g in enumerate(gs):
  if g[0]==px and g[1]==py:
   if power:
    score+=200
    gs[i]=[8,6]
   else:
    lives-=1
    hud()
    SL(.35)
    reset()
    for y in range(len(maze)):
     for x in range(17):cell(x,y)
    hud()
    return True
 return False
def play():
 global maze,px,py,gs,turn,score,lives,power,remaining
 maze=[list(row)for row in ROWS]
 remaining=sum(row.count('.')+row.count('o')for row in ROWS)
 score=0;lives=3;power=0
 reset()
 FR(0,0,320,222,BLACK)
 for y in range(len(maze)):
  for x in range(17):cell(x,y)
 hud()
 actor(px,py,YELLOW)
 for i,g in enumerate(gs):actor(g[0],g[1],GHOST[i])
 want=2;direction=2;tick=MT()
 while lives and remaining:
  for i in range(4):
   if KD(K[i]):want=i
  now=MT()
  if now-tick<.15:
   SL(.02)
   continue
  tick=now
  old=(px,py)
  dx,dy=D[want]
  if free(px+dx,py+dy):direction=want
  dx,dy=D[direction]
  if free(px+dx,py+dy):px+=dx;py+=dy
  c=maze[py][px]
  if c in'.o':
   score+=50 if c=='o'else 10
   power=35 if c=='o'else power
   remaining-=1;maze[py][px]=' '
  cell(old[0],old[1])
  cell(px,py)
  if hit():continue
  turn+=1
  if turn%2==0:
   for i,g in enumerate(gs):
    ox,oy=g
    ways=[(ox+dx,oy+dy)for dx,dy in D if free(ox+dx,oy+dy)]
    if ways:
     if RI(0,4)==0:
      nx,ny=ways[RI(0,len(ways)-1)]
     else:
      def dist(p):return abs(p[0]-px)+abs(p[1]-py)
      best=ways[0]
      for q in ways[1:]:
       if(power and dist(q)>dist(best))or(not power and dist(q)<dist(best)):best=q
      nx,ny=best
     gs[i]=[nx,ny]
     cell(ox,oy)
     if hit():break
  actor(px,py,YELLOW)
  for i,g in enumerate(gs):actor(g[0],g[1],(GHOST[i]if not power else(35,35,230)))
  if power:power-=1
  hud()
 ready('YOU WIN!'if remaining==0 else'GAME OVER')
while True:play()