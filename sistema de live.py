import time
import os
import sys
import subprocess
import shutil

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
    ________________________________________________________________
   |                       Menu Boot                    |  mundos   |
   |____________________________________________________|___________|
   |                                                    |mundo-osint|
   |comandos das tools                      [1]         |   [01]    |
   |                                                    |           |
   |programas pintester para baixar         [2]         |MundoDocker|
   |                                                    |   [02]    |
   |como usar programas                     [3]         |           |
   |                                                    |           |
   |esconder ip do seu pc                   [4]         |           |
   |e baixar tor browser                    [44]        |           |
   |                                                    |           |
   |teste pro programador                   [5]         |           |
   |                                                    |           |
   |wireshark                               [6]         |___________|
   |                                                    |           |
   |passar tempo                            [7]         | wordlist  |
   |                                                    |   [30]    |
   |interface do ettercap                   [8]         |           |
   |____________________________________________________|___________|
\033[0m
"""]

WordOsint = ["""\033[32m

   +===========MUNDO-OSINT===========+
   §¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨§
   §PhoneInfoga   [10]               §
   §                                 §
   §sherlock      [11]               §
   §                                 §
   §                                 §
   §                                 § 
   §                                 §
   §                                 §
   §                                 §
   §                                 §
   §                                 §
   §                                 §
   § voltar       [00]               §
   §                                 § 
   +=================================+

\033[0m
"""]

WordDock = ["""
   -----------=MUNDO-DOCKER=-----------
   /baixar docker  [20]               /
   \                                  
   /baixar tudo    [21]               /
   \                                  
   /wpsacan        [22]               /
   \                                  
   /                                  /
   \                                  
   /                                  /
   \                                  
   /                                  /
   \                                  
   /                                  /
   \                                  
   /                                  /
   \                                  
   /                                  /
   ------------------------------------

"""]

def wpscaN():
    wp = input("WPscan: ").strip()

    if not wp:
      print("sem URL")
      return

    sc = shutil.which("sudo docker run --rm wpscanteam/wpscan --url ")

    if not sc:
       print("wpscan não encontrado no docker")
       return

    subprocess.run([sc, wp], check=False)
    input("\ndigite enter para sair...")

def wordDockes():
   for linha in WordDock:
      print(linha)

def phoneinfog():
    phone = input("phoneinfoga: ").strip()

    if not phone:
      print("esta sem numero!")
      return

    foga = shutil.which("phoneinfoga")

    if not foga:
       print("phoneinfoga não encontrado no PATH")
       return

    subprocess.run([foga, phone], check=False)
    input("\ndigite enter para sair...")

def sherlock_menu():
    lock = input("sherlock: ").strip()

    if not lock:
        print("nome de usuario vazio!")
        return

    sherlock = shutil.which("sherlock")

    if not sherlock:
        print("Sherlock não encontrado no PATH.")
        return

    subprocess.run([sherlock, lock], check=False)
    input("\ndegite enter para sair...")


def mundoOsi():
   for linha in WordOsint:
      print(linha)

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
     print(" -> hashcat <-")
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
     os.system("sudo apt install hashcat")
     os.system("pkg install hashcat")
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
    print("\033[33mhashcat: serve para quebrar senhas com força bruta e você pode usar o comando hashcat -m 0 -a 0 hash.txt rockyou.txt para quebrar senhas de um alvo !MAS VOCÊ TEM QUE TEM QUE TER UMA WORDLIST!\033[0m")
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
   break

 elif escolha == "02":
    carregamento()
    os.system("clear")
    wordDockes()
    print("\033[32m")
    escolha2 = input("escolha uma opção: ")
    print("\033[0m")

    if escolha2 == "20":
       os.system("clear")
       os.system("sudo apt install docker.io docker-compose -y")
       os.system("sudo systemctl enable --now docker")
       os.system("docker --version")
       input("|:|")

    elif escolha2 == "21":
       os.system("clear")
       os.system("docker pull wpscanteam/wpscan")


    elif escolha2 == "22":
        os.system("clear")
        wpscaN()

 elif escolha == "01":
     carregamento()
     os.system("clear")
     mundoOsi()
     print("\033[32m")
     escolha1 = input("escolha uma opção: ")
     print("\033[0m")

     if escolha1 == "10":
        carregamento()
        os.system("clear")
        print("digite phoneinfoga scan -n [numero da pessoa]")
        time.sleep(5)
        os.system("clear")
        phoneinfog()
        input("|:|")

     elif escolha1 == "11":
        carregamento()
        os.system("clear")
        os.system("https://github.com/sherlock-project/sherlock.git")
        os.system("cd sherlock")
        os.system("clear")
        time.sleep(3)
        sherlock_menu()
     elif escolha1 == "00":
      print("bye")

 elif escolha == "30":
        carregamento()
        os.system("clear")
        print("digite o G para gerar e B para baixar V para ver a wordlist")
        word = input(": ").lower()

        if word == "g":
           os.system("clear")
           os.system("cewl https://docs.python.org/3/ -w palavras.txt")
           print("quer ver a onde esta a wordlist? Y/n")
           ver = input(": ").lower()
           if ver == "y":
               os.system("clear")
               os.system("which palavras.txt")
               input("pressione enter para voltar: ")

           elif word == "n":
              os.system("clear")
              print("ok")
              input("pressione enter para voltar: ")

        elif word == "b":
           os.system("clear")
           os.system("sudo apt install cewl")

        elif word == "v":
           os.system("clear")
           os.system("ls -l palavras.txt")
           os.system("cat palavras.txt")
           os.system("which palavras.txt")
           time.sleep(1)
           input("pressione enter para voltar...")


 else :
    print(f"tax tolo fei tirou {escolha} da onde?")
    time.sleep(2)
    os.system("clear")
    menu()
    print("\033[32m")
    escolha = input("escolha uma opção: ")
    print("\033[0m")
