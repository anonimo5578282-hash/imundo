import time
import os
import sys

os.system("clear")
logs = ["""                                    
                          #@                                   +              .- -==   :::   .:-:  .  .:::::. +%#                           
                        - :                              *:   .. *%%-  .*.=*.:+ + --  .=.*  .-.      .:--::.:-- . %                         
                      @*                         * +.%  :  *.=. :  =.  :+ :.  :*  +  *-    :-**     .:::::-------- -##                      
                    =*+.                       :+**%.   +  +       *.  :-  * : = -=*=   -  +  :+  ..:::.----------:.  @                     
                 @++-:                    @*  -  : +=*   +. :    :+    ** +-: =- --   :==%  .* -   .  :.:::-----------:=##                  
                +--.    ...             ==+   .%+ . ..   *   -@@:        +=+:   %@   :-* : :.  @    ..  :::::::---+-++-+  #                 
               +-:        .::..       :.:-:+-   .  %++                             :   *. **  :-+       ....:::---+++++++-:##               
             %+-:             .@@=+::*   : -==: %                                       :- @= +%.+@ -%%=+: .:.:---++++++++ . =              
           ##%+-:.            +     :#@=* + .                                            .. :-+*@+  +*     ...::---+++++-+---  ##           
          *****+++--::.      .=      .   ***                                                :::. *+%+ .=%   . :-::-+--++++++++  ##          
         #@=+--------:..      *      @*.                                                         -++#=@-::-   . .---:-+++++*+++: ##         
        ****+++++---:::.       .#=@=.==:                       .                               .::::+++**       .::---++++++++++. %#        
      =##=****+++-::...             -.                    -=#=   ..   ......                    ..:--:-:: *      ::..-+++++++**+++ =#@      
      #%=******+-::.              %-.           ..         .:%#%           .......       ...      ...::. %       ....--+*++++****** -#      
     ====*****++--:.            %+:.     .@#@%*:             .:##%.              ...    . *-  .     ..               :-+++********** =@     
    %====*****++--:           =+:.    ##*--:.                  -@#%*:               ...    -***%    ..  .. *          :--+++++****+++-@#    
   @#%=======**+--.           +:.  #%                          =+-:             .     ..    :--++*#*    .:--#::+*===.  :--++********+:.##   
  *%=========**+--.          =-: :#+.     -*+.             . %@.                  ..    .     .--+:  @   :-++=          .:--++********- #   
  #@%%%====*++-.            %+-.:@%=+ .@@=-:              -%@:    -:++++++++++++++*       ..:+-:.    ::@  :-++#           .:--++*******+@#  
 =%%%========**+-:         =*-. +%*:@#*:.                                                    .-+**=:::==   :-++    .: .:--++***********+ #  
 ###@@%%===**++-      :   =%+ @=##%*:.. ::                                          .           .: #%+-#*    .-++-::+=   .:-++****=******## 
 @@%%%%%%%%==*++-   @%-+*+*--#@+   .:+=%*                                .                   .. :.:-+*===@@  .:.. :-+**=%#.--+***===****:-# 
*..======***++-.###=*-    @*+@=*-  @#=+-                          .-:--+     .                 :--+-.::--**%  +*%.        .:-++**********+##
=#@@@@@@@%%==*+:        *=*-+@@=.#@*-..                        -+:  -@+  :-+.      ...          .-+*=% .:+**-.-+**:       :-++**=========+@#
=#@@@@@@%%%=*-::.     :=- :..%+#*+-:.:++.    .       :  .: .-*=@.   -#+   .==*:.-:.              .:-+*@::+*=  .#        ...:--+***=======-%%
@%%%%%=****+--.    %@=+ ..+=@#**--  =%:.             -*+%%%%@##*.   . .    +=@%%@*+*=-         :::---+++#**#..:*@           :-+++*******+-.#
+  +%%%%%%==*+-##%%=*::.. @     :.*#%-              =@@@@####@=+.  ..#.    -*%###@@@#@           .+*-.-+**%@- .+*=.        :-+***=======**-#
 *@####@@%%=*+-          -@*#=-+-#@=+:  .          +@#######@%== . ::#:  . +*=%########          .-++%:-++*+##:-+**.       :-+**==========+#
@######@@%%=*+-           %-#@@=#=+-: .%.  .       @#########@@=-: .-#+  .:*==**#######        :.  .-*%-:++@  :-+**. ..... :-+**===========#
@#######@@%==*-.           %#%*=%*+: *@. .         =@@@@@@###@#%=.:.+#=..:+*==+=@@@@@###     .:.+-.-+**#++*=# :-:-  ....:.:.-+**==========%#
########@@%==*-   :       @-=*@#@=*:*#+:.   .     =%@@@@@######@%*.:*#%:.+*===+@@@@@@###     ..::=*:.-:*@-%#@:+:        .:---++*==========@#
@#######@@%=*+-++-     . %=-##=%%=-=#=-..     .   *@@@@@@#######%@=-*#@:+*===*=@@@@@@@##=   :...:+%*:+*=*==+::-=   ....  .-++****========*@#
*@@#@@@@@@%==%=*:       *=--  %=++:#%*-.:.-+   . =%@@@@@@@@######@%+=##-======@@@@@@@@### .  :.::-*%*:+===*@ -+*%. ....:..-++*===========+#=
      #@@@#@%=*+ ::-       %#@@%*%+@%*-- @*-.   .+@@@@@@@@@#######%=@##=%%===@@@@@@@@@@## :..*+::-+*%:--+:-*-:@   ......--:-+*=========*+=# 
    @#####@@%=++%*.  -     %##@#%%*#%=*:==%:+.   =@@@@@@@@$@@#####@@###@@@%=@#@@@@@@@@@##.:::*-::+++=--+*=@#-*=# .....:..-+*=**==========#  
   ####@@#@%=@%=+ ++      . =%##=*#@%%*-.#==:-..+%@@@@@@@$@@@@###########@@@@@@@@@$@@@@###:--=%.:+*+@***==%+*-*  ......+-:-**===========%#  
  #@.: ##@##@%=*%=+ .+      -%*@%##@@=++*@@**-:+*%@@@@@@$@@@@@@##########@@@@@@@@@$@@@@@##:-+=#.-+*=#+%%%@%+*@ .:....-..-*****=========*@#  
      #####@%@@%*.%= -+      %=+##= +-++%@%%*+:@=%@@@@@@$@@@@@@@#####@@@@@@@@@@@@@$@@@@@##:+*=#--**=%#@##*+*= .::::.:.-+*++*==========*%#   
     ##=@####@=%#%-== --      %=*##%@%%%###%=-%**%@@@@@@$@@@@@@@@@@@@@@@@@@@@@@@@@$@@@@@##+**=#-+:-==%@#*+-+%.::::::.+-:+*============*#    
       @####@##%=@%+== ++ . .  #+###@#@%+##@=**%+@@@@@@@$@@@@@@@@@@@@@@@@@@@@@@@@@$@@@@@##+**=@==%*%@@*--=@ .:::::::++-*=**=========**@     
      #.-####@@#@=%%+%= *.-     #.%####@+##%@-.*:=@@@@@@$@@@@@@@@@@@@@@@@@@@@@@@@@$@@@@@@#*==#=@%@@@@@#%% .::..::::++-*=*===========*@@     
        ##%####@@@=@@+=*** * :   -@#%= -#@@-===*+.*%@@@@$@@@@@@@@@@@@@@@@@@@@@@@@@@$@@@@*-*=@@%#@@@@##=@....:::.::+--*=*===========*=%      
          ######@##=%%==+=-=.-     =@%*%@##@@%%%++.-%@@$@@@@@@@@@@@@@@@@@@@@@@@@@@@@$@%====*%@#+*- --+#......::--::+***============*#       
        @.+######@##%%%=%%=+* -. :   -@=%+=@##@@-*@=.-=@@@@@@@@@@@@@@@@@@@@@@@@@@@@@#@@@@@@@@#+::+++%=.........:-*****=============@        
          #+ #####@@@%@%@==+=-=::+      +-@###=@@+##*.:=@@@@@@@@@@@@@@@@@@@@@@@@@@@#@#@#######+**==-........:-++++*===============%         
           #*@#####@#@#@=@=%=*%-*+.+       *%#%-@@@@@=+*@@@@@@@@@@@@@@@@@@@@@@@@@##@=##:*-:*=*@+.   ......:-++******============%           
             ++#%#####@#%#%#=%=*%-** - -      #*.=@@*=*=@@@@@@@@@@@@@@@@@@@@@@@@@###@@%*=%*@        ....--++**===%%============@            
                ##########@#%@=@%*%-+-*:.-..        +.-=@@@@@@@@@@@@@@@@@@@@@@@@@####*             ::..-+***===%%%%%%=========@             
               + #.#.####@#@#@@@=@=*==*-*:* -... .   .**@@@@@@@@@@@@@@@@@@@@@@@@@@##@+          .- -++:+*====%%%%%%%%%%====%#               
                    #########@#@@@=%%%*%:=.*-+: - :  .**@@@@@@@@@@@@@@@@@@@@@@@@@@###       : +.:++-*=**==%%%%%%%%%%%%%%%%=%                
                     --=#######@#%@@@%@*@*=**--+.++ +: .%@@@@@@@@@@@@@@@@@@@@@@@@@##@. :: + +-+*:*=*=%%==%%%%%%%%%%%%%%%%*                  
                       #########@#@#@#=@%%==**%-*% *- -+.%@@@@@@@@@@@@@@@@@@@@@@@@%@.--:--+*-%+%=*%%=%%%%@%%%%%%%%%%%%%+                    
                           #-######@#@#@@%%%=@*=@+==-*=*.-*=  .. +=======*   .:+-.:+--=+-%+%=%%=@=%%%%@@%@@@%%%%%%%%@                       
                             #@#########@@#%#%%@%%@*=%%+==%++*******++******+--=**-%=+%=*%%%@%@%@@%@@@@@@@@@@%%%%%@                         
                              # .#########@#@@##%#%%@@%=%@@*=%%%%%==**==%%%%%*+@%%*@@=@@%%@%@@@@@@@@@@@@@@@@@@%%=                                                                                       
"""]

boot = ["""\033[32m
    ______________________________________________________________
   |                       Menu Boot                              |
   |______________________________________________________________|
   |                                                              |
   |comandos das tools                                [1]         |
   |                                                              |
   |programas pintester para baixar                   [2]         |
   |                                                              |
   |como usar programas                               [3]         |
   |                                                              |
   |esconder ip do seu pc                             [4]         |
   |e baixar tor browser                              [44]        |
   |                                                              |
   |teste pro programador                             [5]         |
   |                                                              |
   |wireshark                                         [6]         |
   |                                                              |
   |passar tempo                                      [7]         |
   |                                                              |
   |interface do ettercap                             [8]         |
   |______________________________________________________________|
\033[0m
"""]

def logo():
    for linha in logs:
     print(linha)

def menu():
   for linha in boot:
     print(linha)

def carregamento():
    for porcentagem in range(101):
        os.system("clear")

        barras = porcentagem // 5
        barra = "█" * barras + "=" * (20 - barras)

        print(f"Carregando [{barra}] {porcentagem}%")

        time.sleep(0.03)

while True:
 logo()
 time.sleep(4)
 os.system("clear") 
 menu()
 print("\033[32m")
 escolha = input("escolha uma opção: ")
 print("\033[0m")

 if escolha == "1":
     carregamento()
     os.system("clear")
     print(" -> nmap <-")
     time.sleep(1)
     print(" -> dirb <-")
     time.sleep(1)
     print(" -> nikto <-")
     time.sleep(1)
     print(" -> metasploit <- msfconsole ")
     time.sleep(1)
     print(" -> sqlmap <-")
     time.sleep(1)
     print(" -> john the ripper <- john")
     time.sleep(1)
     print(" -> ncrack <-")
     time.sleep(1)
     print(" -> ettercap <-")
     time.sleep(1)
     print("--Só isso por enquanto--")
     input("aperte enter para voltar ao menu")

 elif escolha == "2":
     carregamento()
     os.system("clear")
     os.system("sudo apt install nmap")
     os.system("pkg install nmap")
     os.system("sudo apt install dirb")
     os.system("pkg install dirb")
     os.system("sudo apt install nikto")
     os.system("pkg install nikto")
     os.system("sudo apt install metasploit-framework")
     os.system("pkg install metasploit-framework")
     os.system("sudo apt install sqlmap")
     os.system("pkg install sqlmap")
     os.system("sudo apt install john")
     os.system("pkg install john")
     os.system("sudo apt install ncrack")
     os.system("pkg install ncrack")
     os.system("sudo apt install ettercap-text-only")
     os.system("pkg install ettercap-text-only")
     print("alguns programas pode não ter baixado!")
     input("aperte enter para voltar ao menu")

 elif escolha == "3":
    carregamento()
    os.system("clear")
    print("\033[44mnmap: serve para escanear portas de um alvo, tem como usar quanto por IP ou por URL tipo nmap www.site.com.br , nmap 123.456.789.012 \033[0m")
    time.sleep(2)
    print("dirb: serve para você achar URL escondidas em um site tipo dirb www.site.com")
    time.sleep(2)
    print("nikto: serve para escanear vulnerabilidades de um alvo você usar a URL junto com -h tipo nikto -h www.site.com.br")
    time.sleep(2)
    print("\033[32mmetasploit: serve para explorar vulnerabilidades de um alvo e você pode usar o msfconsole para abrir o metasploit e depois usar o comando search para procurar exploits de um alvo \033[0m")
    time.sleep(2)
    print("\033[33msqlmap: serve para explorar vulnerabilidades de um banco de dados e você pode usar o comando sqlmap -u www.site.com.br --dbs para procurar bancos de dados de um alvo\033[0m")
    time.sleep(2)
    print("\033[31mjohn the ripper: serve para quebrar senhas com força bruta e você pode usar o comando john --wordlist=rockyou.txt --rules --stdout | john --stdin --format=raw-md5 hash.txt para quebrar senhas de um alvo !MAS VOCÊ TEM QUE TEM QUE TER UMA WORDLIST!\033[0m")
    time.sleep(2)
    print("\033[32mettercap: serve para analizar redes onlines use  ettercap -T -r [pacote] recomendo usar junto com wireshark \033[0m")
    time.sleep(1)
    input("aperte enter para voltar ao menu")

 elif escolha == "4":
    carregamento()
    os.system("clear")
    ai = input("M para mudar de IP e B para baixar ").lower()
    if ai == "b":
       os.system("sudo apt install git")
       os.system("git clone https://github.com/s-r-e-e-r-a-j/IPGhost.git")
       input("aperte enter para voltar ao menu")

    elif ai == "m":
       os.system("cd IPGhost && sudo ipghost")
       input("aperte enter para voltar ao menu")

 elif escolha == "44":
    carregamento()
    os.system("clear")
    ei = input("A para abrir tor browser B para baixar Tor Browser: ").lower()
    if ei == "b":
       os.system("sudo apt install torbrowser-launcher")
    elif ei == "a":
       os.system("torbrowser-launcher")
       
 elif escolha == "5":
    carregamento()
    os.system("clear")
    print("esse é o modo de desenvolvedor vai ter literalmente nada aqui então se quiser sair eu apóio :)")
    input("aperte enter para voltar ao menu")
    os.system("clear")
    menu()
    print("\033[32m")
    escolha = input("escolha uma opção: ")
    print("\033[0m")

 elif escolha == "6":
    carregamento()
    os.system("clear")
    print("A para abrir o wireshark B para baixar o wireshark")
    ii = input(": ").lower()

    if ii == "b":
      os.system("sudo apt install wireshark")
      input("enter para voltar: ")


    elif ii == "a":
       os.system("wireshark")

 elif escolha == "7":
    carregamento()
    os.system("clear")
    print("a para abrir b para baixar")
    oi = input(": ").lower()

    if oi == "a":
       os.system("freedoom1")
       input("enter para voltar: ")

    elif oi == "b":
       os.system("sudo apt install freedoom")
       input("enter para voltar: ")

 elif escolha == "8":
    carregamento()
    os.system("clear")
    print("A para abrir B para baixar")
    ui = input(": ").lower()

    if ui == "a":
       os.system("sudo ettercap -G")

    elif ui == "b":
       print("!ATENÇÃO!, O ETTERCAP NORMAL PODE SER DESISTALADO AO BAIXAR A INTERFACE DO ETTERCAP")
       os.system("sudo apt install ettercap-graphical")

 elif escolha == "exit":
   print("saindo do programa...")
   time.sleep(1)
   sys.exit()

 else :
    print(f"tax tolo fei tirou {escolha} da onde?")
    time.sleep(2)
    os.system("clear")
    menu()
    print("\033[32m")
    escolha = input("escolha uma opção: ")
    print("\033[0m")
