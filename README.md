# Grafo e Caminho Euleriano 🌐

Este repositório contém implementações em Python de funções para manipulação de grafos e determinação de caminhos eulerianos.

## 📁 Estrutura do Projeto

O código é composto pelos seguintes arquivos principais:

- **grafo.py**: Contém funções para manipulação de um grafo direcionado representado como um dicionário, onde as chaves são os vértices e os valores são listas de vértices adjacentes.
- **caminho_euleriano.py**: Implementa a função `Cad_eul_fec(adj)`, que determina e imprime um caminho euleriano fechado a partir de uma lista de adjacências.

## Funcionamento

### Manipulação de Grafos

O arquivo `grafo.py` inclui as seguintes funções:

- **insere_vertice(vertice)**: Insere um vértice no grafo, se ele ainda não estiver presente.
- **delete_vertice(vertice)**: Exclui um vértice do grafo, juntamente com todas as suas arestas.
- **insere_aresta(v1, v2)**: Insere uma aresta direcionada entre os vértices v1 e v2 no grafo.
- **delete_aresta(v1, v2)**: Exclui a aresta direcionada entre os vértices v1 e v2 do grafo.
- **grau_vert(vertice)**: Retorna o grau do vértice especificado.
- **det_viz(v1, v2)**: Determina se dois vértices são vizinhos no grafo.

### Caminho Euleriano

O arquivo `caminho_euleriano.py` contém a função `Cad_eul_fec(adj)`, que utiliza a lista de adjacências para determinar e imprimir um caminho euleriano fechado.

## 🚀 Como Usar

1. Certifique-se de ter o interpretador Python instalado em seu ambiente.
2. Clone o repositório:
   ```bash
   git clone https://github.com/gabigam/Grafo-e-Caminho-Euleriano.git
   ```
3. Navegue até o diretório do projeto:
   ```bash
   cd Grafo-e-Caminho-Euleriano
   ```
4. Execute o arquivo `grafo.py` para utilizar as funções de manipulação de grafos. Os exemplos de uso estão incluídos no próprio arquivo:
   ```bash
   python grafo.py
   ```
5. Execute o arquivo `caminho_euleriano.py` para determinar e imprimir caminhos eulerianos fechados:
   ```bash
   python caminho_euleriano.py
   ```

## Observações

- Os grafos são representados como dicionários, onde as chaves são os vértices e os valores são listas de vértices adjacentes.
- Os caminhos eulerianos são determinados a partir de listas de adjacências, onde cada índice da lista representa um vértice e os valores são listas de vértices adjacentes.
```

