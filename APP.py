import streamlit as st
import matplotlib
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from scipy import interpolate

st.set_page_config(page_title = 'PDT IMAGING SYSTEM')
st.image('pdt.png')
st.title('PAKISTAN DETECTOR TECHNOLOGIES IMAGING SYSTEM')
st.subheader('Choose EXCEL file')
upload=st.file_uploader('EXCEL FILE',type='xlsx')

if upload:
    st.subheader('MODES:')
    mode1 = st.button('Depth Detection')
    mode2 = st.button('Fe/Non-Fe Detection')

    if mode1:
        st.markdown('---')
        excel_data_df = pd.read_excel(upload, engine='openpyxl')
        col1, col2, col3 = st.columns(3)
        with col2:
            st.dataframe(excel_data_df)

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

        cmap = 'jet'
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

        axe.grid(True, linewidth=0.3, color='w')
        norm = matplotlib.colors.Normalize(vmin=min(z), vmax=max(z), clip=False)

        plt.colorbar(plt.cm.ScalarMappable(cmap=cmap, norm=norm))
        st.markdown('---')
        st.write(fig, figsize=(2, 2))

    elif mode2:
        st.markdown('---')
        excel_data_df = pd.read_excel(upload, engine='openpyxl')
        col1, col2, col3 = st.columns(3)
        with col2:
            st.dataframe(excel_data_df)

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

        cmap = 'seismic'
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

        axe.grid(True, linewidth=0.3, color='k')
        norm = matplotlib.colors.Normalize(vmin=min(z), vmax=max(z), clip=False)

        plt.colorbar(plt.cm.ScalarMappable(cmap=cmap, norm=norm))
        st.markdown('---')
        st.write(fig, figsize=(2, 2))








