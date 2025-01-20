from fastapi import FastAPI
import gradio as gr

# تعريف الصفحتين
def page1():
    return "مرحبًا بك في الصفحة الأولى! 😊"

def page2():
    return "مرحبًا بك في الصفحة الثانية! 🌟"

# إنشاء واجهتي Gradio
demo1 = gr.Interface(fn=page1, inputs=None, outputs="text", live=True)
demo2 = gr.Interface(fn=page2, inputs=None, outputs="text", live=True)

# إنشاء تطبيق FastAPI
app = FastAPI()

@app.get('/')
async def root():
    return {"message": "Gradio app is running. Visit /page1 or /page2 for the respective pages."}

# ربط الصفحتين بمسارات مختلفة
app = gr.mount_gradio_app(app, demo1, path='/page1')
app = gr.mount_gradio_app(app, demo2, path='/page2')

# تشغيل التطبيق (يمكنك تشغيله باستخدام: uvicorn app:app --reload)
