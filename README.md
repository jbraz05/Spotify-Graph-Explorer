# 🎵 Spotify Graph Explorer

Uma aplicação web interativa para visualização e análise de grafos de colaborações musicais do Spotify, implementando algoritmos clássicos de teoria dos grafos com uma interface moderna e intuitiva.

## 📋 Sobre o Projeto

O **Spotify Graph Explorer** é uma ferramenta educacional e interativa que transforma dados de músicas populares do Spotify em um grafo de colaborações entre artistas. Cada vértice representa um artista e cada aresta representa uma colaboração musical, com pesos calculados baseados no número de streams. A aplicação permite explorar essas conexões através de algoritmos fundamentais de grafos, como BFS, DFS, Dijkstra e Bellman-Ford.

## ✨ Funcionalidades

### 🎯 Visualização Interativa
- **Grafo dinâmico**: Visualização em tempo real usando Vis.js com física de partículas
- **Busca de artistas**: Sistema de busca rápida para localizar artistas no grafo
- **Interatividade**: 
  - Clique simples em vértices para visualizar conexões
  - Duplo clique em vértices para abrir o perfil do artista no Spotify
  - Clique em arestas para ouvir a música colaborativa no Spotify

### 🔍 Algoritmos de Exploração
- **BFS (Busca em Largura)**: Exploração nível por nível a partir de um artista
- **DFS (Busca em Profundidade)**: Exploração em profundidade do grafo

### 🛤️ Algoritmos de Caminho Mínimo
- **Dijkstra**: Encontra o caminho mais curto entre dois artistas (pesos positivos)
- **Bellman-Ford**: Detecta ciclos negativos e calcula caminhos mínimos com pesos negativos

### 🧪 Recursos Avançados
- **Teste de pesos negativos**: Simulação de arestas com pesos negativos para testar o algoritmo de Bellman-Ford
- **Reset de pesos**: Restauração dos pesos originais do grafo
- **Destaque visual**: Caminhos e explorações destacados com cores diferentes
- **Informações detalhadas**: Exibição de estatísticas e métricas dos algoritmos

## 🛠️ Tecnologias Utilizadas

### Backend
- **Python 3.x**: Linguagem principal
- **Flask**: Framework web para API REST
- **Estrutura de dados customizada**: Implementação própria de grafos

### Frontend
- **HTML5/CSS3**: Interface responsiva e moderna
- **JavaScript (ES6+)**: Lógica de interação e comunicação com API
- **Vis.js Network**: Biblioteca para visualização de grafos interativos

### Processamento de Dados
- **Pandas**: Manipulação e análise de dados CSV
- **CSV Processing**: Leitura e processamento de datasets do Spotify

## 📁 Estrutura do Projeto

```
projeto-grafos-pt2/
├── app.py                 # Aplicação Flask principal
├── requirements.txt       # Dependências do projeto
├── data/
│   └── Popular_Spotify_Songs.csv  # Dataset de músicas
├── src/
│   ├── graph.py          # Classe Graph (estrutura de dados)
│   ├── utils.py          # Funções utilitárias (carregamento de dados)
│   └── algorithms/
│       ├── bfs.py         # Algoritmo BFS
│       ├── dfs.py         # Algoritmo DFS
│       ├── dijkstra.py    # Algoritmo de Dijkstra
│       └── bellman_ford.py # Algoritmo de Bellman-Ford
├── templates/
│   └── index.html        # Interface principal
└── static/
    └── css/
        └── styles.css     # Estilos customizados
```

## 🚀 Como Executar

### Pré-requisitos
- Python 3.8 ou superior
- pip (gerenciador de pacotes Python)

### Instalação

1. **Clone o repositório** (ou baixe os arquivos do projeto)

2. **Instale as dependências**:
```bash
pip install -r requirements.txt
```

3. **Execute a aplicação**:
```bash
python app.py
```

4. **Acesse no navegador**:
```
http://localhost:5000
```

A aplicação estará rodando e pronta para uso!

## 🎓 Conceitos de Teoria dos Grafos Aplicados

- **Representação de grafos**: Lista de adjacência
- **Grafos não direcionados**: Colaborações bidirecionais entre artistas
- **Grafos ponderados**: Pesos baseados em streams (popularidade)
- **Busca em grafos**: BFS e DFS
- **Caminhos mínimos**: Dijkstra e Bellman-Ford
- **Detecção de ciclos negativos**: Validação do algoritmo de Bellman-Ford

## 📊 Características do Dataset

- **Fonte**: Popular Spotify Songs
- **Estrutura**: Músicas com informações de artistas e streams
- **Processamento**: 
  - Criação automática de arestas entre artistas colaboradores
  - Cálculo de pesos baseado em streams (inverso da popularidade)
  - Remoção de nós isolados e self-loops

## 🎨 Interface do Usuário

- **Sidebar interativa**: Controles para seleção de artistas e execução de algoritmos
- **Visualização central**: Grafo interativo com zoom, pan e seleção
- **Feedback visual**: Cores diferenciadas para origem (azul), destino (vermelho) e caminho (amarelo)
- **Mensagens informativas**: Área de output com resultados e estatísticas dos algoritmos

## 📝 Documentação Adicional

Para mais detalhes sobre a implementação e teoria dos algoritmos, consulte a [documentação completa do projeto](https://docs.google.com/document/d/1ZwDILgKgvY2REE313Dnm3LVUKpA_uV-44ZZfRPipQoo/edit?usp=sharing).

## 🔧 Melhorias Futuras

- [ ] Implementação de mais algoritmos (A*, Floyd-Warshall)
- [ ] Exportação de visualizações
- [ ] Filtros por gênero musical
- [ ] Análise de comunidades (clustering)
- [ ] Métricas de centralidade

## 👨‍💻 Desenvolvimento

Projeto desenvolvido como parte do estudo de **Teoria dos Grafos**, demonstrando a aplicação prática de algoritmos fundamentais em um contexto real e interativo.

---

**Status do Projeto**: ✅ Completo e funcional

**Licença**: Este projeto é de uso educacional.
