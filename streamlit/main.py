#Writing Methods
import streamlit as st
import sys
import pandas as pd
import numpy as np

#For Title of the App
st.title("Create a Title like me using st.title()") 

#For subheaders
st.header("Make a header like me using st.header()") 

#For headers ( smaller than Title, bigger than subheader) 
st.subheader("Hi I am a subheader, made using st.subheader()")

#For writing paragraphs
st.text("Hi I am a text function")

#passing command line arguments using [--script args] and the streamlit urn function
st.write("Command-line arguments passed to the script at the run:")
st.write(sys.argv)

#writing to the app without using streamlit methods
st.write("1. Creating a table without streamlit methods:pure pandas")
df = pd.DataFrame({
    'first colum':[1, 2, 3 , 4 ,5],
    'second colum':[10, 20, 30, 40, 50]
})
df

#Do the same table uisng st.write() method
st.write("2. Here is our first attempt to create a table using st.write and data frame pandas")
st.write(pd.DataFrame({
    'first colum':[1, 2, 3 , 4 ,5],
    'second colum':[10, 20, 30, 40, 50]
}))
st.info("I am created with st.info. I am here to inform you that me, the table above has been created by calling the Datafrme with the st.write() method. st.write knows what to do!")

#creating a random table using st.dataframe
st.write("3. Creating a Radom Normal table with st.dataframe. ")
dataframe = np.random.randn(10, 20) #generate standar normalised numbers 10 rows and 20 columns, mean 0 std 1. 
st.dataframe(dataframe)

#using pandas styler and numpy 
st.write("4. Create a table and highlight maximum values in each column. Also name columns differently :)")
dataframe = pd.DataFrame(
    np.random.randn(10, 20),
    columns=('col %d' %i for i in range(20))
)
st.dataframe(dataframe.style.highlight_max(axis=0))

#same thing with st.table() method, observe differences, it doesnt fit the content in the cell like st.dataframe. 
st.write("4. Same as above using st.table() :)")
dataframe = pd.DataFrame(
    np.random.randn(10, 20),
    columns=('col %d' %i for i in range(20))
)
st.table(dataframe)

#markdown text

st.markdown("**Hello** World! I am a markdown text!:)s")

