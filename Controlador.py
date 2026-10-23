nome = input("Nome do time: ")
quant = int(input("Quantidade de partidas: "))
empate = 0
vitoria = 0
derrota = 0
total_feito = 0
total_sofrido = 0
for c in range(1, quant + 1):
  print(f"====== PARTIDA {c} =======")
  gols_feitos = int(input("Gols feitos: "))
  gols_sofridos = int(input("Gols sofridos: "))
  print(f"Gols feitos: {gols_feitos}")
  print(f"Gols sofridos: {gols_sofridos}")
  total_sofrido += gols_sofridos
  total_feito += gols_feitos
  if gols_feitos > gols_sofridos:
    vitoria += 1
  elif gols_feitos == gols_sofridos:
    empate += 1
  else:
    derrota += 1
print(f"========= Relatorio do time: {nome} =========")
saldo = total_feito - total_sofrido

print(f"Saldo de gols: {saldo}")
print(f"Vitorias: {vitoria}")
print(f"Empates: {empate}")
print(f"Derrotas: {derrota}")
print(F"Gols feitos: {total_feito}")
print(f"Gols sofridos: {total_sofrido}")

    
    
  
  
