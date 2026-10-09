import streamlit as st
from google import genai
from PIL import Image

# 頁面基本設定
st.set_page_config(page_title="本地端AI垃圾分類系統", page_icon="♻️")
st.title("♻️ 本地端AI垃圾分類系統")

# 使用你截圖中的 API 金鑰
API_KEY = "AQ.Ab8RN6L87EoHGo6tjsOVFrVjgh_-kMPigallLC6TF5WglCusgGA"

try:
    # 使用新版 google-genai 專屬的 Client 初始化方式
    client = genai.Client(api_key=API_KEY)
except Exception as e:
    st.error(f"Client 初始化失敗：{e}")

# 檔案上傳元件
uploaded_file = st.file_uploader("上傳的照片", type=["jpg", "jpeg", "png"])

if uploaded_file is not None:
    image = Image.open(uploaded_file)
    st.image(image, use_container_width=True)
    
    if st.button("🔍 開始 AI 分析"):
        with st.spinner("AI 正在精準分析中，請稍候..."):
            try:
                # 設定符合你排版期望的提示詞
                prompt = """請仔細辨識這張圖片中的主要物品，並嚴格依照以下結構與排版回覆繁體中文內容：

這張圖片中的主要物品與相關分類說明如下：

1. 物品名稱：[填入具體物品名稱與特徵]

2. 垃圾分類類別：
   - [列出對應的分類說明]

3. 處理建議：
   - [條列式說明具體的處理與回收建議]"""

                # 呼叫最新穩定支援的模型進行真實視覺辨識
                response = client.models.generate_content(
                    model='gemini-2.5-flash',
                    contents=[prompt, image]
                )
                
                st.success("分析完成！")
                st.markdown(response.text)
                
            except Exception as e:
                st.error(f"分析失敗：{e}")