import streamlit as st
import matplotlib
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from scipy import interpolate

st.set_page_config(page_title = 'PDT IMAGING SYSTEM',layout="wide")
st.title('PAKISTAN DETECTOR TECHNOLOGIES IMAGING SYSTEM 📈📉📊')
st.subheader('Choose EXCEL file')
upload=st.file_uploader('EXCEL FILE',type='xlsx')

if upload:
    st.markdown('---')
    excel_data_df = pd.read_excel(upload, engine='openpyxl')
    st.dataframe(excel_data_df)
    st.subheader('Select Colormap')
    jet = st.checkbox('Jet')
    seismic = st.checkbox('Seismic')
    puor = st.checkbox('PuOr')
    twilight = st.checkbox('Twilight')
    twilight_s = st.checkbox('Twilight Shifted')
    if jet:
        cmap = 'jet'
    elif seismic:
        cmap = 'seismic'
    elif puor:
        cmap = 'PuOr'
    elif twilight:
        cmap = 'twilight'
    elif twilight_s:
        cmap = 'twilight_shifted'

    st.subheader('Select Grid Color')
    st.text("Select only one")
    w = st.checkbox('White')
    k = st.checkbox('Black')
    g = st.checkbox('Green')
    y = st.checkbox('Yellow')
    if w:
        gc = 'w'
    elif k:
        gc = 'k'
    elif g:
        gc = 'g'
    elif y:
        gc = 'y'

    X = excel_data_df['x'].tolist()
    Y = excel_data_df['y'].tolist()
    Z = excel_data_df['z'].tolist()

    X = np.array(X)
    Y = np.array(Y)
    Z = np.array(Z)
    # Flatten trial data to meet your requirement:
    x = X.ravel()
    y = Y.ravel()
    z = Z.ravel()

    # Resampling on as square grid with given resolution:
    resolution = 8
    xlin = np.linspace(min(x), max(x), resolution)
    ylin = np.linspace(min(y), max(y), resolution)
    Xlin, Ylin = np.meshgrid(xlin, ylin)

    # Linear multi-dimensional interpolation:
    interpolant = interpolate.NearestNDInterpolator([r for r in zip(x, y)], z)
    Zhat = interpolant(Xlin.ravel(), Ylin.ravel()).reshape(Xlin.shape)
    # Render and interpolate again if necessary:
    fig, axe = plt.subplots()

    axe.imshow(Zhat, origin="lower", cmap=cmap, interpolation='bicubic', extent=[min(x), max(x), min(y), max(y)])

    # plt.xlabel('X Values', fontsize = 15)
    # plt.ylabel('Y Values', fontsize = 15)

    plt.xticks(np.arange(min(x), max(x) + 1, 1.0))
    plt.yticks(np.arange(min(y), max(y) + 1, 1.0))

    axe.set_xticklabels([])
    axe.set_yticklabels([])

    axe.grid(True, linewidth=0.3, color=gc)
    norm = matplotlib.colors.Normalize(vmin=min(z), vmax=max(z), clip=False)

    plt.colorbar(plt.cm.ScalarMappable(cmap=cmap, norm=norm))
    st.markdown('---')
    st.write(fig)

