from kandinsky import fill_rect as draw,draw_string as drawtxt;from ion import keydown;from random import randint;i=1;c={0:(255,255,255)}
while i<8192:c[i]=(randint(100,255),randint(100,255),randint(100,255));i*=2
def a(m,l):
 o=True
 while o:
  q,j=randint(0,4),randint(0,4);r=randint(0,19);p=2<<(r>15)+(r>18)
  if m[q][j][0]:continue
  else:m[q][j][0]=p;o=False
 drawtxt('Score : '+str(l),59,-2);draw(57,15,206,206,(0,0,0))
 for q in range(5):
  for j in range(5):
   n=m[q][j][0];draw(58+41*j,16+41*q,40,40,c[n])
   if n:drawtxt(str(n),78+41*j-len(str(n))*5,28+41*q,(0,0,0),c[n])
def v(l,p,t):
 n=False
 for q in range(5):
  e=[l[q][j][0] for j in range(5)]if t==0 else[l[q][4-j][0]for j in range(5)]if t==3 else[l[j][q][0]for j in range(5)]if t==1 else[l[4-j][q][0]for j in range(5)]
  s=[x for x in e if x];z=[];j=0
  while j<len(s):
   x=s[j]
   if j+1<len(s)and x==s[j+1]:x*=2;p+=x;j+=1
   z.append(x);j+=1
  z+=[0]*(5-len(z))
  if z!=e:n=True
  for j in range(5):
   x=[z[j],0]
   if t==0:l[q][j]=x
   elif t==3:l[q][4-j]=x
   elif t==1:l[j][q]=x
   else:l[4-j][q]=x
 return l,p,n
def g(n=None,m=0):
 try:
  try:
   for r in range(5):
    for j in range(5):n[r][j]
  except (IndexError,TypeError):n=[[[0 for r in range(2)]for r in range(5)]for r in range(5)];a(n,m)
  q=True
  while q:
   o=False
   for t in(0,3,2,1):
    if keydown(t):
     o=True;n,m,l=v(n,m,t)
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