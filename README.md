![image](https://github.com/yagojardimm/Trab-estrutura-de-dados/assets/134665777/0e4c999d-15b7-4b8a-ac69-aab319ffca37)

# Curso: Engenharia de Software 
# Disciplina: Estrutura de Dados Avançados
# <a href='https://github.com/marciogarridoLaCop'>Professor: Marcio Alexandre Dias Garrido</a>
# Período: 4° Período
  
🌌 Simulador de Rotas Interestelares: Missão Garrido (Nemesis Protocol)
🚀 Visão Geral do Projeto
A humanidade está à beira do colapso. A Terra, sufocada por décadas de exploração e poluição, busca uma segunda chance entre as estrelas. O Simulador de Rotas Interestelares: Missão Garrido é a ferramenta vital para essa esperança.

Inspirado no universo de "Interstellar", este projeto Python modela o sistema solar como um grafo e utiliza o Algoritmo de Dijkstra para encontrar a rota mais eficiente para o nosso novo lar potencial, o Planeta Edmunds. O grande desafio: otimizar o tempo decorrido na Terra, considerando os efeitos da dilatação temporal em cada região do espaço, e garantir que a missão possa impactar a geração atual antes que a situação na Terra se torne irreversível.

Este projeto simula a complexidade do planejamento de rotas interestelares, priorizando a otimização temporal crítica para a sobrevivência da humanidade.

📖 O Storytelling da Missão Garrido
A jornada da humanidade para sobreviver.

Cenário de Crise: A Terra em Agonia
Imaginem um futuro não muito distante. A Terra, nosso lar, clama por socorro. Décadas de exploração desenfreada dos recursos naturais, somadas à poluição implacável, levaram nosso planeta a um ponto de desequilíbrio irreversível. A humanidade, desesperada, olha para as estrelas em busca de uma segunda chance, um novo lar antes que seja tarde demais.

![Terra em Agonia](assets/screenshots/ChatGPT_Image_6_de_jun. de 2025, 01_51_55.png)

A Centelha de Esperança: Projeto Lázaro Prime e os Mundos Desiludidores
Foi nesse cenário de urgência que nasceu o 'Projeto Lázaro Prime'. Um programa audacioso que enviou sondas não tripuladas através do recém-descoberto Portal Estelar perto de Saturno. Por décadas, a comunicação foi esporádica e os dados, muitas vezes, desanimadores. Planetas como o 'Planeta Miller', com sua órbita traiçoeira e dilatação temporal extrema, e o 'Planeta Mann', um mundo gelado e inóspito, enviaram relatórios que, embora cientificamente valiosos, não ofereciam esperança de colonização imediata.

O Sinal Vital: O Triunfo do Planeta Edmunds
No entanto, em meio a essa desilusão, uma das últimas sondas a reportar, a 'Lázaro-12', transmitiu um conjunto de dados surpreendentemente promissor. De um planeta distante, orbitando uma estrela no sistema de Gargantua: o 'Planeta Edmunds'. Mais crucialmente, a Lázaro-12 conseguiu transmitir um 'ping' de confirmação de seu pouso bem-sucedido e leituras ambientais estáveis por um período significativo antes de silenciar – um feito que nenhuma outra sonda em um planeta potencialmente habitável havia conseguido. Era a prova de conceito. Nossa última chance.

![Planeta Edmunds Exuberante](assets/screenshots/ChatGPT_Image_6_de_jun. de 2025, 01_47_38.png)

A Missão Garrido: Uma Corrida Contra o Tempo
Essa transmissão, embora breve, acendeu uma chama de esperança. Com esta 'prova de conceito' de habitabilidade, a 'Missão Garrido' foi concebida. Não é uma exploração cega, mas uma corrida contra o tempo para alcançar este sinal de esperança, confirmar e estabelecer uma presença em Edmunds. O desafio é imenso: precisamos encontrar a rota mais eficiente, otimizando o tempo terrestre, e tudo isso dentro de uma restrição crítica de 200 anos terrestres para que a missão tenha impacto na geração atual antes que a situação na Terra se torne irreversível. Edmunds é o farol.

A Solução: O Algoritmo de Dijkstra
Como especialistas em problemas computacionais complexos, sabíamos que a chave para a Missão Garrido estava em um algoritmo clássico: o Algoritmo de Dijkstra. Nosso sistema planetário foi modelado como um grafo, onde cada planeta é um nó e as rotas são arestas, ponderadas pelo tempo de nave e, crucialmente, pela dilatação temporal em relação à Terra.

Mapeando o Cosmos: Visualização do Grafo
Desenvolvemos uma visualização em Python que nos permite mapear o sistema interestelar. Cada nó representa um local – da Terra ao Buraco de Minhoca perto de Saturno, passando pelos perigosos Planetas Miller e Mann, até o nosso objetivo, o Planeta Edmunds. As cores dos nós indicam sua importância: verde para o objetivo, azul para a partida, roxo para pontos chave, e amarelo/vermelho para áreas de risco ou críticas.

A Rota Essencial: Demonstração Animada
Aplicando Dijkstra, otimizamos a rota não apenas pelo tempo de nave da tripulação, mas pelo tempo decorrido na Terra. Nossa simulação animada revela a sequência de locais que minimiza o impacto temporal aqui. Vejam como o caminho se revela, conectando a Terra a Edmunds, passando por pontos estratégicos.

Os Resultados: Tempo e Esperança
Encontramos a rota! Com ela, a tripulação da Missão Garrido enfrentará um tempo de nave de 5 anos. Mas o mais importante: o tempo total decorrido na Terra para esta rota será de 7 anos. Isso significa que a restrição de 200 anos foi ATENDIDA. Uma notícia que pode definir o destino da humanidade.

Conclusão: A Mensagem Final
A Missão Garrido é mais do que uma jornada espacial; é um símbolo da resiliência humana. Com a engenhosidade da computação e a força da colaboração, nós do Nemesis Protocol esperamos abrir caminho para um novo capítulo na história da humanidade. O futuro nos aguarda, e estamos prontos para desvendar cada rota.

![Novo Horizonte: Planeta e Esperança](assets/screenshots/ChatGPT_Image_6_de_jun. de 2025, 02_23_42.png)

✨ Funcionalidades
Modelagem de Grafo Interstelar: Representação dos planetas e pontos de interesse como nós e rotas como arestas em um grafo.

Cálculo de Tempo Duplo: Consideração do tempo de navegação (para a tripulação) e o tempo decorrido na Terra (afetado pela dilatação temporal) em cada trecho da rota.

Otimização de Rota com Dijkstra: Utilização do algoritmo de Dijkstra para encontrar o caminho que minimiza o tempo total decorrido na Terra.

Fatores de Dilatação Temporal: Inclusão de fatores de dilatação temporal específicos para cada região do espaço, simulando efeitos gravitacionais (como em Gargantua e Miller).

Visualização Dinâmica: Geração de um mapa estelar interativo com matplotlib, mostrando os nós (planetas/locais) e as arestas (rotas), com cores distintas para cada tipo de local.

Animação da Rota Otimizada: Animação do caminho encontrado pelo algoritmo de Dijkstra, destacando a sequência ideal para a navegação.

Verificação de Restrição Temporal: Validação se a rota otimizada se encaixa dentro de um limite máximo de tempo terrestre permitido para a missão.

💡 Conceitos Utilizados
Teoria da Relatividade (Dilatação Temporal): O tempo passa mais devagar em regiões com alta gravidade. Este conceito é fundamental para calcular o "tempo na Terra" em contraste com o "tempo de nave".

Teoria dos Grafos com NetworkX: O sistema interestelar é modelado como um grafo (rede) onde:

Nós (Nodes): Representam planetas e pontos de interesse (Terra, Saturno (BM), Sist. Gargantua, Miller (Órbita), Mann (Órbita), Planeta Edmunds, Gargantua (Manobra)).

Arestas (Edges): Representam as rotas entre esses pontos, com pesos (custos) associados.

Algoritmo de Dijkstra: Um algoritmo clássico de busca de caminho mais curto em grafos ponderados, utilizado aqui para encontrar a rota que minimiza o tempo total na Terra.

Matplotlib: Biblioteca de visualização em Python, usada para criar o mapa estelar e animar a rota da nave.**
