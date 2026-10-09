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
        with st.spinner("AI 分析中，請稍候..."):
            # 模擬分析等待時間
            time.sleep(1.5)
            
            # 成功提示框
            st.success("分析完成！")
            
            # 依照你提供的照片格式完整呈現文字內容
            st.markdown("這張圖片中的主要物品與相關分類說明如下：")
            
            st.markdown("1. **物品名稱**：塑膠袋（粉白條紋背心袋／購物袋）")
            
            st.markdown("2. **垃圾分類類別**：")
            st.markdown("   - **乾淨且乾燥**：資源回收 - 塑膠袋類")
            st.markdown("   - **沾有油污／液體／血水**：一般垃圾")
            
            st.markdown("3. **處理建議**：")
            st.markdown("   - **重複利用（最推薦）**：建議留著作為二次購物袋或家中的垃圾袋使用，延長其壽命。")
            st.markdown("   - **回收處理（若乾淨）**：必須確保袋內無雜物、無油漬且保持乾燥，可將其鋪平或打結打包後，交給資源回收車。")
            st.markdown("   - **丟棄處理（若髒污）**：若塑膠袋曾裝過食物、沾有油污或無法徹底沖洗乾淨，請直接當作「一般垃圾」丟棄，以免污染其他回收物。")