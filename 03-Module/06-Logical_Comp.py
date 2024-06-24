#!/bi/python

#Os operadores de comparação são utilizados para comparar valores

# ==
# !=
# >
# <
# >=
# <=

Valor1 = 50
Valor2 = 40

comparacao = Valor1 == Valor2

print(comparacao)

comparacao = Valor1 != Valor2

print(comparacao)


# AND
# OR
# NOT

# 100 == 100 AND 200 == 200 # True
# 100 == 100 AND 100 == 200 AND 400 == 400 # False

# 100 == 100 OR 200 == 200 # True
# 200 == 100 OR 200 == 200 # True
# 200 == 100 OR 100 == 200 OR 400 == 400 # TRUE
# 200 == 100 OR 100 == 200 OR 300 == 400 #False