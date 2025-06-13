# MATRIZ DE DISTÂNCIAS ENTRE CENTROS E DESTINOS (ampliada)
distancias = {
    "Belém": {
        "Manaus": 529, "Porto Alegre": 3193, "Rio de Janeiro": 3245, "Fortaleza": 1615,
        "Curitiba": 3126, "Salvador": 2100, "São Luís": 806, "Belo Horizonte": 2821,
        "Natal": 2101, "Goiânia": 2163
    },
    "Recife": {
        "Manaus": 5698, "Porto Alegre": 3800, "Rio de Janeiro": 2331, "Fortaleza": 800,
        "Curitiba": 3467, "Salvador": 839, "São Luís": 1613, "Belo Horizonte": 2064,
        "Natal": 297, "Goiânia": 2142
    },
    "Brasília": {
        "Manaus": 3490, "Porto Alegre": 2027, "Rio de Janeiro": 1148, "Fortaleza": 2200,
        "Curitiba": 1366, "Salvador": 1445, "São Luís": 1613, "Belo Horizonte": 740,
        "Natal": 2246, "Goiânia": 209
    },
    "São Paulo": {
        "Manaus": 3971, "Porto Alegre": 1114, "Rio de Janeiro": 429, "Fortaleza": 3120,
        "Curitiba": 408, "Salvador": 1962, "São Luís": 2919, "Belo Horizonte": 586,
        "Natal": 2927, "Goiânia": 934
    },
    "Florianópolis": {
        "Manaus": 4442, "Porto Alegre": 458, "Rio de Janeiro": 1144, "Fortaleza": 3617,
        "Curitiba": 300, "Salvador": 2482, "São Luís": 3439, "Belo Horizonte": 1174,
        "Natal": 3427, "Goiânia": 1435
    }
}

# LISTA DE ENTREGAS (exemplo de cenário ampliado)
entregas = [
    {"destino": "Porto Alegre", "prazo": 2, "volume": 500},
    {"destino": "Manaus", "prazo": 4, "volume": 1200},
    {"destino": "Rio de Janeiro", "prazo": 3, "volume": 800},
    {"destino": "Fortaleza", "prazo": 2, "volume": 1000},
    {"destino": "Curitiba", "prazo": 1, "volume": 900},
    {"destino": "Salvador", "prazo": 2, "volume": 700},
    {"destino": "São Luís", "prazo": 2, "volume": 600},
    {"destino": "Belo Horizonte", "prazo": 3, "volume": 1200},
    {"destino": "Natal", "prazo": 2, "volume": 400},
    {"destino": "Goiânia", "prazo": 4, "volume": 900}
]

# PARÂMETROS DOS CAMINHÕES
capacidade_caminhao = 2000  # kg
tempo_max_operacao_horas = 10  # horas
velocidade_media = 80  # km/h (exemplo realista)

# FUNÇÃO PARA ENCONTRAR O CENTRO MAIS PRÓXIMO DE UM DESTINO
def centro_mais_proximo(destino):
    centro, distancia = min(
        ((centro, distancias[centro][destino]) for centro in distancias),
        key=lambda x: x[1]
    )
    return centro, distancia

# FUNÇÃO DE ROTEAMENTO E ALOCAÇÃO DAS ENTREGAS
def roteamento_otimizado(entregas, capacidade_caminhao, tempo_max_operacao_horas, velocidade_media):
    alocacao = {}
    for entrega in entregas:
        destino = entrega["destino"]
        volume = entrega["volume"]
        centro, distancia = centro_mais_proximo(destino)
        tempo_viagem = distancia / velocidade_media  # em horas

        if centro not in alocacao:
            alocacao[centro] = {"entregas": [], "carga_total": 0, "distancia_total": 0, "tempo_total": 0}

        if (
            (alocacao[centro]["carga_total"] + volume) <= capacidade_caminhao
            and (alocacao[centro]["tempo_total"] + tempo_viagem) <= tempo_max_operacao_horas
        ):
            alocacao[centro]["entregas"].append({
                "destino": destino,
                "distancia": distancia,
                "volume": volume,
                "tempo_viagem_horas": round(tempo_viagem, 2)
            })
            alocacao[centro]["carga_total"] += volume
            alocacao[centro]["distancia_total"] += distancia
            alocacao[centro]["tempo_total"] += tempo_viagem
        else:
            print(f"Restrição de tempo ou capacidade excedida no caminhão de {centro} para entrega em {destino}.")

    return alocacao

# EXECUTANDO O ALGORITMO
resultado = roteamento_otimizado(
    entregas,
    capacidade_caminhao,
    tempo_max_operacao_horas,
    velocidade_media
)

# EXIBIÇÃO DOS RESULTADOS
for centro, dados in resultado.items():
    print(f"Centro: {centro}")
    print("  Entregas:")
    for e in dados["entregas"]:
        print(
            f"    - Destino: {e['destino']} | Distância: {e['distancia']} km | "
            f"Volume: {e['volume']} kg | Tempo de Viagem: {e['tempo_viagem_horas']} h"
        )
    print(f"  Carga total alocada: {dados['carga_total']} kg")
    print(f"  Distância total percorrida: {dados['distancia_total']} km")
    print(f"  Tempo total de viagem: {round(dados['tempo_total'], 2)} h\n")
