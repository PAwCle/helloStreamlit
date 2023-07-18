
import numpy as np
import altair as alt
import pandas as pd
import streamlit as st

st.header('st.write')
st.subheader('This is a subheader')

st.write('Hello, *world!* :sunglasses:')

st.write(1234)

df = pd.DataFrame({
    'first column': [1,2,3,4],
    'second column': [10,20,30,40]
})


st.write('Below is a DataFrame:', df, 'Above is a DataFrame')


df2 = pd.DataFrame(
    np.random.randn(200,3),
    columns=['a','b','c']
)

c = alt.Chart(df2).mark_circle().encode(
    x='a', y='b', size='c', tooltip=['a','b','c']
)

st.write(c)
st.caption('This is a string that explains something above.')

########### MARKDOWN
st.markdown('Streamlit is **_really_ cool**.')
st.markdown("This text is :red[colored red], and this is **:blue[colored]** and bold.")
st.markdown(":green[$\sqrt{x^2+y^2}=1$] is a Pythagorean identity. :pencil:")

st.text('This is some text.')

st.latex(r'''
    a + ar + a r^2 + a r^3 + \cdots + a r^{n-1} =
    \sum_{k=0}^{n-1} ar^k =
    a \left(\frac{1-r^{n}}{1-r}\right)
    ''')

code = '''def hello():
    print("Hello, Streamlit!")'''
st.code(code, language='python')
###########