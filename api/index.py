"""
Vercel Serverless Function 入口 - 启动 Streamlit
"""
import os
import sys

# 添加项目根目录到路径
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

# 设置 Streamlit 环境变量
os.environ.setdefault('STREAMLIT_SERVER_HEADLESS', 'true')
os.environ.setdefault('STREAMLIT_SERVER_PORT', '8080')
os.environ.setdefault('STREAMLIT_SERVER_ADDRESS', '0.0.0.0')
os.environ.setdefault('STREAMLIT_SERVER_ENABLE_CORS', 'true')
os.environ.setdefault('STREAMLIT_BROWSER_GATHER_USAGE_STATS', 'false')

from streamlit.web import cli as stcli

# 启动 Streamlit
if __name__ == '__main__':
    app_path = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'web', 'app.py')
    sys.argv = ['streamlit', 'run', app_path, '--server.port=8080', '--server.address=0.0.0.0']
    stcli.main()
else:
    # Vercel 需要的 handler
    from fastapi import FastAPI
    from fastapi.middleware.wsgi import WSGIMiddleware
    from streamlit.web.server import Server
    
    app = FastAPI()
    
    # 简单响应，实际 Streamlit 部署更复杂
    @app.get("/")
    async def root():
        return {"message": "Pixelle-Video API is running"}
    
    handler = app
