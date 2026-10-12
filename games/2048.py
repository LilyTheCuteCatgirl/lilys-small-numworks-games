from kandinsky import fill_rect as draw,draw_string as drawtxt;from ion import keydown;from random import randint,choice;i=1;c={0:(255,255,255)}
while i<8192:c[i]=(randint(100,255),randint(100,255),randint(100,255));i*=2
b=[1]*1024+[2]*512+[4]*256+[8]*128+[16]*64+[32]*32+[64]*16+[128]*8+[256]*4+[512]*2+[1024]
def a(m,l):
 o=True
 while o:
  q,j,p=(randint(0,4),randint(0,4),choice(b))
  if m[q][j][0]:continue
  else:m[q][j][0]=p;o=False
 drawtxt('Score : '+str(l),59,-2);draw(57,15,206,206,(0,0,0))
 for q in range(5):
  for j in range(5):
   n=m[q][j][0];draw(58+41*j,16+41*q,40,40,c[n])
   if n:drawtxt(str(n),78+41*j-len(str(n))*5,28+41*q,(0,0,0),c[n])
def h(l,p):
 n=False
 for q in range(0,5):
  for j in range(1,5):
   m,o=l[q][j-1:j+1]
   if not o[0]:continue
   if m[0]:
    if m[0]==o[0]and(not(m[1]or o[1])):l[q][j-1],l[q][j]=([2*m[0],1],[0,0]);p+=2*m[0];n=True
    else:continue
   else:l[q][j-1],l[q][j]=(o.copy(),[0,0]);n=True
   j-=1
   while j!=0:
    m,o=l[q][j-1:j+1]
    if not m[0]:l[q][j-1],l[q][j]=(o.copy(),[0,0]);n=True
    elif m[0]==o[0]and(not(m[1]or o[1])):n=True;l[q][j-1],l[q][j]=([o[0]*2,1],[0,0]);p+=2*o[0]
    else:break
    j-=1
 for q in range(5):
  for j in range(5):l[q][j][1]=0
 return(l,p,n)
def d(l,p):
 n=False
 for q in range(0,5):
  for j in range(1,5):
   j=4-j;m,o=l[q][j:j+2]
   if not m[0]:continue
   if o[0]:
    if m[0]==o[0]and(not(m[1]or o[1])):l[q][j+1],l[q][j]=([2*m[0],1],[0,0]);n=True;p+=2*m[0]
    else:continue
   else:l[q][j+1],l[q][j]=(m.copy(),[0,0]);n=True
   j+=1
   while j!=4:
    m,o=l[q][j:j+2]
    if not o[0]:l[q][j+1],l[q][j]=(m.copy(),[0,0]);n=True
    elif m[0]==o[0]and(not(m[1]or o[1])):l[q][j+1],l[q][j]=([m[0]*2,1],[0,0]);n=True;p+=2*m[0]
    else:break
    j+=1
 for q in range(5):
  for j in range(5):l[q][j][1]=0
 return(l,p,n)
def f(l,p):
 n=False
 for q in range(0,5):
  for j in range(1,5):
   j=4-j;m,o=(l[j][q],l[j+1][q])
   if not m[0]:continue
   if o[0]:
    if m[0]==o[0]and(not(m[1]or o[1])):l[j+1][q],l[j][q]=([2*m[0],1],[0,0]);n=True;p+=2*m[0]
    else:continue
   else:l[j+1][q],l[j][q]=(m.copy(),[0,0]);n=True
   j+=1
   while j!=4:
    m,o=(l[j][q],l[j+1][q])
    if not o[0]:l[j+1][q],l[j][q]=(m.copy(),[0,0]);n=True
    elif m[0]==o[0]and(not(m[1]or o[1])):l[j+1][q],l[j][q]=([m[0]*2,1],[0,0]);n=True;p+=2*m[0]
    else:break
    j+=1
 for q in range(5):
  for j in range(5):l[q][j][1]=0
 return(l,p,n)
def k(l,p):
 n=False
 for q in range(0,5):
  for j in range(1,5):
   m,o=(l[j-1][q],l[j][q])
   if not o[0]:continue
   if m[0]:
    if m[0]==o[0]and(not(m[1]or o[1])):l[j-1][q],l[j][q]=([2*m[0],1],[0,0]);n=True;p+=2*m[0]
    else:continue
   else:l[j-1][q],l[j][q]=(o.copy(),[0,0]);n=True
   j-=1
   while j!=0:
    m,o=(l[j-1][q],l[j][q])
    if not m[0]:l[j-1][q],l[j][q]=(o.copy(),[0,0]);n=True
    elif m[0]==o[0]and(not(m[1]or o[1])):n=True;l[j-1][q],l[j][q]=([m[0]*2,1],[0,0]);p+=2*m[0]
    else:break
    j-=1
 for q in range(5):
  for j in range(5):l[q][j][1]=0
 return(l,p,n)
def g(n=None,m=0):
 try:
  try:
   for r in range(5):
    for j in range(5):n[r][j]
  except (IndexError,TypeError):n=[[[0 for r in range(2)]for r in range(5)]for r in range(5)];a(n,m)
  q=True
  while q:
   o=False
   if keydown(0):
    o=True;n,m,l=h(n,m)
    if l:a(n,m)
   if keydown(3):
    o=True;n,m,l=d(n,m)
    if l:a(n,m)
   if keydown(2):
    o=True;n,m,l=f(n,m)
    if l:a(n,m)
   if keydown(1):
    o=True;n,m,l=k(n,m)
    if l:a(n,m)
   if o:
    while keydown(0)or keydown(1)or keydown(2)or keydown(3):pass
    q=False
    for r in range(5):
     for j in range(5):
      p=n[r][j][0]
      if not p or(r>0 and p==n[r-1][j][0])or(r<4 and p==n[r+1][j][0])or(j>0 and p==n[r][j-1][0])or(j<4 and p==n[r][j+1][0]):q=True;break
 except KeyboardInterrupt:pass
 return m
print('Score :',g())