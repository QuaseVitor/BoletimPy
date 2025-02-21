caminho = 'boletim.txt'
boletim = []
nomedoaluno = input('Insira o nome do aluno: ').capitalize()


while True:
    try:
        
        materia = input("insira o nome da materia: ").capitalize()
        
        if materia == 'Sair':
            break
        
        nota = int(input('insira a nota: '))
        

        
    except ValueError:
        continue
    
    boletim.append(f'{materia} == {nota}')
    

adicionar = ''

for i in boletim:
    adicionar += '\n' + i

with open(caminho, 'a') as escrita: 
    escrita.write( '\n' + nomedoaluno +":")
    escrita.write( adicionar + '\n' )
    
