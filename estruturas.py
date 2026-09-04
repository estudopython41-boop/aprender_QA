
"""os_teste = ["login válido", "login inválido", "login sem senha"]

for i, v enumerate(casos_teste):
    print(list(enumerate(casos_teste)))

casos_teste = ["login válido", "login inválido", "login sem senha"]

for i, v in enumerate(casos_teste):
    print(f"caso{i + 1} : {v}")


codigos_sucesso = {200, 201, 204}

codigo_recebido = 201

# Uso do 'in', identação e ':' ajustados
if codigo_recebido in codigos_sucesso:
    print(f"código {codigo_recebido}: de sucesso!")
else:
    print(f"código {codigo_recebido} não era esperado.")"""

erros_criticos = [500, 502, 503]
codigo = 404

if codigo not in erros_criticos:
    print(f"codigo {codigo} não é um erro crítico de servidor.")

