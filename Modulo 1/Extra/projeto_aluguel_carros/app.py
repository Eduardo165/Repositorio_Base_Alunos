import streamlit as st

#------------------------------ SIDEBAR
st.sidebar.image('log.png')

st.sidebar.title('Duzeira car - Aluguel de carros')
carros= ['kiwid','amarok', 'ix35', 'elantra']
modelo = st.sidebar.selectbox('Selecione o carro alugado', carros)



#------------------------------PRINCIPAL
st.title('Duzeira car - Aluguel de carros')
st.markdown(f'## Voce escolheu o modelo:  {modelo}')
st.image(f'{modelo}.png')

if modelo== 'KIWID':
    diaria= 150

elif modelo== 'AMAROK':
    diaria=250

elif modelo== 'IX35':
    diaria=300

elif modelo=='ELANTRA':
    diaria=358

dias = st.text_input(f'Por quantos dias voce alugou o {modelo} ?')
km= st.text_input(f'Quantos km voce rodou ?')

if st.button('Calcular'):
    dias= int(dias)
    km= float(km)

    total_dias = dias * diaria
    total_km = km*0.30
    aluguel= total_dias + total_km

    st.warning(f'voce alugou o {modelo} por {dias} dias e rodou {km} km. O valor doa aluguel sera R${aluguel}')