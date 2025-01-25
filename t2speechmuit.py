import gradio as gr
from gradio_client import Client
iconlink='<svg class="mud-icon-root mud-svg-icon mud-icon-size-medium" focusable="false" viewBox="0 0 24 24" aria-hidden="true" role="img"><!--!--><path d="M0 0h24v24H0z" fill="none"></path><path d="M3.9 12c0-1.71 1.39-3.1 3.1-3.1h4V7H7c-2.76 0-5 2.24-5 5s2.24 5 5 5h4v-1.9H7c-1.71 0-3.1-1.39-3.1-3.1zM8 13h8v-2H8v2zm9-6h-4v1.9h4c1.71 0 3.1 1.39 3.1 3.1s-1.39 3.1-3.1 3.1h-4V17h4c2.76 0 5-2.24 5-5s-2.24-5-5-5z"></path></svg>'
iconview='<svg class="mud-icon-root mud-svg-icon mud-icon-size-medium" focusable="false" viewBox="0 0 24 24" aria-hidden="true" role="img"><!--!--><path d="M0 0h24v24H0z" fill="none"></path><path d="M12 4.5C7 4.5 2.73 7.61 1 12c1.73 4.39 6 7.5 11 7.5s9.27-3.11 11-7.5c-1.73-4.39-6-7.5-11-7.5zM12 17c-2.76 0-5-2.24-5-5s2.24-5 5-5 5 2.24 5 5-2.24 5-5 5zm0-8c-1.66 0-3 1.34-3 3s1.34 3 3 3 3-1.34 3-3-1.34-3-3-3z"></path></svg>'
def herficon(href,icon="",classicon="",style="height:20px"):
  return f'<a href="{href}" style={style} class="mud-button-root mud-icon-button mud-success-text hover:mud-success-hover mud-ripple mud-ripple-icon" >{icon}</a>'
def generate_table():
    models_data = [
        {"name": "Model 1", "audio": "https://wasmdashai-runtasking.hf.space/file=/tmp/gradio/50f8c04962e405b10912113a3f374b76065d0a2adaf6c14bef6030d5a214cebc/audio.wav", "link": "https://example.com/model1"},
        {"name": "Model 2", "audio":"https://wasmdashai-runtasking.hf.space/file=/tmp/gradio/50f8c04962e405b10912113a3f374b76065d0a2adaf6c14bef6030d5a214cebc/audio.wav", "link": "https://example.com/model2"},
        {"name": "Model 3", "audio": "https://wasmdashai-runtasking.hf.space/file=/tmp/gradio/50f8c04962e405b10912113a3f374b76065d0a2adaf6c14bef6030d5a214cebc/audio.wav", "link": "https://example.com/model3"},
    ]

    # إنشاء صفوف الجدول
    table_content = []
    for model in models_data:
        row = [
            model["name"],
            f'<audio style="height:35px" src="{model["audio"]}" controls></audio>',
            f'<div class="mud-grid-item">{herficon("http://lahja.runasp.net/services",iconlink)+herficon("http://lahja.runasp.net/services",iconview)}</div>',
            
        ]
        table_content.append(row)

    return table_content
bodyicon = """
    <style>
      :root {
    --name: default;

    --primary-500: rgba(11, 186, 131, 1);
    }
    
    
    .mud-icon-root.mud-svg-icon {
        fill: rgba(11,186,131,1);
      }
      .mud-icon-size-medium{
        font-size: 4.25rem !important;
        width: 2.25rem !important;
        height: 2.25rem !important;
      }
     .mud-ripple {
    --mud-ripple-offset-x: 0;
    --mud-ripple-offset-y: 0;
    position: relative;
    overflow: hidden;
}
.mud-icon-button {
    flex: 0 0 auto;
    padding: 12px;
    overflow: visible;
    font-size: 1.5rem;
    text-align: center;
    transition: background-color 150ms cubic-bezier(0.4, 0, 0.2, 1) 0ms;
    border-radius: 50%;
    color: var(--mud-palette-action-default);
}
.mud-button-root {
    color: inherit;
    border: 0;
    cursor: pointer;
    margin: 0;
    display: inline-flex
;
    outline: 0;
    padding: 0;
    position: relative;
    align-items: center;
    user-select: none;
    border-radius: 0;
    vertical-align: middle;
    -moz-appearance: none;
    justify-content: center;
    text-decoration: none;
    background-color: rgba(0, 0, 0, 0);
    -webkit-appearance: none;
    -webkit-tap-highlight-color: rgba(0, 0, 0, 0);
}
button, [type=button], [type=reset], [type=submit] {
    -webkit-appearance: button;
}
.mud-success-text {
    color: rgba(0,200,83,1) !important;
    --mud-ripple-color:rgba(0,200,83,1) !important;
}


.mud-success-hover {
    background-color: rgba(0,200,83,0.058823529411764705) !important;
    --mud-ripple-color: rgba(0,200,83,0.058823529411764705) !important;
}

.gap.svelte-vt1mxs {
    gap: 8px !important;
}
    </style>
 
    </div>
"""

def greet(text: str,category="",language="ar",dialect="SA",max_token=0.8,Temperature=1.0,streaming=True) -> str:
    return gr.MultimodalTextbox(interactive=True,value=None)
def  cheack_token(token_auth=""):
    
     return True 
def load_model(request: gr.Request):
    
    if request:
       
       
       data=dict(request.query_params)
       if cheack_token(data["token"]):
              try:
                  return data["name_model"]
              except: pass

       return ""
    
categories = ["Please Select", "Category 1", "Category 2", "Category 3"]
languages = ["Please Select", "Arabic", "English", "French"]
model_types = ["Please Select", "Type 1", "Type 2", "Type 3"]
dialects = ["Please Select", "Najdi", "Hijazi", "Gulf"]
genders = ["Please Select", "Male", "Female"]
with gr.Blocks() as demo:
    gr.HTML(bodyicon)
   
    state=gr.State("")
    with gr.Row():
        with gr.Accordion("الخيارات"):
              with gr.Row():
                    category_dropdown = gr.Dropdown(label="الفئة", choices=categories, value="Please Select")
                    language_dropdown = gr.Dropdown(label="اللغة", choices=languages, value="Please Select")
                    model_type_dropdown = gr.Dropdown(label="نوع النموذج", choices=model_types, value="Please Select")
        
                    dialect_dropdown = gr.Dropdown(label="نوع اللهجة", choices=dialects, value="Please Select")
    with gr.Row():
             gr.Dataframe( headers=["Model", "Audio","View"],
                           value=generate_table(),
                                    interactive=False,
                                    datatype="markdown",
                                    # col_count=3,
                                    
                                    
                                   # wrap=False,
                                    row_count=4,

                                    label="##       Models Table",
                                     show_fullscreen_button=True,
                                    show_row_numbers=True,
                                    # column_widths=[30,80,20],
                                  #  show_label=False


                                         )
    
             with gr.Column():
                  with gr.Row():
                        temperature_slider = gr.Slider(label="Temperature", minimum=0.1, maximum=5, step=0.1, value=0.7)
                        speech_rate_slider = gr.Slider(label="Max Token", minimum=50, maximum=120000, step=50, value=1024)
                        streaming_toggle = gr.Checkbox(label="Streaming", value=True)
                  chat_input=gr.MultimodalTextbox(interactive=True,
                                                          file_count="single",
                                                          placeholder="Enter message or upload file...", show_label=False,
                                                          lines=6,
                                                          max_lines=6)
                  chat_input.submit(
                               greet,
                              inputs=[
                                  chat_input,
          
                                  speech_rate_slider,
                                  temperature_slider,
                                  streaming_toggle,
                              ],
                              outputs=[chat_input],
            )
            

    demo.load(fn=load_model,inputs=None,outputs=[state])
