'''
  este programa encuentra el maximo comun divisor de dos numeros A y B
  con A > B con el algoritmo de euclides tomando que

  mcd(A,0) = A
  mcd(0,B) = B

  si A mod B = r entonces mcd(A,B)=mcd(B,r)
'''

def maximo_comun_divisor(a, b):
  if a < b:
    a, b = b, a
  while b != 0:
    r = a % b
    a = b
    b = r
  return a
  
a = int(input('Proporcione el valor de A: '))
b = int(input('Proporcione el valor de B: '))

print(f'Maximo comun divisor de {a} y {b} es: {maximo_comun_divisor(a, b)}')