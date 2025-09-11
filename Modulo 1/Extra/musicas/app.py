import streamlit as st


#------------------SIDEBAR

st.sidebar.image('logo.png')

st.sidebar.title('Trackverse - Playlist')

estilo_musical= ['Pagode' , 'Rock' , 'Reggae' , 'Funk']

musica_escolhida = st.sidebar.selectbox ('O que voce quer ouvir: ' , estilo_musical)


#-------------------------------PRINCIPAL


st.title('Trackverse - Playlist')
st.markdown(f'### Voce escolheu: {musica_escolhida}')

if musica_escolhida == 'Pagode':
    artistas = ['Fundo de quintal' , 'Zeca pagodinho' , 'Thiaguinho']
    artista=st.sidebar.selectbox(f'Escolha um artista: ', artistas)

    if artista == 'Fundo de quintal':
        st.video('https://youtu.be/2Xka3X_fP4g?si=1ag57xsN8hoiHPS3') 

    elif 'Zeca pagodinho':
        st.video('https://youtu.be/fqszqmqjpjY?si=-xo4pHPf90njJEml')

    elif artista == 'Thiaguinho':
        st.video('https://youtu.be/xNRtGCwmoQw?si=k5RGN1gGBo_MbdZD')

    

elif musica_escolhida == 'Rock':
    artistas= ['Elvis presley' , 'Freddie mercury' , 'McCartney']
    artista=st.sidebar.selectbox(f'Escolha um artista: ' ,artistas)

    if artista =='Elvis presley':
        st.video('https://youtu.be/vGJTaP6anOU?si=ZvhOHZHDOGNjZJha')

    elif artista =='Freddie mercury':
        st.video('https://youtu.be/ksNoe8W2jTc?si=XEWy97Fz45BQNCKm')

    elif  artista =='McCartney':
        st.video('https://youtu.be/u6T5C-jzSH0?si=OrnvkSWjTtiSuQTF')


elif musica_escolhida == 'Reggae':
    artistas= ['Bob marley' , 'Jonh Holt'  , 'Yellowman']
    artista=st.sidebar.selectbox(f'Escolha um artista:' , artistas)
    if  artista =='Bob marley':

        st.video('https://youtu.be/69RdQFDuYPI?si=O9KBgo5lEo1NPPgt')

    elif  artista =='Jonh Holt':
        st.video('https://youtu.be/uDT3tXnGFYk?si=iEmpRyQtfmQCPbnD') 


    elif artista == 'Yellowman':
        st.video('https://youtu.be/11S5QPjx3uU?si=SE9Q_OV9UcTM-HXT')



elif musica_escolhida == 'Funk':
    artistas= ['Mc kevin' , 'Mc ryan sp' , 'Mc hariel ']
    artista=st.sidebar.selectbox(f'Escolha um artista :' , artistas) 


if  artista == 'Mc kevin':
    st.video('https://youtu.be/Vvi6pMQj0BI?si=w9O3EEiXUEeILw5D')

elif  artista == 'Mc ryan sp':
    st.video('https://youtu.be/rBgEpYrkiI0?si=3wXvlj39dClqUH4p')

elif  artista == 'Mc hariel':
    st.video ('https://youtu.be/muF5Xuf5qUY?si=12CTUEhXTQPuqh-i')






