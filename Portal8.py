from time import time
cvf=0
Portal=2
import os
import binascii
namez = input("ul or for compress cl for extract for compress zst cld fo extract zst cldd? ")
#@Author Jurijus pacalovas
class compression:
    def cryptograpy_compression(self):
               
                self.name = "Written: Jurijus pacalovas Price Protal 5 000 000 Euro cost Date: 13/08/2021 17: 25 Deep 14.5 ERA"
                if namez=="ul":
                    corridors=0
                    cor=7
                    name = input("What is name of file? ")
                    namea="file.W"
                    namem=""
                    namema="?"
                    Portal=2
                    assxw=0
                    blockw=5
                    blockw1=4
                    nameas=name
                    nac=len(nameas)
                    if nameas[nac-5:nac]==".docx":
                    	Portal=1
                    if nameas[nac-4:nac]==".pdf":
                    	Portal=3
                    if nameas[nac-4:nac]==".doc":
                    	Portal=1
                    if nameas[nac-4:nac]==".png":
                    	Portal=7

                    	
                    nameas=name+".bin"
                    
                    
                    
                    
                    
                    nac=len(nameas)
                    
                    countraz=0
                    cvf=2
                    cvf1=0
                    s=""
                    e2=0
                    e3=2
                    e4=""
                    c=2
                    sw=2
                    elw=0
                 
                    sda3=""
                    sda2=""

                    sscvf=0
                    
                    qqqqwzl=0

                    block=1

                    x=0
                    x1=0
                    x2=0
                    x = time()

                    with open(nameas, "w") as f4:
                            f4.write(s)
                    with open(nameas, "a") as f3:
                            f3.write(s)
                    with open(name, "rb") as binary_file:

                       # Read the whole file at once
                        data = binary_file.read()
                        if Portal==7 and data[0:41]!=b'\x89\x50\x4e\x47\x0d\x0a\x1a\x0a\x00\x00\x00\x0d\x49\x48\x44\x52\x00\x00\x04\x38\x00\x00\x09\x24\x08\x02\x00\x00\x00\x76\xb1\x58\xf8\x00\x00\x00\x01\x73\x52\x47\x42':

                         	print("Sorry, this incorect format of file. Please, change format back.")
                         	raise SystemExit
                        if Portal==7 and data[0:41]==b'\x89\x50\x4e\x47\x0d\x0a\x1a\x0a\x00\x00\x00\x0d\x49\x48\x44\x52\x00\x00\x04\x38\x00\x00\x09\x24\x08\x02\x00\x00\x00\x76\xb1\x58\xf8\x00\x00\x00\x01\x73\x52\x47\x42':     
                        	data=data[41:]
                        	

                        s=str(data)
                       
                        lenf1=len(data)
                        lenf5=len(data)
                        
                        assx=0
                        qqqwz=0
                       
                        while assx<10:
                       
                            aas1=0
                            a1=0

                            cvf=cvf+1
                            
                            countraz=countraz+1

                            with open(nameas, "ab") as f2:
                                if countraz==1:
                                    sda=bin(int(binascii.hexlify(data),16))[2:]
                                    lenf=len(sda)
                                    lenf1=len(data)
                                
                                    xc=(lenf1*8)-lenf
                                    z=0
                                    if xc!=0:
                                        while z<xc:
                                            sda="0"+sda
                                            z=z+1
                                            
                                    sda=sda+sda2

                                    if countraz==1:
                                        sda2=sda
                            
                                    n = int(sda2, 2)
                                
                                    qqwslenf=len(sda2)
                                    qqwslenf=(qqwslenf/8)*2
                                    qqwslenf=str(qqwslenf)
                                    qqwslenf="%0"+qqwslenf+"x"
                             
                                    jl=binascii.unhexlify(qqwslenf % n)
                                    sssssw=len(jl)
                                    
                                    data=jl
                                    qqqwz=qqqwz+1
                                   
                                    if countraz==1:

                                        lenf5=len(data)

                                    sda=bin(int(binascii.hexlify(data),16))[2:]
                                    lenf=len(sda)

                                    lenf1=len(data)
                                
                                    xc=(lenf1*8)-lenf
                                    z=0
                                    if xc!=0:
                                        while z<xc:
                                            sda="0"+sda
                                            z=z+1

                                    sda2=sda

                                    lenf3=len(sda2)
                                lenf2=len(sda2)  
                                                
                                e4=sda2[e2:e3]
                                
                                block=block+1

                                if Portal==3:
	                                corridors=corridors+1%257
	                                
	                                if block<=corridors:
	                                    if e4=="0":
	                                        sda3=sda3+"0"
	                                        e4="0"
	                                        block=corridors
	                                        e4=""
	                                        
	                                    if e4=="1":
	                                        sda3=sda3+"1"
	                                        e4="1"
	                                        block=7
	                                        e4=""
	
	                                if block>=corridors:
	                                    if e4=="1":
	                                        sda3=sda3+"0"
	                                        e4="0"
	                                        block=0
	                                        e4=""
	                                        
	                                    if e4=="0":
	                                        sda3=sda3+"1"
	                                        e4="1"
	                                        block=0
	                                        e4=""
	                                        
	                                if block<=6:
	                                    if e4=="0":
	                                        sda3=sda3+"1"
	                                        e4="1"
	                                        block=7
	                                        e4=""
	                                       
	                                    if e4=="1":
	                                        sda3=sda3+"0"
	                                        e4="0"
	                                        block=7
	                                        e4=""
	                                             
	                                if block==corridors:
	                                    if e4=="1":
	                                        sda3=sda3+"0"
	                                        e4="0"
	                                        block=corridors
	                                        e4=""
	                                                 
	                                if e4=="0":
	                                        sda3=sda3+"1"
	                                        e4="1"
	                                        block=0
	                                        e4=""    
                                
                                if Portal==2 or Portal==7:
                                	corridors=corridors+1%257
                                
	                                if block<=3:
	                                    if e4=="0":
	                                        sda3=sda3+"0"
	                                        e4="0"
	                                        block=corridors
	                                        e4=""
	                                        
	                                    if e4=="1":
	                                        sda3=sda3+"1"
	                                        e4="1"
	                                        block=7
	                                        e4=""
	
	                                if block>=8:
	                                    if e4=="1":
	                                        sda3=sda3+"0"
	                                        e4="0"
	                                        block=0
	                                        e4=""
	                                        
	                                    if e4=="0":
	                                        sda3=sda3+"1"
	                                        e4="1"
	                                        block=0
	                                        e4=""
	                                        
	                                if block<=6:
	                                    if e4=="0":
	                                        sda3=sda3+"1"
	                                        e4="1"
	                                        block=7
	                                        e4=""
	                                       
	                                    if e4=="1":
	                                        sda3=sda3+"0"
	                                        e4="0"
	                                        block=7
	                                        e4=""
	                                             
	                                if block==7:
	                                    if e4=="1":
	                                        sda3=sda3+"0"
	                                        e4="0"
	                                        block=0
	                                        e4=""
	                                                 
	                                if e4=="0":
	                                        sda3=sda3+"1"
	                                        e4="1"
	                                        block=0
	                                        e4=""     
	                                	
	                                
                                if Portal==1:
                                 
                                     corridors=corridors+1%8
                                     if block==corridors%3:
                                         if e4=="0":
                                         	sda3=sda3+"0"
                                         	e4="0"
                                         	block=0
                                         	e4=""
                                         	
                                         if e4=="1":
                                         	sda3=sda3+"1"
                                         	e4="1"
                                         	block=0
                                         	e4=""
                                     if block>=corridors%8:
                                         if e4=="1":
                                         	sda3=sda3+"0"
                                         	e4="0"
                                         	
                                         	e4=""
                                         	
                                         if e4=="0":
                                             sda3=sda3+"1"
                                             e4="1"
                                             
                                             e4=""
                                     if block<=corridors%6 and block>3:
                                         if e4=="0":
                                         	sda3=sda3+"1"
                                         	e4="1"
                                         	
                                         	e4=""
                                         	
                                         if e4=="1":
                                         	sda3=sda3+"0"
                                         	e4="0"
                                         	
                                         	e4=""
                                     if block==corridors%7:
                                         if e4=="1":
                                         	sda3=sda3+"0"
                                         	e4="0"
                                         	e4=""
                                     if e4=="0":
                                         sda3=sda3+"1"
                                         e4="1"
                                         
                                         e4=""   
	                                                  
                                e2=e2+1
                                e3=e3+1

                                e4=""
                          
                                if e3==cvf:
                                    e2=0
                                    e3=1
                                    
                                    cvf=cvf+1

                                    cvf=sw
                                    sw=sw+1
                             
                                if cvf==lenf5*8+4:
                                    sw=sw+2
                                    cvf=c
                                    cvf1=cvf1+1
                                     
                                    c=c+2

                                if cvf1==1:
                                   
                                    n = int(sda3, 2)
                                
                                    qqwslenf=len(sda3)
                                    qqwslenf=(qqwslenf/8)*2
                                    qqwslenf=str(qqwslenf)
                                    qqwslenf="%0"+qqwslenf+"x"
                             
                                    jl=binascii.unhexlify(qqwslenf % n)
                                    sssssw=len(jl)
                                    data=jl
                                    qqqwz=qqqwz+1
                                    szxzzza=""
                                    szxzs=""
                            
                                    assxw=assxw+1
                                    if assxw==1:
                                        assx=10
                                        if assx==10:
                                        	
                                            f2.write(jl)
                                            x2 = time()
                                            x3=x2-x
                                            return print(x3)
           
    def cryptograpy_unpack(self):                      
                 if namez=="cl":
                    corridors=0
                    cor=7
                    name = input("What is name of file? ")
                    Portal=2
                    namea="file.W"
                    namem=""
                    namema="?"
                 
                    assxw=0
                    blockw=5
                    blockw1=4
                    nameas=name
                    nac=len(nameas)
                    nameas=name[:nac-4]
                    nac=len(nameas)
                    if nameas[nac-5:nac]==".docx":
                    	Portal=1
                    if nameas[nac-4:nac]==".pdf":
                    	Portal=3
                    if nameas[nac-4:nac]==".doc":
                    	Portal=1
                    if nameas[nac-4:nac]==".png":
                    	Portal=7
                    
                    
                    countraz=0
                    cvf=2
                    cvf1=0
                    s=""
                    e2=0
                    e3=2
                    e4=""
                    c=2
                    sw=2
                    elw=0
                 
                    sda3=""
                    sda2=""

                    sscvf=0
                    
                    qqqqwzl=0

                    block=1

                    x=0
                    x1=0
                    x2=0
                    x = time()

                    with open(nameas, "w") as f4:
                            f4.write(s)
                    with open(nameas, "a") as f3:
                            f3.write(s)
                    with open(name, "rb") as binary_file:

                        # Read the whole file at once
                        data = binary_file.read()
                        
                        s=str(data)
                        
                        lenf1=len(data)
                        lenf5=len(data)
                        
                        assx=0
                        qqqwz=0
                       
                        while assx<10:
                       
                            aas1=0
                            a1=0

                            cvf=cvf+1
                            
                            countraz=countraz+1

                            with open(nameas, "ab") as f2:
                                if countraz==1:
                                    sda=bin(int(binascii.hexlify(data),16))[2:]
                                    lenf=len(sda)
                                    lenf1=len(data)
                                
                                    xc=(lenf1*8)-lenf
                                    z=0
                                    if xc!=0:
                                        while z<xc:
                                            sda="0"+sda
                                            z=z+1
                                            
                                    sda=sda+sda2

                                    if countraz==1:
                                        sda2=sda
                            
                                    n = int(sda2, 2)
                                
                                    qqwslenf=len(sda2)
                                    qqwslenf=(qqwslenf/8)*2
                                    qqwslenf=str(qqwslenf)
                                    qqwslenf="%0"+qqwslenf+"x"
                             
                                    jl=binascii.unhexlify(qqwslenf % n)
                                    sssssw=len(jl)
                                    
                                    data=jl
                                    qqqwz=qqqwz+1
                                   
                                    if countraz==1:

                                        lenf5=len(data)

                                    sda=bin(int(binascii.hexlify(data),16))[2:]
                                    lenf=len(sda)

                                    lenf1=len(data)
                                
                                    xc=(lenf1*8)-lenf
                                    z=0
                                    if xc!=0:
                                        while z<xc:
                                            sda="0"+sda
                                            z=z+1

                                    sda2=sda

                                    lenf3=len(sda2)
                                lenf2=len(sda2)  
                                                
                                e4=sda2[e2:e3]
                                
                                block=block+1

                                if Portal==3:
	                                corridors=corridors+1%257
	                                
	                                if block<=corridors:
	                                    if e4=="0":
	                                        sda3=sda3+"0"
	                                        e4="0"
	                                        block=corridors
	                                        e4=""
	                                        
	                                    if e4=="1":
	                                        sda3=sda3+"1"
	                                        e4="1"
	                                        block=7
	                                        e4=""
	
	                                if block>=corridors:
	                                    if e4=="1":
	                                        sda3=sda3+"0"
	                                        e4="0"
	                                        block=0
	                                        e4=""
	                                        
	                                    if e4=="0":
	                                        sda3=sda3+"1"
	                                        e4="1"
	                                        block=0
	                                        e4=""
	                                        
	                                if block<=6:
	                                    if e4=="0":
	                                        sda3=sda3+"1"
	                                        e4="1"
	                                        block=7
	                                        e4=""
	                                       
	                                    if e4=="1":
	                                        sda3=sda3+"0"
	                                        e4="0"
	                                        block=7
	                                        e4=""
	                                             
	                                if block==corridors:
	                                    if e4=="1":
	                                        sda3=sda3+"0"
	                                        e4="0"
	                                        block=corridors
	                                        e4=""
	                                                 
	                                if e4=="0":
	                                        sda3=sda3+"1"
	                                        e4="1"
	                                        block=0
	                                        e4=""    
                                if Portal==2 or Portal==7:
                                	corridors=corridors+1%257
                                
	                                if block<=3:
	                                    if e4=="0":
	                                        sda3=sda3+"0"
	                                        e4="0"
	                                        block=corridors
	                                        e4=""
	                                        
	                                    if e4=="1":
	                                        sda3=sda3+"1"
	                                        e4="1"
	                                        block=7
	                                        e4=""
	
	                                if block>=8:
	                                    if e4=="1":
	                                        sda3=sda3+"0"
	                                        e4="0"
	                                        block=0
	                                        e4=""
	                                        
	                                    if e4=="0":
	                                        sda3=sda3+"1"
	                                        e4="1"
	                                        block=0
	                                        e4=""
	                                        
	                                if block<=6:
	                                    if e4=="0":
	                                        sda3=sda3+"1"
	                                        e4="1"
	                                        block=7
	                                        e4=""
	                                       
	                                    if e4=="1":
	                                        sda3=sda3+"0"
	                                        e4="0"
	                                        block=7
	                                        e4=""
	                                             
	                                if block==7:
	                                    if e4=="1":
	                                        sda3=sda3+"0"
	                                        e4="0"
	                                        block=0
	                                        e4=""
	                                                 
	                                if e4=="0":
	                                        sda3=sda3+"1"
	                                        e4="1"
	                                        block=0
	                                        e4=""     
                                	
                                
                                if Portal==1:
                                     
                                     corridors=corridors+1%8
                                     if block==corridors%3:
                                         if e4=="0":
                                         	sda3=sda3+"0"
                                         	e4="0"
                                         	block=0
                                         	e4=""
                                         	
                                         if e4=="1":
                                         	sda3=sda3+"1"
                                         	e4="1"
                                         	block=0
                                         	e4=""
                                     if block>=corridors%8:
                                         if e4=="1":
                                         	sda3=sda3+"0"
                                         	e4="0"
                                         	
                                         	e4=""
                                         	
                                         if e4=="0":
                                             sda3=sda3+"1"
                                             e4="1"
                                             
                                             e4=""
                                     if block<=corridors%6 and block>3:
                                         if e4=="0":
                                         	sda3=sda3+"1"
                                         	e4="1"
                                         	
                                         	e4=""
                                         	
                                         if e4=="1":
                                         	sda3=sda3+"0"
                                         	e4="0"
                                         	
                                         	e4=""
                                     if block==corridors%7:
                                         if e4=="1":
                                         	sda3=sda3+"0"
                                         	e4="0"
                                         	e4=""
                                     if e4=="0":
                                         sda3=sda3+"1"
                                         e4="1"
                                         
                                         e4=""  
                                 
                                     


                                e2=e2+1
                                e3=e3+1

                                e4=""
                          
                                if e3==cvf:
                                    e2=0
                                    e3=1
                                    
                                    cvf=cvf+1

                                    cvf=sw
                                    sw=sw+1
                             
                                if cvf==lenf5*8+4:
                                    sw=sw+2
                                    cvf=c
                                    cvf1=cvf1+1
                                     
                                    c=c+2

                                if cvf1==1:
                                    
                                    n = int(sda3, 2)
                                
                                    qqwslenf=len(sda3)
                                    qqwslenf=(qqwslenf/8)*2
                                    qqwslenf=str(qqwslenf)
                                    qqwslenf="%0"+qqwslenf+"x"
                             
                                    jl=binascii.unhexlify(qqwslenf % n)
                                    sssssw=len(jl)
                                    data=jl
                                    if Portal==7:                               	jl=b'\x89\x50\x4e\x47\x0d\x0a\x1a\x0a\x00\x00\x00\x0d\x49\x48\x44\x52\x00\x00\x04\x38\x00\x00\x09\x24\x08\x02\x00\x00\x00\x76\xb1\x58\xf8\x00\x00\x00\x01\x73\x52\x47\x42' +jl
                                    qqqwz=qqqwz+1
                                    szxzzza=""
                                    szxzs=""
                            
                                    assxw=assxw+1
                                    if assxw==1:
                                        assx=10
                                        if assx==10:
                                           
                                            f2.write(jl)
                                            x2 = time()
                                            x3=x2-x
                                            return print(x3)
                 
    def cryptograpy(self):
                if namez=="cld":
                    name = input("What is name of file? ")
                    namea="file.W"
                    namem=""
                    namema="?"
                    Portal=2
                    assxw=0
                    blockw=5
                    blockw1=4
                    nameas=name
                    nac=len(nameas)
                    if nameas[nac-8:nac]==".jpg.bin":
                    	Portal=4
                    if nameas[nac-8:nac]==".png.bin":
                    	Portal=4
                    if nameas[nac-4:nac]==".jpg":
                    	Portal=4
                    if nameas[nac-4:nac]==".png":
                    	Portal=4
                    nameas=name+".bin.bin"
                        
                    countraz=0
                    cvf=2
                    cvf1=0
                    s=""
                    e2=0
                    e3=2
                    e4=""
                    c=2
                    sw=2
                    elw=0
                   
                    sda3=""

                    sscvf=0
                    
                    qqqqwzl=0

                    block=0

                    x=0
                    x1=0
                    x2=0
                    x = time()
                   
                    with open(nameas, "w") as f4:
                            f4.write(s)
                    with open(nameas, "a") as f3:
                            f3.write(s)
                    with open(name, "rb") as binary_file:
                        # Read the whole file at once
                        data = binary_file.read()
                        lenf10=len(data)
                   
                        if Portal==4:
                        	import brotli
                        	data=brotli.compress(data)
                        
                        else:	
                            import zstandard
                            data=zstandard.compress(data)
                        s=str(data)
                        lenf1=len(data)
                        lenf5=len(data)
               
                        
                        with open(nameas, "ab") as f2:
                            assx=10
                            if assx==10:
                                
                                f2.write(data)
                                x2 = time()
                                x3=x2-x
                                return print(x3)
                                
    def cryptograpy_unpack2(self):
                if namez=="cldd":
                    name = input("What is name of file? ")
                    namea="file.W"
                    namem=""
                    namema="?"
                    Portal=2
                    assxw=0
                    blockw=5
                    blockw1=4
                    nameas=name
                    nac=len(nameas)
                    nameas=nameas[:nac-8]
                    nac=len(nameas)
                    if nameas[nac-8:nac]==".jpg.bin":
                    	Portal=4
                    if nameas[nac-8:nac]==".png.bin":
                    	Portal=4
                    if nameas[nac-4:nac]==".jpg":
                    	Portal=4
                    if nameas[nac-4:nac]==".png":
                    	Portal=4
                        
                    countraz=0
                    cvf=2
                    cvf1=0
                    s=""
                    e2=0
                    e3=2
                    e4=""
                    c=2
                    sw=2
                    elw=0
                   
                    sda3=""

                    sscvf=0
                    
                    qqqqwzl=0

                    block=0

                    x=0
                    x1=0
                    x2=0
                    x = time()
                   
                    with open(nameas, "w") as f4:
                            f4.write(s)
                    with open(nameas, "a") as f3:
                            f3.write(s)
                    with open(name, "rb") as binary_file:
                        # Read the whole file at once
                        data = binary_file.read()
                        lenf10=len(data)
                       
                        
                        if Portal==4:
                        	import brotli
                        	data=brotli.decompress(data)
                        if Portal==5:	
                            import zstandard
                            data=zstandard.decompress(data)
                   
                        
                        
                        s=str(data)
                        lenf1=len(data)
                        lenf5=len(data)
                
                        with open(nameas, "ab") as f2:
                            assx=10
                            if assx==10:
                                
                                f2.write(data)
                                x2 = time()
                                x3=x2-x
                                return print(x3) 
                                
    def cryptograpy3(self):
                if namez=="cld3":
                    name = input("What is name of file? ")
                    namea="file.W"
                    namem=""
                    namema="?"
                    Portal=5
                    assxw=0
                    blockw=5
                    blockw1=4
                    nameas=name
                    nac=len(nameas)             
                    if nameas[nac-16:nac]==".jpg.bin.bin.bin":
                    	Portal=2
                    if nameas[nac-16:nac]==".png.bin.bin.bin":
                    	Portal=2
                    if nameas[nac-12:nac]==".jpg.bin.bin":
                    	Portal=2
                    if nameas[nac-12:nac]==".png.bin.bin":
                    	Portal=4
                    nac=len(nameas)
                    nameas=name+".bin.bin.bin"
                    
                    countraz=0
                    cvf=2
                    cvf1=0
                    s=""
                    e2=0
                    e3=2
                    e4=""
                    c=2
                    sw=2
                    elw=0
                   
                    sda3=""

                    sscvf=0
                    
                    qqqqwzl=0

                    block=0

                    x=0
                    x1=0
                    x2=0
                    x = time()
                   
                    with open(nameas, "w") as f4:
                            f4.write(s)
                    with open(nameas, "a") as f3:
                            f3.write(s)
                    with open(name, "rb") as binary_file:
                        # Read the whole file at once
                        data = binary_file.read()
                        if Portal==4 and data[0:4]!=b'\ab\x26\e8\x0d' :
                        	print("Program close because this is it finish to compress bofore.")
                        	raise SystemExit
                        if Portal==4 and data[0:4]==b'\ab\x26\e8\x0d' :             
                        	data=data[4:]
                        	
                        if  data [0:4] == b'\x28\xb5\x2f\xfd' and Portal==5:
                            data=data[4:]                         
                        if Portal == 2:
                        	print("Program close because this is it finish to compress bofore.")
                        	raise SystemExit

                        
                        
                        s=str(data)
                        lenf1=len(data)
                        lenf5=len(data)
             
                        
                        with open(nameas, "ab") as f2:
                            assx=10
                            if assx==10:
                                f2.write(data)
                                x2 = time()
                                x3=x2-x
                                return print(x3)      
 
    def cryptograpy_unpack3(self):
                if namez=="cldd3":
                    name = input("What is name of file? ")
                    namea="file.W"
                    namem=""
                    namema="?"
                    
                    Portal=5
                    assxw=0
                    blockw=5
                    blockw1=4
                    nameas=name
                    nac=len(nameas)
                    nameas=name[:nac-12]
                    if nameas[nac-16:nac]==".jpg.bin.bin.bin":
                    	Portal=2
                    if nameas[nac-16:nac]==".png.bin.bin.bin":
                    	Portal=2
                    if nameas[nac-12:nac]==".jpg.bin.bin":
                    	Portal=2
                    if nameas[nac-12:nac]==".png.bin.bin":
                    	Portal=4    
                    countraz=0
                    cvf=2
                    cvf1=0
                    s=""
                    e2=0
                    e3=2
                    e4=""
                    c=2
                    sw=2
                    elw=0
                   
                    sda3=""

                    sscvf=0
                    
                    qqqqwzl=0

                    block=0

                    x=0
                    x1=0
                    x2=0
                    x = time()
                   
                    with open(nameas, "w") as f4:
                            f4.write(s)
                    with open(nameas, "a") as f3:
                            f3.write(s)
                    with open(name, "rb") as binary_file:
                        # Read the whole file at once
                        data = binary_file.read()
                        if Portal==4:
              	
                           data= b'\ab\x26\e8\x0d'+data
                        if Portal==5:
                        	data = b'\x28\xb5\x2f\xfd'+data   
                        if Portal == 2:
                        	print("Program close because you did incorrect fings.")
                        s=str(data)
                        lenf1=len(data)
                        lenf5=len(data)
    
                        
                        with open(nameas, "ab") as f2:
                            assx=10
                            if assx==10:
                                
                                f2.write(data)
                                x2 = time()
                                x3=x2-x
                                return print(x3)                       

           

d=compression()

xw=d.cryptograpy_compression()
print(xw)

xw1=d.cryptograpy_unpack()
print(xw1)

xw2=d.cryptograpy()
print(xw2)

xw3=d.cryptograpy_unpack2()
print(xw3)

xw4=d.cryptograpy_unpack3()
print(xw4)


xw5=d.cryptograpy3()
print(xw5)
