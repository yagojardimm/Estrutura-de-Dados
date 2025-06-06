![image](https://github.com/yagojardimm/Trab-estrutura-de-dados/assets/134665777/0e4c999d-15b7-4b8a-ac69-aab319ffca37)

# Curso: Engenharia de Software 
# Disciplina: Estrutura de Dados Avançados
# <a href='https://github.com/marciogarridoLaCop'>Professor: Marcio Alexandre Dias Garrido</a>
# Período: 4° Período
  
## 🌌 Simulador de Rotas Interestelares: Missão Garrido (Nemesis Protocol)
🚀 Visão Geral do Projeto
A humanidade está à beira do colapso. A Terra, sufocada por décadas de exploração e poluição, busca uma segunda chance entre as estrelas. O Simulador de Rotas Interestelares: Missão Garrido é a ferramenta vital para essa esperança.

Inspirado no universo de "Interstellar", este projeto Python modela o sistema solar como um grafo e utiliza o Algoritmo de Dijkstra para encontrar a rota mais eficiente para o nosso novo lar potencial, o Planeta Edmunds. O grande desafio: otimizar o tempo decorrido na Terra, considerando os efeitos da dilatação temporal em cada região do espaço, e garantir que a missão possa impactar a geração atual antes que a situação na Terra se torne irreversível.

Este projeto simula a complexidade do planejamento de rotas interestelares, priorizando a otimização temporal crítica para a sobrevivência da humanidade.

## 📖 O Storytelling da Missão Garrido

A "Missão Garrido" é uma corrida contra o tempo para encontrar um novo lar para a humanidade, já que a Terra está em colapso devido à exploração e poluição. Após o fracasso de várias sondas do "Projeto Lázaro Prime" em encontrar planetas habitáveis, a sonda Lázaro-12 enviou um sinal promissor do "Planeta Edmunds", acendendo uma nova esperança.

O desafio é encontrar a rota mais eficiente para Edmunds, otimizando o tempo terrestre (impactado pela dilatação temporal) para que a missão seja concluída em menos de 200 anos terrestres. A solução encontrada envolve o uso do "Algoritmo de Dijkstra", que modela o sistema estelar como um grafo, onde planetas são nós e rotas são arestas com pesos baseados nos tempos de nave e terrestre.

O projeto utiliza uma visualização animada em Python para demonstrar a rota otimizada, que, de acordo com os cálculos, levará 5 anos de tempo de navegação e apenas 7 anos de tempo terrestre, atendendo à restrição crítica e oferecendo um novo capítulo para a humanidade.

## ✨ Funcionalidades
Modelagem de Grafo Interstelar: Representação dos planetas e pontos de interesse como nós e rotas como arestas em um grafo.

Cálculo de Tempo Duplo: Consideração do tempo de navegação (para a tripulação) e o tempo decorrido na Terra (afetado pela dilatação temporal) em cada trecho da rota.

Otimização de Rota com Dijkstra: Utilização do algoritmo de Dijkstra para encontrar o caminho que minimiza o tempo total decorrido na Terra.

Fatores de Dilatação Temporal: Inclusão de fatores de dilatação temporal específicos para cada região do espaço, simulando efeitos gravitacionais (como em Gargantua e Miller).

Visualização Dinâmica: Geração de um mapa estelar interativo com matplotlib, mostrando os nós (planetas/locais) e as arestas (rotas), com cores distintas para cada tipo de local.

Animação da Rota Otimizada: Animação do caminho encontrado pelo algoritmo de Dijkstra, destacando a sequência ideal para a navegação.

Verificação de Restrição Temporal: Validação se a rota otimizada se encaixa dentro de um limite máximo de tempo terrestre permitido para a missão.

## 💡 Conceitos Utilizados
Teoria da Relatividade (Dilatação Temporal): O tempo passa mais devagar em regiões com alta gravidade. Este conceito é fundamental para calcular o "tempo na Terra" em contraste com o "tempo de nave".

Teoria dos Grafos com NetworkX: O sistema interestelar é modelado como um grafo (rede) onde:

Nós (Nodes): Representam planetas e pontos de interesse (Terra, Saturno (BM), Sist. Gargantua, Miller (Órbita), Mann (Órbita), Planeta Edmunds, Gargantua (Manobra)).

Arestas (Edges): Representam as rotas entre esses pontos, com pesos (custos) associados.

Algoritmo de Dijkstra: Um algoritmo clássico de busca de caminho mais curto em grafos ponderados, utilizado aqui para encontrar a rota que minimiza o tempo total na Terra.

Matplotlib: Biblioteca de visualização em Python, usada para criar o mapa estelar e animar a rota da nave.**
