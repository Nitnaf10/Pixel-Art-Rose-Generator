import random
import sys
import argparse
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

def main():
    parser = argparse.ArgumentParser(description='Generate symmetric maze images')
    subparsers = parser.add_subparsers(dest='command', required=True, help='Commands')
    
    # Save command
    save_parser = subparsers.add_parser('save', help='Save a generated image')
    save_parser.add_argument('name', help='Name of the image file')
    save_parser.add_argument('--seed', type=int, help='Random seed')
    save_parser.add_argument('--size', type=int, help='Size parameter (creates 2*size+1 image)')
    save_parser.add_argument('--step', type=int, help='Number of steps')
    
    # Read command
    read_parser = subparsers.add_parser('read', help='Read metadata from an image')
    read_parser.add_argument('name', help='Name of the image file')
    
    # Help command
    help_parser = subparsers.add_parser('help', help='Show help message')
    
    args = parser.parse_args()
    
    if args.command == 'save':
        if args.seed is None:
            args.seed = random.getrandbits(32)
        if args.size is None:
            args.size = random.randint(10, 110)
        if args.step is None:
            args.step = random.randint(args.size, args.size**2)
        
        print(f"Generating with seed={args.seed}, size={args.size}, step={args.step}")
        image = CustomImage(args.size)
        image.bot1(args.step, args.seed)
        image.save(args.name, args.seed, args.step)
        print(f"Image saved as generated/{args.name}.png")
        
    elif args.command == 'read':
        print(read_comment(f"generated/{args.name}.png"))
        
    elif args.command == 'help':
        parser.print_help()

if __name__ == "__main__":
    main()
