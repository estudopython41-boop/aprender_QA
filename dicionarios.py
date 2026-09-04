
"""usuario = {
"nome": "ana",
"idade": 25,
"ativo": "True"
}
print(usuario.items())
for valor in usuario.items():
    print(valor)"""

resposta_api = {
    "status_code": 200,
    "mensagem": "sucesso",
    "tempo_resposta": 120
}

# Corrigido o !== para !=
if resposta_api["status_code"] != 200:
    print("Erro na API")

# Removida a crase depois de resposta_api
print("tempo de resposta", resposta_api["tempo_resposta"])