import streamlit as st
import time

st.write("Sliders and select boxes and sidebars")
add_selectbox = st.sidebar.selectbox(
    'How would you like to be contacted?',
    ('Email', 'Phone', 'Message', 'Other')
)

add_slider = st.sidebar.slider(
    'Select a range of values', 
    0.0, 100.0, (25.0, 75.0)
)

#Columns
st.write('columns')
left_column, right_column = st.columns(2)
left_column.button("Press Me")

with right_column:
    chosen = st.radio(
        'Sorting hat',
        ("Gryffindor", "Slytherin", "Ravenclaw", "Huffelpuff")
    )
    st.write(f"You are in {chosen} house!")


st.header("Show progress")

'Starting a long computation'
latest_iteration = st.empty()
bar = st.progress(0)

for i in range(100):
  # Update the progress bar with each iteration.
  latest_iteration.text(f'Iteration {i+1}')
  bar.progress(i + 1)
  time.sleep(0.1)

'...and now we\'re done!'