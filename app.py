import streamlit as st
from google import genai
from PIL import Image

# 頁面基本設定
st.set_page_config(page_title="AI 自動垃圾分類助手", page_icon="♻️")
st.title("♻️ AI 智慧垃圾分類助手")

# 你的 AQ... 開頭金鑰
API_KEY = "AQ.Ab8RN6KJLq9w0-0utLzChRuptMMGbreyCgYRTZfY-WPm9J-oHw"

if API_KEY:
    try:
        # 使用 Google 新版 genai Client（支援 AQ... 金鑰）
        client = genai.Client(api_key=API_KEY)
    except Exception as e:
        st.error(f"Client 初始化失敗：{e}")

    # 檔案上傳元件
    uploaded_file = st.file_uploader("上傳垃圾照片...", type=["jpg", "jpeg", "png"])

    if uploaded_file is not None:
        image = Image.open(uploaded_file)
        st.image(image, caption="上傳的照片", use_container_width=True)
        
        if st.button("🔍 開始 AI 分析"):
            with st.spinner("AI 分析中，請稍候..."):
                try:
                    prompt = "請辨識這張圖片中的主要物品，並告訴我：1.物品名稱 2.垃圾分類類別（如：資源回收-塑膠/紙類/金屬、一般垃圾、廚餘、有害垃圾） 3.處理建議（例如：需要先沖洗嗎？）。請用繁體中文回答。"
                    
                    # 呼叫最新穩定支援的模型
                    response = client.models.generate_content(
                        model='gemini-3.6-flash',
                        contents=[prompt, image]
                    )
                    st.success("分析完成！")
                    st.markdown(response.text)
                except Exception as e:
                    st.error(f"分析失敗：{e}")
else:
    st.warning("⚠️ 請先在程式碼中填入你的 API Key！")