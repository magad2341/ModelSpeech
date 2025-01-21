import gradio as gr
from gradio_client import Client



from gradio import ChatMessage

import os
import time

sleep_time = 0.5
def ask_ai(message ):
    client = Client("wasmdashai/T2T")
    result = client.predict(
        text=message,
        key="AIzaSyC85_3TKmiXtOpwybhSFThZdF1nGKlxU5c",
        api_name="/predict"
    )
    return result
def generate_audio(text):
   client = Client("wasmdashai/RunTasking")
   result = client.predict(
    		text=text,
    		name_model="wasmdashai/vits-ar-sa-huba-v2",
    		speaking_rate=0.8,
    		api_name="/predict"
    )
   return result
   
import time

# Chatbot demo with multimodal input (text, markdown, LaTeX, code blocks, image, audio, & video). Plus shows support for streaming text.



def add_message(history, message):
    for x in message["files"]:
        history.append({"role": "user", "content": {"path": x}})
    if message["text"] is not None:
        history.append({"role": "user","content": message["text"]})
    return history, gr.MultimodalTextbox(value=None, interactive=False)


def bot(history: list):
   # if   history[-1]["type"]=="text":
    message=history[-1]["content"]
    response = ask_ai(message)
    history.append({"role": "assistant", "content": ""})
    for character in response:
        history[-1]["content"] += character
        time.sleep(0.05)
        yield history

def greet(text: str,key="",category="",language="ar",dialect="SA",max_token=0.8,Temperature=1.0,streaming=True) -> str:
    client = Client("wasmdashai/T2T")
    result = client.predict(
        text=text,
        key=key,
        api_name="/predict"
    )
    return gr.MultimodalTextbox(interactive=True,value=None),result

def print_like_dislike(x: gr.LikeData,history):
    
    return generate_audio(history[x.index]["content"])
    #print(x.index, x.value, x.liked




# Dropdown options
categories = ["Please Select", "Category 1", "Category 2", "Category 3"]
languages = ["Please Select", "Arabic", "English", "French"]
model_types = ["Please Select", "Type 1", "Type 2", "Type 3"]
dialects = ["Please Select", "Najdi", "Hijazi", "Gulf"]
genders = ["Please Select", "Male", "Female"]

# Body Icon HTML
bodyicon = """
    <style>
      :root {
    --name: default;

    --primary-500: rgba(11, 186, 131, 1);
    }
      .shadow-primary {
        box-shadow: 0 4px 8px rgba(0, 123, 255, 0.25);
      }
      .icon-xxl {
        width: 170px;
        height: 170px;
        line-height: 6.8rem;
        align-items: center;
      }
      .icon-md, .icon-lg, .icon-xl, .icon-xxl {
        display: flex;
        justify-content: center;
        align-items: center;
        border-radius: 50%;
        box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
        background-color: #ffffff;
      }
      .flex-shrink-0 {
        flex-shrink: 0 !important;
      }
      .rounded-circle {
        border-radius: 50% !important;
      }
      .text-center {
        text-align: center;
      }
      .mud-icon-root.mud-svg-icon {
        fill: rgba(11,186,131,1);
      }
      .mud-icon-size-large {
        font-size: 4.25rem !important;
        width: 7.25rem !important;
        height: 7.25rem !important;
      }
      .mud-success-text {
        color: rgba(11,186,131,1);
      }
      .icon-cont-center {
        display: flex;
        justify-content: center;
        align-items: center;
        width: 100%;

      }
      .built-with.svelte-sar7eh.svelte-sar7eh.svelte-sar7eh {
        display:none !important;
      }
     footer.svelte-sar7eh.svelte-sar7eh.svelte-sar7eh {
    position: fixed;
    right: 20px;
    top: 0;
}
       .gap.svelte-vt1mxs {
    gap: 8px !important;
}
    </style>

"""
users = [("admin", "password123"), ("user", "userpass")]

# Gradio Interface
with gr.Blocks() as demo:
    with gr.Row():
        with gr.Column(scale=1):
            gr.Markdown("### الخيارات")
            category_dropdown = gr.Dropdown(label="الفئة", choices=categories, value="Please Select")
            language_dropdown = gr.Dropdown(label="اللغة", choices=languages, value="Please Select")
          #  model_type_dropdown = gr.Dropdown(label="نوع النموذج", choices=model_types, value="Please Select")

            dialect_dropdown = gr.Dropdown(label="نوع اللهجة", choices=dialects, value="Please Select")
            gr.Markdown("### الإعدادات")
            temperature_slider = gr.Slider(label="Temperature", minimum=0.1, maximum=5, step=0.1, value=0.7)
            speech_rate_slider = gr.Slider(label="Max Token", minimum=50, maximum=120000, step=50, value=1024)
            streaming_toggle = gr.Checkbox(label="Streaming", value=True)

        with gr.Column(scale=3):
            gr.HTML(bodyicon)  # Display the icon
            out_audio = gr.Audio(label="Output",autoplay=True,visible=False)
    



            chatbot = gr.Chatbot(elem_id="chatbot", bubble_full_width=False, type="messages")

            chat_input = gr.MultimodalTextbox(
                interactive=True,
                file_count="multiple",
                placeholder="Enter message or upload file...",
                show_label=False,
                sources=["microphone", "upload"],
                lines=3,
                max_lines=3,
                

            )

            chat_msg = chat_input.submit(
                add_message, [chatbot, chat_input], [chatbot, chat_input]
            )
            bot_msg = chat_msg.then(bot, chatbot, chatbot, api_name="bot_response")
            bot_msg.then(lambda: gr.MultimodalTextbox(interactive=True), None, [chat_input])

          


            chatbot.like(print_like_dislike, chatbot, out_audio, like_user_message=True)
