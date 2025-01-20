from fastapi import FastAPI
import gradio as gr

from gradio_ui import demo
import t2speech
import t2text
app = FastAPI()

@app.get('/')
async def root():
    return 'Gradio app is running at /gradio', 200

app = gr.mount_gradio_app(app, demo, path='/studio-t2speech')
app = gr.mount_gradio_app(app, t2speech.demo, path='/t2speech')

app = gr.mount_gradio_app(app, t2text.demo, path='/studio-t2text')

app = gr.mount_gradio_app(app, demo, path='/vbot')

app = gr.mount_gradio_app(app, demo, path='/chatbot')

