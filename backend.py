import streamlit as st
import pandas as pd

 
st.write(pd.read_csv('graph data.csv'))

# 假设你有一个数据框 df，包含了名字（name）和相关的列
uploaded_file = st.file_uploader("upload your graph in the format like the table below (in csv)", type=["csv"])

if uploaded_file is not None:
    # 读取上传的文件
    data = pd.read_csv(uploaded_file)  
else:
    data = pd.read_csv('graph data.csv')
    st.write('upload is unsuccessful, default data is used')
 
df = pd.DataFrame(data)
st.write(df)
# 在Streamlit应用中创建一个下拉菜单，用于选择一个名字
selected_name = st.selectbox('Select a property:', df['properties'])

# 在数据框中找到选择的名字对应的行
selected_row = df[df['properties'] == selected_name]

# 显示相应行等于1的列
st.write(f"Property with the name {selected_name} is similar to these properties in rental price:")
#st.write(selected_row.loc[:, selected_row.eq(1).any()])
df2 = selected_row.loc[:, selected_row.eq(1).any()]
st.write(df2.columns)



 
