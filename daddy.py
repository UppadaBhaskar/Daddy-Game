import pygame
pygame.init()
#pygame.font.init()
screen=pygame.display.set_mode((1061,707))
title='DADDY'
start_sound=pygame.mixer.Sound('start.wav')
count1=-1
count2=-1
p=0
q=0
r=1011
s=0
d=0
a1=0
a2=0
z1=0
z2=0
e=1
f1=0 
alive_1=0
alive_2=0


#start page of the game
def home():
    def help():
        global start_sound
        pygame.display.set_caption(title)
        txt_font=pygame.font.Font('SwipeRaceDemo.ttf',50)
        txt_font1=pygame.font.Font('Aldrich-Regular.ttf',30)
        def info():           
            
            font_image1=txt_font.render('BACK',True,(255,255,255))
            screen.blit(font_image1,(380,433))
        def show_txt():
            font_image=txt_font.render('instructions',True,(0,255,255))
            screen.blit(font_image,(100,50))
            font_image=txt_font1.render('---> play with only alphabets and arrow keys',True,(0,255,255))
            screen.blit(font_image,(100,140))
            font_image=txt_font1.render('---> To insert a key in a position click the respective alphabet',True,(0,255,255))
            screen.blit(font_image,(100,170))
            font_image=txt_font1.render('---> To move a key first press the destination arrow key and ',True,(0,255,255))
            screen.blit(font_image,(100,200))

            font_image=txt_font1.render('       then press the coin to be moved',True,(0,255,255))
            screen.blit(font_image,(100,230))
            font_image=txt_font1.render('---> The player who remained with two coins will be looser',True,(0,255,255))
            screen.blit(font_image,(100,260))            
            font_image=txt_font1.render('       and other will be winner',True,(0,255,255))
            screen.blit(font_image,(100,290))

        game_on=True
        while game_on:
            screen.fill((0,0,0))
            screen.blit(bg,(0,0))
            info()
            show_txt()
            for event in pygame.event.get():
                if event.type==pygame.MOUSEBUTTONDOWN:
                    x,y=pygame.mouse.get_pos() 
                    if x>307 and x<754 and y>410 and y<488:
                        start_sound.play()
                        game_on=False
                                           
                if event.type==pygame.QUIT:
                    game_on=False
            pygame.display.update()


    def game():
        global start_sound,count1,count2,p,q,r,s,d,a1,a2,z1,z2,e,f1,alive_1,alive_2

        select_sound=pygame.mixer.Sound('drop.wav')
        transition_sound=pygame.mixer.Sound('fast transition.wav')

        #txt_font=pygame.font.Font('Aldrich-Regular.ttf', 32)
        txt_font=pygame.font.Font('Aldrich-Regular.ttf',32)
        txt_font1=pygame.font.Font('FontsFree-Net-EvilEmpire.ttf',32)

        # start sound
        

        #text font

        def show_alpha():
            for i in range(65,89):
                font_image=txt_font1.render(chr(i),True,(0,255,255))
                screen.blit(font_image,(X1[chr(i)],Y1[chr(i)]))
        def info():
            
            font_image=txt_font1.render('RESTART',True,(255,255,255))
            screen.blit(font_image,(24,560))
            font_image=txt_font1.render('BACK',True,(255,255,255))
            screen.blit(font_image,(24,611))

        def show_score1(x,y):
            global alive_1,alive_2
            font_image=txt_font.render('ALIVE | KILLS \n',True,(158,235,52))
            font_image1=txt_font.render(str(11-alive_1) + '     ' + str(alive_2),True,(158,235,52))
            screen.blit(font_image,(x,y))
            screen.blit(font_image1,(x+60,y+40))

        def show_score2(x,y):
            global alive_1,alive_2
            font_image=txt_font.render('ALIVE | KILLS \n',True,(0,50
            ,236))
            font_image1=txt_font.render( str(11-alive_2) + '      ' +  str(alive_1),False,(52,73,236))
            screen.blit(font_image,(x,y))
            screen.blit(font_image1,(x+60,y+40))
        #creating the coins
        coin1=[]
        coin2=[]
        record=[]
        selected=[]
        moved=[]

        s_r1=[[]] # sequence recording takes place in this record.
        s_r2=[[]]
        compare=[0,0]
        junk=0


        for i in range(12):
            coin1.append(pygame.image.load('g1.png'))
            coin2.append(pygame.image.load('g2.png'))


        #  DICTIONARY OF THE POSITIONS
        
        X={ "A":142, "B":505, "C":868, "D":263, "E":505, "F":747, "G":384, "H":505,
            "I":626, "J":142, "K":263, "L":384, "M":626, "N":747, "O":868,
            "P":384, "Q":505, "R":626, "S":263, "T":505, "U":747,
            "V":142, "W":505, "X":868,"Y":263,"Z":741
        }

        Y={ "A":133, "B":133, "C":133, "D":217, "E":217, "F":217, "G":301, "H":301,
            "I":301, "J":384, "K":384, "L":384, "M":384, "N":384, "O":384,
            "P":467, "Q":467, "R":467, "S":551, "T":551, "U":551,
            "V":635, "W":635, "X":635,"Y":15,"Z":15
        }

        #aplhabes positions
        X1={ "A":111, "B":480, "C":925, "D":232, "E":480, "F":802, "G":356, "H":520,
            "I":682, "J":111, "K":237, "L":356, "M":682, "N":802, "O":925,
            "P":356, "Q":480, "R":682, "S":237, "T":473, "U":802,
            "V":111, "W":520, "X":925
        }

        Y1={ "A":167, "B":167, "C":167, "D":258, "E":258, "F":258, "G":313, "H":354,
            "I":313, "J":422, "K":422, "L":422, "M":422, "N":422, "O":422,
            "P":504, "Q":504, "R":504, "S":591, "T":591, "U":591,
            "V":679, "W":679, "X":679
        }

        #  players changing coins position (Right,Left,Up,Down)
        c_p={
                "A":{  "R":"B" ,"L":"0","U":"0","D":"J"}, "B":{  "R":"C" ,"L":"A","U":"0","D":"E"}, "C":{  "R":"0" ,"L":"B","U":"0","D":"O"},
                "D":{  "R":"E" ,"L":"0","U":"0","D":"K"},  "E":{ "R":"F" ,"L":"D","U":"B","D":"H"}, "F":{  "R":"0" ,"L":"E","U":"0","D":"N"},
                "G":{  "R":"H" ,"L":"0","U":"0","D":"L"}, "H":{  "R":"I" ,"L":"G","U":"E","D":"0"}, "I":{  "R":"0" ,"L":"H","U":"0","D":"M"},
                "J":{  "R":"K" ,"L":"0","U":"A","D":"V"}, "K":{  "R":"L" ,"L":"J","U":"D","D":"S"}, "L":{  "R":"0" ,"L":"K","U":"G","D":"P"},
                "M":{  "R":"N" ,"L":"0","U":"I","D":"R"}, "N":{  "R":"O" ,"L":"M","U":"F","D":"U"}, "O":{  "R":"0" ,"L":"N","U":"C","D":"X"},
                "P":{  "R":"Q" ,"L":"0","U":"L","D":"0"}, "Q":{  "R":"R" ,"L":"P","U":"0","D":"T"}, "R":{  "R":"0" ,"L":"Q","U":"M","D":"0"},
                "S":{  "R":"T" ,"L":"0","U":"K","D":"0"}, "T":{  "R":"U" ,"L":"S","U":"Q","D":"W"}, "U":{  "R":"0" ,"L":"T","U":"N","D":"0"},
                "V":{  "R":"W" ,"L":"0","U":"J","D":"0"}, "W":{  "R":"X" ,"L":"V","U":"T","D":"0"}, "X":{  "R":"0" ,"L":"W","U":"O","D":"0"}

        }

        # list of sequenced coins

        k=[["A" ,"B", "C"], ["A" ,"J", "V"], ["V" ,"W", "X"], ["C" ,"O", "X"], ["D" ,"E", "F"], ["D" ,"K", "S"], ["S" ,"T", "U"], 
        ["F" ,"N", "U"], ["G" ,"H", "I"], ["G" ,"L", "P"], ["P" ,"Q", "R"], ["R" ,"M", "I"], ["J" ,"K", "L"],
        ["B" ,"E", "H"], ["M" ,"N", "O"], ["Q" ,"T", "W"] ]


        #coins images

        def player1(x,y):
            count1=1
            count2=1
            #if len(record)<=22:
            for i in range(len(record)):
                # here count tells how many times c1 and c2 has to blit
                x=X[record[i]]
                y=Y[record[i]]
                if count1<=12 and count2<=11:   #here if c2 false then at last coin1 doesnt blit
                    if i%2==0:
                        screen.blit(coin1[i//2],(x,y))
                        count1+=1
                    else:
                        
                        screen.blit(coin2[i//2],(x,y))
                        count2+=1
                else:
                    pass

        def check():
            global f1
            
            for i in range(len(k)):
                    
                    if k[i][0] in record and k[i][1] in record and k[i][2] in record and record.index(k[i][0])%2==0 and record.index(k[i][1])%2==0 and record.index(k[i][2])%2==0:
                        
                        if k[i] not in s_r1:
                            f1=1
                            
                        

                            
                    if k[i][0] in record and k[i][1] in record and k[i][2] in record and record.index(k[i][0])%2==1 and record.index(k[i][1])%2==1 and record.index(k[i][2])%2==1:   
                        
                        if k[i] not in s_r2:
                            f1=1
                        
                        
                            


        def kill(c):
            global a1,a2,z1,f1
            a1=a2
            z1=z2
            for i in range(len(k)):
                    
                    if k[i][0] in record and k[i][1] in record and k[i][2] in record and record.index(k[i][0])%2==0 and record.index(k[i][1])%2==0 and record.index(k[i][2])%2==0:
                        if k[i] in s_r1:
                            continue
                        elif k[i] not in s_r1:
                            s_r1.append(k[i])
                            a2+=1
                            
                            if len(record)==22:
                                z1+=1
                            
                            if c in record and record.index(c)%2==1:
                                record[record.index(c)]="Y"
                                f1=0
                            else:
                                s_r1.pop(-1)
                                a2-=1
                    if k[i][0] in record and k[i][1] in record and k[i][2] in record and record.index(k[i][0])%2==1 and record.index(k[i][1])%2==1 and record.index(k[i][2])%2==1:   
                        if k[i] in s_r2:
                            continue
                        elif k[i] not in s_r2:
                            s_r2.append(k[i])
                            a2+=1
                            
                            if len(record)==22:
                                z1+=1
                            
                            if c in record and record.index(c)%2==0:
                                record[record.index(c)]="Z"
                                f1=0
                            else:
                                s_r2.pop(-1)
                                a2-=1
                                                                


        def run():
                global select_sound
                for i in range(len(selected)):
                    x=i
                if len(moved)>0 and c_p[selected[x]][moved[x]]!="0" and c_p[selected[x]][moved[x]] not in record:#c_p here is the position to be empty
                    record[record.index(selected[x])]=c_p[selected[x]][moved[x]]
                    #select_sound.play()
                        
            
        # initializing x,y positions
        c1_x=1011
        c1_y=0

        #icon=pygame.image.load()
        #pygame.display.set_icon(icon)
        pygame.display.set_caption(title)

        #background image
        bg=pygame.image.load('bg.png')
        game_on=True
        while game_on:
            #print(selected,moved)
            #print(record)
            check()
            
            
            #print(compare)

            #print(s_r1 ,"\n",s_r2)
            #print(z1,z2)
            alive_2=record.count('Y')
            alive_1=record.count('Z')
            
            screen.fill((0,0,0))
            screen.blit(bg,(0,0))
            show_alpha()
            show_score1(20,3)
            show_score2(825,3)
            info()
            player1(c1_x,c1_y)
            
            for event in pygame.event.get():

                if event.type==pygame.QUIT:
                    game_on=False
                if event.type==pygame.MOUSEBUTTONDOWN:
                    x,y =pygame.mouse.get_pos()
                    if x>18 and x<131 and y>552 and y<592:
                        start_sound.play()
                        game()
                        return
                    elif x>19 and x<117 and y>606 and y<642:
                        start_sound.play()
                        game_on=False
                if event.type==pygame.KEYDOWN and len(selected)!=len(moved):
                    select_sound.play()
                    
                    if event.key==pygame.K_DOWN:
                        
                            moved[-1]="D"
                        
                    elif event.key==pygame.K_UP:
                            moved[-1]="U"
                        
                    elif event.key==pygame.K_RIGHT:
                            moved[-1]="R"
                        
                    elif event.key==pygame.K_LEFT:
                            moved[-1]="L"


                if event.type==pygame.KEYDOWN and len(selected)==len(moved):
                    select_sound.play()
                    

                    if event.key==pygame.K_DOWN:
                        
                            moved.append("D")
                        
                    elif event.key==pygame.K_UP:
                            moved.append("U")
                        
                    elif event.key==pygame.K_RIGHT:
                            moved.append("R")
                        
                    elif event.key==pygame.K_LEFT:
                            moved.append("L")
        
                if event.type==pygame.KEYUP:
                    
                    
                    if event.key==pygame.K_a:            
                            # here if A already in list then no input taken
                            # if coin selected then item not entered into the list and len(moved)>0 and moved[-1]!=
                        if "A" in record:
                            kill("A")
                            if z1==z2 and len(record)==22:
                                z2=z1
                                if e!=record.index("A")%2 and len(moved)>0 and moved[-1]!="U" and moved[-1]!="L"  and f1==0:
                                    e=record.index("A")%2
                                    selected.append("A")
                                if len(selected)==len(moved):
                                    run()
                                elif len(selected)>len(moved):
                                    selected.pop(-1)

                            a1=a2
                            continue
                        elif len(record)<=22 and a1==a2 and f1==0:
                            record.append("A")
                            if len(record)>22:
                                for i in range(22,len(record)):
                                    record.pop(i)
                            c1_x,c1_y=X["A"],Y["A"]
                        
                    elif event.key==pygame.K_b:
                        
                        if "B" in record:
                            kill("B")
                            if z1==z2 and len(record)==22:
                                z2=z1
                                if e!=record.index("B")%2 and len(moved)>0 and moved[-1]!="U"  and f1==0:
                                    e=record.index("B")%2
                                    selected.append("B")
                                
                                if len(selected)==len(moved):
                                    run()
                                elif len(selected)>len(moved):
                                    selected.pop(-1)
                            a1=a2
                            continue
                        elif len(record)<=22 and a1==a2 and f1==0:
                            record.append("B")
                            if len(record)>22:
                                for i in range(22,len(record)):
                                    record.pop(i)
                            c1_x,c1_y=X["B"],Y["B"]
                            
                                    
                    elif event.key==pygame.K_c:
                        
                        if "C" in record:
                            kill("C")
                            if z1==z2 and len(record)==22:
                                z2=z1
                                if e!=record.index("C")%2 and len(moved)>0 and moved[-1]!="U" and moved[-1]!="R"  and f1==0:
                                    e=record.index("C")%2
                                    selected.append("C")
                                
                                if len(selected)==len(moved):
                                    run()
                                elif len(selected)>len(moved):
                                    selected.pop(-1)
                            a1=a2
                            continue
                        elif len(record)<=22 and a1==a2 and f1==0:
                            record.append("C")
                            if len(record)>22:
                                for i in range(22,len(record)):
                                    record.pop(i)
                            c1_x,c1_y=X["C"],Y["C"]
                            
                                    
                    elif event.key==pygame.K_d:
                        
                        if "D" in record:
                            kill("D")
                            if z1==z2 and len(record)==22:
                                z2=z1
                                if e!=record.index("D")%2 and len(moved)>0 and moved[-1]!="L" and moved[-1]!="U"  and f1==0:
                                    e=record.index("D")%2
                                    selected.append("D")
                                
                                if len(selected)==len(moved):
                                    run()
                                elif len(selected)>len(moved):
                                    selected.pop(-1)
                            a1=a2
                            continue
                        elif len(record)<=22 and a1==a2 and f1==0:
                            record.append("D")
                            if len(record)>22:
                                for i in range(22,len(record)):
                                    record.pop(i)
                            c1_x,c1_y=X["D"],Y["D"]
                            

                    elif event.key==pygame.K_e:
                        if "E" in record:
                            kill("E")
                            if z1==z2 and len(record)==22:
                                z2=z1
                                if e!=record.index("E")%2 and len(moved)>0 and f1==0:
                                    e=record.index("E")%2
                                    selected.append("E")
                                
                                if len(selected)==len(moved):
                                    run()
                                elif len(selected)>len(moved):
                                    selected.pop(-1)
                            a1=a2
                            continue
                        elif len(record)<=22 and a1==a2 and f1==0:
                            record.append("E")
                            if len(record)>22:
                                for i in range(22,len(record)):
                                    record.pop(i)
                            c1_x,c1_y=X["E"],Y["E"]
                        
                    
                    elif event.key==pygame.K_f:
                        if "F" in record:
                            kill("F")
                            if z1==z2 and len(record)==22:
                                z2=z1
                                if e!=record.index("F")%2 and len(moved)>0 and moved[-1]!="R" and moved[-1]!="U"  and f1==0:
                                    e=record.index("F")%2
                                    selected.append("F")
                                
                                if len(selected)==len(moved):
                                    run()
                                elif len(selected)>len(moved):
                                    selected.pop(-1)
                            a1=a2
                            continue
                        elif len(record)<=22 and a1==a2 and f1==0:
                            record.append("F")

                            if len(record)>22:
                                for i in range(22,len(record)):
                                    record.pop(i)
                            c1_x,c1_y=X["F"],Y["F"]
                        
                    elif event.key==pygame.K_g:
                        if "G" in record:
                            kill("G")
                            if z1==z2 and len(record)==22:
                                z2=z1
                                if e!=record.index("G")%2 and len(moved)>0 and moved[-1]!="U" and moved[-1]!="L"  and f1==0:
                                    e=record.index("G")%2
                                    selected.append("G")
                                
                                if len(selected)==len(moved):
                                    run()
                                elif len(selected)>len(moved):
                                    selected.pop(-1)
                            a1=a2
                            continue
                        elif len(record)<=22 and a1==a2 and f1==0:
                            record.append("G")
                            if len(record)>22:
                                for i in range(22,len(record)):
                                    record.pop(i)
                            c1_x,c1_y=X["G"],Y["G"]
                        

                    elif event.key==pygame.K_h:
                        if "H" in record:
                            kill("H")
                            if z1==z2 and len(record)==22:
                                z2=z1
                                if e!=record.index("H")%2 and len(moved)>0 and moved[-1]!="D"  and f1==0:
                                    e=record.index("H")%2
                                    selected.append("H")
                                
                                if len(selected)==len(moved):
                                    run()
                                elif len(selected)>len(moved):
                                    selected.pop(-1)
                            a1=a2
                            continue
                        elif len(record)<=22 and a1==a2 and f1==0:
                            record.append("H")
                            if len(record)>22:
                                for i in range(22,len(record)):
                                    record.pop(i)
                            c1_x,c1_y=X["H"],Y["H"]
                        

                    elif event.key==pygame.K_i:
                        if "I" in record:
                            kill("I")
                            if z1==z2 and len(record)==22:
                                z2=z1
                                if e!=record.index("I")%2 and len(moved)>0 and moved[-1]!="R" and moved[-1]!="U"  and f1==0:
                                    e=record.index("I")%2
                                    selected.append("I")
                                
                                if len(selected)==len(moved):
                                    run()
                                elif len(selected)>len(moved):
                                    selected.pop(-1)
                            a1=a2
                            continue
                        elif len(record)<=22 and a1==a2 and f1==0:
                            record.append("I")
                            if len(record)>22:
                                for i in range(22,len(record)):
                                    record.pop(i)
                            c1_x,c1_y=X["I"],Y["I"]
                        

                    elif event.key==pygame.K_j:
                        if "J" in record:
                            kill("J")
                            if z1==z2 and len(record)==22:
                                z2=z1
                                if e!=record.index("J")%2 and len(moved)>0 and moved[-1]!="L"  and f1==0:
                                    e=record.index("J")%2
                                    selected.append("J")
                                
                                if len(selected)==len(moved):
                                    run()
                                elif len(selected)>len(moved):
                                    selected.pop(-1)
                            a1=a2
                            continue
                        elif len(record)<=22 and a1==a2 and f1==0:
                            record.append("J")
                            if len(record)>22:
                                for i in range(22,len(record)):
                                    record.pop(i)
                            c1_x,c1_y=X["J"],Y["J"]
                        

                    elif event.key==pygame.K_k:
                        if "K" in record:
                            kill("K")
                            if z1==z2 and len(record)==22:
                                z2=z1
                                if e!=record.index("K")%2  and len(moved)>0 and f1==0:
                                    e=record.index("K")%2
                                    selected.append("K")
                                
                                if len(selected)==len(moved):
                                    run()
                                elif len(selected)>len(moved):
                                    selected.pop(-1)
                                
                            a1=a2
                            continue
                        elif len(record)<=22 and a1==a2 and f1==0:
                            record.append("K")
                            if len(record)>22:
                                for i in range(22,len(record)):
                                    record.pop(i)
                            c1_x,c1_y=X["K"],Y["K"]
                        
                        
                    elif event.key==pygame.K_l:
                        if "L" in record:
                            kill("L")
                            if z1==z2 and len(record)==22:
                                z2=z1
                                if e!=record.index("L")%2 and len(moved)>0 and moved[-1]!="R"  and f1==0:
                                    e=record.index("L")%2
                                    selected.append("L")
                                
                                if len(selected)==len(moved):
                                    run()
                                elif len(selected)>len(moved):
                                    selected.pop(-1)
                            a1=a2
                            continue
                        elif len(record)<=22 and a1==a2 and f1==0:
                            record.append("L")
                            if len(record)>22:
                                for i in range(22,len(record)):
                                    record.pop(i)
                            c1_x,c1_y=X["L"],Y["L"]
                        

                    elif event.key==pygame.K_m:
                        if "M" in record:
                            kill("M")
                            if z1==z2 and len(record)==22:
                                z2=z1
                                if e!=record.index("M")%2 and len(moved)>0 and moved[-1]!="L"  and f1==0:
                                    e=record.index("M")%2
                                    selected.append("M")
                                
                                if len(selected)==len(moved):
                                    run()
                                elif len(selected)>len(moved):
                                    selected.pop(-1)
                            a1=a2
                            continue
                        elif len(record)<=22 and a1==a2 and f1==0:
                            record.append("M")

                            if len(record)>22:
                                for i in range(22,len(record)):
                                    record.pop(i)
                            c1_x,c1_y=X["M"],Y["M"]
                        
                    elif event.key==pygame.K_n:
                        if "N" in record:
                            kill("N")
                            if z1==z2 and len(record)==22:
                                z2=z1
                                if e!=record.index("N")%2 and len(moved)>0 and f1==0:
                                    e=record.index("N")%2
                                    selected.append("N")
                                
                                if len(selected)==len(moved):
                                    run()
                                elif len(selected)>len(moved):
                                    selected.pop(-1)
                            a1=a2
                            continue
                        elif len(record)<=22 and a1==a2 and f1==0:
                            record.append("N")
                            if len(record)>22:
                                for i in range(22,len(record)):
                                    record.pop(i)
                            c1_x,c1_y=X["N"],Y["N"]
                        

                    elif event.key==pygame.K_o:
                        if "O" in record:
                            kill("O")
                            if z1==z2 and len(record)==22:
                                z2=z1
                                if e!=record.index("O")%2 and len(moved)>0 and moved[-1]!="R"  and f1==0:
                                    e=record.index("O")%2
                                    selected.append("O")
                                
                                if len(selected)==len(moved):
                                    run()
                                elif len(selected)>len(moved):
                                    selected.pop(-1)
                            a1=a2
                            continue
                        elif len(record)<=22 and a1==a2 and f1==0:
                            record.append("O")
                            if len(record)>22:
                                for i in range(22,len(record)):
                                    record.pop(i)
                            c1_x,c1_y=X["O"],Y["O"]
                        

                    elif event.key==pygame.K_p:
                        if "P" in record:
                            kill("P")
                            if z1==z2 and len(record)==22:
                                z2=z1
                                if e!=record.index("P")%2 and len(moved)>0 and moved[-1]!="D" and moved[-1]!="L"  and f1==0:
                                    e=record.index("P")%2
                                    selected.append("P")
                                
                                if len(selected)==len(moved):
                                    run()
                                elif len(selected)>len(moved):
                                    selected.pop(-1)
                            a1=a2
                            continue
                        elif len(record)<=22 and a1==a2 and f1==0:
                            record.append("P")
                            if len(record)>22:
                                for i in range(22,len(record)):
                                    record.pop(i)
                            c1_x,c1_y=X["P"],Y["P"]
                        

                    elif event.key==pygame.K_q:
                        if "Q" in record:
                            kill("Q")
                            if z1==z2 and len(record)==22:
                                z2=z1
                                if e!=record.index("Q")%2 and len(moved)>0 and moved[-1]!="U"  and f1==0:
                                    e=record.index("Q")%2
                                    selected.append("Q")
                                
                                    
                                
                                if len(selected)==len(moved):
                                    run()
                                elif len(selected)>len(moved):
                                    selected.pop(-1)
                            a1=a2
                            continue
                        elif len(record)<=22 and a1==a2 and f1==0:
                            record.append("Q")
                            if len(record)>22:
                                for i in range(22,len(record)):
                                    record.pop(i)
                            c1_x,c1_y=X["Q"],Y["Q"]
                        
                    elif event.key==pygame.K_r:
                        if "R" in record:
                            kill("R")
                            if z1==z2 and len(record)==22:
                                z2=z1
                                if e!=record.index("R")%2 and len(moved)>0 and moved[-1]!="R" and moved[-1]!="D"  and f1==0:
                                    e=record.index("R")%2
                                    selected.append("R")
                                
                                if len(selected)==len(moved):
                                    run()
                                elif len(selected)>len(moved):
                                    selected.pop(-1)
                            a1=a2
                            continue
                        elif len(record)<=22 and a1==a2 and f1==0:
                            record.append("R")
                            if len(record)>22:
                                for i in range(22,len(record)):
                                    record.pop(i)
                            c1_x,c1_y=X["R"],Y["R"]
                        

                    elif event.key==pygame.K_s:
                        if "S" in record:
                            kill("S")
                            if z1==z2 and len(record)==22:
                                z2=z1
                                if e!=record.index("S")%2 and len(moved)>0 and moved[-1]!="L" and moved[-1]!="D"  and f1==0:
                                    e=record.index("S")%2
                                    selected.append("S")
                                
                                if len(selected)==len(moved):
                                    run()
                                elif len(selected)>len(moved):
                                    selected.pop(-1)
                            a1=a2
                            continue
                        elif len(record)<=22 and a1==a2 and f1==0:
                            record.append("S")
                            if len(record)>22:
                                for i in range(22,len(record)):
                                    record.pop(i)
                            c1_x,c1_y=X["S"],Y["S"]
                        

                    elif event.key==pygame.K_t:
                        if "T" in record:
                            kill("T")
                            if z1==z2 and len(record)==22:
                                z2=z1
                                if e!=record.index("T")%2 and len(moved)>0 and f1==0:
                                    e=record.index("T")%2
                                    selected.append("T")
                                
                                
                                if len(selected)==len(moved):
                                    run()
                                elif len(selected)>len(moved):
                                    selected.pop(-1)
                            a1=a2
                            continue
                        elif len(record)<=22 and a1==a2 and f1==0:
                            record.append("T")
                            if len(record)>22:
                                for i in range(22,len(record)):
                                    record.pop(i)
                            c1_x,c1_y=X["T"],Y["T"]
                        

                    elif event.key==pygame.K_u:
                        if "U" in record:
                            kill("U")
                            if z1==z2 and len(record)==22:
                                z2=z1
                                if e!=record.index("U")%2 and len(moved)>0 and moved[-1]!="D" and moved[-1]!="R"  and f1==0:
                                    e=record.index("U")%2
                                    selected.append("U")
                                
                                if len(selected)==len(moved):
                                    run()
                                elif len(selected)>len(moved):
                                    selected.pop(-1)
                            a1=a2
                            continue
                        elif len(record)<=22 and a1==a2 and f1==0:
                            record.append("U")

                            if len(record)>22:
                                for i in range(22,len(record)):
                                    record.pop(i)
                            c1_x,c1_y=X["U"],Y["U"]
                        
                    elif event.key==pygame.K_v:
                        if "V" in record:
                                kill("V")
                                if z1==z2 and len(record)==22:
                                    z2=z1
                                    if e!=record.index("V")%2 and len(moved)>0 and moved[-1]!="L" and moved[-1]!="D" and f1==0:
                                        e=record.index("V")%2
                                        selected.append("V")

                                    if len(selected)==len(moved):
                                        run()
                                    elif len(selected)>len(moved):
                                        selected.pop(-1)
                                a1=a2
                                continue
                        elif len(record)<=22 and a1==a2 and f1==0:
                            record.append("V")
                            if len(record)>22:
                                for i in range(22,len(record)):
                                    record.pop(i)
                            c1_x,c1_y=X["V"],Y["V"]
                        

                    elif event.key==pygame.K_w:
                        if "W" in record:
                            kill("W")
                            if z1==z2 and len(record)==22:
                                z2=z1
                                if e!=record.index("W")%2 and len(moved)>0 and moved[-1]!="D"  and f1==0:
                                    e=record.index("W")%2
                                    selected.append("W")
                                
                                if len(selected)==len(moved):
                                    run()
                                elif len(selected)>len(moved):
                                    selected.pop(-1)
                            a1=a2
                            continue
                        elif len(record)<=22 and a1==a2 and f1==0:
                            record.append("W")

                            if len(record)>22:
                                for i in range(22,len(record)):
                                    record.pop(i)
                            c1_x,c1_y=X["W"],Y["W"]
                        
                    elif event.key==pygame.K_x:
                        if "X" in record:
                            kill("X")
                            if z1==z2 and len(record)==22:
                                z2=z1
                                if e!=record.index("X")%2 and len(moved)>0 and moved[-1]!="D" and moved[-1]!="R"  and f1==0:
                                    e=record.index("X")%2
                                    selected.append("X")
                                
                                if len(selected)==len(moved):
                                    run()
                                elif len(selected)>len(moved):
                                    selected.pop(-1)
                            a1=a2
                            continue
                        elif len(record)<=22 and a1==a2 and f1==0:
                            record.append("X")
                            if len(record)>22:
                                for i in range(22,len(record)):
                                    record.pop(i)
                            c1_x,c1_y=X["X"],Y["X"]
            pygame.display.update()



    bg=pygame.image.load('bgs.png')
    
    txt_font1=pygame.font.Font('SwipeRaceDemo.ttf',100)
    txt_font=pygame.font.Font('SwipeRaceDemo.ttf',50)
    txt_font2=pygame.font.Font('SwipeRaceDemo.ttf',35)
    #music loading
    pygame.mixer.music.load('bgm.mpeg')
    pygame.mixer.music.play(-1)

    #text font

    def show_daddy():
        font_image=txt_font1.render('DADDY',True,(187,255,0))
        screen.blit(font_image,(180,150))
        font_image1=txt_font.render('START',True,(255,255,255))
        screen.blit(font_image1,(325,433))
        #(307, 410),(754, 488)
        font_image1=txt_font2.render('QUIT',True,(255,255,255))
        screen.blit(font_image1,(110,628))
        #(86, 605),(324, 665)
        font_image1=txt_font2.render('HELP',True,(255,255,255))
        screen.blit(font_image1,(760,628))
        #(736, 612),(1007, 671)
    pygame.display.set_caption(title)
    game_on=True
    while game_on:
        screen.fill((255,255,255))
        screen.blit(bg,(0,0))
        show_daddy()
        for event in pygame.event.get():
            if event.type==pygame.MOUSEBUTTONDOWN:
                x,y=pygame.mouse.get_pos()
                if x>307 and x<754 and y>410 and y<488:
                    start_sound.play()
                    game()
                elif x>86 and x<324 and y>605 and y<665:
                    start_sound.play()
                    game_on=False
                elif x>736 and x<1007 and y>612 and y<671:
                    start_sound.play()
                    help()
            if event.type==pygame.QUIT:
                game_on=False
        pygame.display.update()

home()
