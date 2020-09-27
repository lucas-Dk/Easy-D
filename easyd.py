# importações
import urllib.request
import sys
from datetime import datetime
import time
# Ano em que o script está sendo rodado
ano = datetime.now().year
print('\033[1mVocê está rodando este programa em {}\033[m'.format(ano))
# Função de início
def titulo(texto):
	print(texto)


# Função que fará o trabalho
def baixar_arquivo(url, local):
	try:
		urllib.request.urlretrieve(url, local)
	except:
		print('\033[1;31mLink quebrado, privado ou inválido!\033[m')
	else:
		print('\033[1;92mArquivo baixado!')
		print('Acesse o arquivo no caminho que você colocou\033[m')

# Início do programa 
print('\nVerificando seu sistema operacional...')
time.sleep(2)
if sys.platform == "linux2" or sys.platform == "linux":
	print('\033[1;32mSistema operacional compativel :)\033[m')
	while True:
		# Chamando a função que mostra o nome

		titulo("""\033[1;31m
				███████╗ █████╗ ███████╗██╗   ██╗     ██████╗ 
				██╔════╝██╔══██╗██╔════╝╚██╗ ██╔╝     ██╔══██╗
				█████╗  ███████║███████╗ ╚████╔╝█████╗██║  ██║
				██╔══╝  ██╔══██║╚════██║  ╚██╔╝ ╚════╝██║  ██║
				███████╗██║  ██║███████║   ██║        ██████╔╝
				╚══════╝╚═╝  ╚═╝╚══════╝   ╚═╝        ╚═════╝ 
				                Versão 2.0                              
			\033[m""")

		# Apresentação do programa
		print()
		print()
		print("""\033[1;95m
######################################################################

				   \033[1;94mMINHAS REDES\033[m
\033[m
\033[1;32mMeu facebook >\033[m https://www.facebook.com/Walker.Lxrd/
\033[1;32mLink do meu github > \033[mhttps://github.com/lucas-Dk

----------------------------------------------------------------------
Exemplo de uso: 
\033[1;96m
url = https://upload.wikimedia.org/wikipedia/commons/thumb/e/e1/FullMoon2010.jpg/280px-FullMoon2010.jpg

local = Users\\any\\downloads\\imagem.jpg  Seu arquivo será salvo neste caminho e terá esse nome\033[m

----------------------------------------------------------------------
\033[1;31m
OBS: LEIA O README.md !!!\033[m\033[1;95m

######################################################################
	\033[m	""")

		print()
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
			break

		else:
			print('\033[1;94mFazendo download do arquivo....\033[m\n')
			baixar_arquivo(link, tipo)

		novamente = str(input('Deseja baixar mais alguma coisa? S ou enter para baixar / N para sair: ')).upper().strip()
		while novamente not in "S" and novamente not in "N":
			novamente = str(input('Deseja baixar mais alguma coisa S/N: ')).upper().strip()

		if novamente == "S" or novamente == "":
			pass
		elif novamente  == "N":
			break

	print()
	titulo('Volte sempre!')
	print()

else:
	print('\033[1;31mERRO')
	print('Sistema não compativel :(\033[m')
