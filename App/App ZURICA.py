#conexão do banco de dados
from genericpath import exists
import os
import shutil
import sys
import mysql.connector # modulo que faz coneção com mysql
from PyQt5 import uic,QtWidgets # MODULO GRAFICO UTILIZADO
from PyQt5.QtWidgets import QMessageBox
meubanco=mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="",
    database="cadastrod"
)
#-------------------------------------------------
#-------------------------------------------------
#-------------------------------------------------
#-------------------------------------------------
#FUNÇOES DO SISTEMA
#Esta função tem como objetivo, de separar o acesso de admin ou user
def escolha_usuario():
    if tela_escolha.ESCOLHA01.isChecked():
        tela_escolha.close()
        tela_login_adm.show()
    if tela_escolha.ESCOLHA02.isChecked():
        tela_escolha.close()
        primeira_tela.show()
#-------------------------------------------------
#-------------------------------------------------
#-------------------------------------------------
#-------------------------------------------------
#abertua e fechamento de tela
def logar_sistema():
    tela_de_cadastro.close()
    primeira_tela.show()
#-------------------------------------------------
#-------------------------------------------------
#-------------------------------------------------
#-------------------------------------------------
#valida no banco de dados se usuario pode logar no sistema.
def logar_usuario():
    primeira_tela.label_5.setText("")
    nome_user = primeira_tela.nomel.text()
    senha_user = primeira_tela.senhal.text()
    cursor = meubanco.cursor()
    try:
        cursor.execute("SELECT senha FROM zurica WHERE login = '{}'".format(nome_user))
        senha_bf = cursor.fetchall()
        if senha_user == senha_bf[0][0]:
            primeira_tela.close()
            tela_abrir.show()
        else:
            primeira_tela.label_5.setText("            Usúario invalido!!!")
    except:
         primeira_tela.label_5.setText("            Usúario invalido!!!")
#-------------------------------------------------
#-------------------------------------------------
#-------------------------------------------------
#-------------------------------------------------
#Valida o acesso do usuario admin
def logar_adm():
    tela_login_adm.escrita.setText("")
    nome_adm=tela_login_adm.nomel.text()
    senha_adm = tela_login_adm.senhal.text()
    if nome_adm == "zurica" and senha_adm == "123":
        tela_login_adm.close()
        tela_de_cadastro.show()
    else:
        tela_login_adm.escrita.setText("           Usúario invalido!!!")
#-------------------------------------------------
#-------------------------------------------------
#-------------------------------------------------
#-------------------------------------------------
#faz o cadastro do usuario via banco de dados
def cadastro():
    c_nome = tela_de_cadastro.nomeint.text()
    c_login = tela_de_cadastro.login.text()
    c_senha1 = tela_de_cadastro.senha1.text()
    c_senha2 = tela_de_cadastro.senha2.text()
    if (c_senha1 == c_senha2) and len(c_senha1) > 3 and len(c_nome) > 3 and len(c_login) > 3:
        try:
            cursor = meubanco.cursor()
            comando_sql = "insert into zurica(nome,login,senha)values(%s,%s,%s)"
            dados = (f"{c_nome}", f"{c_login}", f"{c_senha1}")
            cursor.execute(comando_sql, dados)
            meubanco.commit()
            QMessageBox.about(tela_de_cadastro, "ALERTA", "Cadastro realizado com sucesso!!!")
        except:
            print("erro")
    else:
        QMessageBox.about(tela_de_cadastro, "ALERTA", "Não atendeu os criterios de cadastro ou campo vazio!!!")
#-------------------------------------------------
#-------------------------------------------------
#-------------------------------------------------
#-------------------------------------------------
#carrega a planilha para um arquivo txt a qual vai ser tabulado
def carrega_plan():
    tela_abrir.label.setText("")
    planilha_aberta = QtWidgets.QFileDialog.getOpenFileName()[0]
    try:
        arquivo = planilha_aberta
        with open(arquivo, 'r') as file:
            dados = file.readlines()
        with open('igor.txt', 'w') as registros:
            for dado in dados:
                registros.write(dado)
        tela_abrir.label.setText(arquivo)
    except:
        print("voltou")
#-------------------------------------------------
#-------------------------------------------------
#-------------------------------------------------
#-------------------------------------------------
#abre e fecha tela
def escolha_cpca():
    tela_escolha_ordem.close()
    tela_escolhacpca.show()
#-------------------------------------------------
#-------------------------------------------------
#-------------------------------------------------
#-------------------------------------------------
#abre e fecha tela
def voltar_tela_login():
    tela_abrir.close()
    primeira_tela.show()
#-------------------------------------------------
#-------------------------------------------------
#-------------------------------------------------
#-------------------------------------------------
#abre fecha tela
def proxima_tela_abrir():
    tela_abrir.close()
    tela_escolha_ordem.show()

def voltar_tela_abrir():
    tela_escolha_ordem.close()
    tela_abrir.show()
    
    
def coluna_valor():
    global e_data,e_banco,e_historico,e_conta,e_valor
    e_data = tela_escolha_ordem.data1.value()
    e_banco = tela_escolha_ordem.banco1.value()
    e_conta = tela_escolha_ordem.conta1.value()
    e_valor = tela_escolha_ordem.valor1.value()
    e_historico = tela_escolha_ordem.historico.value()
    if e_data != e_banco and e_conta and e_historico and e_valor:
        tela_escolha_ordem.close()
        tela_escolhacpca.show()
    else:
      QMessageBox.about(tela_escolhacpca, "ALERTA", "posições das colunas incorretas")
 
#-------------------------------------------------
#-------------------------------------------------
#-------------------------------------------------
#-------------------------------------------------
#faz a tabulação do arquivo txt tanto do arquivo a pagar como o a receber
def gerando_tab():
    global e_conta,e_banco,e_data,e_historico,e_valor
    if tela_escolhacpca.ESCOLHA02.isChecked():
       if os.path.exists('igor.txt'):
        tabulacao_txt = open('igor.txt','r')
        linhas = tabulacao_txt.read().split("\n")
        try:
            arquivo_tb = open('tabulação.txt',"wt")
            indice="0"
            if len(linhas)>0:
                for indice in range(len(linhas)):
                    tentativa = linhas[indice].split(';')
                    data = tentativa[e_data].lstrip()
                    cliente=tentativa[e_conta].lstrip()
                    historico = tentativa[e_historico].lstrip()
                    valor = tentativa[e_valor].lstrip().replace(".","")
                    banco = tentativa[e_banco]
                    arquivo_tb.write(str(indice+1).expandtabs(7).zfill(7))
                    arquivo_tb.write(str(data).expandtabs(9))
                    arquivo_tb.write(str(banco).rjust(7))
                    arquivo_tb.write(str(cliente).rjust(7))
                    arquivo_tb.write(str(valor).zfill(17).rjust(17).replace(",","."))
                    arquivo_tb.write(str("00143"+historico).expandtabs(2).zfill(2)+('\n'))
                arquivo_tb.close()
            else:
                QMessageBox.about(tela_escolhacpca, "ALERTA", "Posiçoes das colunas incorretas,voltar a tela anterior")
        except:
            print("gerou")
            tela_escolhacpca.close()
            tela_nome.show()
    if tela_escolhacpca.ESCOLHA01.isChecked():
        if os.path.exists('igor.txt'):
            tabulacao_txt = open('igor.txt','r')
            linhas = tabulacao_txt.read().split("\n")
        try:
            arquivo_tb = open('tabulação.txt',"wt")
            if len(linhas)>0:
                indice="0"
                for indice in range(len(linhas)):
                    tentativa = linhas[indice].split(';')
                    data = tentativa[e_data].lstrip()
                    fornecedor=tentativa[e_conta].lstrip()
                    historico = tentativa[e_historico].lstrip()
                    valor = tentativa[e_valor].lstrip().replace(".","")
                    banco = tentativa[e_banco]
                    arquivo_tb.write(str(indice+1).expandtabs(7).zfill(7))
                    arquivo_tb.write(str(data).expandtabs(9))
                    arquivo_tb.write(str(fornecedor).rjust(7))
                    arquivo_tb.write(str(banco).rjust(7))
                    arquivo_tb.write(str(valor).zfill(17).rjust(17).replace(",","."))
                    arquivo_tb.write(str("00155"+historico).expandtabs(2).zfill(2)+('\n'))
                arquivo_tb.close()
            else:
                print('erro')
        except:
            print("gerou")
            tela_escolhacpca.close()
            tela_nome.show()
#-------------------------------------------------
#-------------------------------------------------
#-------------------------------------------------
#------------------------------------------------- 
#abre e fecha e tela
def voltar_nome(): 
    tela_nome.close()
    tela_escolhacpca.show()
#-------------------------------------------------
#-------------------------------------------------
#-------------------------------------------------
#------------------------------------------------- 
# renomea o arquivo e muda a instensão do arquivo txt e muda seu diretorio
def mudar_nome():
    nome_arq = tela_nome.nomel.text()
    nova_pasta =r"E:\\Projeto integrador\\Aplicativo_zurica\\App\\arquivo final"
    if not os.path.exists(nova_pasta):
        os.makedirs(nova_pasta)
    try:
         os.rename(r"E:\\Projeto integrador\\Aplicativo_zurica\\App\\tabulação.txt",r"E:\\Projeto integrador\\Aplicativo_zurica\\App\\arquivo final\\{}.M21".format(nome_arq.upper()))
    except:
        print('erro')

    tela_nome.close()
    tela_final.show()
    teste =r"C:\Users\Igor Monteiro\Downloads\Arquivo final"
    try:
        shutil.rmtree(teste)
    except OSError as e:
        print(e)
#-------------------------------------------------
#-------------------------------------------------
#-------------------------------------------------
#-------------------------------------------------
# muda pra pasta de download  
def dowload():
    try:
        origem = r"E:\\Projeto integrador\\Aplicativo_zurica\\App\\Arquivo final"
        destino = r"C:\\Users\\Igor Monteiro\\Downloads"
        shutil.move(origem,destino)
        QMessageBox.about(tela_final, "ALERTA", "Download feito com sucesso na pasta arquivo final!!!")
    except:
        QMessageBox.about(tela_final, "ALERTA", "Download feito com sucesso na pasta arquivo final!!!")
#------------------------------------------------- 
#-------------------------------------------------
#-------------------------------------------------
#-------------------------------------------------
#reinicia o processo
def novo():
    tela_final.close()
    tela_abrir.show()
#-------------------------------------------------
#-------------------------------------------------
#-------------------------------------------------
#-------------------------------------------------
#MODULO GRAFICO UTILIZADO
aplicativo = QtWidgets.QApplication([])
#-------------------------------------------------
#-------------------------------------------------
#-------------------------------------------------
#-------------------------------------------------
#IMPORTAÇÃO DA TELAS
tela_escolha = uic.loadUi("tela_escolha.ui")
tela_login_adm=uic.loadUi("tela_login_adm.ui")
primeira_tela=uic.loadUi("primeira_tela.ui")
tela_de_cadastro=uic.loadUi("tela_de_cadastro.ui")
tela_abrir=uic.loadUi("tela_abrir.ui")
tela_escolhacpca=uic.loadUi("tela_escolhacpca.ui")
tela_nome=uic.loadUi("tela_nome.ui")
tela_final=uic.loadUi("download.ui")
tela_escolha_ordem=uic.loadUi("tela_escolhaORDEM.ui")
#-------------------------------------------------
#-------------------------------------------------
#-------------------------------------------------
#-------------------------------------------------
#INTERAÇÃO COM OS  BOTÕES DAS TELAS
tela_escolha.botaoescolha.clicked.connect(escolha_usuario)
tela_login_adm.entrar.clicked.connect(logar_adm)
primeira_tela.entrar.clicked.connect(logar_usuario)
tela_de_cadastro.cadastro.clicked.connect(cadastro)
tela_de_cadastro.pushButton_2.clicked.connect(logar_sistema)
tela_abrir.antl.clicked.connect(voltar_tela_login)
tela_abrir.abrir.clicked.connect(carrega_plan)
tela_abrir.pt.clicked.connect(proxima_tela_abrir)
tela_escolhacpca.voltar.clicked.connect(proxima_tela_abrir)
tela_escolhacpca.botaoescolha.clicked.connect(gerando_tab)
tela_nome.antl.clicked.connect(voltar_nome)
tela_nome.pt.clicked.connect(mudar_nome)
tela_final.dow.clicked.connect(dowload)
tela_final.new_2.clicked.connect(novo)
tela_escolha_ordem.coluna1.clicked.connect(voltar_tela_abrir)
tela_escolha_ordem.coluna2.clicked.connect(coluna_valor)
#-------------------------------------------------
#-------------------------------------------------
#-------------------------------------------------
#-------------------------------------------------
tela_escolha.show()
aplicativo.exec()

