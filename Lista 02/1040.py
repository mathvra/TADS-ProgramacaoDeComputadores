n1, n2, n3, n4 = map(float, input().split())

media1 = ((n1*2)+(n2*3)+(n3*4)+(n4*1))/(2+3+4+1)

print("Media: {:.1f}" .format(media1))

if media1 >= 7.0:
    print("Aluno aprovado.")
elif media1 < 5.0:
    print("Aluno reprovado.")
elif media1 >= 5.0 and media1 <= 6.9:
    print("Aluno em exame.")
    nExame = float(input())
    print("Nota do exame: {:.1f}" .format(nExame))
    media2 = (nExame + media1)/2
    if media2 >= 5.0:
        print("Aluno aprovado.")
    else:
        print("Aluno reprovado.")
    print("Media final: {:.1f}" .format(media2))
