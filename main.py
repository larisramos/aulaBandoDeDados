import sqlite3
nomeBD = input("Nome do Banco de Dados: ")
conector = sqlite3.connect(nomeBD)
cursor = conector.cursor()
cursor.execute('create table agenda (id intenger, nome text, fone text)')
id = 1
nome = "Pessoa"
while nome != "":
  print ("id: ",id)
  nome = input("Nome: ")
  if nome != "":
    fone = input("Fone: ")
    cursor.execute('insert into agenda (id, nome, fone) values (?, ?, ?)', (id, nome, fone))
    conector.commit()
    id = id + 1
cursor.close()
conector.close()
print("Banco de Dados foi CRIADO: ",nomeBD)
  