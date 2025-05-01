import streamlit as st
from few_shot import FewShotPosts
from post_generator import generate_post


length_options = ["Short", "Medium", "Long"]
language_options = ["English"]


st.set_page_config(page_title="LinkedIn Post Generator", layout="centered")

# Main app
def main():
    st.markdown(
        """
        <h1 style='text-align: center; color: #2C3E50;'>🚀 LinkedIn Post Generator</h1>
        <p style='text-align: center; color: gray;'>Craft high-quality LinkedIn posts in seconds!</p>
        <hr>
        """,
        unsafe_allow_html=True
    )

    fs = FewShotPosts()
    
    with st.container():
        st.subheader("🔧 Customize Your Post")
        col1, col2, col3 = st.columns([1, 1, 1])
        
        with col1:
            selected_tag = st.selectbox("🎯 Choose a Title", options=fs.get_tags())
        
        with col2:
            selected_length = st.selectbox("📏 Select Length", options=length_options)
        
        with col3:
            selected_language = st.selectbox("🗣️ Choose Language", options=language_options)

        st.markdown("<br>", unsafe_allow_html=True)
        generate_btn = st.button("✨ Generate Post", use_container_width=True)

    if generate_btn:
        with st.spinner("Creating your awesome post..."):
            post = generate_post(selected_length, selected_language, selected_tag)
        st.success("✅ Post Generated!")
        st.markdown("### 📝 Your LinkedIn Post")
        st.write(post)

if __name__ == "__main__":
    main()
