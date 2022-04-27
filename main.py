from maxHeap import MaxHeap
from Paciente import Paciente
from Pilha import Pilha
import os

chegada = 999
fila = MaxHeap()
ultimosAtendidos = Pilha()

while True:
    print("----------------------------------------------")
    print("")
    print("Adicionar um paciente [1]")
    print("Chamar proximo [2]")
    print("Mostrar o proximo [3]")
    print("Listar os 5 ultimos [4]")
    print("Encerrar o programa [0]")
    resp = input()
    try:
        resp = int(resp)
    except:
        pass

    os.system('cls')
    if resp == 1:
        paciente = Paciente()
        chegada = chegada - 1

        print("----------CADASTRO DE PACIENTE-----------")

        paciente.nome = input("Insira o nome completo do paciente: ")
        paciente.tipoSanguineo = input("Insira o tipo sanguineo do paciente: ")
        paciente.dataNascimento = input("Insira a data de nascimento do paciente: ")
        
        print("De 1 a 10, qual o nivel de prioridade do atendimento?")
        print("MENOS URGENTE: 1 | MAIS URGENTE: 10")
        urgencia = int(input())
        if urgencia >= 1 or urgencia <= 10:
            ordem = (urgencia, chegada, paciente)
            try:
                fila.put(ordem)
            except TypeError:
                print("Erro ao cadastrar paciente, tente novamente")
        else:
            print("Erro ao cadastrar paciente, tente novamente")
    elif resp == 2:
        try:
            atender = fila.get()
            print(atender[2].nome, "compareça a sala de atendimento.")
            ultimosAtendidos.push(atender)
        except TypeError:
            print("Parece que a fila esta vazia")
    elif resp == 3:
        proximo = fila.peek()
        print(proximo[2].nome, "é o proximo da fila.")
    elif resp == 4:
        ultimosAtendidos.peek5()
        input("press ENTER")
    elif resp == 0:
        break
    else:
        print("Insira um valor valido!!")