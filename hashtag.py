#A partir de uma frase recebida em forma de string,a função ira formatar o texto retirando
#os espaços, colocando letras maiusculas após os espaços  e adicionando uma hashtag no começo.

def hashtag(frase):
    frase = frase.strip()
    frase = frase.split(' ')
    index = 0
    while(index < len(frase)):
        frase[index] = frase[index].capitalize()
        
        index= index +1
    frase.insert(0,'#')
    frase = ''.join(frase)
    return(frase)


