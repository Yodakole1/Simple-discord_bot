import string 
import random
import datetime


def get_odgovor(poruka: str) -> str:
    p_poruka = poruka.lower()

    if p_poruka == "cao":
        return "cao"

    if p_poruka == "broj":
        return str(random.randint(1,99))

    if p_poruka == "!help":
        return "`broj sifra joke conv(insert text here)`" 
    
    #if p_poruka == "vreme":
     #   vreme = datetime.datetime.now()
      #  sat = vreme.hour
       # minut = vreme.minute
        #sekund = vreme.second
        #msekund = vreme.microsecond
        #return ("Vreme je " + sat + minut + sekund + msekund) 
    
    if p_poruka == "sifra":
        duzina  = 9
        karakteri="1234567890QWERTYUIOPLKJHGFDSAZXCVBNMqwertyuioplkjhgfdsazxcvbnm@_!+?/"
        password = ""
        for i in range(duzina):
            password = password + random.choice(karakteri)
        return ("Generisani password je ||{}||".format (password))
        
    if p_poruka[:6] == "pogodi":
        randbr = str(random.randint(0,100))    
        brojic = p_poruka[7:]
        if randbr == brojic:
            return 'Pogodio si broj'
        else:
            return "Nisi pogodio"
    
    
    if p_poruka == "joke":
        lista = ["Idu dva mrava ulicom..... i odose.","Idu dva kaktusa pustinjom i prvi kaze drugom pazi da se ne ispumpasssssssssssssss.",]
        fg =  str (random.choice(lista))
        return fg
    
    if p_poruka[:4] == "conv":
        n=5
        novstring=p_poruka[4:]
        bconv=''.join(format(ord(i),'08b')for i in novstring)
        return ("Kad se " + novstring + " konvertuje, dobije se: " + str(bconv))
    
    
    return ""
            
