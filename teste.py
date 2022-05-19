from time import sleep
print("-=-"* 20)
print("  Seja bem-vindo a companhia de logística Gabriel Medeiros")
print("-=-"* 20)
print("             Informe os dados do objeto abaixo")
print("-=-" * 20)
try:
   comprimento = int(input("Digite o comprimento:"))
   largura = int(input("Digite a largura:"))
   altura = int(input("Digite a altura:"))
   dimensao = comprimento * largura * altura

   if dimensao >= 100000:
      print("Não aceitamos objetos tão grandes.")
   else:
      print("             \033[32mO volume do seu produto é {}cm³\033[m".format(dimensao))
   print("-=-" * 20)
except:
   print("Você não digitou um número")

if dimensao <= 1000:
      valor = 10

if dimensao >=1001 <10000:
      valor = 20

if dimensao >=10001 <30000:
      valor = 30

if dimensao >=30001 <100000:
      valor = 50

peso = float(input("Digite o peso (kg):"))
print("                 \033[32mO seu objeto pesa {:.0f}kg\033[m".format(peso))
print("-=-" * 20)
if peso <= 0.1:
      multi = 1

if peso > 0.1 <1:
      multi = 1.5

if peso >1 <10:
      multi = 2

if peso >10 <30:
      multi = 3

if peso >= 30:
      print("Não aceitamos objetos tão pesados.")

calcular= valor * multi

print("Nossas rotas disponíveis são (ESCOLHA USANDO UM NÚMERO):"
         "\n1 - Rio de Janeiro ate São Paulo"
         "\n2 - Brasilia ate São Paulo"
         "\n3 - Rio de Janeiro ate Brasilia")
rota = int(input("Escolha sua rota:"))
print("-=-" * 20)
if rota == 1:
   RS=1
if rota == 2:
   RS= 1.2
if rota == 3:
   RS= 1.5

calcular2 = calcular * RS
print("    **Analisando as informações e calculando o preço**")
sleep(2)
print("           \033[32mO preço total a pagar é de R${:.2f}\033[m".format(calcular2))
print("-=-" * 20)
