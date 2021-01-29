import pandas as pd
import streamlit as st
import altair as alt

#conda install -c conda-forge altair

@st.cache(suppress_st_warning=True)  
def load_data():
    covid = pd.read_csv('Covid-19_SP.csv')
    covid['DATA']= pd.to_datetime(covid['DATA'], format = '%Y-%m-%d')
    latest = covid[covid['DATA']=='2020-11-19'][['CIDADE','CONFIRMADO','MORTES','POPULACAO_ESTIMADA','INDICE_MORTES']]
    return covid, latest

covid, latest = load_data()

#st.dataframe(covid)
st.title('COVID-19 Dashboard')
st.sidebar.markdown('Covid 19 Dashboard')
st.sidebar.markdown("""Este App Web tem o intuito de mostrarde forma visível as informações sobre o Covid-19 em SP""")

st.header('Selecionar a cidade que você quer acompanhar:')
city = st.selectbox('', covid['CIDADE'].unique())

st.header('Escolha o ínice que você deseja acompanhar da cidade de {}'.format(city))
daily = st.selectbox('',('Casos confirmados','Mortes Confirmadas', 'Índice de mortes'))
graph = st.radio('Selecione o tipo de Gráfico:', ('Gráfico de linha','Gráfico scatter'))


st.header(' ')

ca = alt.Chart(covid[covid['CIDADE'] == city]).encode(
    x = 'DATA',
    y = 'CONFIRMADO',
    tooltip = ['DATA', 'CIDADE', 'CONFIRMADO']
).interactive()

re = alt.Chart(covid[covid['CIDADE'] == city]).encode(
    x = 'DATA',
    y = 'MORTES',
    tooltip = ['DATA', 'CIDADE', 'MORTES']
).interactive()

de = alt.Chart(covid[covid['CIDADE'] == city]).encode(
    x = 'DATA',
    y = 'INDICE_MORTES',
    tooltip = ['DATA', 'CIDADE', 'INDICE_MORTES']
).interactive()

cas = alt.Chart(covid[covid['CIDADE'] == city], title='Scatter', width=1000, height=400).mark_circle(color = 'green').encode(
    x = 'DATA',
    y = 'CONFIRMADO',
    size = 'MORTES',
    color = 'INDICE_MORTES',
    tooltip = ['DATA', 'CIDADE', 'CONFIRMADO', 'MORTES', 'INDICE_MORTES']
).interactive()

if daily == 'Casos confirmados':
    if graph == 'Gráfico de linha':
        st.altair_chart(ca.mark_line(color= 'firebrick'))
    else:
        st.altair_chart(ca.mark_circle(color= 'firebrick'))
elif daily == 'Mortes Confirmadas':
    if graph == 'Gráfico de linha':
        st.altair_chart(ca.mark_line(color= 'green'))
    else:
        st.altair_chart(ca.mark_circle(color= 'green'))
elif daily == 'Índice de mortes':
    if graph == 'Gráfico de linha':
        st.altair_chart(ca.mark_line(color= 'blue'))
    else:
        st.altair_chart(ca.mark_circle(color= 'blue'))

st.altair_chart(cas)

a =  alt.Chart(covid[covid['CIDADE'] == city], width=500, height=400).mark_text().encode(
    x = 'dia(DATA):0',
    y = 'mes(DATA):0',
    color = 'sum(MORTES)',
    tooltip = 'sum(MORTES)'
)

b =  alt.Chart(covid[covid['CIDADE'] == city], width=500, height=400).mark_text().encode(
    x = 'dia(DATA):0',
    y = 'mes(DATA):0',
    text =  'sum(MORTES)'
)

c =  alt.Chart(covid[covid['CIDADE'] == city], width=500, height=400).mark_text().encode(
    x = 'dia(DATA):0',
    y = 'mes(DATA):0',
    color = 'sum(MORTES)',
    tooltip = 'sum(MORTES)'
)

d =  alt.Chart(covid[covid['CIDADE'] == city], width=500, height=400).mark_text().encode(
    x = 'dia(DATA):0',
    y = 'mes(DATA):0',
    text =  'sum(MORTES)'
)


st.header('Total de casos confirmados X total mortes {}'.format(city))


con = alt.Chart(covid[covid['CIDADE']==city]).mark_area(color='blue').encode(
    x = 'DATA',
    y = 'MORTES',
    tooltip = ['DATA','MORTES']
).interactive()

rec = alt.Chart(covid[covid['CIDADE']==city]).mark_area(color='green').encode(
    x = 'DATA',
    y = 'CONFIRMADO',
    tooltip = ['DATA','CONFIRMADO']
).interactive()

opt = st.radio(
    'selecione uma das opções:',
    ('Casos Confirmados', 'Mortes Confirmadas')
)

if opt == 'Casos Confirmados':
    st.altair_chart(con)
else:
    st.altair_chart(rec)