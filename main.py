import random
from PIL import Image, PngImagePlugin

class CustomImage:
    def __init__(self,size):
        self.size=size*2+1
        #white background
        self.image=Image.new("1",(self.size,self.size),1)

    def __getitem__(self,pos):
        try:
            return self.image.getpixel((pos[0],pos[1]))
        except:
            return (0,0,0)
    def __setitem__(self,pos,color):
        if type(color) in [list,tuple]:
            self.image.putpixel((pos[0],pos[1]),color)
        elif type(color)==bool:
            if color:
                self.image.putpixel((pos[0],pos[1]),0)
            else:
                pass
        else:
            raise TypeError("color must be a list or a tuple or bool")
    def bot1(self, steps, SEED=False):
        if SEED:
            random.seed(SEED)
        x,y=random.randint(0,(self.size-1)//4)*2,random.randint(0,(self.size-1)//4)*2
        self[x,y]=True
        self[self.size-x-1,y]=True
        self[x,self.size-y-1]=True
        self[self.size-x-1,self.size-y-1]=True
        self[y,x]=True
        self[y,self.size-x-1]=True
        self[self.size-y-1,x]=True
        self[self.size-y-1,self.size-x-1]=True
        for i in range(steps):
            lx,ly=x,y
            options=[(x+2,y),(x-2,y),(x,y+2),(x,y-2)]
            options2=[]
            for pos in options:
                x,y=pos
                #out of screen
                if not (0<=x<self.size and 0<=y<self.size):
                    pass
                elif self[x+1, y]==self[x-1, y]==self[x, y+1]==self[x, y-1]==0:
                    pass
                else:
                    options2.append(pos)
            if len(options2)==0:
                return
            x,y=random.choice(options2)
            mx,my=(lx+x)//2,(ly+y)//2
            self[mx,my]=True
            self[self.size-mx-1,my]=True
            self[mx,self.size-my-1]=True
            self[self.size-mx-1,self.size-my-1]=True
            self[my,mx]=True
            self[my,self.size-mx-1]=True
            self[self.size-my-1,mx]=True
            self[self.size-my-1,self.size-mx-1]=True
            self[x,y]=True
            self[self.size-x-1,y]=True
            self[x,self.size-y-1]=True
            self[self.size-x-1,self.size-y-1]=True
            self[y,x]=True
            self[y,self.size-x-1]=True
            self[self.size-y-1,x]=True
            self[self.size-y-1,self.size-x-1]=True
        self.preview()
    def preview(self):
        #ouvre l'image
        self.image.show()
    def save(self,name,seed,step):
        #ajoute une description au fichier
        pnginfo=PngImagePlugin.PngInfo()
        pnginfo.add_text("seed",str(seed))
        pnginfo.add_text("step",str(step))
        #sauvegarde l'image
        self.image.save(f"generated/{name}.png","PNG",pnginfo=pnginfo)

def read_comment(filename):
    try:
        with Image.open(filename) as img:
            metadata=dict(img.info)
        output=""
        if "seed" in metadata:
            output+=f"seed: {metadata['seed']}\n"
        if "step" in metadata:
            output+=f"step: {metadata['step']}"
        return output
    except Exception as e:
        return f"Error reading metadata: {e}"

def parse(command,values):
    command=" ".join(command.split(" ")[1:])
    for k,v in enumerate(command.split(", ")):
        if "=" in v:
            values[v.split("=")[0]]=v.split("=")[1]
        else:
            values[list(values.keys())[k]]=v
    return values

while True:
    command=input(">>> ")
    if command=="help":
        print("help")
        print("save name, seed=auto, size=auto, step=auto")
        print("read name")
        print("exit")
    elif command=="":
        continue
    elif command.startswith("save"):
        values=parse(command,values={"name":None,"seed":"auto","size":"auto","step":"auto"})
        if values["name"] is None:
            print("name is required")
        else:
            if values["seed"]=="auto":
                values["seed"]=random.getrandbits(32)
            if values["size"]=="auto":
                values["size"]=random.randint(10,110)
            if values["step"]=="auto":
                values["step"]=random.randint(int(values["size"]),int(values["size"])**2)
            image=CustomImage(int(values["size"]))
            image.bot1(int(values["step"]),int(values["seed"]))
            image.save(values["name"],int(values["seed"]),int(values["step"]))
    elif command.startswith("read"):
        values=parse(command,values={"name":None})
        if values["name"] is None:
            print("name is required")
        else:
            print(read_comment(f"generated/{values['name']}.png"))
    elif command=="exit":
        break
    else:
        print(f"unknown command: {command}")


