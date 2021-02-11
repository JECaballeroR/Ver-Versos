import streamlit as st
from pathlib import Path

import start_api



from interface import combine_images, encoding_sentences, preprocess_text

app_formal_name = "Ver-Versos"



# Start the app in wide-mode
st.set_page_config(
    layout="wide", page_title=app_formal_name, initial_sidebar_state="expanded"
)


st.sidebar.title(app_formal_name)
st.sidebar.markdown("Una WebApp que combina la poesía de [Jorge Caballero](https://www.instagram.com/sosiadeldesasosiego/) con imágenes de [Unsplash.](https://unsplash.com/)")

st.sidebar.markdown("## Instrucciones ##")

# Load presaved poems
known_poems_dest = Path("docs") / "collected_poems"
known_poems = {}
for f_poem in known_poems_dest.glob("*.txt"):
    with open(f_poem) as FIN:
        title, lines = preprocess_text(FIN.read())

    known_poems[title] = lines

print(known_poems.keys())

# Select a starting poem and display the choices in the sidebar
default_poem = "En mi pequeño mundo lleno de nada"
poem_list = list(known_poems.keys())
poem_choice = st.sidebar.selectbox(
    "Elige uno de los poemas del siguiente menú desplegable", poem_list, index=poem_list.index(default_poem)
)
lines = known_poems[poem_choice]



# If the user has a custom poem, use it here
with st.beta_expander("Personaliza el texto del poema (da clic aquí)"):
    text_input = st.text_area(
        "Edita (o pega) el poema aquí, una línea por set de imágenes. La primera línea será el título. Oprime [Control+Enter] para procesar.",
        value="\n".join([poem_choice] + lines),
    )
    poem_choice, lines = preprocess_text(text_input)

# Run the selected poem through the model
results = encoding_sentences(lines)


st.title(poem_choice)
#st.sidebar.markdown("-----------------------------------")
st.sidebar.header("Autores")
st.sidebar.markdown("### Travis Hoppe (Metasemantic) (Código base) ###")

st.sidebar.markdown('[![metasemantic]\
                    (https://img.shields.io/badge/Github-@thoppe-metasemantic.svg?colorA=gray&colorB=dodgerblue&logo=github)]\
                    (https://github.com/thoppe)')


st.sidebar.markdown('[![metasemantic]\
                    (https://img.shields.io/badge/Twitter-@metasemantic-metasemantic.svg?colorA=gray&colorB=dodgerblue&logo=twitter)]\
                    (https://twitter.com/metasemantic/)')




st.sidebar.markdown("### JECaballeroR (sosiadeldesasosiego) (Código y poemas) ###")

st.sidebar.markdown('[![JECaballeroR]\
                    (https://img.shields.io/badge/Github-@JECaballeroR-JECaballeroR.svg?colorA=gray&colorB=dodgerblue&logo=github)]\
                    (https://github.com/JECaballeroR)')

st.sidebar.markdown('[![Sosia del desasosiego]\
                    (https://img.shields.io/badge/Instagram-@Sosiadeldesasosiego-JECaballeroR.svg?colorA=gray&colorB=pink&logo=instagram)]\
                    (https://www.instagram.com/sosiadeldesasosiego/)')





st.sidebar.markdown('[![BMAC_JECaballeroR]\
                    (https://img.shields.io/static/v1?label=BuyMeACoffee&message=JECaballeroR&color=yellow&logo=buy-me-a-coffee)]\
                    (https://www.buymeacoffee.com/kIOTtHe)')



# Show the credits for each photo in an expandable sidebar
credits = []
for k, row in enumerate(results):
    line = row["text"]
    st.markdown(f"## *{line}*")
    grid = combine_images(row["unsplashIDs"])

    credits.append(f"*{line}*")

    for image_idx in row["unsplashIDs"]:
        source_url = f"https://unsplash.com/photos/{image_idx}"
        credit = f"[{source_url}]({source_url})"
        credits.append(credit)
    credits.append("\n")

    # caption = ', '.join([f"{x:0.0f}" for x in row['scores']])
    st.image(grid, use_column_width=True)



st.markdown(
    f"{app_formal_name} "
    f"combina poemas e imágenes [CLIP](https://openai.com/blog/clip) de OpenAI. "
    f"Las imágenes se obtienen de Unsplash [landscape dataset](https://github.com/unsplash/datasets) "
    "y fotos destacadas, con créditos al final de la página."
)



st.markdown(
    "Adaptado con amor 💙 del proyecto [alph-the-sacred-river](https://github.com/thoppe/alph-the-sacred-river), por [@metasemantic](https://twitter.com/metasemantic/status/1349446585952989186)"
)

with st.beta_expander("Créditos de las imágenes utilizadas:"):
    st.markdown("Estructura de los créditos: ")
    st.markdown("** Linea del poema ** - Link al las imágenes usadas")
    st.markdown("\n".join(credits))
