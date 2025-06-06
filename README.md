![image](https://github.com/yagojardimm/Trab-estrutura-de-dados/assets/134665777/0e4c999d-15b7-4b8a-ac69-aab319ffca37)

# Curso: Engenharia de Software 
# Disciplina: Estrutura de Dados Avançados
# <a href='https://github.com/marciogarridoLaCop'>Professor: Marcio Alexandre Dias Garrido</a>
# Período: 4° Período
  
# 🚀 Simulador de Rotas Interestelares - Missão Garrido

Este projeto simula o planejamento de rotas interestelares entre planetas e objetos do universo do filme **Interestelar**, considerando o efeito da **dilatação temporal** de acordo com a gravidade de cada local.

A nave parte da Terra e precisa chegar ao Planeta Edmunds dentro de uma **restrição máxima de tempo terrestre**.

## 🔍 Funcionalidades

- Representação gráfica do sistema estelar com:
  - Terra, Saturno, Gargantua, Miller, Mann e Edmunds.
- Cálculo do **tempo na nave** e **tempo na Terra** ao percorrer diferentes rotas.
- Algoritmo de **Dijkstra** para encontrar o caminho que minimiza o tempo na Terra.
- Consideração de **fatores de dilatação temporal** por região.
- Visualização com **matplotlib** com suporte a animação da rota otimizada.

## 🧠 Conceitos Utilizados

- **Teoria da Relatividade**: tempo passa mais devagar em regiões com gravidade intensa.
- **Grafos com NetworkX**: cada planeta é um nó, as rotas são arestas com pesos.
- **Dijkstra**: otimiza a rota com menor custo de tempo na Terra.
- **Animação com matplotlib**: visualização elegante da trajetória da nave.

## 📁 Estrutura do Código

- `main.py`: contém a lógica de criação do grafo, cálculo dos tempos, algoritmo de Dijkstra e visualização.
- `criar_sistema_interestelar_cenario()`: monta o grafo com nós e arestas personalizados.
- `calcular_tempos_caminho_final()`: soma o tempo da nave e da Terra para um caminho específico.
- `encontrar_rota_dijkstra_otimizando_terra()`: encontra a melhor rota respeitando o tempo máximo.
- `visualizar_cenario_interestelar()`: plota o grafo e anima o trajeto da nave.
## 📦 Requisitos
Python 3.7+

networkx

matplotlib
instalar as dependências com: pip install -r requirements.txt


## 🧪 Exemplo de Uso

```python
grafo = criar_sistema_interestelar_cenario()
caminho, tempo_nave, tempo_terra, ok = encontrar_rota_dijkstra_otimizando_terra(
    grafo, origem="Terra", destino="Planeta Edmunds", max_tempo_terra=100
)

visualizar_cenario_interestelar(grafo, caminho_otimizado=caminho)
