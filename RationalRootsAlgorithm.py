import time

# algoritmo para descobrir as raízes racionais de um polinômio.
def briot_ruffini(coefficients: list[int], likely_roots: list[int], lenght_coefficients: int) -> None:
  resultado = coefficients[0]
  for i in likely_roots:
    root = i
    for j in range(1, lenght_coefficients):
      coefficient = coefficients[j]
      resultado = resultado * root + coefficient

    if resultado == 0:
      print('-'*25)
      print('Raiz racional encontrada')
      print(f'A raiz racional é: {root}')
      print('-'*25)

    resultado = coefficients[0] 
  return

def main() -> None:
  num_of_coefficients:int = int(input("Quantos coeficientes tem o polinômio? "))
  #num_of_coefficients = n_coef

  coefficients:list[int] = [int(input(f"Digite o {i+1}º coeficiente: ")) for i in range(num_of_coefficients)]
  #coefficients = coef

  # descobrir P e Q.
  P = coefficients[-1]
  Q = coefficients[0]
  divisors_of_p = []
  divisors_of_q = []

  if P < 0:
    P *= -1
  elif Q < 0:
    Q *= -1

  # descobrir os os divisíveis de P e Q.
  for i in range(1, P + 1):
    if P % i == 0:
      divisors_of_p.append(P / i)
      divisors_of_p.append(P / i * -1)

  for i in range(1, Q + 1):
    if Q % i == 0:
      divisors_of_q.append(Q / i)
      divisors_of_q.append(Q / i * -1)

  likely_roots = divisors_of_p + divisors_of_q

  likely_roots = set(likely_roots)
  likely_roots = list(likely_roots)

  briot_ruffini(coefficients, likely_roots, len(coefficients))

#start_time = time.time()

main()

# Marca o tempo de término
#end_time = time.time()

# Calcula e imprime o tempo de execução
#execution_time = end_time - start_time
#print(f"O tempo de execução do código foi: {execution_time:.6f} segundos")