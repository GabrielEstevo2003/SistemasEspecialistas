import unidecode

refeicoes = [
    {"Nome": "Omelete de Legumes", "Tipo": "cafe da manha", "Restricao": "vegetariano"},
    {"Nome": "Panqueca de Banana", "Tipo": "cafe da manha", "Restricao": "vegano"},
    {"Nome": "Torta de Frango", "Tipo": "cafe da manha", "Restricao": "nenhuma"},
    {"Nome": "Omelete de Espinafre", "Tipo": "cafe da manha", "Restricao": "sem lactose"},
    {"Nome": "Panqueca de Amêndoa", "Tipo": "cafe da manha", "Restricao": "low carb"},

    {"Nome": "Salada de Grao de Bico", "Tipo": "jantar", "Restricao": "vegano"},
    {"Nome": "Bife", "Tipo": "jantar", "Restricao": "nenhuma"},
    {"Nome": "Peixe Assado", "Tipo": "jantar", "Restricao": "low carb"},
    {"Nome": "Sopa de Abóbora com Gengibre", "Tipo": "jantar", "Restricao": "sem lactose"},
    {"Nome": "Ovos Cozidos", "Tipo": "jantar", "Restricao": "vegetariano"},

    {"Nome": "Legumes no Vapor", "Tipo": "almoco", "Restricao": "low carb"},
    {"Nome": "Salada de Atum com Abacate", "Tipo": "almoco", "Restricao": "sem lactose"},
    {"Nome": "Peito de Frango", "Tipo": "almoco", "Restricao": "nenhuma"},
    {"Nome": "Sopa de Feijão", "Tipo": "almoco", "Restricao": "vegano"},
    {"Nome": "Risoto de Legumes", "Tipo": "almoco", "Restricao": "vegetariano"},
]

regras = [
    {"Condicao": {"Tipo": "cafe da manha", "Restricao": "vegetariano"}, "Recomendacao": ["Omelete de Legumes"]},
    {"Condicao": {"Tipo": "cafe da manha", "Restricao": "vegano"}, "Recomendacao": ["Panqueca de Banana"]},
    {"Condicao": {"Tipo": "cafe da manha", "Restricao": "nenhuma"}, "Recomendacao": ["Torta de Frango"]},
    {"Condicao": {"Tipo": "cafe da manha", "Restricao": "low carb"}, "Recomendacao": ["Panqueca de Amêndoa"]},
    {"Condicao": {"Tipo": "cafe da manha", "Restricao": "sem lactose"}, "Recomendacao": ["Omelete de Espinafre"]},

    {"Condicao": {"Tipo": "jantar", "Restricao": "vegetariano"}, "Recomendacao": ["Ovos Cozidos"]},
    {"Condicao": {"Tipo": "jantar", "Restricao": "vegano"}, "Recomendacao": ["Salada de Grao de Bico"]},
    {"Condicao": {"Tipo": "jantar", "Restricao": "nenhuma"}, "Recomendacao": ["Bife"]},
    {"Condicao": {"Tipo": "jantar", "Restricao": "low carb"}, "Recomendacao": ["Peixe Assado"]},
    {"Condicao": {"Tipo": "jantar", "Restricao": "sem lactose"}, "Recomendacao": ["Sopa de Abóbora com Gengibre"]},

    {"Condicao": {"Tipo": "almoco", "Restricao": "sem lactose"}, "Recomendacao": ["Salada de Atum com Abacate"]},
    {"Condicao": {"Tipo": "almoco", "Restricao": "low carb"}, "Recomendacao": ["Legumes no Vapor"]},
    {"Condicao": {"Tipo": "almoco", "Restricao": "vegetariano"}, "Recomendacao": ["Risoto de Legumes"]},
    {"Condicao": {"Tipo": "almoco", "Restricao": "vegano"}, "Recomendacao": ["Sopa de Feijão"]},
    {"Condicao": {"Tipo": "almoco", "Restricao": "nenhuma"}, "Recomendacao": ["Peito de Frango"]},
]


def recomendar_refeicoes(preferencias):
    recomendacoes = []
    for regra in regras:
        condicao = regra["Condicao"]
        if (preferencias["Tipo"] == condicao["Tipo"] and
                preferencias["Restricao"] == condicao["Restricao"]):
            recomendacoes.extend(regra["Recomendacao"])
    return recomendacoes


def main():
    print("============SISTEMA ESPECIALISA: PREFERÊNCIA DE REFEIÇÃO============")

    opcoes_tipo = ["cafe da manha", "almoco", "jantar"]
    opcoes_restricao = ["nenhuma", "vegetariano", "vegano", "low carb", "sem lactose"]

    print("Tipos Disponiveis:", ", ".join(opcoes_tipo))
    tipo = input("Qual refeição você deseja? ").strip().lower()
    tipo = unidecode.unidecode(tipo)


    print("Restrições Disponiveis:", ", ".join(opcoes_restricao))
    restricao = input("Qual e sua restricao?").strip().lower()
    restricao = unidecode.unidecode(restricao)

    if tipo not in opcoes_tipo or restricao not in opcoes_restricao:
        print("Opção Inválida. Tente Novamente.")
        return

    preferencias = {"Tipo": tipo, "Restricao": restricao}

    refeicoes_recomendadas = recomendar_refeicoes(preferencias)

    if refeicoes_recomendadas:
        print("\nRefeições Recomendadas:")
        for r in refeicoes_recomendadas:
            print(f"De acordo com sua escolha: ({tipo} e {restricao}), eu lhe recomendo esse prato:")
            print(f"- {r}")
    else:
        print("\nNenhuma Refeicção para Recomendar!")


if __name__ == "__main__":
    main()

