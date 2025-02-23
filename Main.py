import os


caminho = 'boletim.txt'
boletim = []


while True:
    print("O que voce deseja fazer?")
    decidir = input("\tAdicionar notas\n\tLer notas\n\tFormatar Boletim\n").capitalize()
    if decidir == "Formatar":    
        os.remove(caminho)
        with open(caminho, 'w') as arq:
            arq.write('')
        

    elif decidir =="Ler"or decidir == 'Ler notas': 
        if os.stat(caminho).st_size == 0:
            print('Não há notas salvas\n')
        
        else:
            with open(caminho, 'r') as arq:
                leitura = arq.read()
                print(leitura)
            
    
    elif decidir == "Adicionar":
        nomedoaluno = input('Insira o nome do aluno: ').capitalize()

        print("Insira as materias e notas que deseja adicionar. Quando terminar digite 'sair' para encerrar e salvar os dados")
        while True:
            try:
                
                materia = input("insira o nome da materia(ou 'sair'): ").capitalize()
                
                if materia == 'Sair':
                    break
                
                nota = int(input('insira a nota: '))
                
                if nota > 10 or nota<0:
                    print("Insira um valor de 0 à 10")
                    continue
                
            except ValueError:
                continue
            
            boletim.append(f'{materia} = {nota}')
            

        adicionar = ''

        for i in boletim:
            adicionar += '\n' + i

        with open(caminho, 'a') as escrita: 
            escrita.write( '\n' + nomedoaluno +":")
            escrita.write( adicionar + '\n' )
            
    else:
        print("insira uma opção valida")
        continue    
    
