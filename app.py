import streamlit as st
from multiapp import MultiApp
from apps import (
    home,
    SignalandImageProcessing,
    OptimisationMethodsforDataScience,
    StatisticsforDataScience,
    QuantumInformationQuantumComputingandQuantumAlgorithms,
    NeuralNetworkTheory,
)  # import your app modules here

from PIL import Image

st.set_page_config(
    page_title="DS RPA",
    page_icon="📚",
    layout="wide",
    initial_sidebar_state="expanded",
)

app = MultiApp()

image = Image.open("images/logo.png")
st.sidebar.image(image, width=300)

st.sidebar.markdown(
    """
## Course Dashboard
W2021
"""
)


st.write(
    "<style>div.row-widget.stRadio > div{flex-direction:row;}</style>",
    unsafe_allow_html=True,
)

# Add all your application here
app.add_app("Home", home.app)

app.add_app("Signal and Image Processing", SignalandImageProcessing.app)
app.add_app(
    "Optimisation Methods for Data Science", OptimisationMethodsforDataScience.app
)
app.add_app("Statistics for Data Science", StatisticsforDataScience.app)
app.add_app(
    "Quantum Information, Quantum Computing, and Quantum Algorithms",
    QuantumInformationQuantumComputingandQuantumAlgorithms.app,
)
app.add_app("Neural Network Theory", NeuralNetworkTheory.app)


###############################################################################
# The main app
app.run()

st.sidebar.markdown("<hr/>", unsafe_allow_html=True)
###############################################################################
st.sidebar.markdown(
    """
### Roderick Perez
"""
)
st.sidebar.write("[Email](a12013049@unet.univie.ac.at)")
