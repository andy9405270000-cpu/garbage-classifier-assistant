import streamlit as st
from PIL import Image
import time

# 頁面基本設定
st.set_page_config(page_title="本地端AI垃圾分類系統", page_icon="♻️")
st.title("♻️ 本地端AI垃圾分類系統")

# 檔案上傳元件
uploaded_file = st.file_uploader("上傳垃圾照片...", type=["jpg", "jpeg", "png"])

if uploaded_file is not None:
    image = Image.open(uploaded_file)
    st.image(image, caption="上傳的照片", use_container_width=True)
    
    if st.button("🔍 開始 AI 分析"):
        with st.spinner("AI 分析中，請稍候..."):
            # 模擬分析等待時間
            time.sleep(1.5)
            
            # 呈現漂亮的分析結果
            st.success("分析完成！")
            st.markdown("### 📋 辨識結果報告")
            st.markdown("- **物品名稱**：塑膠飲料瓶")
            st.markdown("- **垃圾分類類別**：資源回收 - 塑膠類")
            st.markdown("- **處理建議**：請先將瓶內殘留液體倒乾、簡單沖洗後，壓扁並投入塑膠資源回收桶。")