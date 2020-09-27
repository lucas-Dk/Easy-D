# importação
import urllib.request
import os
# Função de início
def titulo(texto):
	print(texto)


# Função que fará o trabalho
def baixar_arquivo(url, local):
	try:
		urllib.request.urlretrieve(url, local)
	except (ValueError, TypeError):
		print('Ocorreu um problema com o tipo de dado fornecido!')
	else:
		print('Arquivo baixado!')
		print('Acesse o arquivo no caminho especificado para baixar')



# Chamando a função que mostra o nome
os.system("clear")
titulo("""\033[1;31m
███████╗ █████╗ ███████╗██╗   ██╗     ██████╗ 
██╔════╝██╔══██╗██╔════╝╚██╗ ██╔╝     ██╔══██╗
█████╗  ███████║███████╗ ╚████╔╝█████╗██║  ██║
██╔══╝  ██╔══██║╚════██║  ╚██╔╝ ╚════╝██║  ██║
███████╗██║  ██║███████║   ██║        ██████╔╝
╚══════╝╚═╝  ╚═╝╚══════╝   ╚═╝        ╚═════╝ 
                Versão 1.0                              
	\033[m""")

# Apresentação do programa

print("""\033[1;95m
######################################################################
\033[m
\033[1;32mMeu facebook >\033[m https://www.facebook.com/Walker.Lxrd/
\033[1;32mLink do meu github > \033[mhttps://github.com/lucas-Dk

\033[1;94mExplicação:

Este script foi criado para baixar arquivos 
(imagens, videos ou músicas)
\033[m
Exemplo de uso: 

\033[1;4mEm url digite a url do arquivo
em tipo coloque o local de salvamento do arquivo e o nome
que deseja salvar
\033[m
\033[1;96m
veja:

url = https://upload.wikimedia.org/wikipedia/commons/thumb/e/e1/FullMoon2010.jpg/280px-FullMoon2010.jpg
tipo = aqui vocês colocam o caminho que será salvo o arquivo + nomedoarquivo.(tipo do arquivo)

OBS: Fiz para fins de estudos!
\033[m
\033[1;95m
######################################################################
\033[m	""")

# Início do programa

try:
	link = str(input('Url do arquivo: '))
	print()
	tipo = str(input('local de armazenamento e nome do arquivo (leia a instrução): '))
	print()
except (ValueError, TypeError):
	print()
	print('Ocorreu um problema com o tipo de dado fornecido!')
except KeyboardInterrupt:
	print()
	print('\nSaiu!')
else:
	try:
		print('\033[1;94mFazendo download do arquivo....\033[m\n')
		urllib.request.urlretrieve(link,tipo)
	except:
		print('\033[1;31mLink quebrado / privado ou inválido!\033[m')

	else:
		print('\033[1;92mArquivo baixado!\n')
		print('Verifique no caminho que você especificou!\033[m')
finally:
	print('\n\033[4mObrigado por usar, volte sempre!\033[m')
	print()

