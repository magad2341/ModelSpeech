import gradio as gr
from gradio_client import Client
Style = """
    <style>
      :root {
    --name: default;

    --primary-500: rgba(11, 186, 131, 1);
    }
    """
# دالة استنساخ المساحة
def duplicate_space(space_id, name, description, ram, cpu_cores, disk_space, is_gpu, is_global, bandwidth):
    try:
        client = Client(space_id)
        response = client.duplicate(
            duplicate_name=name,
            private=not is_global,  # إذا كانت عالمية، فهي ليست خاصة
            hardware="t4-small" if is_gpu else "cpu-basic",  # اختيار العتاد حسب وجود GPU
            sdk_version="latest"
        )
        return response
    except Exception as e:
        return f"Error duplicating space: {str(e)}"

# دالة لإنشاء المساحة مع البيانات الجديدة
def add_space(id, name, description, ram, cpu_cores, disk_space, is_gpu, is_global, bandwidth):
    if not id.strip() or not name.strip():
        return "Error: ID and Name are required."

    result = duplicate_space(id, name, description, ram, cpu_cores, disk_space, is_gpu, is_global, bandwidth)
    return str(result)

# بناء واجهة Gradio
with gr.Blocks(theme="soft") as app:
    gr.HTML(Style)
    gr.Markdown("# Add New LAJHA Space")
    gr.Markdown("Fill in the details below to create a new space.")

    with gr.Row():
        id_input = gr.Textbox(label="ID", placeholder="Enter Space ID")
        name_input = gr.Textbox(label="Name", placeholder="Enter Space Name")

    description_input = gr.Textbox(label="Description", placeholder="Enter a short description", lines=2)

    with gr.Row():
        ram_input = gr.Slider(minimum=1, maximum=64, step=1, label="RAM (GB)", value=8)
        cpu_cores_input = gr.Slider(minimum=1, maximum=32, step=1, label="CPU Cores", value=4)

    with gr.Row():
        disk_space_input = gr.Slider(minimum=5, maximum=500, step=5, label="Disk Space (GB)", value=50)
        bandwidth_input = gr.Slider(minimum=10, maximum=1000, step=10, label="Bandwidth (Mbps)", value=100)

    with gr.Row():
        is_gpu_input = gr.Checkbox(label="Enable GPU", value=False)
        is_global_input = gr.Checkbox(label="Global Access", value=True)

    submit_button = gr.Button("Create Space")
    output = gr.Textbox(label="Result")

    submit_button.click(
        fn=add_space,
        inputs=[id_input, name_input, description_input, ram_input, cpu_cores_input, disk_space_input, is_gpu_input, is_global_input, bandwidth_input],
        outputs=output
    )

