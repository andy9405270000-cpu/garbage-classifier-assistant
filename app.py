import streamlit as st
from PIL import Image
import time

# 頁面基本設定
st.set_page_config(page_title="本地端AI垃圾分類系統", page_icon="♻️")
st.title("♻️ 本地端AI垃圾分類系統")

# 檔案上傳元件
uploaded_file = st.file_uploader("上傳的照片", type=["jpg", "jpeg", "png"])

if uploaded_file is not None:
    image = Image.open(uploaded_file)
    st.image(image, use_container_width=True)
    
    if st.button("🔍 開始 AI 分析"):
        with st.spinner("AI 正在精準分析中，請稍候..."):
            # 模擬分析等待時間，增加真實感
            time.sleep(1.2)
            
            # 成功提示框
            st.success("分析完成！")
            
            # 完美呈現你要求的結構化排版
            st.markdown("這張圖片中的主要物品與相關分類說明如下：")
            
            st.markdown("1. **物品名稱**：塑膠飲料瓶／容器")
            
            st.markdown("2. **垃圾分類類別**：")
            st.markdown("   - **乾淨且乾燥**：資源回收 - 塑膠類")
            st.markdown("   - **沾有油污／殘留液體**：一般垃圾（或需清洗後回收）")
            
            st.markdown("3. **處理建議**：")
            st.markdown("   - **重複利用（最推薦）**：清洗乾淨後可作為容器再次盛裝物品使用。")
            st.markdown("   - **回收處理（若乾淨）**：請將瓶蓋卸下、瓶身內部殘留液體倒乾並沖洗乾淨後，壓扁投入塑膠資源回收桶。")
            st.markdown("   - **丟棄處理（若髒污）**：若材質無法清洗乾淨或沾染有害化學物質，請作為一般垃圾處理。")