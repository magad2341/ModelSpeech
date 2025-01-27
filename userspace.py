import gradio as gr
from  gradio_client import Client
def duplicate_space(space_id, duplicate_name, private, hardware, sdk_version):
    try:
        # إنشاء العميل
        client = Client(space_id)

        # تنفيذ عملية الاستنساخ
        response = client.duplicate(
            duplicate_name=duplicate_name,
            private=private,
            hardware=hardware,
            sdk_version=sdk_version
        )
        return response
    except Exception as e:
        return f"Error duplicating space: {str(e)}"

def  get_TypePlan():
    return ["Free","Paid"]


def get_hardware():
    return ['cpu-basic', 'cpu-upgrade', 't4-small', 't4-medium', 'a10g-small', 'a10g-large', 'a100-large']

def get_sdk_version():
    return ["latest"]


def get_private():
    return [True,False]

def get_sizeRam():
   return {
    "minimum": 1,
    "maximum": 64,
    "step": 1,
    "label": "RAM Size (GB)",
    "value": 2
}

def get_sizeStorage():
   return {
    "minimum": 5,
    "maximum": 500,
    "step": 5,
    "label": "Storage Size (GB)",
    "value": 5
}

def add_space(token, space_name, plan_type, hardware_type, ram_size, storage_size, gpu_enabled):
     res=duplicate_space(token, space_name, get_private()[plan_type=="Paid"], hardware_type, get_sdk_version()[0])


     return str(res)


with gr.Blocks() as app:
    gr.Markdown("# Add New Hugging Face Space")
    gr.Markdown("Use this interface to add a new Space with customizable specifications.")

    with gr.Row():
        username = gr.Textbox(label="Username", placeholder="Enter your username")
        space_name = gr.Textbox(label="Space Name", placeholder="Enter a name for your Space")

    with gr.Row():
        choices=get_TypePlan()
        plan_type = gr.Radio(
            choices=choices,
            label="Plan Type",
            value=choices[0],
            interactive=True
        )

    with gr.Row():
        choices=get_hardware()
        hardware_type = gr.Dropdown(
            choices=choices,
            label="Hardware Type",
            value=choices[0]
        )
        ram_size = gr.Slider(
           **get_sizeRam()
        )
        storage_size = gr.Slider(
           **get_sizeStorage()
        )
        gpu_enabled = gr.Checkbox(label="Enable GPU", value=False)

    submit_button = gr.Button("Create Space")
    output = gr.Textbox(label="Result")

    submit_button.click(
        fn=add_space,
        inputs=[username, space_name, plan_type, hardware_type, ram_size, storage_size, gpu_enabled],
        outputs=output
    )
