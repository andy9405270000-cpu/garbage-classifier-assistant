import streamlit as st
from PIL import Image
from google import genai

st.set_page_config(page_title="本地端AI垃圾分類系統", page_icon="♻️")
st.title("♻️ 本地端AI垃圾分類系統")

# 直接初始化 Client
try:
    client = genai.Client()
except Exception as e:
    st.error(f"初始化失敗，請確認環境設定：{e}")

# 圖片上傳與辨識
uploaded_file = st.file_uploader("請上傳垃圾照片...", type=["jpg", "jpeg", "png"])

if uploaded_file is not None:
    image = Image.open(uploaded_file)
    st.image(image, caption="上傳的照片", use_container_width=True)
    
    if st.button("🔍 請 Gemini 開始判定"):
        with st.spinner("Gemini 正在分析垃圾種類..."):
            try:
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