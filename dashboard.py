#Projeto TÓPICOS DE BIG DATA EM PYTHON
#Alunos: Gleyson Souza, João Pedro e João Gabriel
#PROF.: Msc Kayo Henrique de Carvalho Monteiro


#-=- Bibliotecas usadas -=-
import os
import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import dash_bootstrap_components as dbc
import plotly.express as px
import plotly.graph_objects as go

import pandas as pd
import json

#-=====================================================================================================-

#-=- Manipulação dos dados -=-

# mobilidade1_df = pd.read_csv('/2020_BR_Region_Mobility_Report.csv', sep=",", header=0)
# mobilidade2_df = pd.read_csv('/2021_BR_Region_Mobility_Report.csv', sep=",", header=0)
# mobilidade3_df = pd.read_csv('/2022_BR_Region_Mobility_Report.csv', sep=",", header=0)
# covid1_df = pd.read_csv('/HIST_PAINEL_COVIDBR_2020_Parte1_03mai2024.csv', sep=";", header=0)
# covid2_df = pd.read_csv('/HIST_PAINEL_COVIDBR_2020_Parte2_03mai2024.csv', sep=";", header=0)
# covid3_df = pd.read_csv('/HIST_PAINEL_COVIDBR_2021_Parte1_03mai2024.csv', sep=";", header=0)
# covid4_df = pd.read_csv('/HIST_PAINEL_COVIDBR_2021_Parte2_03mai2024.csv', sep=";", header=0)
# covid5_df = pd.read_csv('/HIST_PAINEL_COVIDBR_2022_Parte1_03mai2024.csv', sep=";", header=0)
# covid6_df = pd.read_csv('/HIST_PAINEL_COVIDBR_2022_Parte2_03mai2024.csv', sep=";", header=0)

# ====================== DataFrame Brasil ======================
# df_definitivo1 = pd.concat([covid1_df, covid2_df, covid3_df, covid4_df, covid5_df, covid6_df])
# df_definitivo2 = pd.concat([mobilidade1_df, mobilidade2_df, mobilidade3_df])
# df_brasil1 = df_definitivo1[df_definitivo1["regiao"] == "Brasil"]
# df_brasil2 = df_definitivo2[mobilidade2_df['sub_region_1'].isna()]
# df_brasil2 = df_brasil2[df_brasil2['sub_region_1'] != 'Federal District']
# df_brasil = pd.merge(df_brasil1, df_brasil2, left_on=['data'], right_on=['date'])
# df_brasil['media_acumulada_trabalho'] = df_brasil['workplaces_percent_change_from_baseline'].expanding().mean()
# df_brasil['media_acumulada_transporte'] = df_brasil['transit_stations_percent_change_from_baseline'].expanding().mean()
# df_brasil['media_acumulada_residencial'] = df_brasil['residential_percent_change_from_baseline'].expanding().mean()
# df_brasil['media_acumulada_residencial'] = df_brasil['media_acumulada_residencial'].apply(lambda x: f"{x:.2f}")
# df_brasil['media_acumulada_trabalho'] = df_brasil['media_acumulada_trabalho'].apply(lambda x: f"{x:.2f}")
# df_brasil['media_acumulada_transporte'] = df_brasil['media_acumulada_transporte'].apply(lambda x: f"{x:.2f}")
# df_brasil.to_csv('df_brasil.csv', index=False)

# ====================== DataFrame Estados ======================
# df_estados1 = covid1_df[(~covid1_df["estado"].isna()) & (covid1_df["codmun"].isna())]
# df_estados2 = covid2_df[(~covid2_df["estado"].isna()) & (covid2_df["codmun"].isna())]
# df_estados3 = covid3_df[(~covid3_df["estado"].isna()) & (covid3_df["codmun"].isna())]
# df_estados4 = covid4_df[(~covid4_df["estado"].isna()) & (covid4_df["codmun"].isna())]
# df_estados5 = covid5_df[(~covid5_df["estado"].isna()) & (covid5_df["codmun"].isna())]
# df_estados6 = covid6_df[(~covid6_df["estado"].isna()) & (covid6_df["codmun"].isna())]
# df_estados1 = df_estados1.drop(columns=['interior/metropolitana', 'codRegiaoSaude', 'nomeRegiaoSaude', 'codmun', 'coduf', 'municipio', 'semanaEpi', 'populacaoTCU2019'])
# df_estados2 = df_estados2.drop(columns=['interior/metropolitana', 'codRegiaoSaude', 'nomeRegiaoSaude', 'codmun', 'coduf', 'municipio', 'semanaEpi', 'populacaoTCU2019'])
# df_estados3 = df_estados3.drop(columns=['interior/metropolitana', 'codRegiaoSaude', 'nomeRegiaoSaude', 'codmun', 'coduf', 'municipio', 'semanaEpi', 'populacaoTCU2019'])
# df_estados4 = df_estados4.drop(columns=['interior/metropolitana', 'codRegiaoSaude', 'nomeRegiaoSaude', 'codmun', 'coduf', 'municipio', 'semanaEpi', 'populacaoTCU2019'])
# df_estados5 = df_estados5.drop(columns=['interior/metropolitana', 'codRegiaoSaude', 'nomeRegiaoSaude', 'codmun', 'coduf', 'municipio', 'semanaEpi', 'populacaoTCU2019'])
# df_estados6 = df_estados6.drop(columns=['interior/metropolitana', 'codRegiaoSaude', 'nomeRegiaoSaude', 'codmun', 'coduf', 'municipio', 'semanaEpi', 'populacaoTCU2019'])
# mobilidade1_estados = mobilidade1_df[mobilidade1_df['sub_region_2'].isna()]
# mobilidade2_estados = mobilidade2_df[mobilidade2_df['sub_region_2'].isna()]
# mobilidade3_estados = mobilidade3_df[mobilidade3_df['sub_region_2'].isna()]
# mobilidade1_estados = mobilidade1_estados.dropna(subset=['sub_region_1'])
# mobilidade2_estados = mobilidade2_estados.dropna(subset=['sub_region_1'])
# mobilidade3_estados = mobilidade3_estados.dropna(subset=['sub_region_1'])
# estado_para_sigla = {
#    'Acre': 'AC', 'Alagoas': 'AL', 'Amapá': 'AP', 'Amazonas': 'AM', 'Bahia': 'BA', 'Ceará': 'CE',
#    'Distrito Federal': 'DF', 'Espírito Santo': 'ES', 'Goiás': 'GO', 'Maranhão': 'MA', 'Mato Grosso': 'MT',
#    'Mato Grosso do Sul': 'MS', 'Minas Gerais': 'MG', 'Pará': 'PA', 'Paraíba': 'PB', 'Paraná': 'PR',
#    'Pernambuco': 'PE', 'Piauí': 'PI', 'Rio de Janeiro': 'RJ', 'Rio Grande do Norte': 'RN', 'Rio Grande do Sul': 'RS',
#    'Rondônia': 'RO', 'Roraima': 'RR', 'Santa Catarina': 'SC', 'São Paulo': 'SP', 'Sergipe': 'SE', 'Tocantins': 'TO'
#}
# mobilidade1_estados['estado'] = mobilidade1_estados['sub_region_1'].str.extract(r'State of ([\w\s]+)', expand=False)
# mobilidade2_estados['estado'] = mobilidade2_estados['sub_region_1'].str.extract(r'State of ([\w\s]+)', expand=False)
# mobilidade3_estados['estado'] = mobilidade3_estados['sub_region_1'].str.extract(r'State of ([\w\s]+)', expand=False)
# mobilidade1_estados['estado'] = mobilidade1_estados['estado'].fillna(mobilidade1_estados['sub_region_1'].replace('Federal District', 'Distrito Federal'))
# mobilidade2_estados['estado'] = mobilidade2_estados['estado'].fillna(mobilidade2_estados['sub_region_1'].replace('Federal District', 'Distrito Federal'))
# mobilidade3_estados['estado'] = mobilidade3_estados['estado'].fillna(mobilidade3_estados['sub_region_1'].replace('Federal District', 'Distrito Federal'))
# mobilidade1_estados['estado_sigla'] = mobilidade1_estados['estado'].map(estado_para_sigla)
# mobilidade2_estados['estado_sigla'] = mobilidade2_estados['estado'].map(estado_para_sigla)
# mobilidade3_estados['estado_sigla'] = mobilidade3_estados['estado'].map(estado_para_sigla)
# mobilidade1_estados = mobilidade1_estados.drop(columns=['estado'])
# mobilidade2_estados = mobilidade2_estados.drop(columns=['estado'])
# mobilidade3_estados = mobilidade3_estados.drop(columns=['estado'])
# mobilidade_completa_df = pd.concat([mobilidade1_estados, mobilidade2_estados, mobilidade3_estados], axis=0)
# estados_completa_df = pd.concat([df_estados1, df_estados2, df_estados3, df_estados4, df_estados5, df_estados6])
# merged_df = pd.merge(estados_completa_df, mobilidade_completa_df, left_on=['estado', 'data'], right_on=['estado_sigla', 'date'])
# df_estados=merged_df
# df_estados['media_acumulada_trabalho'] = df_estados['workplaces_percent_change_from_baseline'].expanding().mean()
# df_estados['media_acumulada_transporte'] = df_estados['transit_stations_percent_change_from_baseline'].expanding().mean()
# df_estados['media_acumulada_residencial'] = df_estados['residential_percent_change_from_baseline'].expanding().mean()
# df_estados['media_acumulada_residencial'] = df_estados['media_acumulada_residencial'].apply(lambda x: f"{x:.2f}")
# df_estados['media_acumulada_trabalho'] = df_estados['media_acumulada_trabalho'].apply(lambda x: f"{x:.2f}")
# df_estados['media_acumulada_transporte'] = df_estados['media_acumulada_transporte'].apply(lambda x: f"{x:.2f}")
# df_estados.to_csv('df_estados.csv', index=False)

#-=====================================================================================================-

#-=- Carregamento dos dados -=-

df_estados = pd.read_csv("df_estados.csv")
df_brasil = pd.read_csv("df_brasil.csv")

mapa = json.load(open("geojson/brasil_geo.json", "r"))

mapa["features"][0].keys()

df_estados_ = df_estados[df_estados["data"] == "2021-06-13"]
colunas_selecionadas = {"casosAcumulado": "Casos Acumulados", 
                "casosNovos": "Novos Casos", 
                "obitosAcumulado": "Óbitos Totais",
                "obitosNovos": "Óbitos por dia",
                "transit_stations_percent_change_from_baseline": "Taxa de Mudança nas Estações de Transporte",
                "media_acumulada_transporte": "Taxa Acumulada nas Estações de Transporte",
                "workplaces_percent_change_from_baseline": "Taxa de Mudança no Trabalho",
                "media_acumulada_trabalho": "Taxa Acumulada no Trabalho",
                "residential_percent_change_from_baseline": "Taxa de Mudança nas Residências",
                "media_acumulada_residencial": "Taxa Acumulada nas Residências"
                }

#-=====================================================================================================-

#-=- Instânciação -=-

app = dash.Dash(__name__, external_stylesheets=[dbc.themes.JOURNAL])

fig = px.choropleth_mapbox(df_estados_, locations="estado",
    geojson=mapa, center={"lat": -14.95, "lon": -52.98},
    zoom=4, color="casosNovos", color_continuous_scale="brbg", opacity=0.4,
    hover_data={"casosAcumulado": True, "casosNovos": True, "obitosAcumulado": True, "obitosNovos": True, "estado": True, "transit_stations_percent_change_from_baseline": True, "workplaces_percent_change_from_baseline": True, "residential_percent_change_from_baseline": True, "media_acumulada_transporte": True, "media_acumulada_trabalho": True, "media_acumulada_residencial": ":.1f"}
    )

fig.update_traces(
    hovertemplate=(
        "<b>%{location}</b><br><br>"
        "Casos acumulados: %{z}<br>"
        "Casos novos: %{customdata[1]}<br>"
        "Óbitos acumulados: %{customdata[2]}<br>"
        "Óbitos novos: %{customdata[3]}<br>"
        "Mudança em transporte: %{customdata[5]:.1f}%<br>"
        "Mudança em trabalho: %{customdata[6]:.1f}%<br>"
        "Mudança em residencial: %{customdata[7]:.1f}%<br>"
        "Acumulada transporte: %{customdata[8]:.1f}%<br>"
        "Acumulada trabalho: %{customdata[9]:.1f}%<br>"
        "Acumulada residencial: %{customdata[10]:.1f}%"
    )
)

fig.update_layout(
    mapbox_style="carto-positron",
    autosize=True,
    margin=go.layout.Margin(l=0, r=0, t=0, b=0),
    showlegend=False,)
df_data = df_estados[df_estados["estado"] == "RO"]


fig2 = go.Figure(layout={"template":"plotly_white"})
fig2.add_trace(go.Scatter(x=df_data["data"], y=df_data["casosAcumulado"]))
fig2.update_layout(
    paper_bgcolor="#FFFFFF",
    plot_bgcolor="#FFFFFF",
    autosize=True,
    margin=dict(l=10, r=10, b=10, t=10),
    )

#-=====================================================================================================-

#-=- Layout  -=-

app.layout = dbc.Container(
    children=[
        dbc.Row([
            dbc.Col(
                [
                    dcc.Loading(
                        id="loading-1",
                        type="default",
                        children=[dcc.Graph(id="choropleth-map", figure=fig, 
                            style={'height': '100vh', 'margin-right': '10px'})],
                    ),
                ], md=6),

            dbc.Col([
                html.Div([
                    html.H5(children="Evolução COVID-19 e Relatório de Mobilidade"),
                    dbc.Button("BRASIL", color="info", id="botao-localizacao", size="lg")
                ], style={"background-color": "#F4FBF9", "margin": "-25px", "margin-left": "20px"}),

                html.P("Informe a data na qual deseja obter informações:", style={"margin-top": "40px"}),

                html.Div(
                    className="dropdown",
                    children=[
                        dcc.DatePickerSingle(
                            id="date-picker",
                            min_date_allowed=df_estados.groupby("estado")["data"].min().max(),
                            max_date_allowed=df_estados.groupby("estado")["data"].max().min(),
                            initial_visible_month=df_estados.groupby("estado")["data"].min().max(),
                            date=df_estados.groupby("estado")["data"].max().min(),
                            display_format="MMMM D, YYYY",
                            style={"border": "2px solid #dbdbdb44"},
                        )
                    ],
                ),

        # Primeira linha de 3 cards
        dbc.Row([
            dbc.Col(dbc.Card([
                dbc.CardBody([
                    html.Div([
                        html.Span("Casos recuperados", className="card-texto"),
                        html.H3(style={"color": "#adfc92"}, id="casos-recuperados-texto"),
                        html.Span("Em acompanhamento", className="card-texto"),
                        html.H5(id="em-acompanhamento-texto"),
                    ], className="row"),
                    # Alinhando a imagem com flex
                    html.Div([
                        dbc.CardImg(src="/assets/icons/health-and-care.png", style={"width": "50px", "height": "50px"}),
                    ], className="d-flex align-items-center justify-content-end")
                ], style={"height": "150px", "display": "flex", "justify-content": "space-between", "align-items": "center"})
            ]), md=4),
            
            dbc.Col(dbc.Card([
                dbc.CardBody([
                    html.Div([
                        html.Span("Casos confirmados totais", className="card-texto"),
                        html.H3(style={"color": "#389fd6"}, id="casos-confirmados-texto"),
                        html.Span("Novos casos na data", className="card-texto"),
                        html.H5(id="novos-casos-texto"),
                    ], className="row"),
                    # Alinhando a imagem com flex
                    html.Div([
                        dbc.CardImg(src="/assets/icons/prancheta.png", style={"width": "50px", "height": "50px"}),
                    ], className="d-flex align-items-center justify-content-end")
                ], style={"height": "150px", "display": "flex", "justify-content": "space-between", "align-items": "center"})
            ]), md=4),
            dbc.Col(dbc.Card([
                dbc.CardBody([
                    html.Div([
                        html.Span("Óbitos confirmados", className="card-texto"),
                        html.H3(style={"color": "#b5b2b3"}, id="obitos-texto"),
                        html.Span("Óbitos na data", className="card-texto"),
                        html.H5(id="obitos-na-data-texto"),
                    ], className="row"),
                    # Alinhando a imagem com flex
                    html.Div([
                        dbc.CardImg(src="/assets/icons/x.png", style={"width": "50px", "height": "50px"}),
                    ], className="d-flex align-items-center justify-content-end")
                ], style={"height": "150px", "display": "flex", "justify-content": "space-between", "align-items": "center"})
            ]), md=4),

            dbc.Col(dbc.Card([
                dbc.CardBody([
                    html.Div([
                        html.Span("Taxa de mudança nas estações de transporte (TOTAL)", className="card-texto"),
                        html.H3(style={"color": "#ffca3a"}, id="transit-stations-texto"),  # ID a ser preenchido
                        html.Span("Mudança percentual na data", className="card-texto"),
                        html.H5(id="transit-stations-mudanca-texto"),  # ID a ser preenchido
                    ], className="row"),
                    html.Div([
                        dbc.CardImg(src="/assets/icons/onibus.png", style={"width": "50px", "height": "50px"}),
                    ], className="d-flex align-items-center justify-content-end")
                ], style={"height": "200px", "display": "flex", "justify-content": "space-between", "align-items": "center"})
            ]), md=4),

            dbc.Col(dbc.Card([
                dbc.CardBody([
                    html.Div([
                        html.Span("Taxa de mudança nos locais de trabalho (TOTAL)", className="card-texto"),
                        html.H3(style={"color": "#6a89cc"}, id="workplaces-texto"),  # ID a ser preenchido
                        html.Span("Mudança percentual na data", className="card-texto"),
                        html.H5(id="workplaces-mudanca-texto"),  # ID a ser preenchido
                    ], className="row"),
                    html.Div([
                        dbc.CardImg(src="/assets/icons/trabalho.png", style={"width": "50px", "height": "50px"}),
                    ], className="d-flex align-items-center justify-content-end")
                ], style={"height": "200px", "display": "flex", "justify-content": "space-between", "align-items": "center"})
            ]), md=4),
        
            dbc.Col(dbc.Card([
                dbc.CardBody([
                    html.Div([
                        html.Span("Taxa de mudança nas residências (TOTAL)", className="card-texto"),
                        html.H3(style={"color": "#ff4d4d"}, id="residential-texto"),  # ID a ser preenchido
                        html.Span("Mudança percentual na data", className="card-texto"),
                        html.H5(id="residential-mudanca-texto"),  # ID a ser preenchido
                    ], className="row"),
                    html.Div([
                        dbc.CardImg(src="/assets/icons/casa.png", style={"width": "50px", "height": "50px"}),
                    ], className="d-flex align-items-center justify-content-end")
                ], style={"height": "200px", "display": "flex", "justify-content": "space-between", "align-items": "center"})
            ]), md=4),
        ], style={"background-color": "#F4FBF9"}),
                html.Div([
                    html.P("Selecione que tipo de dado deseja visualizar:", style={"margin-top": "25px"}),
                    dcc.Dropdown(
                        id="localizacao-dropdown",
                        options=[{"label": j, "value": i} for i, j in colunas_selecionadas.items()],
                        value="casosNovos",
                        style={"margin-top": "10px"}
                    ),
                    dcc.Graph(id="grafico-linha", figure=fig2, style={
                        "background-color": "#FFFFFF",
                    }),
                ]),
            ], md=6, style={
                "padding": "25px",
                "background-color": "#F4FBF9"
            }),
        ]),
], fluid=True)


#-=====================================================================================================-

# Interatividade
@app.callback(
    [
        Output("casos-recuperados-texto", "children"),
        Output("em-acompanhamento-texto", "children"),
        Output("casos-confirmados-texto", "children"),
        Output("novos-casos-texto", "children"),
        Output("obitos-texto", "children"),
        Output("obitos-na-data-texto", "children"),
        Output("transit-stations-texto", "children"),
        Output("transit-stations-mudanca-texto", "children"),
        Output("workplaces-texto", "children"),
        Output("workplaces-mudanca-texto", "children"),
        Output("residential-texto", "children"),
        Output("residential-mudanca-texto", "children"),
    ],
    [Input("date-picker", "date"), Input("botao-localizacao", "children")]
)
def display_status(date, location):
    if location == "BRASIL":
        df_data_on_date = df_brasil[df_brasil["data"] == date]
        df_data_until_date = df_brasil[df_brasil["data"] <= date]
    else:
        df_data_on_date = df_estados[(df_estados["estado"] == location) & (df_estados["data"] == date)]
        df_data_until_date = df_estados[(df_estados["estado"] == location) & (df_estados["data"] <= date)]

    # Dados de COVID-19
    recuperados_novos = "-" if df_data_on_date["Recuperadosnovos"].isna().values[0] else f'{int(df_data_on_date["Recuperadosnovos"].values[0]):,}'.replace(",", ".")
    acompanhamentos_novos = "-" if df_data_on_date["emAcompanhamentoNovos"].isna().values[0] else f'{int(df_data_on_date["emAcompanhamentoNovos"].values[0]):,}'.replace(",", ".")
    casos_acumulados = "-" if df_data_on_date["casosAcumulado"].isna().values[0] else f'{int(df_data_on_date["casosAcumulado"].values[0]):,}'.replace(",", ".")
    casos_novos = "-" if df_data_on_date["casosNovos"].isna().values[0] else f'{int(df_data_on_date["casosNovos"].values[0]):,}'.replace(",", ".")
    obitos_acumulado = "-" if df_data_on_date["obitosAcumulado"].isna().values[0] else f'{int(df_data_on_date["obitosAcumulado"].values[0]):,}'.replace(",", ".")
    obitos_novos = "-" if df_data_on_date["obitosNovos"].isna().values[0] else f'{int(df_data_on_date["obitosNovos"].values[0]):,}'.replace(",", ".")

    # Dados de Mobilidade - Total acumulado até a data e mudança específica da data
    transit_stations_total = "-" if df_data_on_date["media_acumulada_transporte"].isna().values[0] else f'{df_data_on_date["media_acumulada_transporte"].values[0]:.1f}%'
    transit_stations_data = "-" if df_data_on_date["transit_stations_percent_change_from_baseline"].isna().values[0] else f'{df_data_on_date["transit_stations_percent_change_from_baseline"].values[0]:.1f}%'
    workplaces_total = "-" if df_data_on_date["media_acumulada_trabalho"].isna().values[0] else f'{df_data_on_date["media_acumulada_trabalho"].values[0]:.1f}%'
    workplaces_data = "-" if df_data_on_date["workplaces_percent_change_from_baseline"].isna().values[0] else f'{df_data_on_date["workplaces_percent_change_from_baseline"].values[0]:.1f}%'
    residential_total = "-" if df_data_on_date["media_acumulada_residencial"].isna().values[0] else f'{df_data_on_date["media_acumulada_residencial"].values[0]:.1f}%'
    residential_data = "-" if df_data_on_date["residential_percent_change_from_baseline"].isna().values[0] else f'{df_data_on_date["residential_percent_change_from_baseline"].values[0]:.1f}%'

    return (
        recuperados_novos,
        acompanhamentos_novos,
        casos_acumulados,
        casos_novos,
        obitos_acumulado,
        obitos_novos,
        transit_stations_total,
        transit_stations_data,
        workplaces_total,
        workplaces_data,
        residential_total,
        residential_data
    )


@app.callback(
        Output("grafico-linha", "figure"),
        [Input("localizacao-dropdown", "value"), Input("botao-localizacao", "children")]
)
def plot_line_graph(plot_type, location):
    if location == "BRASIL":
        df_data_on_location = df_brasil.copy()
    else:
        df_data_on_location = df_estados[(df_estados["estado"] == location)]
    fig2 = go.Figure(layout={"template":"plotly_white"})
    bar_plots = ["casosNovos", "obitosNovos", "transit_stations_percent_change_from_baseline", "workplaces_percent_change_from_baseline", "residential_percent_change_from_baseline"]

    if plot_type in bar_plots:
        fig2.add_trace(go.Bar(x=df_data_on_location["data"], y=df_data_on_location[plot_type]))
    else:
        fig2.add_trace(go.Scatter(x=df_data_on_location["data"], y=df_data_on_location[plot_type]))
    
    fig2.update_layout(
        paper_bgcolor="#FFFFFF",
        plot_bgcolor="#FFFFFF",
        autosize=True,
        margin=dict(l=10, r=10, b=10, t=10),
        )
    return fig2


@app.callback(
    Output("choropleth-map", "figure"), 
    [Input("date-picker", "date")]
)
def update_map(date):
    df_data_on_states = df_estados[df_estados["data"] == date]

    fig = px.choropleth_mapbox(df_data_on_states, locations="estado", geojson=mapa, 
        center={"lat": -14.95, "lon": -52.98},
        zoom=3.5, color="casosAcumulado", color_continuous_scale="brbg", opacity=0.55,
        hover_data={"casosAcumulado": True, "casosNovos": True, "obitosAcumulado": True, "obitosNovos": True, "estado": True, "transit_stations_percent_change_from_baseline": True, "workplaces_percent_change_from_baseline": True, "residential_percent_change_from_baseline": True, "media_acumulada_transporte": True, "media_acumulada_trabalho": True, "media_acumulada_residencial": ":.1f"}
        )
    
    fig.update_traces(
        hovertemplate=(
            "<b>%{location}</b><br><br>"
            "Casos acumulados: %{z}<br>"
            "Casos novos: %{customdata[1]}<br>"
            "Óbitos acumulados: %{customdata[2]}<br>"
            "Óbitos novos: %{customdata[3]}<br>"
            "Mudança em transporte: %{customdata[5]:.1f}%<br>"
            "Mudança em trabalho: %{customdata[6]:.1f}%<br>"
            "Mudança em residencial: %{customdata[7]:.1f}%<br>"
            "Acumulada transporte: %{customdata[8]:.1f}%<br>"
            "Acumulada trabalho: %{customdata[9]:.1f}%<br>"
            "Acumulada residencial: %{customdata[10]:.1f}%"
        )
    )

    fig.update_layout(paper_bgcolor="#D4DADC", mapbox_style="carto-positron", autosize=True,
                    margin=go.layout.Margin(l=0, r=0, t=0, b=0), showlegend=False)
    return fig


@app.callback(
    Output("botao-localizacao", "children"),
    [Input("choropleth-map", "clickData"), Input("botao-localizacao", "n_clicks")]
)
def update_location(click_data, n_clicks):
    changed_id = [p['prop_id'] for p in dash.callback_context.triggered][0]
    if click_data is not None and changed_id != "botao-localizacao.n_clicks":
        state = click_data["points"][0]["location"]
        return "{}".format(state)
    
    else:
        return "BRASIL"

if __name__ == "__main__":
    app.run_server(host="0.0.0.0", port=int(os.environ.get("PORT", 5000)))

#-=====================================================================================================-