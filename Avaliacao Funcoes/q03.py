def primo(numero,verifica):
    print(numero,verifica)
    if(numero<2): #Primeira parte
        print('Entrou < 2')
        return 'Não é primo'
    if(numero==verifica): #Segunda parte
        print('Entrou ==')
        return 'É primo'
    if(numero%verifica==0): #Terceira parte
        print('Entrou %')
        return 'Não é primo'
    return primo(numero,verifica+1)

print(primo(13,2))