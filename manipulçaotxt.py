##vamos abrir um arquivo TXT

arq1 = open('Manipulacao_de_arquivos/arquivos/arquivo.txt','r')

#windows \ # linux /

## ler o arquivo TXT

print(arq1.read())


#voltar o cursor ao inicio 

arq1.seek(0,0)

print(arq1.read())

#fechar o arquivo

arq1.close()

#usar um arquivo em modo gravacao

arq2 = open('Manipulacao_de_arquivos/arquivos/arquivo.txt',"w+")

#gravar 

arq2.write("Tem novo conteudo \n")
arq2.write("Gravei outra linha \n")

arq2.seek(0,0)
print(arq2.read())

#fechar o arquivo
arq2.close()

##abrir uma nova manipulçao de arquivo 

arq3 = open('Manipulacao_de_arquivos/arquivos/arquivo.txt','a+')

arq3.write("Novo conteudo sem apagar o antigo")

arq3.seek(0,0)

print(arq3.read())

arq3.close()

##Gerenciador d context de arquivos 

with open('Manipulacao_de_arquivos/arquivos/arquivo1.txt','w+') as f:
    f.write('Primeira linha \n')
    f.write('segunda linha \n')
    f.seek(0,0)
    grava = str(f.read())
    f.seek(0,0)
    print(f.read())
    

##gravar informaçoes em um segundo arquivo
    
with open('Manipulacao_de_arquivos/arquivos/arquivo2.txt','w+') as f2:
    f2.write(grava)
    f2.seek(0,0)
    print(f2.read())

