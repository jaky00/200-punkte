if __name__ == '__main__':
    def gelscheinrechner (betrag) -> list:
        antwort =[]
        fancyantwort = []
        zwambos: int =0
        zehner: int =0
        funfer: int =0
        zweier: int =0
        einer: int =0
        if(betrag<=0):
            return('deine zahl muss falsch gewesen sein')
        while(betrag>0):
           if(betrag>=20):
               antwort.append('20€')
               betrag= betrag-20
               zwambos=zwambos+1
           elif(betrag>=10):
               antwort.append('10€')
               betrag= betrag-10
               zehner=zehner+1
           elif(betrag>=5):
               antwort.append('5€')
               betrag= betrag-5
               funfer=funfer+1
           elif(betrag>=2):
               antwort.append('2€')
               betrag= betrag-2
               zweier=zweier+1
           elif(betrag>=1):
               antwort.append('1€')
               betrag= betrag-1
               einer=einer+1
        if(zwambos!=0):
            fancyantwort.append(f'{zwambos} mal 20€')
        if(zehner!=0):
            fancyantwort.append(f'{zehner} mal 10€')
        if(funfer!=0):
            fancyantwort.append(f'{funfer} mal 5€')
        if(zweier!=0):
            fancyantwort.append(f'{zweier} mal 2€')
        if(einer!=0):
            fancyantwort.append(f'{einer} mal 1€')
        return(antwort,fancyantwort)

    def main():
        betrag = int(input("Dein betrag: "))
        antwort = gelscheinrechner(betrag)
        print(f'{antwort}')


    main()