import streamlit as st
import numpy as np
import matplotlib.pyplot as plt

# Função para calcular a pontuação final
def calculate_final_score(scores):
    max_score = len(scores) * 3  # Pontuação máxima se todas as variáveis tiverem nota 3
    total_score = sum(scores)
    percentage_score = (total_score / max_score) * 100 if max_score > 0 else 0
    return percentage_score

# Função para plotar o gráfico radar
def plot_radar_chart(scores, categories):
    if len(scores) != len(categories):
        st.error("O número de pontuações e categorias não coincide.")
        return None

    values = scores + scores[:1]  # Repetir o primeiro valor para fechar o círculo
    angles = np.linspace(0, 2 * np.pi, len(scores), endpoint=False).tolist()
    angles += angles[:1]  # Repetir o primeiro ângulo para fechar o gráfico

    fig, ax = plt.subplots(figsize=(8, 8), subplot_kw=dict(polar=True))
    ax.fill(angles, values, color='teal', alpha=0.25)
    ax.plot(angles, values, color='teal', linewidth=2)
    ax.set_yticklabels([])
    ax.set_xticks(angles[:-1])
    ax.set_xticklabels(categories)
    return fig

# Definir variáveis agrupadas por ODS com prefixos

variaveis = {
"ODS 7":[
    {
        "nome": "7.1 Número de programas de conscientização em uso racional de energia",
       "opções": [
            "0: Nenhum programa em operação.",
            "1: Até 2 programas em operação, atingindo até 100 pessoas.",
            "2: 3-5 programas em operação, atingindo 101-500 pessoas.",
            "3: Mais de 5 programas em operação, atingindo mais de 500 pessoas."
        ]
    },

    {
        "nome": "7.2 Número de programas de gestão de eficiência energética",
       "opções": [
            "0: Nenhum programa em operação.",
            "1: Pelo menos um programa, resultando em até 5% de redução no consumo de energia.",
            "2: Pelo menos um programa, resultando em uma redução maior que 5% e menor ou igual a 10% no consumo de energia.",
            "3: Pelo menos um programa com reduções no consumo de energia superiores a 10%."
        ]
    },
    {
        "nome": "7.3 Número de iniciativas de inovação tecnológica em eficiência energética",
       "opções": [
            "0: Nenhuma iniciativa.",
            "1: Até 2 iniciativas tecnológicas implementadas.",
            "2: 3-5 iniciativas tecnológicas implementadas.",
            "3: Mais de 5 iniciativas implementadas."
        ]
    },
    {
        "nome": "7.4 Percentual de energia renovável contratada e produzida em instalações portuárias",
        "options": [
            "0: Nenhum uso de energia renovável.",
            "1: Até 10% da energia utilizada é renovável.",
            "2: Mais de 10% até 50% da energia usada é renovável.",
            "3: Mais de 50% da energia usada é renovável."
        ]
    },
    {
        "nome": "7.5 Percentual de biocombustíveis em cargas elétricas e mecânicas",
        "opções": [
            "0: Nenhum uso de biocombustíveis.",
            "1: Menos de 5% das cargas são operadas com biocombustíveis.",
            "2: 5% a 20% das cargas são operadas com biocombustíveis.",
            "3: Mais de 20% das cargas são operadas com biocombustíveis."
        ]
    },
    {
        "nome": "7.6 Número de iniciativas de inovação tecnológica em energia renovável",
        "opções": [
            "0: Nenhuma iniciativa.",
            "1: Até 2 iniciativas na fase de planejamento ou piloto.",
            "2: 3-5 iniciativas na fase de implementação com resultados preliminares.",
            "3: Mais de 5 iniciativas em plena operação com resultados comprovados."
        ]
    },
    {
        "nome": "7.7 Diversidade de fontes de energia renovável em instalações portuárias",
        "opções": [
            "0: Nenhum uso de fontes renováveis.",
            "1: Uso de 1 tipo diferente de energia renovável.",
            "2: Uso de 2 tipos diferentes de energia renovável.",
            "3: Uso de 3 ou mais tipos diferentes de energia renovável."
        ]
    },
    {
        "nome": "7.8 Quantidade de parcerias para promoção de energia limpa",
        "opções": [
            "0: Nenhuma parceria estabelecida.",
            "1: Até 2 parcerias estabelecidas com foco em energia limpa.",
            "2: 3-5 parcerias estabelecidas com foco em energia limpa.",
            "3: Mais de 5 parcerias estabelecidas com foco em energia limpa."
        ]
    },
    {
        "nome": "7.9 Quantidade de estações de carregamento para veículos elétricos",
        "opções": [
            "0: Nenhuma estação de carregamento disponível.",
            "1: Até 5 estações de carregamento disponíveis.",
            "2: 6-15 estações de carregamento disponíveis.",
            "3: Mais de 15 estações de carregamento disponíveis."
        ]
    },
    {
        "nome": "7.10 Percentual de fornecimento de energia renovável para navios",
        "opções": [
            "0: Nenhum fornecimento de energia renovável para navios.",
            "1: Menos de 10% do fornecimento de energia para navios vem de fontes renováveis.",
            "2: Entre 10% e 30% do fornecimento de energia para navios vem de fontes renováveis.",
            "3: Mais de 30% do fornecimento de energia para navios vem de fontes renováveis."
        ]
    },
    {
        "nome": "7.11 Percentual de abastecimento com GNL",
        "opções": [
            "0: Nenhum abastecimento de GNL.",
            "1: Menos de 5% do fornecimento total de combustível é com GNL.",
            "2: Entre 5% e 20% do fornecimento total de combustível é com GNL.",
            "3: Mais de 20% do fornecimento total de combustível é com GNL."
        ]
    },
    {
        "name": "7.12 Número de iniciativas de inovação tecnológica em atendimento elétrico e energético para navios",
        "options": [
            "0: Nenhuma iniciativa.",
            "1: Até 2 iniciativas de inovação tecnológica em fase de planejamento ou piloto.",
            "2: 3-5 iniciativas em fase de implementação ou avaliação de eficácia.",
            "3: Mais de 5 iniciativas em plena operação, com resultados de eficácia comprovados."
        ]
    },
    {
        "name": "7.13 Quantidade de navios usando energia renovável no porto",
        "opções": [
            "0: Nenhum navio utiliza energia renovável.",
            "1: Até 5% dos navios no porto utilizam energia renovável.",
            "2: 5% a 15% dos navios no porto utilizam energia renovável.",
            "3: Mais de 15% dos navios no porto utilizam energia renovável."
        ]
    },
    {
        "name": "7.14 Tarifas diferenciadas para navios com desempenho acima dos padrões ambientais",
        "opções": [
            "0: Nenhuma aplicação de tarifas diferenciadas.",
            "1: Até 5% de desconto nas tarifas portuárias.",
            "2: 5% a 15% de desconto nas tarifas portuárias.",
            "3: Mais de 15% de desconto nas tarifas portuárias."
        ]
    }
],

    "ODS 8":[
        {
            "nome": "8.1 Ausências devido ao absenteísmo relacionado à saúde",
            "opções": [
                "0: Ausências superiores a 5% do total de horas trabalhadas.",
                "1: Ausências entre 3% e 5%.",
                "2: Ausências entre 1% e 3%.",
                "3: Ausências inferiores a 1%."
            ]
        },
        {
            "nome": "8.2 Afastamentos por doenças ocupacionais",
            "opções": [
                "0: Mais de 10 casos por 100 funcionários.",
                "1: Entre 6 e 10 casos.",
                "2: Entre 2 e 5 casos.",
                "3: Menos de 2 casos."
            ]
        },
        {
            "nome": "8.3 Afastamentos por acidentes",
            "opções": [
                "0: Mais de 10 casos por 100 funcionários.",
                "1: Entre 6 e 10 casos.",
                "2: Entre 2 e 5 casos.",
                "3: Menos de 2 casos."
            ]
        },
        {
            "nome": "8.4 Número de acidentes",
            "opções": [
                "0: Mais de 15 acidentes por 100 funcionários.",
                "1: Entre 10 e 15 acidentes.",
                "2: Entre 5 e 10 acidentes.",
                "3: Menos de 5 acidentes."
            ]
        },
        {
            "nome": "8.5 Acidentes fatais",
            "opções": [
                "0: Qualquer acidente fatal.",
                "1: Sem acidentes fatais, mas com alta taxa de acidentes graves (> 5 por 100 funcionários).",
                "2: Baixa taxa de acidentes graves (1-5 por 100 funcionários).",
                "3: Sem acidentes graves."
            ]
        },
        {
            "nome": "8.6 Percentual de trabalhadores locais em cargos de gestão",
            "opções": [
                "0: Menos de 20%.",
                "1: Entre 20% e 30%.",
                "2: Entre 30,1% e 40%.",
                "3: Mais de 50%."
            ]
        },
        {
            "nome": "8.7 Percentual de mulheres empregadas",
            "opções": [
                "0: Menos de 20%.",
                "1: Igual ou superior a 20% e inferior a 30%.",
                "2: Igual ou superior a 30% e inferior a 50%.",
                "3: Igual ou superior a 50%."
            ]
        },
        {
            "nome": "8.8 Percentual de jovens empregados (14 a 24 anos)",
            "opções": [
                "0: Menos de 5%.",
                "1: Igual ou superior a 5% e inferior a 10%.",
                "2: Igual ou superior a 10% e inferior a 15%.",
                "3: Igual ou superior a 15%."
            ]
        },
        {
            "nome": "8.9 Percentual de funcionários com deficiência",
            "opções": [
                "0: Menos de 2%.",
                "1: Igual ou superior a 2% e inferior a 4%.",
                "2: Igual ou superior a 4% e inferior a 6%.",
                "3: Igual ou superior a 6%."
          ]
        }
    ],
 
   "ODS 9": [
        {
            "nome": "9.1 Número de patentes depositadas e concedidas no INPI (Instituto Nacional da Propriedade Industrial)",
            "opções": [
                "0: Nenhuma patente depositada no ano.",
                "1: Até 2 patentes depositadas no ano, com patentes concedidas.",
                "2: De 3 a 5 patentes depositadas no ano, com patentes concedidas.",
                "3: Mais de 5 patentes depositadas no ano, com patentes concedidas."
            ]
        },
        {
            "nome": "9.2 Número de publicações em periódicos de alto impacto financiadas pelo porto",
            "opções": [
                "0: Nenhuma iniciativa ou resultado significativo.",
                "1: Até 2 publicações em periódicos de alto impacto.",
                "2: De 3 a 5 publicações em periódicos de alto impacto.",
                "3: Mais de 5 publicações em periódicos de alto impacto."
            ]
        },
        {
            "nome": "9.3 Número de prêmios e selos de qualidade relacionados à Inovação",
            "opções": [
                "0: Nenhuma iniciativa ou resultado significativo.",
                "1: Recebimento de até 2 prêmios ou selos de qualidade em inovação.",
                "2: Recebimento de 3 a 5 prêmios ou selos de qualidade em inovação.",
                "3: Recebimento de mais de 5 prêmios ou selos de qualidade em inovação."
            ]
        },
        {
            "nome": "9.4 Posição no ranking de inovação do setor portuário",
            "opções": [
                "0: Posição no quarto quartil no ranking de inovação.",
                "1: Posição no terceiro quartil no ranking de inovação.",
                "2: Posição no segundo quartil no ranking de inovação.",
                "3: Posição no primeiro quartil no ranking de inovação."
            ]
        },
        {
            "nome": "9.5 Nível médio de maturação de inovação por projeto",
            "opções": [
                "0: Nenhum projeto.",
                "1: Projetos em fase de conceito inicial ou desenvolvimento com baixo nível de maturação.",
                "2: Projetos em fase de protótipo ou piloto com nível médio de maturação.",
                "3: Projetos com produtos finais ou soluções implementadas com alto nível de maturidade tecnológica (Technology Readiness Levels)."
            ]
        },
        {
            "nome": "9.6 Diversidade de áreas de conhecimento em projetos de pesquisa aplicada",
            "opções": [
                "0: Nenhuma área de conhecimento envolvida nos projetos.",
                "1: Até 2 áreas de conhecimento envolvidas nos projetos.",
                "2: De 3 a 5 áreas de conhecimento diferentes envolvidas nos projetos.",
                "3: Mais de 5 áreas de conhecimento diferentes envolvidas nos projetos."
            ]
        },
        {
            "nome": "9.7 Percentual de operações automatizadas no porto",
            "opções": [
                "0: Nenhuma operação automatizada.",
                "1: Até 25% das operações automatizadas.",
                "2: De 25% a 50% das operações automatizadas.",
                "3: Mais de 50% das operações automatizadas."
            ]
        },
        {
            "nome": "9.8 Número de acordos com universidades e centros de pesquisa ou projetos financiados",
            "opções": [
                "0: Nenhum acordo ou projeto.",
                "1: Até 2 acordos ou projetos.",
                "2: De 3 a 5 acordos ou projetos estabelecidos.",
                "3: Mais de 5 acordos ou projetos."
            ]
        },
        {
            "nome": "9.9 Número de pesquisadores externos da instituição portuária ou universidade vinculados a projetos de inovação",
            "opções": [
                "0: Nenhum pesquisador externo vinculado.",
                "1: Até 3 pesquisadores externos vinculados.",
                "2: De 4 a 6 pesquisadores externos vinculados.",
                "3: Mais de 6 pesquisadores externos vinculados."
            ]
        },
        {
            "nome": "9.10 Número de empresas parceiras em projetos de inovação",
            "opções": [
                "0: Nenhuma empresa parceira.",
                "1: Até 2 empresas parceiras envolvidas.",
                "2: De 3 a 5 empresas parceiras envolvidas.",
                "3: Mais de 5 empresas parceiras com colaboração efetiva e contribuições significativas."
            ]
        },
        {
            "nome": "9.11 Número de startups apoiadas focadas em soluções inovadoras",
            "opções": [
                "0: Nenhuma startup.",
                "1: Apoio a até 2 startups.",
                "2: Apoio a 3-5 startups.",
                "3: Apoio a mais de 5 startups."
            ]
        },
        {
            "nome": "9.12 Número de acordos com outros portos ou terminais para a promoção da inovação",
            "opções": [
                "0: Nenhum acordo.",
                "1: Até 2 acordos.",
                "2: De 3 a 5 acordos.",
                "3: Mais de 5 acordos."
  ]
        }
    ],

        "ODS 11": [
            {
                "nome": "11.1 Número de reclamações relacionadas ao impacto ambiental e social do porto",
                "opções": [
                    "0: Mais de 10 reclamações anuais.",
                    "1: De 5 a 10 reclamações anuais, com ações de mitigação.",
                    "2: De 2 a 4 reclamações anuais, com ações de mitigação.",
                    "3: Até 1 reclamação anual, com ações de mitigação."
                ]
            },
            {
                "nome": "11.2 Valor do Índice de Controle de Ruído do Porto",
                "opções": [
                    "0: Nenhuma medição do índice.",
                    "1: Índice acima do limite permitido por lei.",
                    "2: Índice dentro dos limites permitidos por lei.",
                    "3: Índice 10% abaixo do limite permitido por lei."
                ]
            },
            {
                "nome": "11.3 Número de projetos de sustentabilidade direcionados à comunidade",
                "opções": [
                    "0: Nenhum projeto.",
                    "1: Até 2 projetos em andamento.",
                    "2: De 3 a 5 projetos em andamento, com impacto inicial comprovado.",
                    "3: Mais de 5 projetos em andamento, com impacto significativo e comprovadamente sustentável."
                ]
            },
            {
                "nome": "11.4 Quantidade de áreas verdes ou espaços públicos desenvolvidos ou mantidos pelo porto",
                "opções": [
                    "0: Nenhuma área verde.",
                    "1: Menos de 10% do espaço total.",
                    "2: Entre 10% e 30% do espaço total.",
                    "3: Mais de 30% do espaço total."
                ]
            },
            {
                "nome": "11.5 Valor total dos investimentos em infraestrutura da comunidade local (estradas, iluminação, saneamento, outros)",
                "opções": [
                    "0: Nenhum investimento.",
                    "1: O investimento total representa menos de 5% do orçamento do porto.",
                    "2: O investimento total representa entre 5% e 10% do orçamento do porto.",
                    "3: O investimento total representa mais de 10% do orçamento do porto."
                ]
            },
            {
                "nome": "11.6 Número de programas ou parcerias para mobilidade sustentável",
                "opções": [
                    "0: Nenhum programa.",
                    "1: Até 2 programas ou parcerias estabelecidas.",
                    "2: De 3 a 5 programas ou parcerias estabelecidas.",
                    "3: Mais de 5 programas ou parcerias estabelecidas."
                ]
            },
            {
                "nome": "11.7 Número de iniciativas de engajamento comunitário pelo porto",
                "opções": [
                    "0: Nenhuma iniciativa.",
                    "1: Até 3 iniciativas de engajamento.",
                    "2: De 4 a 6 iniciativas de engajamento.",
                    "3: Mais de 6 iniciativas de engajamento com ampla cobertura e alta participação da comunidade."
                      ]
        }
    ],


"ODS 12": [
            {
                "nome": "12.1 Valor da Concentração de Poluentes Atmosféricos",
                "opções": [
                    "0: Nenhuma medição de poluentes realizada.",
                    "1: Concentrações de poluentes até 10% acima dos padrões estabelecidos.",
                    "2: Concentrações de poluentes dentro dos padrões estabelecidos.",
                    "3: Concentrações de poluentes 10% abaixo dos padrões estabelecidos."
                ]
            },
            {
                "nome": "12.2 Volume total de água utilizada",
                "opções": [
                    "0: Nenhum controle sobre o uso da água.",
                    "1: Uso de água acima do limite concedido.",
                    "2: Uso de água igual ao limite concedido.",
                    "3: Uso de água 10% abaixo do limite concedido."
                ]
            },
            {
                "nome": "12.3 Volume total de água reutilizada",
                "opções": [
                    "0: Nenhum reaproveitamento de água.",
                    "1: Menos de 10% do total de água utilizada é reutilizada.",
                    "2: Entre 10% e 25% do total de água utilizada é reutilizada.",
                    "3: Mais de 25% do total de água utilizada é reutilizada."
                ]
            },
            {
                "nome": "12.4 Número de acidentes ambientais registrados internamente",
                "opções": [
                    "0: Nenhuma medição para registro de acidentes ambientais.",
                    "1: Dois ou mais acidentes registrados no ano.",
                    "2: Um acidente registrado no ano.",
                    "3: Nenhum acidente ambiental registrado no ano."
                ]
            },
            {
                "nome": "12.5 Quantidade de resíduos gerados",
                "opções": [
                    "0: Nenhum sistema de gestão de resíduos.",
                    "1: Redução de até 5% na geração de resíduos em comparação ao ano anterior.",
                    "2: Redução de 5-10% na geração de resíduos em comparação ao ano anterior.",
                    "3: Redução de mais de 10% na geração de resíduos em comparação ao ano anterior."
                ]
            },
            {
                "nome": "12.6 Percentual de resíduos reciclados e/ou reutilizados",
                "opções": [
                    "0: Nenhuma reciclagem e/ou reutilização de resíduos.",
                    "1: Menos de 30% dos resíduos gerados são reciclados e/ou reutilizados.",
                    "2: Entre 30% e 60% dos resíduos gerados são reciclados e/ou reutilizados.",
                    "3: Mais de 60% dos resíduos gerados são reciclados e/ou reutilizados."
                ]
            },
            {
                "nome": "12.7 Uso de Sistema de Gestão Ambiental",
                "opções": [
                    "0: Nenhum sistema implementado.",
                    "1: Sistema implementado, mas não totalmente integrado às operações diárias.",
                    "2: Sistema implementado e parcialmente integrado às operações diárias.",
                    "3: Sistema totalmente implementado e integrado às operações diárias."
                ]
            },
            {
                "nome": "12.8 Status de Certificação ISO 14000",
                "opções": [
                    "0: Nenhuma iniciativa de certificação.",
                    "1: Não certificado ou em processo de obtenção de certificação.",
                    "2: Certificado, mas sem revisões anuais ou melhorias contínuas.",
                    "3: Certificado com revisões anuais e melhorias contínuas implementadas."
     ]
        }
    ],


"ODS 13": [
    {
        "nome": "13.1 Status do Plano de Estratégia para Mudança Climática",
        "opções": [
            "0: Nenhuma estratégia.",
            "1: Plano estratégico em desenvolvimento, sem ações implementadas.",
            "2: Plano estratégico implementado, com algumas ações em prática.",
            "3: Plano estratégico totalmente operacional, com revisão e atualizações regulares."
        ]
    },
    {
        "nome": "13.2 Inventário de Emissões",
        "opções": [
            "0: Inventário de emissões não realizado.",
            "1: Inventário de emissões realizado, mas desatualizado.",
            "2: Inventário de emissões realizado, atualizado há mais de um ano.",
            "3: Inventário de emissões atualizado anualmente e ativamente utilizado para gestão de emissões."
        ]
    },
    {
        "nome": "13.3 Programa de Gestão de Créditos de Carbono",
        "opções": [
            "0: Nenhum programa de créditos de carbono.",
            "1: Programa em fase inicial, sem créditos gerados ou adquiridos.",
            "2: Programa ativo, com créditos de carbono sendo gerados ou adquiridos.",
            "3: Programa bem estabelecido, com créditos de carbono sendo ativamente geridos."
        ]
    },
    {
        "name": "13.4 Programa de Monitoramento Climático",
        "options": [
            "0: Programa inexistente.",
            "1: Programa em fase de implementação.",
            "2: Programa implementado, mas dados usados de forma limitada.",
            "3: Programa implementado e integrado a um sistema de resposta e planejamento climático."
        ]
    },
    {
        "nome": "13.5 Número de Colaborações e Parcerias para Ação Climática",
        "opções": [
            "0: Nenhuma colaboração ou parceria estabelecida.",
            "1: Até 2 colaborações ou parcerias estabelecidas.",
            "2: 3-5 colaborações ou parcerias com resultados iniciais.",
            "3: Mais de 5 colaborações ou parcerias com impacto significativo e mensurável na ação climática."
        ]
    },
    {
        "name": "13.6 Infraestrutura Resiliente ao Clima",
        "opções": [
            "0: Nenhuma infraestrutura avaliada como resiliente ao clima.",
            "1: Menos de 25% da infraestrutura avaliada como resiliente ao clima.",
            "2: De 25-50% da infraestrutura avaliada como resiliente ao clima.",
            "3: Mais de 50% da infraestrutura avaliada como resiliente ao clima e adaptada."
        ]
    },
    {
        "name": "13.7 Índice de Eficiência do Tráfego de Carga",
        "opções": [
            "0: Índice não calculado.",
            "1: Índice de eficiência abaixo da média do setor.",
            "2: Índice de eficiência na média do setor.",
            "3: Índice de eficiência acima da média do setor, com melhorias contínuas."
        ]
    },
    {
        "nome": "13.8 Percentual de Redução de Emissões por Meio da Implementação de Novas Tecnologias",
        "opções": [
            "0: Nenhum programa de redução de emissões.",
            "1: Redução de emissões inferior a 5% por meio de novas tecnologias.",
            "2: Redução de 5-10% das emissões por meio de novas tecnologias.",
            "3: Redução de mais de 10% das emissões por meio de novas tecnologias."
        ]
    }
],

    "ODS 14": [
        {
            "nome": "14.4 Número de eventos ambientais registrados na costa da região",
            "opções": [
                "0: Nenhum monitoramento de eventos.",
                "1: Mais de 5 eventos ambientais registrados no ano.",
                "2: De 2 a 5 eventos ambientais registrados no ano.",
                "3: 0 a 1 evento ambiental registrado no ano, com respostas rápidas e eficazes."
            ]
        },
        {
            "nome": "14.5 Monitoramento da água de lastro",
            "opções": [
                "0: Sem monitoramento em vigor.",
                "1: Monitoramento inconsistente.",
                "2: Monitoramento regular.",
                "3: Monitoramento sistemático."
            ]
        },
        {
            "nome": "14.6 Área total de habitats marinhos protegidos na área de operação do porto",
            "opções": [
                "0: Nenhum programa de proteção em vigor.",
                "1: Menos de 10% dos habitats marinhos estão sob proteção.",
                "2: 10-25% dos habitats marinhos estão sob proteção.",
                "3: Mais de 25% dos habitats marinhos estão sob proteção, com programas de conservação ativos."
            ]
        },
        {
            "nome": "14.7 Valor total investido em pesquisa de recursos marinhos sustentáveis",
            "opções": [
                "0: Sem investimentos.",
                "1: Investimento inferior a 5% do orçamento total de pesquisa.",
                "2: Investimento de 5-10% do orçamento total de pesquisa.",
                "3: Investimento superior a 10% do orçamento total de pesquisa."
            ]
        },
        {
            "nome": "14.8 Número de projetos de pesquisa marinha financiados pelo porto",
            "opções": [
                "0: Nenhum projeto.",
                "1: Até 2 projetos financiados no ano.",
                "2: De 3 a 5 projetos financiados no ano.",
                "3: Mais de 5 projetos financiados no ano, com colaborações de IES ou centros de pesquisa."
            ]
        }
    ],
   "ODS 17": [
        {
            "nome": "17.1 Status como signatário do Pacto Global da ONU",
            "opções": [
                "0: Não é signatário.",
                "1: Signatário, sem relatório de progresso.",
                "2: Signatário ativo.",
                "3: Signatário ativo, com relatório anual de progresso e metas para melhoria contínua."
            ]
        },
        {
            "nome": "17.2 Alinhamento dos ODS com indicadores IDA e GRI",
            "opções": [
                "0: Nenhum alinhamento documentado.",
                "1: Alinhamento parcial com os ODS.",
                "2: Alinhamento parcial e relatórios regulares sobre o progresso dos ODS.",
                "3: Alinhamento completo e relatórios regulares sobre o progresso dos ODS."
            ]
        },
        {
            "nome": "17.3 Existência de certificação ECOPORTS",
            "opções": [
                "0: Não certificado.",
                "1: Em processo de certificação.",
                "2: Certificado, sem renovação regular.",
                "3: Certificado, com renovação regular e cumprimento de todos os critérios."
            ]
        },
        {
            "nome": "17.4 Publicação do relatório de sustentabilidade",
            "opções": [
                "0: Relatório não publicado.",
                "1: Relatório em fase de implementação.",
                "2: Relatório publicado, mas não em conformidade com os padrões GRI ou equivalente.",
                "3: Relatório publicado e em conformidade com os padrões GRI ou equivalente."
            ]
        },
        {
            "nome": "17.5 Divulgação da posição no IDA",
            "opções": [
                "0: Posição no IDA não divulgada.",
                "1: Posição no IDA divulgada publicamente sem planos de ação para melhoria.",
                "2: Posição no IDA divulgada publicamente.",
                "3: Posição no IDA divulgada publicamente com planos de ação para melhoria."
            ]
        },
        {
            "nome": "17.6 Publicação de indicadores de sustentabilidade",
            "opções": [
                "0: Indicadores não publicados.",
                "1: Indicadores em fase de implementação.",
                "2: Indicadores publicados, mas sem detalhes ou contexto.",
                "3: Indicadores publicados com detalhes, contexto e comparações de desempenho."
            ]
        },
        {
            "nome": "17.7 Registro e comunicação de incidentes ambientais",
            "opções": [
                "0: Sem acompanhamento de registros.",
                "1: Registro e comunicação não sistemáticos.",
                "2: Registro sistemático e comunicação interna.",
                "3: Registro e comunicação sistemáticos, públicos e com ações de resposta."
            ]
        },
        {
            "nome": "17.8 Número de membros independentes no conselho de administração",
            "opções": [
                "0: Nenhum membro independente.",
                "1: Menos de 25% dos membros são independentes.",
                "2: 25-50% dos membros são independentes.",
                "3: Mais de 50% dos membros são independentes."
            ]
        },
        {
            "nome": "17.9 Número de parcerias estabelecidas com ONGs e outras entidades para iniciativas de sustentabilidade",
            "opções": [
                "0: Nenhuma parceria estabelecida.",
                "1: Até 2 parcerias estabelecidas.",
                "2: De 3 a 5 parcerias estabelecidas.",
                "3: Mais de 5 parcerias estabelecidas com projetos em andamento."
            ]
        },
        {
            "nome": "17.10 Listagem de canais de comunicação ativos com stakeholders",
            "opções": [
                "0: Nenhum canal de comunicação.",
                "1: Canais de comunicação limitados ou ineficazes.",
                "2: Alguns canais de comunicação estabelecidos e ativos.",
                "3: Diversos canais de comunicação estabelecidos, ativos e com feedback regular."
            ]
        }
    ]
}
    

# Título da aplicação
st.markdown("<h1 style='color: darkgreen;'> Atributos ODS </h1>", unsafe_allow_html=True)

# Função para exibir conteúdo de cada aba
def display_ods_tab(ods_group):
    st.header(f"{ods_group}")
    scores = []
    categories = []
    for i, variable in enumerate(variaveis[ods_group]):
        try:
            # Validar se as chaves "nome" e "opções" existem
            if "nome" not in variable or "opções" not in variable:
                st.error(f"Erro na configuração da variável na posição {i} do grupo {ods_group}: {variable}")
                continue

            # Exibir selectbox e processar a opção escolhida
            option = st.selectbox(variable["nome"], options=variable["opções"])
            scores.append(int(option.split(":")[0]))  # Extrai o valor numérico da opção
            categories.append(variable["nome"].split(" ")[0])  # Usa o prefixo do nome
        except KeyError as e:
            st.error(f"Erro ao acessar a variável: {e}")
            return
        except ValueError:
            st.error("Erro ao interpretar a opção selecionada.")
            return

    if len(scores) != len(categories):
        st.error("Erro: O número de pontuações e categorias não coincide.")
        return

    # Calcula a pontuação final
    percentage_score = calculate_final_score(scores)
    st.write(f"Pontuação Final ({ods_group}): {percentage_score:.2f}%")

    # Exibe o gráfico radar
    st.subheader("Gráfico Radar")
    radar_chart = plot_radar_chart(scores, categories)
    if radar_chart:
        st.pyplot(radar_chart)

# Criação dinâmica de abas
tab_names = list(variaveis.keys())
tabs = st.tabs(tab_names)

for tab, ods_group in zip(tabs, tab_names):
    with tab:
        display_ods_tab(ods_group)

# Rodapé com fonte e créditos
st.write("---")
st.markdown(
    "<p><strong>Ferramenta desenvolvida por Darliane Cunha.</strong></p>", 
    unsafe_allow_html=True
)

