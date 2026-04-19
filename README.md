# 🏅 Análise Olímpica — Evolução dos 100m (1896–2016)

> Análise exploratória e visualização interativa da evolução dos tempos dos medalhistas de ouro nos 100m rasos masculino e feminino ao longo de 120 anos de Jogos Olímpicos.

---

## 📋 Sobre o Projeto

Este projeto realiza uma **análise completa dos dados históricos das Olimpíadas** (1896–2016), com foco na evolução dos tempos das provas dos 100m rasos. O pipeline segue um fluxo estruturado de 6 etapas — inspirado na metodologia equivalente ao R/RStudio — implementado integralmente em **Python**.

A análise cobre desde a ingestão e limpeza dos dados até a geração de **gráficos interativos** com [Plotly](https://plotly.com/python/), além de um relatório de conclusões no terminal.

---

## ✨ Funcionalidades

- 📥 **Carregamento de dados** via `pandas.read_csv` com tratamento de linhas malformadas
- 🔍 **Inspeção e visualização** dos tipos e estrutura dos dados (`head`, `dtypes`)
- 🔧 **Limpeza e conversão** de tipos — coluna `Result` de `object` para `float64`
- 🎯 **Filtragem** por gênero, evento e medalha (ouro — `G`)
- 📊 **Visualização interativa** com `plotly.graph_objects` (scatter plot com hover detalhado)
- 📝 **Conclusões automáticas** no terminal com destaques históricos e estatísticas de melhora

---

## 🗂️ Estrutura do Projeto

```
analise_olimpiadas/
├── analise_olimpiadas.py   # Script principal com todo o pipeline
├── results.csv             # Dataset com resultados olímpicos (1896–2016)
├── results.json            # Dataset no formato JSON
└── grafico_100m.html       # Gráfico interativo gerado (criado na execução)
```

---

## 🚀 Como Executar

### Pré-requisitos

- Python **3.8+**
- pip

### Instalação das dependências

```bash
pip install pandas plotly
```

### Executando a análise

```bash
python analise_olimpiadas.py
```

Ao final da execução, o gráfico interativo será **aberto automaticamente no navegador** e salvo como `grafico_100m.html` na pasta do projeto.

---

## 🔬 Pipeline de Análise

O script segue um fluxo estruturado de 6 passos:

| Passo | Descrição | Equivalente em R |
|-------|-----------|-----------------|
| **3** | Carregamento dos dados | `read.csv()` |
| **4** | Visualização inicial | `head()` |
| **5** | Ajuste de tipos | `as.double()` / `dplyr` |
| **6** | Filtragem por critérios | `filter()` |
| **7** | Geração de gráficos interativos | `library(plotly)` |
| **8** | Conclusões e relatório | — |

---

## 📊 Exemplo de Saída

### Terminal

```
==============================================================
PASSO 8 - CONCLUSOES
==============================================================

1. EVOLUCAO GERAL
   Os graficos demonstram uma tendencia consistente de queda
   nos tempos dos medalhistas de ouro ao longo de ~120 anos
   de Olimpiadas...

2. HOMENS - 100M
   Tempo mais lento : 12.00s  (Thomas Burke, 1896)
   Tempo mais rapido:  9.63s  (Usain Bolt, 2012)
   Melhora total    :  2.37s em 116 anos

3. MULHERES - 100M
   Tempo mais lento : 12.20s  (Elizabeth Robinson, 1928)
   Tempo mais rapido: 10.54s  (Florence Griffith-Joyner, 1988)
   Melhora total    :  1.66s em 60 anos
```

### Gráfico Interativo

O gráfico exibe dois subplots (homens e mulheres) com:
- **Scatter + linha tracejada** mostrando a evolução temporal
- **Hover detalhado** com nome, nacionalidade, local e tempo
- **Design limpo** com fundo claro e paleta de cores harmoniosa

---

## 🏆 Principais Destaques Históricos

| Atleta | País | Ano | Tempo |
|--------|------|-----|-------|
| **Usain Bolt** | 🇯🇲 Jamaica | 2012 | 9.63s |
| Florence Griffith-Joyner | 🇺🇸 EUA | 1988 | 10.54s |
| Jesse Owens | 🇺🇸 EUA | 1936 | 10.3s |
| Thomas Burke | 🇺🇸 EUA | 1896 | 12.0s |

---

## 📦 Dependências

| Biblioteca | Versão mínima | Uso |
|------------|--------------|-----|
| `pandas` | 1.3+ | Ingestão, limpeza e filtragem dos dados |
| `plotly` | 5.0+ | Geração dos gráficos interativos |

---

## 📁 Dataset

O arquivo `results.csv` contém os resultados das provas olímpicas de atletismo de **1896 a 2016**, com as seguintes colunas:

| Coluna | Descrição |
|--------|-----------|
| `Gender` | Gênero do atleta (`M` / `W`) |
| `Event` | Nome da prova (ex: `100M Men`) |
| `Location` | Cidade-sede dos Jogos |
| `Year` | Ano da edição |
| `Medal` | Tipo de medalha (`G`, `S`, `B`) |
| `Name` | Nome do atleta |
| `Nationality` | Código do país (3 letras) |
| `Result` | Tempo ou distância registrada |

> **Nota:** Linhas com informações adicionais de vento (ex: `+0.1`) são automaticamente ignoradas durante a leitura.

---

## 🤝 Contribuindo

Contribuições são bem-vindas! Sinta-se à vontade para abrir uma *issue* ou enviar um *pull request*.

1. Faça um fork do projeto
2. Crie uma branch para sua feature (`git checkout -b feature/nova-analise`)
3. Commit suas mudanças (`git commit -m 'Add: nova análise por continente'`)
4. Push para a branch (`git push origin feature/nova-analise`)
5. Abra um Pull Request

---

## 📄 Licença

Este projeto está sob a licença **MIT**. Consulte o arquivo [LICENSE](LICENSE) para mais detalhes.

---

<div align="center">
  <sub>Desenvolvido com 🐍 Python + 📊 Plotly · Dados: Olimpíadas 1896–2016</sub>
</div>
