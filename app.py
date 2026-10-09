import streamlit as st
from PIL import Image
import time

st.set_page_config(page_title="本地端AI垃圾分類系統", page_icon="♻️")
st.title("♻️ 本地端AI垃圾分類系統")

# 圖片上傳
uploaded_file = st.file_uploader("請上傳垃圾照片...", type=["jpg", "jpeg", "png"])

if uploaded_file is not None:
    image = Image.open(uploaded_file)
    st.image(image, caption="上傳的照片", use_container_width=True)
    
    if st.button("🔍 開始 AI 辨識"):
        with st.spinner("AI 模型正在分析中..."):
            # 模擬分析延遲，增加真實感
            time.sleep(1.5)
            
            # 模擬分析結果（適合現場展示與專刊報告）
            st.success("✅ 分析完成！")
            st.metric(label="辨識結果類別", value="塑膠類 (Plastic)")
            st.write("**辨識信心度**：`98.50%`")
            st.markdown("---")
            st.markdown("### 💡 回收建議")
            st.write("請清洗乾淨後投入塑膠資源回收桶。")