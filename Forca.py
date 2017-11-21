import os
import random

words3 = ['sob', 'vil', 'fel', 'ceu', 'mal', 'ver', 'ser', 'reu', 'paz', 'ego', 'rol', 'bom', 'dia', 'elo', 'daí', 'tal', 'mau', 'luz', 'voo', 'era', 'fiz', 'lua', 'rua', 'ato', 'ler', 'lei', 'dor', 'rio', 'uma', 'nau', 'bau', 'eco', 'sol', 'voz', 'boi', 'pau', 'sal', 'rei', 'via', 'véu', 'pai', 'van', 'asa', 'som', 'ovo']
words4 = ['fato','amor','esmo','apto','área','ermo','mito','suma','sede','mote','veio','crer','ruim','tolo','soar','ente','gozo','cedo','meio','pose','puta','cela','numa','sela','coxo','vide','urge','asco','fase','vida','alva','medo','caos','cota','face','rege','alvo','ocio','agir','zelo','base','sina','como','onde','rude','cujo','você','prol','nojo','teor','joia','auto','alta','jugo','nexo','casa','traz','agil','deus','auge','idem','ater','vale','doce','mais','tudo','seio','todo','voga','mero','alto','pneu','frio','novo','rito','algo','amar','vovo','orla','lume','tese','dote','item']
words5 = ['algoz','sagaz','mexer','senso','afeto','sutil','cerne','inato','termo','audaz','nobre','vigor','porra','fazer','ideia','lapso','genro','posse','negro','poder','torpe','honra','ardil','anexo','atroz','expor','gleba','justo','muito','sanar','digno','tenaz','corja','cozer','pleno','prole','moral','comum','dever','nenem','fugaz','censo','gesto','causa','afago','brado','ontem','fluir','louco','impor','serio','tenro','vivaz','cisma','denso','seara','enfim','pudor','regra','culto','saber','favor','sinto']
words6 = ['exceto','indole','vereda','inocuo','mister','infame','merito','anseio','apogeu','afavel','pressa','nocivo','idoneo','cinico','facçao','jubilo','escopo','aferir','adorno','apreço','casual','hostil','paixao','alheio','isento','eficaz','enfase','astuto','receio','ludico','abster','ciente','legado','formal','dadiva','difuso','escusa','idiota','gentil','comico','habito','ocioso','dispor','ensejo','extase','utopia','solene','perene','impeto','maroto','alento','duvida','eximir','sançao','lirico','avidez','outrem','alçada','julgar','decoro','lograr','alocar','cortes','otario','coagir','vedado','inerte','sisudo','tacito','acento','cobiça','danado','rancor','prover','remoto','sobrio','etereo','objeto','agonia','buscar','vulgar','inepto']
words7 = ['embuste','exceçao','conjuge','prolixo','empatia','efemero','sublime','analogo','cinismo','recesso','genuino','prodigo','sucinto','audacia','refutar','astucia','inferir','carater','cordial','emergir','isençao','excesso','imputar','apatico','litigio','conciso','ambiguo','trivial','parcial','aspecto','fríiolo','austero','incauto','estirpe','escoria','padecer','auferir','candura','fomento','inercia','oriundo','sintese','sensato','morbido','preciso','despota','alegria','exilado','mitigar','ansioso','ambiçao','ademais','neofito','intuito','hesitar','deleite','certeza','volupia','notorio','virtude','aptidao','alcunha','escasso','sentido','indagar','espurio','vigente','familia','assento','limpido','soberba','verbete','volatil','bizarro','intenso','replica']
words8 = ['inerente','peculiar','denegrir','invasivo','deferido','iminente','reiterar','equidade','essencia','eminente','inserçao','ardiloso','prudente','modestia','desgraça','ascensao','proceder','respeito','alienado','complexo','abstrato','vigoroso','apologia','resoluto','presteza','empirico','escrever','primazia','distinto','conceito','alicerce','respaldo','premissa','analogia','singular','metodico','veridico','abstrair','criterio','expedido','retorica','conserto','relativo','escarnio','elegivel','mediocre','devaneio','instigar','pleitear','vocabulo','consiste','destarte','contenda','despeito','fomentar','repudiar','extravio','sufragio','historia','espectro','suprimir','impavido','conceder','misogino','processo','profícuo','abnegado','inospito','custodia','sinônimo']
words9 = ['reciproco','impressao','retificar','concepçao','concessao','plenitude','essencial','escrupulo','presunçao','resignado','deliberar','superfluo','ratificar','implicito','paradigma','corolario','desdenhar','persuadir','demasiado','hegemonia','hermetico','autentico','adjacente','propósito','indelevel','companhia','hipócrita','instancia','dicotomia','exequivel','interesse','autóctone','leniencia','taciturno','discriçao','constante','irascivel','resoluçao','impetuoso','compaixao','empecilho','preambulo','supressao','inusitado','vagabundo','regozijar','diligente','descriçao','jactancia','pretensao','analitico','pressagio','explicito','eminencia','prudencia','sapiencia','excelente','excedente','individuo','suplantar','arcabouço','mesquinho','discorrer','restriçao','fidedigno','reciproca','magnanimo','estagnado','aquisiçao','limitrofe','altruismo','sintetico','esperança','diferença','expressao','inaudivel','confiança','convicçao','incidente','probidade','plausivel','esdruxulo','convergir','magnifico','intrepido','enfadonho','precursor','contençao','entediado','ludibriar','indolente','relevante','renunciar','sancionar','obstinado','arraigado','moribundo']


lists = [words3, words4, words5, words6, words7, words8, words9]

word = random.choice(random.choice(lists))
board = []
size_board = len(word)
for x in range(0, size_board):
    board.append("_")
errors = []



os.system('mode con: cols=70 lines=30')

print ("Bem vindo ao jogo da Forca!")
print ()

for turn in range(15):
    print ("Turno", turn + 1)
    print ()
    if len(errors) == 0:
        print ("    _____")
        print ("    |   |")
        print ("    |")
        print ("    |")
        print ("    |")
        print ("    |")
        print ("   -----")
        print ("")
    if len(errors) == 1:
        print ("    _____")
        print ("    |   |")
        print ("    |   O")
        print ("    |")
        print ("    |")
        print ("    |")
        print ("   -----")
        print ("")
    if len(errors) == 2:
        print ("    _____")
        print ("    |   |")
        print ("    |   O")
        print ("    |   I")
        print ("    |")
        print ("    |")
        print ("   -----")
        print ("")
    if len(errors) == 3:
        print ("    _____")
        print ("    |   |")
        print ("    |   O")
        print ("    |  /I")
        print ("    |")
        print ("    |")
        print ("   -----")
        print ("")
    if len(errors) == 4:
        print ("    _____")
        print ("    |   |")
        print ("    |   O")
        print ("    |  /I\ ")
        print ("    |")
        print ("    |")
        print ("   -----")
        print ("")
    if len(errors) == 5:
        print ("    _____")
        print ("    |   |")
        print ("    |   O")
        print ("    |  /I\ ")
        print ("    |  /")
        print ("    |")
        print ("   -----")
        print ("")


    
    print ("")

    while True:
        guess_letter = input("Escolha uma letra: ")
        if len(guess_letter) == 1:
            if guess_letter.isalpha():
                if guess_letter not in board:
                    if guess_letter not in errors:
                        break
                    else:
                        print ("Cara, putis grila, só pode ser um peixe desmiolado...")
                else:
                    print ("Cara, putis grila, essa letra já foi... tu tá querendo foder?")        
            else:
                print ("Cara, coloca apenas uma letra!")           
        else:
            print ("Cara, coloca apenas uma letra!")                     
    
               
        
    if guess_letter == word[0]:
        os.system('cls')
        print ("Boa!")
        print ("")
        board[0] = word[0]              
    if guess_letter == word[1]:
        os.system('cls')
        print ("Boa!")
        print ("")
        board[1] = word[1]
    if guess_letter == word[2]:
        os.system('cls')
        print ("Boa!")
        print ("")
        board[2] = word[2]
    if len(word) >= 4:
        if guess_letter == word[3]:
            os.system('cls')
            print ("Boa!")
            print ("")
            board[3] = word[3]
    if len(word) >= 5:
        if guess_letter == word[4]:
            os.system('cls')
            print ("Boa!")
            print ("")
            board[4] = word[4]
    if len(word) >= 6:
        if guess_letter == word[5]:
            os.system('cls')
            print ("Boa!")
            print ("")
            board[5] = word[5]
    if len(word) >= 7:
        if guess_letter == word[6]:
            os.system('cls')
            print ("Boa!")
            print ("")
            board[6] = word[6]
    if len(word) >= 8:
        if guess_letter == word[7]:
            os.system('cls')
            print ("Boa!")
            print ("")
            board[7] = word[7]
    if len(word) >= 9:
        if guess_letter == word[8]:
            os.system('cls')
            print ("Boa!")
            print ("")
            board[8] = word[8]
    
        
    if guess_letter not in word:
        os.system('cls')
        print ("Eeeeeeerrrou!")
        print ()
        errors.append(guess_letter)
            
    if word == str.join('',board):
        print ("A palavra era: " + word)
        print ()
        print ("    _____")
        print ("    |   |")
        print ("    |         O" )
        print ("    |        /I\ ")
        print ("    |        / \ ")
        print ("    |")
        print ("   -----")
        print ("")
        print ("Parabéns!! Tu chitou?")
        venceu = input("Aperte enter para encerrar")
        break
    
    if (len(errors) == 6):
        os.system('cls')
        print ("Perdeu! Poxa, tu foi enforcado, como pode bem observar...")
        print ("Mais sorte  na proxima vida")
        print ("    _____")
        print ("    |   |")
        print ("    |   O", "    X X")
        print ("    |  /I\ ", "  ---")
        print ("    |  / \ ")
        print ("    |")
        print ("   -----")
        print ("")
        print ("A palavra era " + word)
        print ()

        end = input("Aperte enter para encerrar")
        break
            
    print ("Palavra:")
    print (*board)
    print ("")
    print ("Erros:")
    print (*errors)
    print ("")

