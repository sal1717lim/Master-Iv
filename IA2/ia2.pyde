
import logging
import threading
import time
find =False
obst=[[1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
        [1,0,0,0,0,0,2,0,0,0,0,0,0,0,0,1],
        [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
        [1,0,0,0,0,0,0,0,0,0,1,1,0,0,0,1],
        [1,1,0,0,1,0,0,1,0,0,0,0,0,0,0,1],
        [1,0,0,0,1,0,0,1,1,0,0,0,0,0,0,1],
        [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
        [1,0,0,0,0,0,0,0,0,0,0,0,1,0,0,1],
        [1,0,0,0,1,0,0,0,0,0,0,0,1,0,0,1],
        [1,0,0,0,0,0,1,1,0,0,0,0,0,0,0,1],
        [1,0,0,0,0,0,1,0,0,0,0,0,0,0,0,1],
        [1,0,0,0,0,1,0,0,0,0,0,0,0,1,1,1],
        [1,0,0,0,0,0,0,0,1,0,0,0,0,0,0,1],
        [1,0,3,0,0,0,0,1,0,0,0,0,0,0,0,1],
        [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
        [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]
      ]
res1=[[1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
        [1,0,0,0,0,0,2,0,0,0,0,0,0,0,0,1],
        [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
        [1,0,0,0,0,0,0,0,0,0,1,1,0,0,0,1],
        [1,1,0,0,1,0,0,1,0,0,0,0,0,0,0,1],
        [1,0,0,0,1,0,0,1,1,0,0,0,0,0,0,1],
        [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
        [1,0,0,0,0,0,0,0,0,0,0,0,1,0,0,1],
        [1,0,0,0,1,0,0,0,0,0,0,0,1,0,0,1],
        [1,0,0,0,0,0,1,1,0,0,0,0,0,0,0,1],
        [1,0,0,0,0,0,1,0,0,0,0,0,0,0,0,1],
        [1,0,0,0,0,1,0,0,0,0,0,0,0,1,1,1],
        [1,0,0,0,0,0,0,0,1,0,0,0,0,0,0,1],
        [1,0,3,0,0,0,0,1,0,0,0,0,0,0,0,1],
        [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
        [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]
      ]
res2=[[1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
        [1,0,0,0,0,0,2,0,0,0,0,0,0,0,0,1],
        [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
        [1,0,0,0,0,0,0,0,0,0,1,1,0,0,0,1],
        [1,1,0,0,1,0,0,1,0,0,0,0,0,0,0,1],
        [1,0,0,0,1,0,0,1,1,0,0,0,0,0,0,1],
        [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
        [1,0,0,0,0,0,0,0,0,0,0,0,1,0,0,1],
        [1,0,0,0,1,0,0,0,0,0,0,0,1,0,0,1],
        [1,0,0,0,0,0,1,1,0,0,0,0,0,0,0,1],
        [1,0,0,0,0,0,1,0,0,0,0,0,0,0,0,1],
        [1,0,0,0,0,1,0,0,0,0,0,0,0,1,1,1],
        [1,0,0,0,0,0,0,0,1,0,0,0,0,0,0,1],
        [1,0,3,0,0,0,0,1,0,0,0,0,0,0,0,1],
        [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
        [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]
      ]
h=None
w=None
tour=0
fermer1=[]
ouvert1=[]
chemin1=[]
ouvert2=[]
fermer2=[]
chemin2=[]
in1=None
in2=None
in3=None
def dessin(res,img,pos1,pos2):
    

    w=256
    h=256
    for x in range(256):
        for y  in range(256):
            loc = x +y*256
            stepx=256/16
            stepy=256/16
            i=int(y/stepy)
            j=int(x/stepx)
            val=res[i][j]
            if val==0:
                r=0
                g=0
                b=0
            if val==1:
                r=0
                g=0
                b=255
            if val==2:
                r=255
                g=0
                b=0
            if val==3:
                r=0
                g=255
                b=0
            if val==4:
                r=127
                g=127
                b=127
            
            c=color(r,g,b)
            img.pixels[loc]=c
            img.updatePixels()
            image(img,pos1,pos2)
def trouvechemin(fermer):

    
    chemin=[]
    k=len(fermer)-1
    x=fermer[k].pred
    while(x.pred!=None):
        chemin.append(x)
        x=x.pred
    return chemin

class neud:
    def __init__(self,i,j,val):
        self.i=i
        self.j=j
        self.valeur=val
        self.pred=None
def path(re1,img,fermer,pos1,pos2):



    i=0
    j=0
    chemin=trouvechemin(fermer)
    for x in chemin:
        i=x.i
        j=x.j
        if(re1[i][j]==0):
            re1[i][j]=4
        
    dessin(re1,img,pos1,pos2)
def lancerparcourp():
    global obst
    global ouvert2
    i=1
    j=6
    init=neud(1,6,obst[i][j])
    ouvert2.append(init)
    parcourP(init)
def existe(ensemble,i,j):
    for k in ensemble:
        if k.i==i and k.j==j:
            return True 
def parcourP(init):
    global ouvert2
    global fermer2
    global res2
    global in2
    global find
    i=init.i
    j=init.j

    x=init
    while x.valeur!=3 and len(ouvert2)!=0 and not find:
        x=ouvert2[0]
        ouvert2.remove(x)
        fermer2.append(x)
        if x.j-1>=0 and obst[x.i][x.j-1]!=1:
            if not existe(ouvert2,x.i,j-1) and not existe(fermer2,x.i,j-1):
                k=neud(x.i,x.j-1,obst[x.i][x.j-1])
            
                k.pred=x
            
                if k.valeur==3:
                    fermer2.append(k)
                    find=True
                    break
                else:
                    ouvert2.append(k)
                    parcourP(k)
            
           
                    
        if x.i+1<16 and obst[x.i+1][x.j]!=1:
            if not existe(ouvert2,x.i+1,j) and not existe(fermer2,x.i+1,j):
                k=neud(x.i+1,x.j,obst[x.i+1][x.j])
                k.pred=x
            
                if k.valeur==3:
                    print("its found")
                    fermer2.append(k)
                    find=True
                    break
                else:
                    ouvert2.append(k)
                    parcourP(k)
            
        if x.j+1>=0 and obst[x.i][x.j+1]!=1:
            if not existe(ouvert2,x.i,j+1) and not existe(fermer2,x.i,j+1):
                k=neud(x.i,x.j+1,obst[x.i][x.j+1])
                k.pred=x
            
                if k.valeur==3:
                    fermer2.append(k)
                    find=True
                    break
                else:
                    ouvert2.append(k)
                    parcourP(k)
            
    if find:
        path(res2,in2,fermer2,270,0)


    

def parcourL():
    global ouvert1
    global fermer1
    global res1
    global in1
    x=None
    i=1
    j=6
    init=neud(1,6,obst[i][j])
    ouvert1.append(init)
    x=init
    while x.valeur!=3 and len(ouvert1)!=0:
        x=ouvert1[0]
        ouvert1.remove(x)
        fermer1.append(x)
        if x.j-1>=0 and obst[x.i][x.j-1]!=1:
            if not existe(ouvert1,x.i,x.j-1) and not existe(fermer1,x.i,x.j-1):
                print("left")
                k=neud(x.i,x.j-1,obst[x.i][x.j-1])
                k.pred=x
                ouvert1.append(k)
                
        if x.i+1<16 and obst[x.i+1][x.j]!=1:
            if not existe(ouvert1,x.i+1,x.j) and not existe(fermer1,x.i+1,x.j):
                k=neud(x.i+1,x.j,obst[x.i+1][x.j])
                print("down")
                k.pred=x
                ouvert1.append(k)
        if x.j+1>=0 and obst[x.i][x.j+1]!=1:
            if not existe(ouvert1,x.i,x.j+1) and not existe(fermer1,x.i,x.j+1):
                k=neud(x.i,x.j+1,obst[x.i][x.j+1])
                print("rigth")
                k.pred=x
                ouvert1.append(k)
    print(ouvert1)
    path(res1,in1,fermer1,0,0)


def setup():
    global h
    global w
    global tour
    global in1
    global in2
    global in3
    h=256
    w=256
    size(540,350)
    r=0
    g=0
    b=0
    in1 = createImage(w,h,RGB) 
    in3 = createImage(w,h,RGB) 
    in2 = createImage(w,h,RGB) 
    in1.loadPixels()
    in2.loadPixels()
    in3.loadPixels()
    for x in range(256):
        for y  in range(256):
            loc = x +y*256
            stepx=256/16
            stepy=256/16
            i=int(y/stepy)
            j=int(x/stepx)
            val=obst[i][j]
            if val==0:
                r=0
                g=0
                b=0
            if val==1:
                r=0
                g=0
                b=255
            if val==2:
                r=255
                g=0
                b=0
            if val==3:
                r=0
                g=255
                b=0
            c=color(r,g,b)
            in1.pixels[loc]=c
            in2.pixels[loc]=c
            in3.pixels[loc]=c
    image(in1,0,0)
    image(in2,270,0)
    image(in3,540,0)
    fill(0)
    textSize(15)
    text(" largeur dabord                               profondeur dabord",0,280)
    w=256
    h=256
    tour=0

    x = threading.Thread(target=parcourL)
    y = threading.Thread(target=lancerparcourp)
    x.start()
    y.start()
    # x.join()

    
def draw():
    pass
                
        
