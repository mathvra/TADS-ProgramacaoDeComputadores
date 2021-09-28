nTestes = int(input())

def cobaias(nTestes):
    total = 0
    coelho = 0
    rato = 0
    sapo = 0
    for i in range(0, nTestes):
        nCobaias, tipo = input().split()
        nCobaias = int(nCobaias)
        total = total + nCobaias
        if(tipo == 'C'):
            coelho = coelho + nCobaias
        elif(tipo == 'R'):
            rato = rato + nCobaias
        else:
            sapo = sapo + nCobaias
    
    print('Total: {} cobaias' .format(total))
    print('Total de coelhos: {}' .format(coelho))
    print('Total de ratos: {}' .format(rato))
    print('Total de sapos: {}' .format(sapo))
    print('Percentual de coelhos: {:.2f} %' .format((coelho/total)*100))
    print('Percentual de ratos: {:.2f} %' .format((rato/total)*100))
    print('Percentual de sapos: {:.2f} %' .format((sapo/total)*100))

cobaias(nTestes)