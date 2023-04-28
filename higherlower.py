import random
import os
count = 0
def start():
    count=0
    def lowerhigher():
            logo1 = """
  _     _       _                 _                        
 | |   (_)     | |               | |                       
 | |__  _  __ _| |__   ___ _ __  | | _____      _____ _ __ 
 | '_ \| |/ _` | '_ \ / _ \ '__| | |/ _ \ \ /\ / / _ \ '__|
 | | | | | (_| | | | |  __/ |    | | (_) \ V  V /  __/ |   
 |_| |_|_|\__, |_| |_|\___|_|    |_|\___/ \_/\_/ \___|_|   
           __/ |                                           
          |___/                                            
            """
            logo2=""" 
 __   _____ 
 \ \ / / __|
  \ V /\__ \\
   \_/ |___/
             """
            global count
            n1=0
            n2=0
            while n1==n2:
                n1=random.randint(1,700)
                n2=random.randint(1,700)
            print(logo1)
                
            print(f"we have {n1}")
            
            print(logo2)
            print(f"and we have {n2}")
        
            
            comp=int(input(f"Which one is greater {n1} or {n2} type '1' for {n1} and '2' for {n2} : "))
            if comp==1:
                if n1>n2:
                    print("you won")
                    # global count
                    count+=1
                    os.system('cls')
                    lowerhigher()
                elif n1<n2:
                    print("you loose")
                    print(f"Your score : {count}")
            elif comp==2:
                if n1<n2:
                    print("you won")
                    # global count
                    count+=1
                    os.system('cls')
                    lowerhigher()
                elif n1>n2:
                    print("you loose")
                    print(f"Your score : {count}")
    lowerhigher()
start()