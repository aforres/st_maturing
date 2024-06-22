import streamlit as st
import pandas as pd
import numpy as np

st.title('TEST DRAFT ONLY Resources News')
#st.sidebar.title('Navigation')
nav=st.sidebar.radio('Navigation',['Home','Agriculture','Energy'])

if nav == 'Home':
    st.write('Home')
    st.write('Just A Template Page - see Energy')
        
    # Expander section
    with st.expander("About"):
      st.write("""Trying to add a data table, chart, sidebar button with 
              ballons, an image, text input & exploring tabs!""")

    # Sidebar section
    with st.sidebar:
      st.subheader('This is a Sidebar')
      st.write('Button with Balloons 🎈')
      if st.button('Click me!✨'):
        st.balloons()
      else:
        st.write(' ')

    # Dataframe and Chart display section
    st.subheader('Interactive Data Table')
    df = pd.DataFrame(
        np.random.randn(50, 3),  # generates random numeric values!
        columns=["a", "b", "c"])
    st.dataframe(df) 

    st.subheader('Bar Chart 📊')
    st.bar_chart(df)

    # Image upload and text input section
    st.subheader('An Image')
    st.image('http://www.kurzweilai.net/images/boeing2025design.jpg')

    st.subheader('Text Input')
    greet = st.text_input('Write your name, please!')
    st.write('👋 Hey!', greet)


    # Tabs section
    st.subheader('Tabs')
    tab1, tab2 = st.tabs(["TAB 1", "TAB 2"])

    with tab1:
      st.write('WOW!')
      st.image("https://www.onlyinyourstate.com/wp-content/uploads/2016/01/315-e1458990339270.jpg", width=720)

    with tab2:
      st.write('Do you like ice cream? 🍨')
      agree = st.checkbox('Yes! I love it')
      disagree = st.checkbox("Nah! 😅")
      if agree:
        st.write('Even I love it 🤤')
      if disagree:
        st.write('You are boring 😒')

if nav == 'Agriculture':
    st.write('Agriculture')
    st.write('Just A Blank Page - see Energy')
    


if nav == 'Energy':
    st.write('Energy')

    st.subheader("Work Underway to Upgrade High-Voltage Power System in Northwest Ohio")

    st.markdown("Monday - May 13: (RWE) - American Transmission Systems, Inc. (ATSI), a subsidiary of " 
    "FirstEnergy Corp. (NYSE: FE), has started construction to upgrade a 138-kilovolt " 
    "substation in Lucas County's Springfield Township and reconfigure connecting high-voltage " 
    "power lines. The combined work will enhance reliability for nearly 23,000 customers of " 
    "Toledo Edison in the area. \n\n" 

    "ATSI will expand the substation on company-owned property by "
    "17,870 square feet, a 58% increase in the size of its footprint, to install new equipment "
    "– including new automated devices – that will allow the company to enhance and reorganize "
    "the existing transmission lines. This will help reduce the number of power outages that "
    "customers experience and make it easier for the station to be maintained without power "
    "interruptions. \n\n"
                
    "Carl Bridenbaugh, FirstEnergy's Vice President of Transmission: 'This "
    "upgrade to our substation and connecting lines will help prevent outages for thousands of " 
    "Toledo Edison customers in northwest Ohio while providing us with the flexibility we need "
    "to provide safe, reliable power in the future.' ATSI also will upgrade more than 10 miles "
    "of existing transmission lines that connect to the substation and construct a one-mile "
    "section of new line. The new configuration will eliminate potential sources of service "
    "interruptions. "
    ,
        )
