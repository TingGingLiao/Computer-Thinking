#組員:廖挺均，黃鑫凱，郭星暘，陳霆維，張宗棨
##分工內容:
##if topic=='B':
        #print(name,'動畫嗎?我也很喜歡看動畫呢!!讓我們來討論吧')        
        #while True:
            #c = input('你喜歡怎樣的動畫呢,A.熱血燃系 B.恐怖驚悚 C.懸疑推理  L.結束')
            #if c=='A':
                #c111=print(name,'讓我為你推薦一些動畫吧!請抽取你今天適合看的動畫!')
                #while True:
                    #c1=input('請從ABC隨機選一個輸入,若要離開請輸入L:')
                    #if c1=='A':
                        #c11=print(name,'我覺得今天你適合看鬼滅之刃!!水之呼吸 拾之型 生生流轉!')
                        #break
                    #if c1=='B':
                        #c11=print(name,'看來今天適合看火影忍者呢! 穢土轉生!' )
                        #break
                    #if c1=='C':
                        #c11=print(name, '我覺得今天適合看ONE PIECE呢!一起去海上冒險吧')
                        #break
                    #if c1=='L':
                        #c11=print('希望有機會再聊')
                        #break
                    #if c1!='A' and c1!='B' and c1!='C'and c1!='L':
                        #h11=print('你只有ABC三個可以抽或者選擇L離開!!請不要超過範圍!!')
                    #if c11=='你只有ABC三個可以抽!!請不要超過範圍!!':
                        #continue                    
                
            #if c=='B':
                #c222=print(name,'恐怖啊!我倒是有些想法呢!你要參考嗎?')
                #while True:
                    #c2=input('請從ABC隨機選一個輸入,若要離開請輸入L:')
                    #if c2=='A':
                        #c22=print(name,'你是否怨恨一個人呢?希望他早點下地獄!那我們就來看 地獄少女 吧')
                        #break
                    #if c2=='B':
                        #c11=print(name,'在古代的時候!總是有著許多奇奇怪怪的事情發生!就讓我們在 怪化貓 中一探究竟!')
                        #break
                    #if c2=='C':
                        #c22=print(name, '那些傳聞就是真是假呢!? 就讓我們進入 寒蟬鳴泣之時 徹底了解一下吧!')
                        #break
                    #if c2=='L':
                        #c22=print(name,'希望有機會再聊')
                        #break
                    #if c2!='A' and c2!='B' and c2!='C'and c2!='L':
                        #c22=print('你只有ABC三個籤可以抽!!請不要超過範圍!!')
                    #if c22=='你只有ABC三個籤可以抽!!請不要超過範圍!!':
                        #continue
                        
                
            #if c=='C':
                #c333=print(name,'懸疑推理阿!總是讓人回味無窮呢!我這裡有幾個推薦的唷!')
                #while True:
                    #c3=input('請從ABC隨機選一個輸入,若要離開請輸入L:')
                    #if c3=='A':
                       #c33=print(name,'首先想到的當然就是!外表看似小男孩!內心卻是!!!!的 名偵探柯南!!!')
                        #break
                    #if c3=='B':
                        #c33=print(name,'聽說逆轉裁判也是很不錯唷!我小時候還玩過這個動畫的電腦遊戲呢!')
                       #break
                    #if c3=='C':
                       #c33=print(name, '啄木鳥偵探社!聽起來很有趣吧!趕快去看看!!')
                       #break
                    #if c3=='L':
                       #c33=print(name,'希望有機會再聊')
                       #break
                    #if c3!='A' and c3!='B' and c3!='C'and c3!='L':
                        #c33=print('你只有ABC三個籤可以抽!!請不要超過範圍!!')
                    #if c33=='你只有ABC三個籤可以抽!!請不要超過範圍!!':
                        #continue                   
                                
            #if c=='L':
                #xl=print(name,'希望有機會再聊')
                #break 
###角本:剛入大學的新鮮人，對於一切都還不熟悉，所以製造出的對話機器人。裡面有四種功能，分別是
###如果興情不好可以選擇心情，它會讓你紓解陰霾。
###若喜歡動漫，則可以選擇動漫，來跟機器人聊自己喜歡的動漫類型
###想早日在大學生活中盡早交到朋友或想抱怨成績不順利，則可以選擇學業社交。
###喜歡占卜的人也可以選擇占卜，裡面有四種占卜可以選擇，挑選一個來測近日運勢吧
####程式碼
print('嗨. 我是鴟鴞 是一個聊天機器人')
print('我喜歡聊各種話題')
name = input('可以告訴我，你的名字嗎: ')
print('你好', name, ', 很高興認識你')
year = input('我存在太久了，已經忘記現在是幾年了，你可以跟我說現在是西元幾年嗎?: ')
print('我想我知道了 ')
myage = input('你可以猜到我幾歲嗎? 猜猜看:')
myage=int(myage)+30;
print('其實我今年已經 ',myage,'歲')
nyears = 10000 - myage
print('再過', nyears, '年我就滿10000歲了')
print('到時候就是西元', int(year) + nyears,'年')
while True:
    topic=input('你想要聊甚麼呢?請輸入英文代號ABCD,A.心情 B.動畫 C.學業社交 D.占卜 L.結束聊天')
    if topic=='A':    
        print(name,'既然你想聊心情那我們就來談談你現在如何吧?')        
        while True:
            h = input('你現在感覺如何?,A.快樂 B.難過 C.生氣 D.平淡 L.結束')
            if h=='A':
                h111=print(name,'你開心我也很開心，希望你每天都能開開心心,我們來抽取一個開心的祝福吧!')
                while True:
                    h1=input('請從ABC隨機選一個輸入,若要離開請輸入L:')
                    if h1=='A':
                        h11=print(name,'有你的同行；我倍感安全；有你的鼓勵；我充滿力量；有你的思念；我深感幸福；願我最好的朋友開心每一秒；快樂每一天！')
                        break
                    if h1=='B':
                        h11=print(name,'祝你時時開心天天快樂，願你從此戰無不勝攻無不克，一切煩惱見你就後撤，不管在哪你都是最幸福的一個，所有美好的囑咐都是我對你最真誠的祝賀!')
                        break
                    if h1=='C':
                        h11=print(name, '歲月匆匆，願我的祝福常駐你心中；一句平安，代表了我所有的心願.')
                        break
                    if h1=='L':
                        h11=print('希望有機會再聊')
                        break
                    if h1!='A' and h1!='B' and h1!='C'and h1!='L':
                        h11=print('你只有ABC三個籤可以抽或者選擇L離開!!請不要超過範圍!!')
                    if h11=='你只有ABC三個籤可以抽!!請不要超過範圍!!':
                        continue                     
                
            if h=='B':
                h222=print(name,'是遇到了甚麼難過的事情呢?或許我這幾句話能讓你好點。')
                while True:
                    h2=input('請從ABC隨機選一個輸入,若要離開請輸入L:')
                    if h2=='A':
                        h22=print(name,'時間總會過去的，讓時間流走你的煩惱吧!')
                        break
                    if h2=='B':
                        h11=print(name,'不要害怕做錯什麼，即使錯了，也不必懊惱，人生就是對對錯錯，何況有許多事，回頭看來，對錯已經無所謂了。')
                        break
                    if h2=='C':
                        h22=print(name, '能夠把自己壓得低低的，那才是真正的尊貴。')
                        break
                    if h2=='L':
                        h22=print(name,'希望有機會再聊')
                        break
                    if h2!='A' and h2!='B' and h2!='C'and h2!='L':
                        h22=print('你只有ABC三個型態可以選!!請不要超過範圍!!')
                    if h22=='你只有ABC三個型態可以選!!請不要超過範圍!!':
                        continue                    
                
            if h=='C':
                h333=print(name,'生氣了嗎?是發生甚麼讓你不高興的事情呢?沒關係!讓我來安撫你的情緒吧!')
                while True:
                    h3=input('請從ABC隨機選一個輸入,若要離開請輸入L:')
                    if h3=='A':
                        h33=print(name,'朋友是會默默在身邊支持你的，如果遇到瞭不順心的事情就回頭看看，你會發現還有我從始至終都在陪伴著你。快樂起來吧！')
                        break
                    if h3=='B':
                        h33=print(name,'不要在你心情不好或者憤怒的時候做決定，因為這樣的決定永遠是錯的。')
                        break
                    if h3=='C':
                        h33=print(name, '我能感覺到你的心痛，你有你說不出的無奈，但是你做出一副無所謂的樣子，你越是這樣我就越難受。')
                        break
                    if h3=='L':
                        h33=print(name,'希望有機會再聊')
                        break
                    if h3!='A' and h3!='B' and h3!='C'and h3!='L':
                        h33=print('你只有ABC三個可以選!!請不要超過範圍!!')
                    if h33=='你只有ABC三個可以選!!請不要超過範圍!!':
                        continue                    
                
            if h=='D':
                h444=print(name,'平淡的日子也讓人羨慕不是嗎?我還是有幾句話可以給你唷~')
                while True:
                    h4=input('請從ABC隨機選一個輸入,若要離開請輸入L:')
                    if h4=='A':
                        h44=print(name,'用一個平平淡淡的心去看這個世界，你就會發現美無處不在，看似平淡的生活是如此的絢麗多彩！')
                        break
                    if h4=='B':
                        h44=print(name,'世間萬物都是平平淡淡中的。小草是平平淡淡的，它用自己輕柔小的生命，鋪就了綠色天涯；水流是平平淡淡的，它堅持不懈，能把頑石擊得百孔千瘡')
                        break
                    if h4=='C':
                        h44=print(name, '我們害怕歲月，卻不知道活著是多麼的可喜')
                        break
                    if h4=='L':
                        h44=print(name,'希望有機會再聊')
                        break
                    if h4!='A' and h4!='B' and h4!='C'and h4!='L':
                        h44=print('你只有ABC三個可以抽!!請不要超過範圍!!')                        
                    if h44=='你只有ABC三個可以抽!!請不要超過範圍!!':
                        continue                    
                
            if h=='L':
                hl=print(name,'希望有機會再聊')
                break       
               
        
        
    if topic=='B':
        print(name,'動畫嗎?我也很喜歡看動畫呢!!讓我們來討論吧')        
        while True:
            c = input('你喜歡怎樣的動畫呢,A.熱血燃系 B.恐怖驚悚 C.懸疑推理  L.結束')
            if c=='A':
                c111=print(name,'讓我為你推薦一些動畫吧!請抽取你今天適合看的動畫!')
                while True:
                    c1=input('請從ABC隨機選一個輸入,若要離開請輸入L:')
                    if c1=='A':
                        c11=print(name,'我覺得今天你適合看鬼滅之刃!!水之呼吸 拾之型 生生流轉!')
                        break
                    if c1=='B':
                        c11=print(name,'看來今天適合看火影忍者呢! 穢土轉生!' )
                        break
                    if c1=='C':
                        c11=print(name, '我覺得今天適合看ONE PIECE呢!一起去海上冒險吧')
                        break
                    if c1=='L':
                        c11=print('希望有機會再聊')
                        break
                    if c1!='A' and c1!='B' and c1!='C'and c1!='L':
                        h11=print('你只有ABC三個可以抽或者選擇L離開!!請不要超過範圍!!')
                    if c11=='你只有ABC三個可以抽!!請不要超過範圍!!':
                        continue                    
                
            if c=='B':
                c222=print(name,'恐怖啊!我倒是有些想法呢!你要參考嗎?')
                while True:
                    c2=input('請從ABC隨機選一個輸入,若要離開請輸入L:')
                    if c2=='A':
                        c22=print(name,'你是否怨恨一個人呢?希望他早點下地獄!那我們就來看 地獄少女 吧')
                        break
                    if c2=='B':
                        c11=print(name,'在古代的時候!總是有著許多奇奇怪怪的事情發生!就讓我們在 怪化貓 中一探究竟!')
                        break
                    if c2=='C':
                        c22=print(name, '那些傳聞就是真是假呢!? 就讓我們進入 寒蟬鳴泣之時 徹底了解一下吧!')
                        break
                    if c2=='L':
                        c22=print(name,'希望有機會再聊')
                        break
                    if c2!='A' and c2!='B' and c2!='C'and c2!='L':
                        c22=print('你只有ABC三個籤可以抽!!請不要超過範圍!!')
                    if c22=='你只有ABC三個籤可以抽!!請不要超過範圍!!':
                        continue
                        
                
            if c=='C':
                c333=print(name,'懸疑推理阿!總是讓人回味無窮呢!我這裡有幾個推薦的唷!')
                while True:
                    c3=input('請從ABC隨機選一個輸入,若要離開請輸入L:')
                    if c3=='A':
                        c33=print(name,'首先想到的當然就是!外表看似小男孩!內心卻是!!!!的 名偵探柯南!!!')
                        break
                    if c3=='B':
                        c33=print(name,'聽說逆轉裁判也是很不錯唷!我小時候還玩過這個動畫的電腦遊戲呢!')
                        break
                    if c3=='C':
                        c33=print(name, '啄木鳥偵探社!聽起來很有趣吧!趕快去看看!!')
                        break
                    if c3=='L':
                        c33=print(name,'希望有機會再聊')
                        break
                    if c3!='A' and c3!='B' and c3!='C'and c3!='L':
                        c33=print('你只有ABC三個籤可以抽!!請不要超過範圍!!')
                    if c33=='你只有ABC三個籤可以抽!!請不要超過範圍!!':
                        continue                   
                                
            if c=='L':
                xl=print(name,'希望有機會再聊')
                break 
        
    if topic=='C':
        print(name,'學業社交上遇到甚麼困難了嗎?都可以跟我聊聊唷!')        
        while True:
            x = input('學業社交出現甚麼問題?,A.新環境不適應 B.沒朋友 C.成績很爛  L.結束')
            if x=='A':
                x111=print(name,'新環境不適應嗎?那我們看看這些方法能不能解決問題!')
                while True:
                    x1=input('請從ABC隨機選一個輸入,若要離開請輸入L:')
                    if x1=='A':
                        x11=print(name,'鼓起勇氣去認識新的人事物，當你認識了新朋友!就會慢慢改善問題了!')
                        break
                    if x1=='B':
                        x11=print(name,'有時候你只是害怕未知的事物，等你熟悉了，就會適應了')
                        break
                    if x1=='C':
                        x11=print(name, '不要害怕!勇於在新環境中發掘更多的新事物吧!或許會很有收穫呢!')
                        break
                    if x1=='L':
                        x11=print('希望有機會再聊')
                        break
                    if x1!='A' and x1!='B' and x1!='C'and x1!='L':
                        x11=print('你只有ABC三個可以抽或者選擇L離開!!請不要超過範圍!!')
                    if x11=='你只有ABC三個可以抽!!請不要超過範圍!!':
                        continue                    
                
            if x=='B':
                x222=print(name,'朋友嗎?沒事的!我們來看看有甚麼好的建議吧!')
                while True:
                    x2=input('請從ABC隨機選一個輸入,若要離開請輸入L:')
                    if x2=='A':
                        x22=print(name,'或許你只要勇敢地邁向一步!就可以認識新朋友囉!給自己一個勇氣吧!!')
                        break
                    if x2=='B':
                        x11=print(name,'朋友有時候不用太多，但要有幾個是真心相交的!')
                        break
                    if x2=='C':
                        x22=print(name, '不用擔心!說不定其他人也很想認識你呢!所以不要害怕!')
                        break
                    if x2=='L':
                        x22=print(name,'希望有機會再聊')
                        break
                    if x2!='A' and x2!='B' and x2!='C'and x2!='L':
                        x22=print('你只有ABC三個可以抽!!請不要超過範圍!!')
                    if x22=='你只有ABC三個可以抽!!請不要超過範圍!!':
                        continue                    
                
            if x=='C':
                x333=print(name,'擔心成績嗎!沒事的!我們一起來找問題吧')
                while True:
                    x3=input('請從ABC隨機選一個輸入,若要離開請輸入L:')
                    if x3=='A':
                        h33=print(name,'有時候只是自己念書的方法用錯了!換一個方法試試看吧!')
                        break
                    if x3=='B':
                        x33=print(name,'如果發現自己都念不懂!那你可能需要去尋求外在的幫助!有時候別人更容易將你的疑惑解開呢!')
                        break
                    if x3=='C':
                        x33=print(name, '現在成績不好!可能只是你的努力尚未發揮成效!說不定之後你的成績就會大成長呢!')
                        break
                    if x3=='L':
                        x33=print(name,'希望有機會再聊')
                        break
                    if x3!='A' and x3!='B' and x3!='C'and x3!='L':
                        x33=print('你只有ABC三個籤可以抽!!請不要超過範圍!!')
                    if x33=='你只有ABC三個籤可以抽!!請不要超過範圍!!':
                        continue                    
                
            
            if x=='L':
                xl=print(name,'希望有機會再聊')
                break 
    if topic=='D':
        print(name,'喔~原來你想要占卜你的命運嗎!')        
        while True:
            z = input('請選擇你想要的方式!,A.卜卦 B.籤筒 C.塔羅牌  L.結束')
            if z=='A':
                z111=print(name,'原來你想要卜卦阿!我們就來卜卦吧')
                while True:
                    z1=input('請從ABC隨機選一個輸入,若要離開請輸入L:')
                    if z1=='A':
                        z11=print(name,'卜卦結果是!是火上地下的晉卦呢!看來將會有進步唷!')
                        break
                    if z1=='B':
                        z11=print(name,'卜卦結果是!是上雷下火的豐卦呢!看來將會所豐收唷!')
                        break
                    if z1=='C':
                        z11=print(name,'卜卦結果是!是上火下山的旅卦呢!看來將會有事情需要多加探索唷!')
                        break
                    if z1=='L':
                        z11=print('希望有機會再聊')
                        break
                    if z1!='A' and z1!='B' and z1!='C'and z1!='L':
                        z11=print('你只有ABC三個可以抽或者選擇L離開!!請不要超過範圍!!')
                    if z11=='你只有ABC三個可以抽!!請不要超過範圍!!':
                        continue                    
                
            if z=='B':
                z222=print(name,'籤筒阿!那我只負責抽唷!解籤的話請你自己上網查囉~')
                while True:
                    z2=input('請從ABC隨機選一個輸入,若要離開請輸入L:')
                    if z2=='A':
                        z22=print(name,'第四十四吉，盤中黑白子，一著要先機，天龍降甘澤，洗出舊根基')
                        break
                    if z2=='B':
                        z11=print(name,'第六十六凶，水滯少波濤，飛鴻落羽毛，重憂心緒亂，閑事惹風騷')
                        break
                    if z2=='C':
                        z22=print(name, '第三十四吉，臘木春將至，芳菲喜再新，鯤鯨興巨浪，舉鉤祿為真')
                        break
                    if z2=='L':
                        z22=print(name,'希望有機會再聊')
                        break
                    if z2!='A' and z2!='B' and z2!='C'and z2!='L':
                        z22=print('你只有ABC三個籤可以抽!!請不要超過範圍!!')
                    if z22=='你只有ABC三個籤可以抽!!請不要超過範圍!!':
                        continue                    
                
            if z=='C':
                z333=print(name,'塔羅牌嗎!那就請你在心裡默想吧!抽到後可以上網查詢意思唷')
                while True:
                    z3=input('請從ABC隨機選一個輸入,若要離開請輸入L:')
                    if z3=='A':
                        z33=print(name,'劍八正，這代表甚麼呢?')
                        break
                    if z3=='B':
                        h33=print(name,'杯一正，這代表甚麼呢?')
                        break
                    if z3=='C':
                        h33=print(name,'杖五正，這又代表甚麼呢?')
                        break
                    if z3=='L':
                        h33=print(name,'希望有機會再聊')
                        break
                    if z3!='A' and z3!='B' and z3!='C'and z3!='L':
                        h33=print('你只有ABC三張牌可以抽!!請不要超過範圍!!')
                    if z33=='你只有ABC三張牌可以抽!!請不要超過範圍!!':
                        continue       
                       
                
               
            if z=='L':
                z5l=print(name,'希望有機會再聊')
                break
    if topic=='L':
        q44=print(name,'很高興能與你聊天，希望你有美好的一天，再見!')
        break