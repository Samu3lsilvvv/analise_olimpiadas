# -*- coding: utf-8 -*-
"""
=============================================================
  DESAFIO - Analise Olimpica: Evolucao dos 100m (1896-2016)
  Equivalente ao fluxo R/RStudio, escrito em Python
=============================================================

Passo a passo:
  3. Carregando os dados   (read.csv   -> pd.read_csv)
  4. Visualizando os dados (head       -> df.head())
  5. Ajustando os dados    (as.double  -> pd.to_numeric / dplyr -> pandas)
  6. Analisando os dados   (filter     -> df[condicao])
  7. Apresentando results  (plotly R   -> plotly.graph_objects)
  8. Conclusoes            (via terminal + HTML)
"""

import sys, os
import pandas as pd
import plotly.graph_objects as go
from plotly.subplots import make_subplots

# Forca UTF-8 no stdout para evitar erros de encoding no Windows
sys.stdout.reconfigure(encoding="utf-8")

SEP = "=" * 62

# ------------------------------------------------------------------
# PASSO 3 - Carregando os dados
# R: dados <- read.csv("results.csv", sep=",")
# ------------------------------------------------------------------
CSV_PATH = os.path.join(os.path.dirname(os.path.abspath(__file__)), "results.csv")

# Algumas linhas possuem coluna extra de vento (ex: +0.1)
# Usamos 'on_bad_lines="skip"' para ignorar essas linhas extras
dados = pd.read_csv(
    CSV_PATH,
    sep=",",
    usecols=[0, 1, 2, 3, 4, 5, 6, 7],
    names=["Gender", "Event", "Location", "Year", "Medal", "Name", "Nationality", "Result"],
    header=0,
    on_bad_lines="skip",
)

print(SEP)
print("PASSO 3 - Dados carregados com sucesso!")
print(f"  Linhas: {len(dados)}  |  Colunas: {len(dados.columns)}")
print(f"  Colunas: {list(dados.columns)}")

# ------------------------------------------------------------------
# PASSO 4 - Visualizando os dados
# R: head(dados)
# ------------------------------------------------------------------
print()
print(SEP)
print("PASSO 4 - head(dados) - primeiras 6 linhas:")
print(dados.head(6).to_string(index=False))

# ------------------------------------------------------------------
# PASSO 5 - Ajustando os dados
# R: summary(dados)  -> Result e' character -> as.double(dados$Result)
# ------------------------------------------------------------------
print()
print(SEP)
print("PASSO 5 - summary(dados) - tipos originais das colunas:")
print(dados.dtypes.to_string())

# Conversao: character -> double  (equivalente a as.double em R)
# Valores nao numericos (ex: "None", "25:05.17") viram NaN
dados["Result"] = pd.to_numeric(dados["Result"], errors="coerce")

print()
print("  -> Coluna 'Result' convertida para double (float64).")
print(f"  Tipo atual   : {dados['Result'].dtype}")
print(f"  Valores validos: {dados['Result'].notna().sum()} / {len(dados)}")

# ------------------------------------------------------------------
# PASSO 6 - Analisando os dados
# R: mulheres_100m <- filter(dados, Gender=="W", Event=="100M Women", Medal=="G")
#    homens_100m   <- filter(dados, Gender=="M", Event=="100M Men",   Medal=="G")
# ------------------------------------------------------------------
print()
print(SEP)
print("PASSO 6 - Filtrando medalhistas de ouro nos 100m:")

mulheres_100m = dados[
    (dados["Gender"] == "W") &
    (dados["Event"]  == "100M Women") &
    (dados["Medal"]  == "G")
].copy()

homens_100m = dados[
    (dados["Gender"] == "M") &
    (dados["Event"]  == "100M Men") &
    (dados["Medal"]  == "G")
].copy()

# Remove NaN e ordena por ano
mulheres_100m = mulheres_100m.dropna(subset=["Result"]).sort_values("Year").reset_index(drop=True)
homens_100m   = homens_100m.dropna(subset=["Result"]).sort_values("Year").reset_index(drop=True)

print(f"\n  mulheres_100m -> {len(mulheres_100m)} registros")
print(mulheres_100m[["Year", "Location", "Name", "Nationality", "Result"]].to_string(index=False))

print(f"\n  homens_100m   -> {len(homens_100m)} registros")
print(homens_100m[["Year", "Location", "Name", "Nationality", "Result"]].to_string(index=False))

# ------------------------------------------------------------------
# PASSO 7 - Graficos interativos (Plotly)
# R: library(plotly); plot_ly(type="scatter", mode="markers")
# ------------------------------------------------------------------
print()
print(SEP)
print("PASSO 7 - Gerando graficos interativos com Plotly...")

fig = make_subplots(
    rows=2, cols=1,
    vertical_spacing=0.20
)

# --- Scatter Homens ---
fig.add_trace(
    go.Scatter(
        x=homens_100m["Year"],
        y=homens_100m["Result"],
        mode="markers+lines",
        name="Homens (Ouro)",
        marker=dict(
            size=11,
            color="#f97316",
            symbol="circle",
            line=dict(color="white", width=1.5)
        ),
        line=dict(color="#f97316", width=2, dash="dot"),
        customdata=homens_100m[["Name", "Nationality", "Location"]].values,
        hovertemplate=(
            "<b>%{customdata[0]}</b> (%{customdata[1]})<br>"
            "Local: %{customdata[2]}<br>"
            "Ano: %{x}<br>"
            "Tempo: <b>%{y:.2f}s</b><extra></extra>"
        ),
    ),
    row=1, col=1
)

# --- Scatter Mulheres ---
fig.add_trace(
    go.Scatter(
        x=mulheres_100m["Year"],
        y=mulheres_100m["Result"],
        mode="markers+lines",
        name="Mulheres (Ouro)",
        marker=dict(
            size=11,
            color="#a855f7",
            symbol="circle",
            line=dict(color="white", width=1.5)
        ),
        line=dict(color="#a855f7", width=2, dash="dot"),
        customdata=mulheres_100m[["Name", "Nationality", "Location"]].values,
        hovertemplate=(
            "<b>%{customdata[0]}</b> (%{customdata[1]})<br>"
            "Local: %{customdata[2]}<br>"
            "Ano: %{x}<br>"
            "Tempo: <b>%{y:.2f}s</b><extra></extra>"
        ),
    ),
    row=2, col=1
)

fig.update_layout(
    height=860,
    template="plotly_white",
    legend=dict(
        orientation="h",
        y=1.00, x=0.5, xanchor="center",
        bgcolor="rgba(255,255,255,0.8)",
        bordercolor="#e2e8f0", borderwidth=1
    ),
    hovermode="x unified",
    plot_bgcolor="#f8fafc",
    paper_bgcolor="#f8fafc",
    margin=dict(t=120, b=60, l=70, r=30),
)

# Titulo principal manualmente posicionado acima de tudo
fig.add_annotation(
    text="<b>Evolucao dos Tempos nos 100m Olimpicos - Medalhistas de Ouro (1896-2016)</b>",
    xref="paper", yref="paper",
    x=0.5, y=1.07,
    showarrow=False,
    font=dict(size=15, color="#1e293b"),
    xanchor="center", yanchor="bottom",
)

# Subtitulos dos subplots posicionados manualmente (sem sobreposicao)
fig.add_annotation(
    text="Homens - 100m Rasos: Evolucao do Ouro Olimpico (1896-2016)",
    xref="paper", yref="paper",
    x=0.5, y=1.01,
    showarrow=False,
    font=dict(size=13, color="#374151"),
    xanchor="center", yanchor="bottom",
)
fig.add_annotation(
    text="Mulheres - 100m Rasos: Evolucao do Ouro Olimpico (1928-2016)",
    xref="paper", yref="paper",
    x=0.5, y=0.46,
    showarrow=False,
    font=dict(size=13, color="#374151"),
    xanchor="center", yanchor="bottom",
)

fig.update_xaxes(
    showgrid=True, gridcolor="#e2e8f0",
    tickmode="linear", dtick=8,
    title_text="Ano"
)

# Eixo Y invertido: tempo menor (mais rapido) fica mais ALTO no grafico
fig.update_yaxes(
    showgrid=True, gridcolor="#e2e8f0",
    title_text="Tempo (segundos)",
)

# Salvar o HTML
OUTPUT_HTML = os.path.join(os.path.dirname(os.path.abspath(__file__)), "grafico_100m.html")
fig.write_html(OUTPUT_HTML)
print(f"  Grafico salvo em: {OUTPUT_HTML}")

# Exibir direto no navegador via Plotly (equivalente a plot() no R)
fig.show()

# ------------------------------------------------------------------
# PASSO 8 - Conclusoes
# ------------------------------------------------------------------
h_max = homens_100m.loc[homens_100m["Result"].idxmax()]
h_min = homens_100m.loc[homens_100m["Result"].idxmin()]
m_max = mulheres_100m.loc[mulheres_100m["Result"].idxmax()]
m_min = mulheres_100m.loc[mulheres_100m["Result"].idxmin()]

print()
print(SEP)
print("PASSO 8 - CONCLUSOES")
print(SEP)
print(f"""
1. EVOLUCAO GERAL
   Os graficos demonstram uma tendencia consistente de queda
   nos tempos dos medalhistas de ouro ao longo de ~120 anos
   de Olimpiadas, refletindo avancos no treinamento esportivo,
   nutricao, tecnologia e profissionalizacao do esporte.

2. HOMENS - 100M
   Tempo mais lento : {h_max['Result']:.2f}s  ({h_max['Name']}, {int(h_max['Year'])})
   Tempo mais rapido: {h_min['Result']:.2f}s  ({h_min['Name']}, {int(h_min['Year'])})
   Melhora total    : {h_max['Result'] - h_min['Result']:.2f}s em {int(h_min['Year']) - int(h_max['Year'])} anos

3. MULHERES - 100M
   Tempo mais lento : {m_max['Result']:.2f}s  ({m_max['Name']}, {int(m_max['Year'])})
   Tempo mais rapido: {m_min['Result']:.2f}s  ({m_min['Name']}, {int(m_min['Year'])})
   Melhora total    : {m_max['Result'] - m_min['Result']:.2f}s em {int(m_min['Year']) - int(m_max['Year'])} anos

4. DESTAQUES HISTORICOS
   - Usain Bolt (JAM): recorde olimpico de 9.63s em Londres 2012,
     dominando completamente as edicoes de 2008, 2012 e 2016.
   - Florence Griffith-Joyner (USA): 10.54s em Seul 1988.
   - Jesse Owens (USA): 10.3s em Berlim 1936, impactante para a epoca.

5. PADRAO DE MELHORA
   A curva nao e linear. Ha periodos de estagnacao seguidos de
   saltos repentinos, geralmente associados a atletas excepcionais
   ou a inovacoes na preparacao fisica e tecnica.

6. DIFERENCA DE GENERO
   Os homens correm aprox. 0.8-1.0s mais rapido que as mulheres,
   diferenca relativamente constante ao longo do tempo.
""")
print("Analise concluida! O grafico foi aberto no navegador.")
