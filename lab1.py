from pathlib import Path
from PIL import Image
    

def convert_to_png(path):
    im = Image.open(path)
    path=path.with_suffix('.png')
    im.save(path) 
def zamiana_(text, tab):
    for i in tab:
        text=text.replace(i, '')
        
    return text
def zamiana2(text, tab2):
    for key, value in tab2.items():
        text=text.replace(key, value)
        
    return text
def main():
        # print("hello")
    # imie,nazwisko,rok=input("podaj imie, nazwisko, rok urodzenia\n\r\n\r").split(' ')
    
    # print("twoje imie to :", imie)
    # print("nazwisko:", nazwisko)
    # print("rok:", rok)
    
    # kod = '1234'
    # print("poda koda:\n\r") 
    # while(input()!=kod):
    #     print("źle")
    # print("dobrzeee\n\r")
    
    path = Path('.')
    print('file count: ', sum(1 for x in path.glob('*') if x.is_file()))
    
    for x in path.glob('**/*'):
        print(x)
        if x.suffix=='.jpg':
            print("konwertowanie plików jpg na png")
            convert_to_png(x)
        
    print("konwertowanie plików jpg na png")
            
    path = Path('1.jpg')
    convert_to_png(path)
    
    # tab = ['się', 'i', 'oraz', 'nigdy', 'dlaczego']
    # text=input('podaj ciag wyrazow:')
    # print(text)
    # text2 = zamiana(text,tab)
    # print(text2)
    
    tab2 = {
        'i': 'oraz',
        'oraz': 'i',
        'nigdy': 'prawie nigdy',
        'dlaczego': 'czemu'
        }
    text=input('podaj ciag wyrazow:')
    print(text)
    text2 = zamiana2(text,tab2)
    print(text2)
               

    
       
if __name__ == '__main__':
    main()
    