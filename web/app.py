"""
Pixelle-Video Web UI - Simple version for Streamlit deployment
"""
import sys
from pathlib import Path

# Fix path - add project root and web directory
_script_dir = Path(__file__).resolve().parent
_project_root = _script_dir.parent
if str(_project_root) not in sys.path:
    sys.path.insert(0, str(_project_root))
if str(_script_dir) not in sys.path:
    sys.path.insert(0, str(_script_dir))

import streamlit as st

# Setup page config
st.set_page_config(
    page_title="Pixelle-Video - AI Video Generator",
    page_icon="🎬",
    layout="wide",
)

def main():
    st.title("🎬 Pixelle-Video AI 视频生成器")
    
    st.markdown("""
    ### 欢迎使用 AI 视频生成工具！
    
    ✅ **功能特点：**
    - 输入文本自动生成视频脚本
    - AI 自动生成画面和配音
    - 支持多种风格和比例
    
    🚀 **正在部署中，更多功能即将上线...**
    """)
    
    # Simple text input for testing
    prompt = st.text_area("请输入你想生成的视频内容：", height=150, placeholder="例如：做一个关于春天的15秒短视频...")
    
    if st.button("🎬 生成视频", type="primary"):
        if prompt:
            st.info("🚀 正在调用 AI 生成视频，请稍候...")
            st.success("✅ 功能开发中，敬请期待！")
        else:
            st.warning("请先输入视频内容")

if __name__ == "__main__":
    main()
