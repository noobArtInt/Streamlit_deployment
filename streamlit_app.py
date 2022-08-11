
import streamlit as st
import pandas as pd

def data_elements():
    st.markdown("# Welcome to Data Elements 📚")
    st.sidebar.markdown("# Data Elements 📚")
    st.write('##')

    # dataframe -> Display a dataframe as an interactive table.
    st.subheader('The Dataframe command')
    st.write('This command is used to display a dataframe as an interactive table. We can also pass a Pandas Styler object to change the style of the rendered DataFrame.')
    st.write('The displayed dataframe is interactive in the following ways')
    st.write("➦ **Column sorting:** sort columns by clicking on their headers.")
    st.write("➦ **Column resizing:** resize columns by dragging and dropping column header borders.")
    st.write("➦ **Table (height, width) resizing:** resize tables by dragging and dropping the bottom right corner of tables.")
    st.write("➦ **Search:** search through data by clicking a table, use ctrl+f to bring up the search bar.")
    st.write("➦ **Copy to clipboard:** select one or multiple cells, copy them to clipboard, and paste them into your favorite spreadsheet software.")
    st.write('##')
    l1,r1=st.columns([1,2])
    with l1:
        st.caption('Writing a dataframe')
        st.dataframe(pd.DataFrame({
            'Name': ['John', 'Daisy'],
            'Email': ['john@yahoo.com', 'daisy@gmail.com'],
            'Marks': [95, 85]
            }), width=400, height=100)
    with r1:
        st.code("""st.dataframe(pd.DataFrame({
            'Name': ['John', 'Daisy'],
            'Email': ['john@yahoo.com', 'daisy@gmail.com'],
            'Marks': [95, 85]
            }), width=400, height=100) """,language='python')
    st.write('---')

    # table -> Display a static table.
    st.subheader('The Table command')
    st.write('The table command is used to display a table on to the web page. This command is different from st.dataframe when it comes to interactivity and layout.')
    st.write('##')
    l2,r2=st.columns([1,2])
    with l2:
        st.caption('Writing a table')
        st.table(pd.DataFrame({
            'Name': ['John', 'Daisy'],
            'Email': ['john@yahoo.com', 'daisy@gmail.com'],
            'Marks': [95, 85]
            }))
    with r2:
        st.code(""" st.table(pd.DataFrame({
            'Name': ['John', 'Daisy'],
            'Email': ['john@yahoo.com', 'daisy@gmail.com'],
            'Marks': [95, 85]
            }))""",language='python')
    st.write('---')

    # Metric -> Display a metric in big bold font, with an optional indicator of how the metric changed.
    st.subheader("The Metric command")
    st.write("This command is used to display a metric in big bold font, with an optional indicator of how the metric changed. The delta indicator color can also be inverted or turned off")
    st.write('##')
    l3,r3=st.columns([1,2])
    with l3:
        st.caption("Displaying metrics or KPI's")
        st.metric(label='Sales', value='2000$', delta='150$')
    with r3:
        st.write('##')
        st.code("st.metric(label='Sales', value='2000$', delta='150$')",language='python')
    st.write('##')

    # Multiple KPI's side by side
    st.caption("Displaying multiple KPI's using st.columns")
    col1, col2, col3, col4 = st.columns(4)
    col1.metric("Total Cost", '250$', '50$')
    col1.code("""col1.metric("Total Cost", 
    '250$', '50$')""",language='python')
    col2.metric("Storage cost", '125$', '-5$')
    col2.code("""col2.metric("Storage cost", 
    '125$', '-5$')""", language='python')
    col3.metric("Stage cost", "100$", "7$")
    col3.code("""col3.metric("Stage cost",
     "100$", "7$")""", language='python')
    col4.metric("Failsafe Cost", "25$", "-10$")
    col4.code("""col4.metric("Failsafe Cost",
    "25$", "-10$")""", language='python')
    st.write('---')

    # json -> Display object or string as a pretty-printed JSON string.
    st.subheader('The Json command')
    st.write("This command is used to display object or string as a pretty-printed JSON string. This command also has an optional boolean argument that allows the user to set whether the initial state of this json element should be expanded. The default value for this argument is set to True.")
    l4,r4=st.columns([1,2])
    with l4:
        st.caption('Writing a Json')
        st.json('{"name":"John", "age":30, "car":null}')
    with r4:
        st.write('##')
        st.write('##')
        st.code("""st.json('{"name":"John", "age":30, "car":null}')""",language='python')
    st.write('---')

    st.markdown("For additional information, pls refer this link : {}".format('https://docs.streamlit.io/library/api-reference/data'))

data_elements()
