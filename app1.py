import streamlit as st
import google.generativeai as genai

# ✅ Set Gemini API key
genai.configure(api_key="your-api-key")

# 🖼️ Page Title
st.set_page_config(page_title="Gemini AI Blog Generator", page_icon="📝")
st.title("📝 Gemini AI Blog Generator")
st.markdown("Welcome to your AI-powered blogging assistant! 💡 Just give a topic, choose tone & word limit, and let Gemini write for you!")

# 🎯 User Inputs
topic = st.text_input("📌 Enter a blog topic")
tone = st.selectbox("🎭 Choose the tone", ["Formal", "Casual", "Creative", "Professional"])
word_limit = st.slider("✍️ Select word limit", 100, 1000, 400, step=100)

# ➕ Generate Button
if st.button("🚀 Generate Blog"):
    if topic:
        with st.spinner("Generating blog... Please wait..."):
            try:
                # ✅ Load Gemini model
                model = genai.GenerativeModel(model_name="models/gemini-2.5-pro")
                chat = model.start_chat()
                
                # 🔥 Prompt with tone and word limit
                prompt = (
                    f"Write a {tone.lower()} blog post of around {word_limit} words "
                    f"on the topic: '{topic}'. The content should be informative and engaging."
                )
                
                response = chat.send_message(prompt)
                
                # ✅ Display result
                st.success("✅ Blog Generated Successfully!")
                st.markdown("### 📖 Your Blog")
                st.text_area("Generated Blog", response.text, height=400)

                # 📥 Download Button
                st.download_button(
                    label="📩 Download Blog as .txt",
                    data=response.text,
                    file_name=f"{topic.replace(' ', '_')}_blog.txt",
                    mime="text/plain"
                )
            except Exception as e:
                st.error(f"❌ Error: {e}")
    else:
        st.warning("⚠️ Please enter a topic.")
