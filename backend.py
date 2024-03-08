# -*- coding: utf-8 -*-
"""
Created on Fri Mar  8 20:53:16 2024

@author: 142397
"""

import streamlit as st
import pandas as pd

# 假设你有一个数据框 df，包含了名字（name）和相关的列
data = {'name': ['Alice', 'Bob', 'Charlie', 'David'],
        'col1': [0, 1, 0, 1],
        'col2': [1, 0, 1, 0],
        'col3': [1, 1, 0, 0]}
df = pd.DataFrame(data)

# 在Streamlit应用中创建一个下拉菜单，用于选择一个名字
selected_name = st.selectbox('选择一个名字:', df['name'])

# 在数据框中找到选择的名字对应的行
selected_row = df[df['name'] == selected_name]

# 显示相应行等于1的列
st.write(f"名字为 {selected_name} 的行中等于1的列:")
st.write(selected_row.loc[:, selected_row.eq(1).any()])