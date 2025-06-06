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


## ⚙️ Requisitos
Para rodar este projeto, você precisará de:

Python 3.7+

As seguintes bibliotecas Python:

networkx

matplotlib

Instalação
Clone o repositório:

git clone https://github.com/yagojardimm/Estrutura-de-Dados.git
cd Estrutura-de-Dados


Crie e ative um ambiente virtual (opcional, mas recomendado):

python -m venv venv
# No Windows:
.\venv\Scripts\activate
# No macOS/Linux:
source venv/bin/activate

Instale as dependências:

pip install -r requirements.txt
## 🖼️ Telas do Frontend (Nemesis Protocol Web)

Para uma experiência visual completa da narrativa e funcionalidades do projeto, explore as telas da nossa aplicação web:

### Tela Inicial (Home)
![image](https://github.com/user-attachments/assets/7a75ca1b-ef7a-4f2d-8b16-d9e2abd9dd63)


### O Desafio (Problema)
[image](https://github.com/user-attachments/assets/ef03c3d0-9b88-4f2e-9468-c0c9ef5db4af)



### Storytelling da Missão
[image](https://github.com/user-attachments/assets/21236f8c-3c5a-4d55-9476-86a4b3c263d4)



### A Equipe (Scrum)
![image](https://github.com/user-attachments/assets/e7deb879-690e-4529-9bb0-e6ab7e784e6e)



---
## 🚀 Como Usar
Para executar a simulação da Missão Garrido:

Certifique-se de que todas as dependências estão instaladas (veja a seção Instalação).

Execute o script main.py a partir da raiz do projeto:

python src/main.py

O script irá:

Inicializar o grafo do sistema interestelar.

Calcular a rota mais otimizada em tempo terrestre da Terra para o Planeta Edmunds.

Exibir no console os resultados da simulação: a rota encontrada, o tempo total de nave, o tempo total na Terra e se a restrição de 200 anos foi atendida.

Gerar uma visualização interativa do grafo com a rota animada usando matplotlib.

Exemplo de Saída no Console:
🚀 Iniciando simulação da Missão Garrido (cenário Interestelar)...
    Objetivo: Encontrar a rota MAIS RÁPIDA EM TEMPO TERRESTRE de 'Terra' para 'Planeta Edmunds',
              e verificar se respeita o limite de 200.0 anos terrestres.
              Tripulação: Matheus, Yago, Caio, João.
----------------------------------------------------------------------

✨ ROTA MAIS RÁPIDA EM TEMPO TERRESTRE (via Dijkstra) ENCONTRADA! ✨

    ➡️ Sequência de Locais Sugerida:
        Terra -> Saturno (BM) -> Sist. Gargantua -> Mann (Órbita) -> Gargantua (Manobra) -> Planeta Edmunds

    ⏳ Tempo Total Estimado de Nave (Tripulação) para esta rota: 2.860 anos.
    🌍 Tempo Total Estimado Decorrido na Terra para esta rota: 7.000 anos.
    ✅ RESTRIÇÃO DE TEMPO TERRESTRE ATENDIDA (<= 200.0 anos).
----------------------------------------------------------------------

ℹ️ INFORMAÇÕES SOBRE OS LOCAIS NA ROTA (Cenário Interestelar):

    📍 Local: Terra
        Info: Ponto de partida da Missão Garrido.
        Fator de Dilatação da Região (aprox.): 1x
----------------------------------------
    📍 Local: Saturno (BM)
        Info: Buraco de Minhoca para sistema Gargantua.
        Fator de Dilatação da Região (aprox.): 1x
----------------------------------------
    📍 Local: Sist. Gargantua
        Info: Entrada do sistema de Gargantua.
        Fator de Dilatação da Região (aprox.): 10x
----------------------------------------
    📍 Local: Mann (Órbita)
        Info: Planeta Mann: possível ponto de passagem.
        Fator de Dilatação da Região (aprox.): 5x
----------------------------------------
    📍 Local: Gargantua (Manobra)
        Info: Manobra de slingshot em Gargantua.
        Fator de Dilatação da Região (aprox.): 75000x
----------------------------------------
    📍 Local: Planeta Edmunds
        Info: Planeta Edmunds: destino principal da Missão Garrido.
        Fator de Dilatação da Região (aprox.): 2x
----------------------------------------

🛤️ DETALHES DOS TRECHOS DA ROTA OTIMIZADA (Cenário Interestelar):

    ➡️ Trecho: De 'Terra' para 'Saturno (BM)':
        ⏳ Tempo de Nave: 2.0000 anos (2.0a)
        🌍 Tempo na Terra (para este trecho): 2.00 anos
----------------------------------------
    ➡️ Trecho: De 'Saturno (BM)' para 'Sist. Gargantua':
        ⏳ Tempo de Nave: 0.0100 anos (0.01a)
        🌍 Tempo na Terra (para este trecho): 0.10 anos
----------------------------------------
    ➡️ Trecho: De 'Sist. Gargantua' para 'Mann (Órbita)':
        ⏳ Tempo de Nave: 0.3000 anos (0.3a)
        🌍 Tempo na Terra (para este trecho): 1.50 anos
----------------------------------------
    ➡️ Trecho: De 'Mann (Órbita)' para 'Gargantua (Manobra)':
        ⏳ Tempo de Nave: 0.0500 anos (0.05a)
        🌍 Tempo na Terra (para este trecho): 3750.00 anos
----------------------------------------
    ➡️ Trecho: De 'Gargantua (Manobra)' para 'Planeta Edmunds':
        ⏳ Tempo de Nave: 0.5000 anos (0.5a)
        🌍 Tempo na Terra (para este trecho): 750.00 anos
----------------------------------------
======================================================================

🌌 Gerando visualização do mapa estelar...

✅ Simulação Concluída.

## 📄 Licença
Este projeto está licenciado sob a Licença MIT. Veja o arquivo LICENSE para mais detalhes.

## 👨‍💻 Equipe e Agradecimentos
Este projeto foi desenvolvido com a paixão pela exploração espacial e a resolução de problemas complexos.

Desenvolvedores:

Matheus Beiruth

Yago da Costa

Caio Cezar Jotta

João Pedro Portela



