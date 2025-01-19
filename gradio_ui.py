import gradio as gr
from gradio_client import Client


def greet(text: str) -> str:
    client = Client("wasmdashai/RunTasking")
    result = client.predict(
    		text=text,
    		name_model="wasmdashai/vits-ar-sa-huba-v2",
    		speaking_rate=0.8,
    		api_name="/predict"
    )
    return result


demo = gr.Interface(
    fn=greet,
    inputs=gr.components.Textbox(label='Input'),
    outputs=["audio"],
    allow_flagging='never'
)
