'''
Solution unibrow.py
'''
'''
Solution unibrow.py
'''

import streamlit as st
import pandas as pd
from pandaslib import (
    read_file,
    get_column_names,
    get_columns_of_type,
    get_unique_values,
    filter_dataframe
)

st.title("UniBrow")
st.caption("The Universal data browser")

uploaded_file = st.file_uploader("Upload your data file", type=["csv", "xlsx", "json"])

if uploaded_file:
    try:
        # Load file into DataFrame
        df = read_file(uploaded_file)
        st.success("File loaded successfully!")

        # Column multiselect
        column_names = get_column_names(df)
        selected_columns = st.multiselect("Select columns to display", column_names, default=column_names)
        filtered_df = df[selected_columns]

        # Optional filter toggle
        if st.toggle("Apply filter to a text column?"):
            text_columns = get_columns_of_type(df, 'object')

            if text_columns:
                filter_column = st.selectbox("Select a column to filter by", text_columns)
                unique_vals = get_unique_values(df, filter_column)
                selected_value = st.selectbox("Select value", unique_vals)

                # Apply row filter
                filtered_df = filter_dataframe(filtered_df, filter_column, selected_value)
            else:
                st.warning("No text columns available to filter.")

        # Show filtered dataframe
        st.subheader("Filtered Data")
        st.dataframe(filtered_df)

        # Show description of numeric columns
        st.subheader("Descriptive Statistics")
        st.dataframe(filtered_df.describe())

    except Exception as e:
        st.error(f"Error loading file: {e}")
