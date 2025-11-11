import time                                                                 
import random                                                               
def scramble(length=20):                                                    
                                                                            
    faces = ['U', 'D', 'L', 'R', 'F', 'B']                                  
    modifiers = ['', '2', "'"]                                              
    scramble = []                                                           
    last_face = None                                                        
                                                                            
    for _ in range(length):                                                 
        while True:                                                         
            face = random.choice(faces)                                     
            if face != last_face:                                           
                break                                                       
                                                                            
        modifier = random.choice(modifiers)                                 
                                                                            
        scramble.append(f"{face}{modifier}")                                
        last_face = face                                                    
                                                                            
    return " ".join(scramble)                                               
def scrprint():                                                             
    if __name__ == "__main__":                                              
        scramble_sequence = scramble(length=20)                             
        print(scramble_sequence)                                            
                                                                            
def sw():                                                                   
    scrprint()                                                              
    input()                                                                 
    start = time.time()                                                     
    input()                                                                 
    end = time.time()                                                       
    timetk = round(end - start,2)                                           
    print(timetk)                                                           
    print()                                                                 
    sw()                                                                    
sw()                       
