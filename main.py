
import pickle
import datetime
import os

dados={}
try:
 arq_dados = open("dados.dat", "rb")
 dados = pickle.load(arq_dados)
 arq_dados.close()
except:
 arq_dados = open("dados.dat", "wb")
 arq_dados.close()

servicos={}
try:
 arq_servicos = open("servicos.dat", "rb")
 servicos = pickle.load(arq_servicos)
 arq_servicos.close()
except:
 arq_servicos = open("servicos.dat", "wb")
 arq_servicos.close()

ordens={}
try:
 arq_ordens = open("ordens.dat", "rb")
 ordens = pickle.load(arq_ordens)
 arq_ordens.close()
except:
 arq_ordens = open("ordens.dat", "wb")
 arq_ordens.close()
data=datetime.datetime.now()


def menu():
  os.system('clear')
  print('='*46)
  print('*'*17 + 'PY COMPUTER' +'*'*18)
  print('='*46)
  print()
  print('-'*16 +'MENU PRINCIPAL' +'-'*16)
  print()
  print('CLIENTES------------------------------Digite 1')
  print('SERVIÇOS------------------------------Digite 2')
  print('ORDEM DE SERVIÇO----------------------Digite 3')
  print('SOBRE---------------------------------Digite 4')
  print('SAIR----------------------------------Digite 0')
  print()
  esc=int(input('Escolha sua opção: '))
  print()
  return esc
  

def clientes():
  
  os.system('clear')
  print('='*46)
  print('*'*17 + 'PY COMPUTER' + '*'*18)
  print('='*46)
  print()
  print('-'*16+'MENU CLIENTES'+'-'*16)
  print()
  print('*CADASTRAR CLIENTE-------------------Digite 1')
  print('*PROCURAR CADASTRO-------------------Digite 2')
  print('*EDITAR CADASTRO---------------------Digite 3')
  print('*LISTAR TODOS------------------------Digite 4')
  print('*EXCLUIR CADASTRO--------------------Digite 5')
  print('*VOLTAR AO MENU PRINCIPAL------------Digite 0')
  print()
  esc=int(input('Escolha sua opção: '))
  print()
  return esc
   

def service():
  os.system('clear')
  print('='*46)
  print('*'*17+'PY COMPUTER'+'*'*18)
  print('='*46)
  print()
  print('-'*16+'MENU SERVIÇOS'+'-'*16)
  print()
  print('*PROCURAR SERVIÇO--------------------Digite 1')
  print('*LISTAR TODOS------------------------Digite 2')
  print('*FAZER ORÇAMENTO---------------------Digite 3')
  print('*ADICIONAR SERVIÇO-------------------Digite 4')
  print('*EXCLUIR SERVIÇO---------------------Digite 5')
  print('*VOLTAR AO MENU PRINCIPAL------------Digite 0')
  print()
  esc=int(input('Escolha sua opção: '))
  print()
  return esc
  

def ord_serv():
  os.system('clear')
  print('='*46)
  print('*'*17+'PY COMPUTER'+'*'*18)
  print('='*46)
  print()
  print('------------MENU ORDEM DE SERVIÇO-------------')
  print()
  print('*ENTRADA DE OS-------------------------Digite 1')
  print('*PROCURAR OS---------------------------Digite 2')
  print('*ATUALIZAR OS--------------------------Digite 3')
  print('*EXCLUIR OS----------------------------Digite 4')
  print('*LISTAR TODAS OS-----------------------Digite 5')
  print('*VOLTAR AO MENU PRINCIPAL--------------Digite 0')
  print()
  esc=int(input('Escolha sua opção: '))
  print()
  return esc
  

def sobre():
  os.system('clear')
  print('='*46)
  print('*'*17+'PY COMPUTER'+'*'*18)
  print('='*46)
  print()
  print('---------------SOBRE O PROJETO----------------')
  print()
  print('Projeto em desenvolvimento para a  Py Computer,\nempresa de manutenção de computadores. Servirá\ncomo sistema interno com informações de clientes,\nserviços realizados com respectivos valores e\nOrdem de Serviço(OS).\n\nDesenvolvedora: Anne Gabrielle')
  print()
  esc=int(input('Deseja voltar ao Menu Principal?\nDigite 0: '))
  print()
  return esc


def cadastro_cliente():
  print('Vamos realizar o cadastro!')
  print()
  nome=input('Nome do cliente: ')
  email=input('E-mail: ')
  cpf=input('CPF: ')
  tel=input('Telefone: ')
  end=input('Endereço: ')
  print()
  dados[cpf] = [nome, tel, email, end]
  print('Cadastro realizado com sucesso!')
  print()
  input('Aperte ENTER para continuar')
  
  
def busca_cliente():
  cpf=input('Informe o CPF do cadastro que deseja encontrar: ')
  print()
  if cpf in dados:
    print("NOME: ", dados[cpf][0])
    print("TELEFONE: ", dados[cpf][1])
    print("E-MAIL: ", dados[cpf][2])
    print('ENDEREÇO: ', dados[cpf][3])
    print()       
  else:
    print("CPF não encontrado!")
  input('Aperte ENTER para continuar')
      

def editar_cadastro(): 
  os.system('clear')
  print('='*46)
  print('*'*17+'PY COMPUTER'+'*'*18)
  print('='*46)
  print()
  print('Deseja alterar nome?------------------Digite 1')
  print('Deseja alterar e-mail?----------------Digite 2')
  print('Deseja alterar endereço?--------------Digite 3')
  print('Deseja alterar telefone?--------------Digite 4')
  print('voltar-------------0')
  print()
  edit=int(input('O que deseja alterar? '))
  print()
  return edit
   

def editar_nome():
  
  cpf=input('Informe o CPF do cadastro que deseja alterar: ')
  print()
  if cpf in dados:
    novo=input('Informe o nove nome: ')
    print()
    dados[cpf][0]=novo
    print('Alteração realizada com sucesso!')
    print()
  else:
    print('CPF não encontrado!')
    print()
  input('Aperte ENTER para continuar')

       
def editar_email():
  cpf=input('Informe o CPF do cadastro que deseja alterar: ')
  print()
  if cpf in dados:
    novo=input('Informe o novo e-mail: ')
    print()
    dados[cpf][2]=novo
    print('Alteração realizada com sucesso!')
    print()   
  else:
    print('CPF não encontrado!')
    print() 
  input('Aperte ENTER para continuar')
   

def editar_telefone():
  cpf=input('Informe o CPF do cadastro que deseja alterar: ')
  print()
  if cpf in dados:
    novo=input('Informe o novo telefone: ')
    print()
    dados[cpf][1]=novo
    print('Alteração realizada com sucesso!')
    print()  
  else:
    print('CPF não encontrado!')
  input('Aperte ENTER para continuar')
      
       
def editar_endereco():
  cpf=input('Informe o CPF do cadastro que deseja alterar: ')
  print()
  if cpf in dados:
    novo=input('Informe o novo endereço:')
    print()
    dados[cpf][3]=novo
    print('Alteração realizada com sucesso!')
    print()
  else:
    print('CPF não encontrado!')
  input('Aperte ENTER para continuar')
  print()


def listar_cadastros():
  for cpf in dados:
    print(f'Nome: {dados[cpf][0]}, Telefone: {dados[cpf][1]}, Endereço: {dados[cpf][3]}, E-mail: {dados[cpf][2]}')
    print()
  input('Aperte ENTER para continuar')
              

def excluir_cadastro():
  print('Vamos excluir o cadastro!')
  print()
  cpf=input('Digite o CPF do cadastro que deseja excluir: ')
  print()
  if cpf in dados:
    del dados[cpf]
    print('Cadastro excluído com sucesso!') 
    print()
  else:
    print('CPF não encontrado!')
    print()
  input('Aperte ENTER para continuar')


def procurar_servico():
  cod=input('Digite o código do serviço que deseja encontrar: ')
  print()
  if cod in servicos:
    print("SERVIÇO: ", servicos[cod][0])
    print("VALOR: ", servicos[cod][1])
    print()      
  input('Aperte ENTER para continuar')
  
      
def listar_servicos():
  print('Lista de todos os serviços prestados pela Py Computer')
  print()
  for pos in servicos:
    print(f'Código: {pos}--- Serviço: {servicos[pos][0]}--- Valor: {servicos[pos][1]}')
    print()
  input('Aperte ENTER para continuar')
 

def orcamento():
  soma=0
  resp='S'
  while resp=='S':    
    cod=input('Digite o código do serviço a ser realizado: ')
    print()
    if cod in servicos:
      x=float(servicos[cod][1])
      soma= soma+x
    resp=input('Deseja acrescentar mais um serviço ao orçamento?\nSe sim, digite S.\nSe não, digite N: ').upper()
    print()
    if resp=='N':
      print('O orçamento total é R$ %.2f'%(soma))
      print()
  input('Aperte ENTER para continuar')

def inserir_serv():
  print('Vamos realizar o cadastro do novo serviço!') 
  print()
  nome=input('Serviço a ser adicionado: ')
  print()
  valor=input('Qual o valor do serviço?: ')
  print()
  cod=input('Digite um código para o serviço: ')
  print()
  if cod not in servicos:
    servicos[cod]=[nome,valor]
    print('Serviço adicionado com sucesso!')
    print()
  else:
    print('Código já existe!')
    print()
  input('Aperte ENTER para continuar')
  
def excluir_servico():
  print('Vamos excluir o serviço')
  print()
  cod=input('Qual o código do serviço que deseja excluir?  ')
  print()
  if cod in servicos:
    del servicos[cod]
    print('Serviço excluído com sucesso!')
    print()
  else:
    print('Código de serviço não encontrado!')
    print()
  input('Aperte ENTER para continuar')


def entrada_ordem():
  nome=input('Nome do cliente:')
  cpf=input('CPF:')
  fun=input('Funcionário responsável:')
  serv=input('Serviços a serem realizados:')
  obs=input('Observações:')
  ent=input('Data de entrada:')
  prev=input('Previsão de entrega:')
  os=data.strftime('%d%m%Y%H%M%S')
  print()
  ordens[cpf] = [nome, fun, serv, obs, ent, prev, os]
  print('Entrada de Ordem de serviço cadastrada!')
  print()
  input('Aperte ENTER para continuar')
  


def procurar_ordem():
  cpf=input('Digite o CPF da ordem de serviço que deseja encontrar: ')
  
  print()
  if cpf in ordens:
    print("Nome: ", ordens[cpf][0])
    print("Funcionário responsável: ", ordens[cpf][1])
    print("Serviços contratados: ", ordens[cpf][2])
    print('Observações:', ordens[cpf][3])
    print('Data de entrada:', ordens[cpf][4])
    print('Previsão de entrega:', ordens[cpf][5])
    print('Número da Ordem de Serviço:', ordens[cpf][6])
    print()    
  else:
    print("CPF não encontrado!")
    print()
  input('Aperte ENTER para continuar')



def atualizar_ordem():
  os.system('clear')
  print('='*46)
  print('*'*17+'PY COMPUTER'+'*'*18)
  print('='*46)
  print()
  print('Deseja alterar nome?---------------------------Digite 1')
  print('Deseja alterar funcionário responsável?--------Digite 2')
  print('Deseja alterar serviços contratados?-----------Digite 3')
  print('Deseja alterar observações?--------------------Digite 4')
  print('Deseja alterar data de entrada?----------------Digite 5 ')
  print('Deseja alterar previsão de entrega?------------Digite 6 ')
  print()
  atual=int(input('O que deseja alterar? '))
  print()
  return atual


def alterar_nome():
  cpf=input('Informe o CPF da Ordem de Serviço que deseja alterar: ')
  print()
  if cpf in ordens:
    novo=input('Informe o nove nome:')
    print()
    ordens[cpf][0]=novo
    print('Alteração realizada com sucesso!')
    print()
  else:
    print('CPF não encontrado!')
    print()
  input('Aperte ENTER para continuar')
  


def alterar_funcionario():
  cpf=input('Informe o CPF da Ordem de Serviço que deseja alterar: ')
  print()
  if cpf in ordens:
    novo=input('Informe o novo funcionário responsável: ')
    print()
    ordens[cpf][1]=novo
    print('Alteração realizada com sucesso!')
    print()
  else:
    print('CPF não encontrado!')
    print()
  input('Aperte ENTER para continuar')
 


def serv_cont():
  cpf=input('Informe o CPF da Ordem de Serviço que deseja alterar: ')
  print()
  if cpf in ordens:
    novo=input('Informe o novo serviço a ser realizado: ')
    print()
    ordens[cpf][2]=novo
    print('Alteração realizada com sucesso!')
    print()
  else:
    print('CPF não encontrado!')
    print()
  input('Aperte ENTER para continuar')
 

def alterar_obs():
  cpf=input('Informe o CPF da Ordem de Serviço que deseja alterar: ')
  print()
  if cpf in ordens:
    novo=input('Informe as novas observações: ')
    print()
    ordens[cpf][3]=novo
    print('Alteração realizada com sucesso!')
    print()
  else:
    print('CPF não encontrado!')
    print()
  input('Aperte ENTER para continuar')


def alterar_ent():
  cpf=input('Informe o CPF da Ordem de Serviço que deseja alterar: ')
  print()
  if cpf in ordens:
    novo=input('Informe a nova data de entrega: ')
    print()
    ordens[cpf][4]=novo
    print('Alteração realizada com sucesso!')
    print()
  else:
    print('CPF não encontrado!')
    print()
  input('Aperte ENTER para continuar')


def alterar_prev():
  cpf=input('Informe o CPF da Ordem de Serviço que deseja alterar: ')
  print()
  if cpf in ordens:
    novo=input('Informe a nova previsão de entrega: ')
    print()
    ordens[cpf][5]=novo
    print('Alteração realizada com sucesso!')
    print()
  else:
    print('CPF não encontrado!')
    print()
  input('Aperte ENTER para continuar')
 


def excluir_ordem():
  cpf=input('Digite o CPF da Ordem de Serviço que deseja excluir: ')
  print()
  if cpf in ordens:
    del ordens[cpf]
    print('Ordem de Serviço excluida com sucesso!')
    print()
  else:
    print("CPF não encontrado!")
    print()
  input('Aperte ENTER para continuar')

def listar_ordens():
  for cpf in ordens:
    print(f'Nome: {ordens[cpf][0]}, Funcionário responsável: {ordens[cpf][1]}, Serviços contratados: {ordens[cpf][2]}, Observações: {ordens[cpf][3]}, Data de entrada: {ordens[cpf][4]}, Previsão de entrega: {ordens[cpf][5]}, Número da OS: {ordens[cpf][6]} ')
    print()
  input('Aperte ENTER para continuar')
  


start=menu()
while start!=0:  
  if start==1:
    op=clientes() 
    while op!=0:
      if op==1:
        cadastro_cliente() 
      elif op==2:
        busca_cliente() 
      elif op==3:
        alt=editar_cadastro()
        while alt!=0:
          if alt==1:
            editar_nome()
          elif alt==2:
            editar_email()
          elif alt==3:
            editar_endereco()
          elif alt==4:
            editar_telefone()
          alt=0        
      elif op==4:
        listar_cadastros()      
      elif op==5:
        excluir_cadastro()
      op=clientes()
  elif start==2:
    op=service()
    while op!=0:
      if op==1:
        procurar_servico()
      elif op==2:
        listar_servicos()
      elif op==3:
        orcamento()     
      elif op==4:
        inserir_serv()
      elif op==5:
        excluir_servico()
      op=service()
    
  elif start==3:
    op=ord_serv()
    while op!=0:
      if op==1:
        entrada_ordem()
      elif op==2:
        procurar_ordem()
      elif op==3:
        alt=atualizar_ordem()
        while alt !=0:
          if alt==1:
            alterar_nome()
          elif alt==2:
            alterar_funcionario()
          elif alt==3:
            serv_cont()
          elif alt==4:
            alterar_obs()
          elif alt==5:
            alterar_ent()
          elif alt==6:
            alterar_prev()
          alt=0
      elif op==4:
        excluir_ordem()
      elif op==5:
        listar_ordens()
      op=ord_serv()
  elif start==4:
    op=sobre()
    while op!=0:
      op=sobre()  
  start=menu()    
else:
  print('Programa encerrado!')
  print()
  
    
    
arq_dados = open("dados.dat", "wb")
pickle.dump(dados, arq_dados)
arq_dados.close()

arq_servicos = open("servicos.dat", "wb")
pickle.dump(servicos, arq_servicos)
arq_servicos.close()

arq_ordens = open("ordens.dat", "wb")
pickle.dump(ordens, arq_ordens)
arq_ordens.close()
