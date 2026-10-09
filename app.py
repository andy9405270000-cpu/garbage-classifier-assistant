import streamlit as st
from PIL import Image
from google import genai

st.set_page_config(page_title="Gemini 智慧垃圾分類助手", page_icon="♻️")
st.title("♻️ Gemini 智慧垃圾分類系統")

# 從 Streamlit 秘密金鑰讀取 Gemini API Key
if "GEMINI_API_KEY" in st.secrets:
    api_key = st.secrets["GEMINI_API_KEY"]
else:
    api_key = st.text_input("請輸入您的 Gemini API Key", type="password")

uploaded_file = st.file_uploader("請上傳垃圾照片...", type=["jpg", "jpeg", "png"])

if uploaded_file is not None and api_key:
    image = Image.open(uploaded_file)
    st.image(image, caption="上傳的照片", use_container_width=True)
    
    if st.button("🔍 請 Gemini 開始判定"):
        with st.spinner("Gemini 正在分析垃圾種類..."):
            try:
                # 初始化 Client
                client = genai.Client(api_key=api_key)
                
                # 呼叫 Gemini 模型進行影像辨識
                response = client.models.generate_content(
                    model="gemini-2.5-flash",
                    contents=[
                        image,
                        "請判斷這張照片中的垃圾屬於哪一類（例如：紙類、塑膠類、金屬類、玻璃類、廚餘或其他），並給出簡短的回收建議。"
                    ]
                )
                
                st.success("✅ 分析完成！")
                st.write(response.text)
                
            except Exception as e:
                st.error(f"發生錯誤：{e}")