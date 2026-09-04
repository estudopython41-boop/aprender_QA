# Ambientes de teste fixos

"""ambientes = ("desenvolvimento", "homologação", "produção")
print(ambientes[0]) # desenvolvimento
print(ambientes[1]) # homologação
print(ambientes[2]) # produção
print(ambientes[-1]) # produção (indice negativo)

# códigos HTTP de sucesso esperado
codigo_sucesso =(200, 201, 204)

# Tipos mistos (permitido)
dado_mistro = ("QA", 3, True,)

# para criar uma tupla precisa de () e ,
#Correto
ambiente = ("produção",)

#errado - é uma apenas uma string entre parênteses
ambiente = ("produção")

# usando lista - risco de altereação acidental
urls = ["https://dev.api.com", "https://hml.api.com", "https://api.com"]
urls[2] = "https://hml.api.com" #TypeError imediato

# Usando tupla - protegido contra alteraçaõ
urls = ["https://dev.api.com", "https://hml.api.com", "https://api.com"]
urls[2] = "https://hml.api.com" #TypeError imediato

codigos_sucesso = [200, 201, 204]

print(len(codigos_sucesso))

for codigo in codigos_sucesso:
    print(f"validando código {codigo}")


CONFIG_BANCO = ("localhost", 5432, "qa_database")
host = CONFIG_BANCO[0]
port = CONFIG_BANCO[1]
user = CONFIG_BANCO[2]"""


