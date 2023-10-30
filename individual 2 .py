# Lista de candidatos e seus resultados
candidatos = {
    "Candidato 1": "e5_t10_p8_s8",
    "Candidato 2": "e10_t7_p7_s8",
    "Candidato 3": "e8_t5_p4_s9",
    "Candidato 4": "e2_t2_p2_s1",
    "Candidato 5": "e10_t10_p8_s9"
}

# Função para buscar candidatos com base nas notas mínimas
def buscar_candidatos(notas_minimas):
    candidatos_selecionados = []

    for candidato, resultado in candidatos.items():
        # Divida a string de resultado em partes e converta em inteiros
        partes = resultado.split("_")
        notas = [int(part[1:]) for part in partes]

        # Verifique se todas as notas são maiores ou iguais às notas mínimas
        if all(nota >= minima for nota, minima in zip(notas, notas_minimas)):
            candidatos_selecionados.append(candidato)

    return candidatos_selecionados

# Solicita as notas mínimas ao usuário
e_min = int(input("Nota mínima de entrevista (e): "))
t_min = int(input("Nota mínima de teste teórico (t): "))
p_min = int(input("Nota mínima de teste prático (p): "))
s_min = int(input("Nota mínima de soft skills (s): "))

# Chama a função para buscar candidatos com base nas notas mínimas
candidatos_selecionados = buscar_candidatos([e_min, t_min, p_min, s_min])

# Exibe os candidatos encontrados
if candidatos_selecionados:
    print("Candidatos que atendem aos critérios:")
    for candidato in candidatos_selecionados:
        print(candidato)
else:
    print("Nenhum candidato atende aos critérios especificados.")
    