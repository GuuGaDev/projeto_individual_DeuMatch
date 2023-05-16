#função que contém estrutura condicional e de repetição, tem o objetivo de filtrar os candidatos da lista_candidatos
def filtrar_candidatos(lista_candidatos, nota_min_e, nota_min_t, nota_min_p, nota_min_s):
    candidatos_adeptos = []
    for candidato in lista_candidatos:
        if (candidato['nota_e'] >= nota_min_e and
            candidato['nota_t'] >= nota_min_t and
            candidato['nota_p'] >= nota_min_p and
            candidato['nota_s'] >= nota_min_s):
            candidatos_adeptos.append(candidato)
    return candidatos_adeptos

# Dicionário com os dados dos candidatos
lista_candidatos = [
    {'nome': 'Rafael', 'nota_e': 7, 'nota_t': 9, 'nota_p': 8, 'nota_s': 4},
    {'nome': 'Aline', 'nota_e': 5, 'nota_t': 8, 'nota_p': 7, 'nota_s': 6},
    {'nome': 'Rodrigo', 'nota_e': 6, 'nota_t': 7, 'nota_p': 6, 'nota_s': 9},
    {'nome': 'Maria', 'nota_e': 6, 'nota_t': 6, 'nota_p': 9, 'nota_s': 5},
    {'nome': 'Jose', 'nota_e': 8, 'nota_t': 6, 'nota_p': 7, 'nota_s': 9}
]

# Ler notas mínimas do usuário 
nota_min_e = int(input("Digite a nota mínima da entrevista: "))
nota_min_t = int(input("Digite a nota mínima do teste teórico: "))
nota_min_p = int(input("Digite a nota mínima do teste prático: "))
nota_min_s = int(input("Digite a nota mínima do teste de soft skills: "))

# Encontrar candidatos que o usuário deseja 
candidatos_encontrados = filtrar_candidatos(lista_candidatos, nota_min_e, nota_min_t, nota_min_p, nota_min_s)

# imprimir os resultados 
if len(candidatos_encontrados) > 0:
    print("Os seguintes candidatos atendem aos critérios:")
    for candidato in candidatos_encontrados:
        nome = candidato['nome']
        nota_e = candidato['nota_e']
        nota_t = candidato['nota_t']
        nota_p = candidato['nota_p']
        nota_s = candidato['nota_s']
        print(f"{nome} e_{nota_e}t_{nota_t}p_{nota_p}s_{nota_s}")
else:
    print("Nenhum candidato atende aos requisitos")