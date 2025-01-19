import gradio as gr
from gradio_client import Client




def greet(text: str,category="",language="ar",dialect="SA",gender="Male",model_type="wasmdashai/vits-ar-sa-huba-v2",speaking_rate=0.8,double_duration=1.0,streaming=True) -> str:
    client = Client("wasmdashai/RunTasking")
    result = client.predict(
    		text=text,
    		name_model=model_type,
    		speaking_rate=speaking_rate,
    		api_name="/predict"
    )
    return result




# demo = gr.Interface(fn=greet, inputs=["text",model_choices,gr.Slider(0.1, 1, step=0.1,value=0.8),gr.Slider(0.1, 5, step=0.1,value=1.0)], outputs=[gr.Audio(streaming=True, autoplay=True)], allow_flagging='never')

# Function for generating a response based on selected options
def generate_response(category, language, model_type, dialect, gender, temperature, speech_rate, streaming):
    response = f"""
    Response:
    - Category: {category}
    - Language: {language}
    - Model Type: {model_type}
    - Dialect: {dialect}
    - Gender: {gender}
    - Temperature: {temperature}
    - Speech Rate: {speech_rate}
    - Streaming: {"Enabled" if streaming else "Disabled"}
    """
    return response

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
        width: 220px;
        height: 220px;
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
        width: 8.25rem !important;
        height: 8.25rem !important;
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
    </style>
    <div class="icon-cont-center  ">
    <div id="logo-icon-static-id" class="icon-xxl text-center shadow-primary rounded-circle flex-shrink-0">
        <svg class="mud-icon-root mud-svg-icon mud-success-text mud-icon-size-large" style="direction:ltr !important;margin:8px !important" focusable="false" viewBox="0 0 24 24" aria-hidden="true" role="img">
            <title>API</title>
            <path d="M0 0h24v24H0z" fill="none"></path>
            <path d="M6 13c-.55 0-1 .45-1 1s.45 1 1 1 1-.45 1-1-.45-1-1-1zm0 4c-.55 0-1 .45-1 1s.45 1 1 1 1-.45 1-1-.45-1-1-1zm0-8c-.55 0-1 .45-1 1s.45 1 1 1 1-.45 1-1-.45-1-1-1zm-3 .5c-.28 0-.5.22-.5.5s.22.5.5.5.5-.22.5-.5-.22-.5-.5-.5zM6 5c-.55 0-1 .45-1 1s.45 1 1 1 1-.45 1-1-.45-1-1-1zm15 5.5c.28 0 .5-.22.5-.5s-.22-.5-.5-.5-.5.22-.5.5.22.5.5.5zM14 7c.55 0 1-.45 1-1s-.45-1-1-1-1 .45-1 1 .45 1 1 1zm0-3.5c.28 0 .5-.22.5-.5s-.22-.5-.5-.5-.5.22-.5.5.22.5.5.5zm-11 10c-.28 0-.5.22-.5.5s.22.5.5.5.5-.22.5-.5-.22-.5-.5-.5zm7 7c-.28 0-.5.22-.5.5s.22.5.5.5.5-.22.5-.5-.22-.5-.5-.5zm0-17c.28 0 .5-.22.5-.5s-.22-.5-.5-.5-.5.22-.5.5.22.5.5.5zM10 7c.55 0 1-.45 1-1s-.45-1-1-1-1 .45-1 1 .45 1 1 1zm0 5.5c-.83 0-1.5.67-1.5 1.5s.67 1.5 1.5 1.5 1.5-.67 1.5-1.5-.67-1.5-1.5-1.5zm8 .5c-.55 0-1 .45-1 1s.45 1 1 1 1-.45 1-1-.45-1-1-1zm0 4c-.55 0-1 .45-1 1s.45 1 1 1 1-.45 1-1-.45-1-1-1zm0-8c-.55 0-1 .45-1 1s.45 1 1 1 1-.45 1-1-.45-1-1-1zm0-4c-.55 0-1 .45-1 1s.45 1 1 1 1-.45 1-1-.45-1-1-1zm3 8.5c-.28 0-.5.22-.5.5s.22.5.5.5.5-.22.5-.5-.22-.5-.5-.5zM14 17c-.55 0-1 .45-1 1s.45 1 1 1 1-.45 1-1-.45-1-1-1zm0 3.5c-.28 0-.5.22-.5.5s.22.5.5.5.5-.22.5-.5-.22-.5-.5-.5zm-4-12c-.83 0-1.5.67-1.5 1.5s.67 1.5 1.5 1.5 1.5-.67 1.5-1.5-.67-1.5-1.5-1.5zm0 8.5c-.55 0-1 .45-1 1s.45 1 1 1 1-.45 1-1-.45-1-1-1zm4-4.5c-.83 0-1.5.67-1.5 1.5s.67 1.5 1.5 1.5 1.5-.67 1.5-1.5-.67-1.5-1.5-1.5zm0-4c-.83 0-1.5.67-1.5 1.5s.67 1.5 1.5 1.5 1.5-.67 1.5-1.5-.67-1.5-1.5-1.5z"></path>
        </svg>
    </div>
    </div>
"""

# Gradio Interface
with gr.Blocks() as demo:
    with gr.Row():
        with gr.Column(scale=1):
            gr.Markdown("### الخيارات")
            category_dropdown = gr.Dropdown(label="الفئة", choices=categories, value="Please Select")
            language_dropdown = gr.Dropdown(label="اللغة", choices=languages, value="Please Select")
          #  model_type_dropdown = gr.Dropdown(label="نوع النموذج", choices=model_types, value="Please Select")
            
            gender_dropdown = gr.Dropdown(label="الجنس", choices=genders, value="Please Select")
            
            gr.Markdown("### الإعدادات")
            temperature_slider = gr.Slider(label="Temperature", minimum=0.1, maximum=5, step=0.1, value=0.7)
            speech_rate_slider = gr.Slider(label="Speech Rate", minimum=0.1, maximum=1.0, step=0.1, value=0.8)
            streaming_toggle = gr.Checkbox(label="Streaming", value=True)
        
        with gr.Column(scale=3):
            gr.HTML(bodyicon)  # Display the icon
            out_audio = gr.Audio(label="Output",autoplay=True)
            with gr.Row():
                    dialect_dropdown = gr.Dropdown(label="نوع اللهجة", choices=dialects, value="Please Select")
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
            
            # input_textbox = gr.Textbox(
            #     label="Input text",
            #     placeholder="تحدث مع AI",
            #     lines=3,
            #     max_lines=3
            # )
            chat_input = gr.MultimodalTextbox(interactive=True,
                                          file_count="single",
                                          placeholder="Enter message or upload file...", show_label=False, lines=3,
                                           max_lines=3)
            
           # submit_button = gr.Button("Generate Response")

            # Connect button to function
            chat_input.submit(
                greet,
                inputs=[
                    chat_input,
                    category_dropdown,
                    language_dropdown,
                    dialect_dropdown,
                    gender_dropdown,
                    model_choices,
                   
                    speech_rate_slider,
                    temperature_slider,
                    streaming_toggle,
                ],
                outputs=out_audio,
            )

# Launch the application

