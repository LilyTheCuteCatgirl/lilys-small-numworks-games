from kandinsky import fill_rect as F,draw_string as S;from ion import keydown as K;from random import randint as I;i=1;c={0:(255,255,255)}
while i<8192:c[i]=(I(100,255),I(100,255),I(100,255));i*=2
def a(m,l):
 o=1
 while o:
  q,j=I(0,4),I(0,4);r=I(0,19);p=2<<(r>15)+(r>18)
  if m[q][j]:continue
  m[q][j]=p;o=0
 S('Score : '+str(l),59,-2);F(57,15,206,206,(0,0,0))
 for q in range(5):
  for j in range(5):
   n=m[q][j];F(58+41*j,16+41*q,40,40,c[n])
   if n:S(str(n),78+41*j-len(str(n))*5,28+41*q,(0,0,0),c[n])
def v(l,p,t):
 n=0
 for q in range(5):
  e=[l[q][j] for j in range(5)]if t==0 else[l[q][4-j]for j in range(5)]if t==3 else[l[j][q]for j in range(5)]if t==1 else[l[4-j][q]for j in range(5)]
  s=[x for x in e if x];z=[];j=0
  while j<len(s):
   x=s[j]
   if j+1<len(s)and x==s[j+1]:x*=2;p+=x;j+=1
   z.append(x);j+=1
  z+=[0]*(5-len(z))
  if z!=e:n=1
  for j in range(5):
   x=z[j]
   if t==0:l[q][j]=x
   elif t==3:l[q][4-j]=x
   elif t==1:l[j][q]=x
   else:l[4-j][q]=x
 return l,p,n
def g(n=None,m=0):
 try:
  if n==None:n=[[0]*5 for r in range(5)];a(n,m)
  q=1
  while q:
   o=0
   for t in(0,3,2,1):
    if K(t):
     o=1;n,m,l=v(n,m,t)
     if l:a(n,m)
   if o:
    while K(0)or K(1)or K(2)or K(3):pass
    q=0
    for r in range(5):
     for j in range(5):
      p=n[r][j]
      if not p or(r>0 and p==n[r-1][j])or(r<4 and p==n[r+1][j])or(j>0 and p==n[r][j-1])or(j<4 and p==n[r][j+1]):q=1;break
 except KeyboardInterrupt:pass
 return m
print('Score :',g())