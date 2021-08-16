#conexão do banco de dados
import os
import mysql.connector # modulo que faz coneção com mysql
from PyQt5 import uic,QtWidgets # MODULO GRAFICO UTILIZADO
from PyQt5.QtWidgets import QMessageBox
meubanco=mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="",
    database="usuarios"
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
        cursor.execute("SELECT senha FROM cadastro WHERE login = '{}'".format(nome_user))
        senha_bf = cursor.fetchall()
        if senha_user == senha_bf[0][0]:
            primeira_tela.close()
            tela_abrir.show()
        else:
            primeira_tela.label_5.setText("Dados digitados incorretos!!!")
    except:
         primeira_tela.label_5.setText("           Usúario invalido!!!")
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
            comando_sql = "insert into cadastro(nome,login,senha)values(%s,%s,%s)"
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
        print("erro")
#-------------------------------------------------
#-------------------------------------------------
#-------------------------------------------------
#-------------------------------------------------
#abre e fecha tela
def escolha_cpca():
    tela_abrir.close()
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
def voltar_tela_abrir():
    tela_escolhacpca.close()
    tela_abrir.show()
#-------------------------------------------------
#-------------------------------------------------
#-------------------------------------------------
#-------------------------------------------------
#faz a tabulação do arquivo txt tanto do arquivo a pagar como o a receber
def gerando_tab():
    if tela_escolhacpca.ESCOLHA02.isChecked():
       if os.path.exists('igor.txt'):
        tabulacao_txt = open('igor.txt','r')
        linhas = tabulacao_txt.read().split("\n")
        try:
            arquivo_tb = open('clientetab.txt',"wt")
            if len(linhas)>0:
                for indice in range(len(linhas)):
                    tentativa = linhas[indice].split(';')
                    data = tentativa[0].lstrip()
                    cliente=tentativa[1].lstrip()
                    historico = tentativa[2].lstrip()
                    valor = tentativa[3].lstrip().replace(".","")
                    banco = tentativa[4]
                    arquivo_tb.write(str(indice+1).expandtabs(8).zfill(7))
                    arquivo_tb.write(str(data).expandtabs(9))
                    arquivo_tb.write(str(banco).rjust(7))
                    arquivo_tb.write(str(cliente).rjust(7))
                    arquivo_tb.write(str(valor).zfill(18).rjust(18).replace(",","."))
                    arquivo_tb.write(str("    "+historico).expandtabs(49)+('\n'))
                arquivo_tb.close()
            else:
                print('erro')
        except:
            print("mudança")
            tela_escolhacpca.close()
            tela_nome.show()
    if tela_escolhacpca.ESCOLHA01.isChecked():
        if os.path.exists('igor.txt'):
            tabulacao_txt = open('igor.txt','r')
            linhas = tabulacao_txt.read().split("\n")
        try:
            arquivo_tb = open('fornecedortb.txt',"wt")
            if len(linhas)>0:
                for indice in range(len(linhas)):
                    tentativa = linhas[indice].split(';')
                    data = tentativa[0].lstrip()
                    fornecedor=tentativa[1].lstrip()
                    historico = tentativa[2].lstrip()
                    valor = tentativa[3].lstrip().replace(".","")
                    banco = tentativa[4]
                    arquivo_tb.write(str(indice+1).expandtabs(8).zfill(7))
                    arquivo_tb.write(str(data).expandtabs(9))
                    arquivo_tb.write(str(fornecedor).rjust(7))
                    arquivo_tb.write(str(banco).rjust(7))
                    arquivo_tb.write(str(valor).zfill(18).rjust(18).replace(",","."))
                    arquivo_tb.write(str("    "+historico).expandtabs(49)+('\n'))
                arquivo_tb.close()
            else:
                print('erro')
        except:
            print("mudança")
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
def mudar_nome():
    nome_arq = tela_nome.nomel.text()
    print(nome_arq)


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
tela_abrir.pt.clicked.connect(escolha_cpca)
tela_escolhacpca.voltar.clicked.connect(voltar_tela_abrir)
tela_escolhacpca.botaoescolha.clicked.connect(gerando_tab)
tela_nome.antl.clicked.connect(voltar_nome)
tela_nome.pt.clicked.connect(mudar_nome)
#-------------------------------------------------
#-------------------------------------------------
#-------------------------------------------------
#-------------------------------------------------
tela_escolha.show()
aplicativo.exec()

