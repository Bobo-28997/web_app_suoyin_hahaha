import streamlit as st

st.set_page_config(page_title="模拟审核系统索引", layout="wide")

st.title("🧭 模拟审核系统索引主页")

col1, col2, col3 = st.columns(3)

with col1:
    st.subheader("💰 重卡提成审核系统")
    st.write("这里是介绍。")
    st.markdown(
       "[👉 打开重卡提成审核系统](https://webapp1testname-y2ybwz5k7jappz2pbke7ezf.streamlit.app/)",
       unsafe_allow_html=True
    )

with col2:
    st.subheader("📊 轻卡提成审核系统")
    st.write("这里是介绍。")
    # 直接显示一个点击链接
    st.markdown(
       "[👉 打开轻卡提成审核系统](https://web-app-check-table-tablelighttruck-2n5s4k8censz7fjgy9wfzt.streamlit.app/)",
       unsafe_allow_html=True
    )

with col3:
    st.subheader("📈 二手车提成审核系统")
    st.write("这里是介绍。")
# 直接显示一个点击链接
    st.markdown(
       "[👉 打开二手车提成审核系统](https://web-app-check-table-doublehandcar-f8x3bmweeavwzughieqfif.streamlit.app/)",
       unsafe_allow_html=True
    )
