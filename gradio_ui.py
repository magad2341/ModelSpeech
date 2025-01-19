import gradio as gr
from gradio_client import Client


def greet(text: str,name_model="wasmdashai/vits-ar-sa-huba-v2",speaking_rate=0.8,double_duration=1.0) -> str:
    client = Client("wasmdashai/RunTasking")
    result = client.predict(
    		text=text,
    		name_model=name_model,
    		speaking_rate=speaking_rate,
    		api_name="/predict"
    )
    return result

model_choices = gr.Dropdown(
                            choices=[

                                "wasmdashai/vits-ar-sa-huba-v1",
                                 "wasmdashai/vits-ar-sa-huba-v2",

                                 "wasmdashai/vits-ar-sa-A",
                                "wasmdashai/vits-ar-ye-sa",
                                "wasmdashai/vits-ar-sa-M-v1",
                                 "wasmdashai/vits-ar-sa-M-v2",
                                "wasmdashai/vits-en-v1"


                            ],
                            label="اختر النموذج",
                            value="wasmdashai/vits-ar-sa-huba-v2",
                        )


demo = gr.Interface(fn=greet, inputs=["text",model_choices,gr.Slider(0.1, 1, step=0.1,value=0.8),gr.Slider(0.1, 5, step=0.1,value=1.0)], outputs=[gr.Audio(streaming=True, autoplay=True)], allow_flagging='never')
