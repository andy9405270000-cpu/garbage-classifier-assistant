import streamlit as st
import google.generativeai as genai
from PIL import Image

# 頁面基本設定
st.set_page_config(page_title="本地端AI垃圾分類系統", page_icon="♻️")
st.title("♻️ 本地端AI垃圾分類系統")

# 設定你的 API 金鑰
API_KEY = "AQ.Ab8RN6KJLq9w0-0utLzChRuptMMGbreyCgYRTZfY-WPm9J-oHw"

if API_KEY:
    try:
        # 設定 Google GenAI 金鑰
        genai.configure(api_key=API_KEY)
        # 建立模型實例
        model = genai.GenerativeModel('gemini-1.5-flash')
    except Exception as e:
        st.error(f"模型初始化失敗：{e}")

    # 檔案上傳元件
    uploaded_file = st.file_uploader("上傳垃圾照片...", type=["jpg", "jpeg", "png"])

    if uploaded_file is not None:
        image = Image.open(uploaded_file)
        st.image(image, caption="上傳的照片", use_container_width=True)
        
        if st.button("🔍 開始 AI 分析"):
            with st.spinner("AI 分析中，請稍候..."):
                try:
                    prompt = "請辨識這張圖片中的主要物品，並告訴我：1.物品名稱 2.垃圾分類類別（如：資源回收-塑膠/紙類/金屬、一般垃圾、廚餘、有害垃圾） 3.處理建議（例如：需要先沖洗嗎？）。請用繁體中文回答。"
                    
                    # 進行內容生成
                    response = model.generate_content([prompt, image])
                    
                    st.success("分析完成！")
                    st.markdown(response.text)
                except Exception as e:
                    st.error(f"分析失敗：{e}")
else:
    st.warning("⚠️ 請先在程式碼中填入你的 API Key！")