import pandas as pd
import streamlit as st
from PIL import Image
from bokeh.models.widgets import Div
import streamlit as st
import warnings
warnings.filterwarnings('ignore')

bpk_icon = Image.open("assets/BPK.ico")
LOGO_IMAGE = "assets/BPK.png"
st.set_page_config(
    layout="centered", page_icon=bpk_icon, page_title="Arsip Digital BPK Perwakilan Sumsel", initial_sidebar_state="auto"
) #layout use wide instead of centered

col1, col2 = st.columns([2,5])
with col1:
    st.image(bpk_icon, width =150, use_column_width=True)
with col2:
    st.title("Arsip Digital")
    st.subheader('BPK perwakilan Sumatera Selatan')

option_2 = ''



with st.sidebar:
    col1, col2 = st.columns([1, 3])
    with col1:
        st.image(bpk_icon, width=150, use_column_width=True)

    with col2:
        st.write("BPK perwakilan Sumsel")

    option = st.radio(
        'Data apa yang ingin anda cari?',
        ('Pemeriksaan', 'Non Pemeriksaan'))

    if option == 'Pemeriksaan':
        option_2 = st.selectbox(
        'Pilih Subauditorat',
        ('', 'Subauditorat Sumsel I', 'Subauditorat Sumsel II'))



    elif option == 'Non Pemeriksaan':
        option_2 = st.selectbox(
            'Kesekretariatan',
            ('', 'Sekretariat Perwakilan', 'Subbag Humas dan TU', 'Subbag SDM', 'Subbag Keuangan', 'Subbag Umum dan TI', 'Subbag Hukum'))

if option_2 == '':
    image = Image.open('assets/IMG-20210419-WA0112.jpg')
    st.image(image, caption='BPK Perwakilan Sumsel')

option_3 = '' #default value for option_3 so it won't throw any exception

if option_2 == 'Subauditorat Sumsel I':
     option_3 = st.selectbox(
          'Pilih Entitas',
          ( '',
            'Kabupaten Ogan Komering Ilir',
            'Kota Lubuk Linggau',
            'Kabupaten Banyuasin',
            'Kabupaten Ogan Ilir',
            'Kabupaten Ogan Komering Ulu Timur',
            'Kota Palembang',
            'Kabupaten Penukal Abab Lematang Ilir',
            'Kabupaten Musi Rawas Utara'))

elif option_2 == 'Subauditorat Sumsel II':
     option_3 = st.selectbox(
          'Pilih Entitas',
          ( '',
            'Kabupaten Lahat',
           'Kabupaten Musi Banyuasin',
           'Kabupaten Ogan Komering Ulu Selatan',
           'Kota Prabumulih',
           'Kabupaten Muara Enim',
           'Kabupaten Musi Rawas',
           'Kabupaten Ogan Komering Ulu',
           'Kota Pagar Alam',
           'Kabupaten Empat Lawang'))

elif option_2 == 'Sekretariat Perwakilan':
    option_3 = st.selectbox('Pilih arsip', ('', 'a', 'b',
                                            'c', 'd', 'e',
                                            'Uncategorized'))
elif option_2 == 'Subbag Humas dan TU':
    option_3 = st.selectbox('Pilih arsip', ('', 'a', 'b',
                                            'c', 'd', 'e',
                                            'Uncategorized'))
elif option_2 == 'Subbag SDM':
    option_3 = st.selectbox('Pilih arsip', ('', 'a', 'b',
                                            'c', 'd', 'e',
                                            'Uncategorized'))
elif option_2 == 'Subbag Keuangan':
    option_3 = st.selectbox('Pilih arsip', ('', 'a', 'b',
                                            'c', 'd', 'e',
                                            'Uncategorized'))
elif option_2 == 'Subbag Umum dan TI':
    option_3 = st.selectbox('Pilih arsip', ('', 'Nota Dinas Keluar','Nota Dinas Masuk', 'Nota Dinas',
                                            'Surat Keluar', 'Dokumen Kontrak', 'Laporan BMN',
                                            'Berita Acara', 'Formulir Peminjaman TI', 'Formulir Permintaan ATK', 'Uncategorized'))
elif option_2 == 'Subbag Hukum':
    option_3 = st.selectbox('Pilih arsip', ('', 'a', 'b',
                                            'c', 'd', 'e',
                                            'Uncategorized'))

option_4 = ''

if option_3 in ['Kabupaten Ogan Komering Ilir',
            'Kota Lubuk Linggau',
            'Kabupaten Banyuasin',
            'Kabupaten Ogan Ilir',
            'Kabupaten Ogan Komering Ulu Timur',
            'Kota Palembang',
            'Kabupaten Penukal Abab Lematang Ilir',
            'Kabupaten Musi Rawas Utara'] :
    option_4 = st.selectbox('Pilih LHP', ['', 'Laporan Keuangan', 'PDTT', 'Investigasi'])

elif option_3 in ['Kabupaten Lahat',
           'Kabupaten Musi Banyuasin',
           'Kabupaten Ogan Komering Ulu Selatan',
           'Kota Prabumulih',
           'Kabupaten Muara Enim',
           'Kabupaten Musi Rawas',
           'Kabupaten Ogan Komering Ulu',
           'Kota Pagar Alam',
           'Kabupaten Empat Lawang'] :
    option_4 = st.selectbox('Pilih LHP', ['', 'Laporan Keuangan', 'PDTT', 'Investigasi'])

#block subbag umum
elif option_2 == 'Subbag Umum dan TI' and option_3 == 'Nota Dinas Keluar':
    if st.button('Klik saya'):
        js = "window.open('https://drive.google.com/drive/folders/11vlI8mOiU8iBUJ_vfgTYfCPjMuHcJWxP?usp=sharing')"  # New tab or window
        html = '<img src onerror="{}">'.format(js)
        div = Div(text=html)
        st.bokeh_chart(div)

elif option_2 == 'Subbag Umum dan TI' and option_3 == 'Nota Dinas Masuk':
    if st.button('Klik saya'):
        js = "window.open('https://drive.google.com/drive/folders/1eyHRbs5aUHeNTMOqYEvHJ-t5sjFstVLV?usp=sharing')"  # New tab or window
        html = '<img src onerror="{}">'.format(js)
        div = Div(text=html)
        st.bokeh_chart(div)

elif option_2 == 'Subbag Umum dan TI' and option_3 == 'Nota Dinas':
    if st.button('Klik saya'):
        js = "window.open('https://portal.bpk.go.id/sites/palembang/subbagumum/Arsip%20TI/DB%20ARSIP%20DIGITAL/Sekretariat/Subbag%20Umum%20dan%20TI/Nota%20Dinas')"  # New tab or window
        html = '<img src onerror="{}">'.format(js)
        div = Div(text=html)
        st.bokeh_chart(div)

elif option_2 == 'Subbag Umum dan TI' and option_3 == 'Surat Keluar':
    if st.button('Klik saya'):
        js = "window.open('https://drive.google.com/drive/folders/1lzOYQF2rt8Rlcb6ONkN6tYWJrm8cGmRb?usp=sharing')"  # New tab or window
        html = '<img src onerror="{}">'.format(js)
        div = Div(text=html)
        st.bokeh_chart(div)
elif option_2 == 'Subbag Umum dan TI' and option_3 == 'Dokumen Kontrak':
    if st.button('Klik saya'):
        js = "window.open('https://drive.google.com/drive/folders/1c-ZqWi8tHez0YxoHDYTNImmBJhpVCiTy?usp=sharing')"  # New tab or window
        html = '<img src onerror="{}">'.format(js)
        div = Div(text=html)
        st.bokeh_chart(div)
elif option_2 == 'Subbag Umum dan TI' and option_3 == 'Laporan BMN':
    if st.button('Klik saya'):
        js = "window.open('https://drive.google.com/drive/folders/1R90VfdH1DCyzQwaicTj6ZA5EJIWKv8t3?usp=sharing')"  # New tab or window
        html = '<img src onerror="{}">'.format(js)
        div = Div(text=html)
        st.bokeh_chart(div)
elif option_2 == 'Subbag Umum dan TI' and option_3 == 'Berita Acara':
    if st.button('Klik saya'):
        js = "window.open('https://drive.google.com/drive/folders/1Ckps_sezLMBdppIlZAoobOmdPljaWxAO?usp=sharing')"  # New tab or window
        html = '<img src onerror="{}">'.format(js)
        div = Div(text=html)
        st.bokeh_chart(div)
elif option_2 == 'Subbag Umum dan TI' and option_3 == 'Formulir Peminjaman TI':
    if st.button('Klik saya'):
        js = "window.open('https://drive.google.com/drive/folders/1820HL-PQjZnMBQUpXYZTQtpXNGqhYSYF?usp=sharing')"  # New tab or window
        html = '<img src onerror="{}">'.format(js)
        div = Div(text=html)
        st.bokeh_chart(div)
elif option_2 == 'Subbag Umum dan TI' and option_3 == 'Formulir Permintaan ATK':
    if st.button('Klik saya'):
        js = "window.open('https://drive.google.com/drive/folders/1utHMEgPfeBj9F1Cve6feIdr7aOQY0BCy?usp=sharing')"  # New tab or window
        html = '<img src onerror="{}">'.format(js)
        div = Div(text=html)
        st.bokeh_chart(div)
elif option_2 == 'Subbag Umum dan TI' and option_3 == 'Uncategorized':
    if st.button('Klik saya'):
        js = "window.open('https://drive.google.com/drive/folders/1YR-Fo_beW2YOoI_r5jRuicmy2X2_JoKk?usp=sharing')"  # New tab or window
        html = '<img src onerror="{}">'.format(js)
        div = Div(text=html)
        st.bokeh_chart(div)
#blok setlan not finished!
elif option_2 == 'Sekretariat Perwakilan':
    if st.button('Klik saya'):
        js = "window.open('https://drive.google.com/drive/u/1/folders/1MWJTLFJcneqm--JoSUqb_2j4-oigBm_8')"  # New tab or window
        html = '<img src onerror="{}">'.format(js)
        div = Div(text=html)
        st.bokeh_chart(div)

#block humas tu not finish
elif option_2 == 'Subbag Humas dan TU':
    if st.button('Klik saya'):
        js = "window.open('https://drive.google.com/drive/folders/1820HL-PQjZnMBQUpXYZTQtpXNGqhYSYF?usp=sharing')"  # New tab or window
        html = '<img src onerror="{}">'.format(js)
        div = Div(text=html)
        st.bokeh_chart(div)

#block sdm not finish
elif option_2 == 'Subbag SDM':
    if st.button('Klik saya'):
        js = "window.open('https://drive.google.com/drive/folders/1820HL-PQjZnMBQUpXYZTQtpXNGqhYSYF?usp=sharing')"  # New tab or window
        html = '<img src onerror="{}">'.format(js)
        div = Div(text=html)
        st.bokeh_chart(div)

#block keuangan not finish
elif option_2 == 'Subbag Keuangan':
    if st.button('Klik saya'):
        js = "window.open('https://drive.google.com/drive/folders/1820HL-PQjZnMBQUpXYZTQtpXNGqhYSYF?usp=sharing')"  # New tab or window
        html = '<img src onerror="{}">'.format(js)
        div = Div(text=html)
        st.bokeh_chart(div)

#block hukum not finish
elif option_2 == 'Subbag Hukum':
    if st.button('Klik saya'):
        js = "window.open('https://drive.google.com/drive/folders/1820HL-PQjZnMBQUpXYZTQtpXNGqhYSYF?usp=sharing')"  # New tab or window
        html = '<img src onerror="{}">'.format(js)
        div = Div(text=html)
        st.bokeh_chart(div)

if option_4 != '' and option_4 in ['Laporan Keuangan', 'PDTT', 'Investigasi']:
    year = st.slider(
        "Tahun Arsip",
        2015, 2022, (2018, 2019))

