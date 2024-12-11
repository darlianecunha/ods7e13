import streamlit as st
import numpy as np
import matplotlib.pyplot as plt

# Função para calcular a pontuação final
def calculate_final_score(scores):
    max_score = len(scores) * 3  # pontuação máxima se todas as variáveis tiverem nota 3
    total_score = sum(scores)
    percentage_score = (total_score / max_score) * 100
    return percentage_score

# Função para plotar o gráfico radar
def plot_radar_chart(scores, categories):
    if len(scores) != len(categories):
        st.error("O número de pontuações e categorias não coincide.")
        return None
    
    values = scores + scores[:1]  # Repetir o primeiro valor para fechar o círculo
    angles = np.linspace(0, 2 * np.pi, len(scores), endpoint=False).tolist()
    angles += angles[:1]  # Repetir o primeiro ângulo para fechar o gráfico

    fig, ax = plt.subplots(figsize=(10, 10), subplot_kw=dict(polar=True))
    ax.fill(angles, values, color='teal', alpha=0.25)
    ax.plot(angles, values, color='teal', linewidth=2)
    ax.set_yticklabels([])
    ax.set_xticks(angles[:-1])
    ax.set_xticklabels(categories)
    return fig

# Definir variáveis agrupadas por ODS com prefixos

variables = {
"ODS 7": [
{"name": "7.1 Número de programas de conscientização em uso racional de energia", "options": [
"0: Nenhum programa em operação.",
"1: Até 2 programas em operação, atingindo até 100 pessoas.",
"2: 3-5 programas em operação, atingindo 101-500 pessoas.",
"3: Mais de 5 programas em operação, atingindo mais de 500 pessoas."
]},
{"name": "7.2 Número de programas de gestão de eficiência energética", "options": [
"0: Nenhum programa em operação.",
"1: Pelo menos um programa, resultando em até 5% de redução no consumo de energia.",
"2: Pelo menos um programa, resultando em uma redução maior que 5% e menor ou igual a 10% no consumo de energia.",
"3: Pelo menos um programa com reduções no consumo de energia superiores a 10%."
]},
{"name": "7.3 Número de iniciativas de inovação tecnológica em eficiência energética", "options": [
"0: Nenhuma iniciativa.",
"1: Até 2 iniciativas tecnológicas implementadas.",
"2: 3-5 iniciativas tecnológicas implementadas.",
"3: Mais de 5 iniciativas implementadas."
]},
{"name": "7.4 Percentual de energia renovável contratada e produzida em instalações portuárias", "options": [
"0: Nenhum uso de energia renovável.",
"1: Até 10% da energia utilizada é renovável.",
"2: Mais de 10% até 50% da energia usada é renovável.",
"3: Mais de 50% da energia usada é renovável."
]},
{"name": "7.5 Percentual de biocombustíveis em cargas elétricas e mecânicas", "options": [
"0: Nenhum uso de biocombustíveis.",
"1: Menos de 5% das cargas são operadas com biocombustíveis.",
"2: 5% a 20% das cargas são operadas com biocombustíveis.",
"3: Mais de 20% das cargas são operadas com biocombustíveis."
]},
{"name": "7.6 Número de iniciativas de inovação tecnológica em energia renovável", "options": [
"0: Nenhuma iniciativa.",
"1: Até 2 iniciativas na fase de planejamento ou piloto.",
"2: 3-5 iniciativas na fase de implementação com resultados preliminares.",
"3: Mais de 5 iniciativas em plena operação com resultados comprovados."
]},
{"name": "7.7. Diversidade de fontes de energia renovável em instalações portuárias", "options": [
"0: Nenhum uso de fontes renováveis.",
"1: Uso de 1 tipo diferente de energia renovável.",
"2: Uso de 2 tipos diferentes de energia renovável.",
"3: Uso de 3 ou mais tipos diferentes de energia renovável."
]},
{"name": "7.8 Quantidade de parcerias para promoção de energia limpa", "options": [
"0: Nenhuma parceria estabelecida.",
"1: Até 2 parcerias estabelecidas com foco em energia limpa.",
"2: 3-5 parcerias estabelecidas com foco em energia limpa.",
"3: Mais de 5 parcerias estabelecidas com foco em energia limpa."
]},
{"name": "7.9 Quantidade de estações de carregamento para veículos elétricos", "options": [
"0: Nenhuma estação de carregamento disponível.",
"1: Até 5 estações de carregamento disponíveis.",
"2: 6-15 estações de carregamento disponíveis.",
"3: Mais de 15 estações de carregamento disponíveis."
]},
{"name": "7.10 Percentual de fornecimento de energia renovável para navios", "options": [
"0: Nenhum fornecimento de energia renovável para navios.",
"1: Menos de 10% do fornecimento de energia para navios vem de fontes renováveis.",
"2: Entre 10% e 30% do fornecimento de energia para navios vem de fontes renováveis.",
"3: Mais de 30% do fornecimento de energia para navios vem de fontes renováveis."
]},
{"name": "7.11 Percentual de abastecimento com GNL", "options": [
"0: Nenhum abastecimento de GNL.",
"1: Menos de 5% do fornecimento total de combustível é com GNL.",
"2: Entre 5% e 20% do fornecimento total de combustível é com GNL.",
"3: Mais de 20% do fornecimento total de combustível é com GNL."
]},
{"name": "7.12 Número de iniciativas de inovação tecnológica em atendimento elétrico e energético para navios", "options": [
"0: Nenhuma iniciativa.",
"1: Até 2 iniciativas de inovação tecnológica em fase de planejamento ou piloto.",
"2: 3-5 iniciativas em fase de implementação ou avaliação de eficácia.",
"3: Mais de 5 iniciativas em plena operação, com resultados de eficácia comprovados."
]},
{"name": "7.13 Quantidade de navios usando energia renovável no porto", "options": [
"0: Nenhum navio utiliza energia renovável.",
"1: Até 5% dos navios no porto utilizam energia renovável.",
"2: 5% a 15% dos navios no porto utilizam energia renovável.",
"3: Mais de 15% dos navios no porto utilizam energia renovável."
]},
{"name": "7.14 Tarifas diferenciadas para navios com desempenho acima dos padrões ambientais", "options": [
"0: Nenhuma aplicação de tarifas diferenciadas.",
"1: Até 5% de desconto nas tarifas portuárias.",
"2: 5% a 15% de desconto nas tarifas portuárias.",
"3: Mais de 15% de desconto nas tarifas portuárias."
]}

],

"ODS 13": [
{"name": "13.1 Status do Plano de Estratégia para Mudança Climática", "options": [
"0: Nenhuma estratégia.",
"1: Plano estratégico em desenvolvimento, sem ações implementadas.",
"2: Plano estratégico implementado, com algumas ações em prática.",
"3: Plano estratégico totalmente operacional, com revisão e atualizações regulares."
]},
{"name": "13.2 Inventário de Emissões", "options": [
"0: Inventário de emissões não realizado.",
"1: Inventário de emissões realizado, mas desatualizado.",
"2: Inventário de emissões realizado, atualizado há mais de um ano.",
"3: Inventário de emissões atualizado anualmente e ativamente utilizado para gestão de emissões."
]},
{"name": "13.3 Programa de Gestão de Créditos de Carbono", "options": [
"0: Nenhum programa de créditos de carbono.",
"1: Programa em fase inicial, sem créditos gerados ou adquiridos.",
"2: Programa ativo, com créditos de carbono sendo gerados ou adquiridos.",
"3: Programa bem estabelecido, com créditos de carbono sendo ativamente geridos."
]},
{"name": "13.4 Programa de Monitoramento Climático", "options": [
"0: Programa inexistente.",
"1: Programa em fase de implementação.",
"2: Programa implementado, mas dados usados de forma limitada.",
"3: Programa implementado e integrado a um sistema de resposta e planejamento climático."
]},
{"name": "13.5 Número de Colaborações e Parcerias para Ação Climática", "options": [
"0: Nenhuma colaboração ou parceria estabelecida.",
"1: Até 2 colaborações ou parcerias estabelecidas.",
"2: 3-5 colaborações ou parcerias com resultados iniciais.",
"3: Mais de 5 colaborações ou parcerias com impacto significativo e mensurável na ação climática."
]},
{"name": "13.6 Infraestrutura Resiliente ao Clima", "options": [
"0: Nenhuma infraestrutura avaliada como resiliente ao clima.",
"1: Menos de 25% da infraestrutura avaliada como resiliente ao clima.",
"2: De 25-50% da infraestrutura avaliada como resiliente ao clima.",
"3: Mais de 50% da infraestrutura avaliada como resiliente ao clima e adaptada."
]},
{"name": "13.7 Índice de Eficiência do Tráfego de Carga", "options": [
"0: Índice não calculado.",
"1: Índice de eficiência abaixo da média do setor.",
"2: Índice de eficiência na média do setor.",
"3: Índice de eficiência acima da média do setor, com melhorias contínuas."
]},
{"name": "13.8 Percentual de Redução de Emissões por Meio da Implementação de Novas Tecnologias", "options": [
"0: Nenhum programa de redução de emissões.",
"1: Redução de emissões inferior a 5% por meio de novas tecnologias.",
"2: Redução de 5-10% das emissões por meio de novas tecnologias.",
"3: Redução de mais de 10% das emissões por meio de novas tecnologias."
]}

]}


    
# Título da aplicação
st.markdown("<h1 style='color: darkgreen;'> Atributos ODS 7 e 13</h1>", unsafe_allow_html=True)

# Criação de abas para SDG 7 e 13
tab1, tab2 = st.tabs(["ODS 7", "ODS 13"])

# Função para exibir conteúdo de cada aba
def display_ods_tab(ods_group):
    st.header(f"{ods_group}")
    scores = []
    categories = []
    for variable in variables[ods_group]:
        option = st.selectbox(variable["name"], options=variable["options"])
        scores.append(int(option[0]))  # Converte o primeiro caractere da opção selecionada em inteiro
        prefix = variable["name"].split(" ")[0]
        categories.append(prefix)

    if len(scores) != len(categories):
        st.error("Erro: O número de pontuações e categorias não coincide.")
        return

    # Calcula a pontuação final
    percentage_score = calculate_final_score(scores)
    st.write(f"Final Score {ods_group}: {percentage_score:.2f}%")

    # Exibe o gráfico radar
    st.subheader("Gráfico Radar")
    radar_chart = plot_radar_chart(scores, categories)
    if radar_chart:
        st.pyplot(radar_chart)

# Exibe as variáveis e resultados para cada aba
with tab1:
    display_ods_tab("ODS 7")

with tab2:
    display_ods_tab("ODS 13")

    
# Rodapé com fonte e créditos
st.write("---")
st.markdown(
    "<p><strong>Ferramenta desenvolvida por Darliane Cunha.</strong></p>", 
    unsafe_allow_html=True
)



