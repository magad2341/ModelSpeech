import pandas as pd
from random import randint
import gradio as gr
import plotly.express as px
# افتراض بيانات لتوضيح الفكرة
service_data = pd.DataFrame(
    {
        "time": pd.date_range("2021-01-01", end="2021-01-05", periods=200),
        "requests": [randint(5, 20) for i in range(200)],
        "errors": [randint(0, 3) for i in range(200)],
        "service_type": ["Text to Speech", "Text to Dialect", "Speech to Speech"] * 66 + ["Text to Speech"] * 2,

    }
)
service_data_tod = pd.DataFrame(
    {
        
        "value": [100,50]*3,
        "TypeData": ["requests","errors"]*3,
        "service_type": ["Text to Speech", "Text to Dialect", "Speech to Speech"]*2 ,
        
    }
)

def change_filter(service_type,data,name_type="Type"):
            if service_type == "ALL":
                return data
            else:
                return data[data[name_type] == service_type]
def createPlotCard(data,labels,type_chart="bar"):
   return gr.BarPlot(data, x=labels["x"], y=labels["y"], color=labels["Type"])  if type_chart=="bar" else gr.LinePlot(data, x=labels["x"], y=labels["y"], color=labels["Type"])
   

def  BarServiceCard(data,labels=None,titel="Bar Service",type_chart="bar"):
        
        
        if labels is None:
            labels = {
                "label_dropdown":"Type",
                "Type": "Type",
                "x": "x",
                "y": "y"
            }
          
            
        with gr.Accordion(titel) as panel:
                  dropdownchart=gr.Radio(["bar","line"], value=type_chart, label="Chart Type")
                  dropdown=gr.Dropdown(choices=["ALL"]+list(data[labels["Type"]].unique()), label=labels["label_dropdown"])
                  dashplot=createPlotCard(data,labels,type_chart)
                  dropdown.change(fn=lambda service_type: change_filter(service_type,data,labels["Type"]), inputs=dropdown, outputs=dashplot)
                  dropdownchart.change(fn=lambda type_chart: createPlotCard(data,labels,type_chart), inputs=dropdownchart, outputs=dashplot)
        return panel
# بيانات حول الخطط
plan_data = {
    "current_plan_requests": 300,
    "remaining_requests": 150
}
bodyicon = """
    <style>
      :root {
    --name: default;

    --primary-500: rgba(11, 186, 131, 1);
    }
    """
# فهرس النصوص للغات (عربي وإنجليزي)
translations = {
    "ar": {
        "start_date": "تاريخ البدء",
        "end_date": "تاريخ الانتهاء",
        "apply_btn": "تطبيق الفلتر",
        "group_by": "تجميع البيانات بواسطة",
        "aggregation": "طريقة التجميع",
        "requests_by_time_title": "الطلبات حسب الوقت",
        "errors_by_time_title": "الأخطاء حسب الوقت",
        "requests_by_service_title": "الطلبات حسب نوع الخدمة",
        "total_requests": "إجمالي الطلبات في الخطة الحالية",
        "remaining_requests": "الطلبات المتبقية",
        "none": "لا شيء",
        "30m": "30 دقيقة",
        "1h": "ساعة",
        "4h": "4 ساعات",
        "1d": "يوم",
        "requests_by_service": "الطلبات حسب نوع الخدمة",
        "errors_by_service": "الأخطاء حسب نوع الخدمة"
    },
    "en": {
        "start_date": "Start Date",
        "end_date": "End Date",
        "apply_btn": "Apply Filter",
        "group_by": "Group Data By",
        "aggregation": "Select Aggregation Method",
        "requests_by_time_title": "Requests Over Time",
        "errors_by_time_title": "Errors Over Time",
        "requests_by_service_title": "Requests by Service Type Over Time",
        "total_requests": "Total Requests in Current Plan",
        "remaining_requests": "Remaining Requests",
        "none": "None",
        "30m": "30 minutes",
        "1h": "1 hour",
        "4h": "4 hours",
        "1d": "1 day",
        "requests_by_service": "Requests by Service Type",
        "errors_by_service": "Errors by Service Type"
    }
}
def plot_plan_data():
    labels = ["Used Requests", "Remaining Requests"]
    values = [plan_data["current_plan_requests"], plan_data["remaining_requests"]]
    
    # إنشاء المخطط باستخدام plotly
    fig = px.pie(
        names=labels,
        values=values,
        title="Plan Requests Distribution",
        hole=0.4,  # مخطط دائري مجوف
        color_discrete_sequence=["rgba(11, 186, 131, 1)", "#99CCFF"]
    )
    fig.update_layout(
        paper_bgcolor='rgba(0,0,0,0)',  # خلفية الورقة
        plot_bgcolor='rgba(0,0,0,0)',  # خلفية الرسم
        font_color='black'  # النص الأسود للوضع العادي (يتغير حسب الوضع الليلي)
    )
    return fig

def plot_plan_data_services():
    labels =  ["Text to Speech", "Text to Dialect", "Speech to Speech"]
    values = [100, 200 ,200 ]
    
    # إنشاء المخطط باستخدام plotly
    fig = px.pie(
        names=labels,
        values=values,
        title="Service Usage and Status",
        hole=0.4,  # مخطط دائري مجوف
        color_discrete_sequence=["rgba(11, 186, 131, 1)", "#99CCFF","#559CCF"]
    )
    fig.update_layout(
        paper_bgcolor='rgba(0,0,0,0)',  # خلفية الورقة
        plot_bgcolor='rgba(0,0,0,0)',  # خلفية الرسم
        font_color='black'  # النص الأسود للوضع العادي (يتغير حسب الوضع الليلي)
    )
    return fig
# بناء الواجهة
def create_dashboard(language):
    labels = translations[language]

    with gr.Blocks() as service_dashboard:
        lang = gr.State("")
        gr.HTML(bodyicon)

        # دالة لتغيير اللغة
        def change_language(lang):
            updated_labels = translations[lang]
            return [gr.update(value=updated_labels["start_date"]),
                    gr.update(value=updated_labels["end_date"]),
                    gr.update(value=updated_labels["apply_btn"]),
                    gr.update(value=updated_labels["group_by"]),
                    gr.update(value=updated_labels["aggregation"]),
                    gr.update(value=updated_labels["requests_by_time_title"]),
                    gr.update(value=updated_labels["errors_by_time_title"]),
                    gr.update(value=updated_labels["requests_by_service_title"]),
                    gr.update(value=updated_labels["total_requests"]),
                    gr.update(value=updated_labels["remaining_requests"])]

        # language_selector = gr.Radio(["en", "ar"], value=language, label="Select Language")
        # language_selector.change(change_language, language_selector, service_dashboard)
        with gr.Column():
                gr.Markdown("## Plan Requests Visualization")
                with gr.Row():
                      gr.Plot(plot_plan_data_services)
                      gr.Plot(plot_plan_data)
        with gr.Accordion(labels["apply_btn"]) as panel1:
            with gr.Row():
                start = gr.DateTime("2025-01-01 00:00:00", label=labels["start_date"])
                end = gr.DateTime("2025-01-05 00:00:00", label=labels["end_date"])
                apply_btn = gr.Button(labels["apply_btn"], scale=0)

            with gr.Row():
                group_by = gr.Radio([labels["none"], labels["30m"], labels["1h"], labels["4h"], labels["1d"]], value=labels["none"], label=labels["group_by"])
                aggregate = gr.Radio(["sum", "mean", "median", "min", "max"], value="sum", label=labels["aggregation"])
            with gr.Row():
                  # مخططات للطلبات
                  requests_by_time = gr.LinePlot(
                      service_data,
                      x="time",
                      y="requests",
                      title=labels["requests_by_time_title"]
                  )

                  # مخططات للأخطاء
                  errors_by_time = gr.LinePlot(
                      service_data,
                      x="time",
                      y="errors",
                      title=labels["errors_by_time_title"]
                  )

            labels_service = {
            "label_dropdown":"Type Service",
            "Type": "service_type",
            "x": "time",
            "y": "requests"
            }
            panel=BarServiceCard(service_data,labels_service,labels["requests_by_time_title"])
            time_graphs = [requests_by_time, errors_by_time]
            group_by.change(
                      lambda group: [gr.LinePlot(x_bin=None if group == labels["none"] else group)] * len(time_graphs),
                      group_by,
                      time_graphs
                  )
            aggregate.change(
                      lambda aggregate: [gr.LinePlot(y_aggregate=aggregate)] * len(time_graphs),
                      aggregate,
                      time_graphs
                  )

                # خدمة rescale
            def rescale(select: gr.SelectData):
                    return select.index
            rescale_evt = gr.on([plot.select for plot in time_graphs], rescale, None, [start, end])

            for trigger in [apply_btn.click, rescale_evt.then]:
                    trigger(
                        lambda start, end: [gr.LinePlot(x_lim=[start, end])] * len(time_graphs), [start, end], time_graphs
                    )


        # خدمات الفلترة
      
    
 

        with gr.Accordion(labels["requests_by_service"]) as panel2:
                  labels_servs = {
                      "label_dropdown":"Type Service",
                      "Type": "TypeData",
                      "x": "value",
                      "y": "service_type"
                  }
                
                  panel5=BarServiceCard(service_data_tod,labels_servs,type_chart="bar")

    return service_dashboard



language = "ar"  # قم بتغيير اللغة هنا
dashboard = create_dashboard(language)

