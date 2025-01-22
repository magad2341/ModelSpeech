import pandas as pd
from random import randint
import gradio as gr

# افتراض بيانات لتوضيح الفكرة
service_data = pd.DataFrame(
    {
        "time": pd.date_range("2021-01-01", end="2021-01-05", periods=200),
        "requests": [randint(5, 20) for i in range(200)],
        "errors": [randint(0, 3) for i in range(200)],
        "service_type": ["Text to Speech", "Text to Dialect", "Speech to Speech"] * 66 + ["Text to Speech"] * 2
    }
)

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
        
        with gr.Row():
            start = gr.DateTime("2021-01-01 00:00:00", label=labels["start_date"])
            end = gr.DateTime("2021-01-05 00:00:00", label=labels["end_date"])
            apply_btn = gr.Button(labels["apply_btn"], scale=0)

        with gr.Row():
            group_by = gr.Radio([labels["none"], labels["30m"], labels["1h"], labels["4h"], labels["1d"]], value=labels["none"], label=labels["group_by"])
            aggregate = gr.Radio(["sum", "mean", "median", "min", "max"], value="sum", label=labels["aggregation"])

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

        # مخططات الخدمة حسب الزمن
        requests_by_service_time = gr.LinePlot(
            service_data,
            x="time",
            y="requests",
            color="service_type",
            title=labels["requests_by_service_title"]
        )

        # خدمات الفلترة
        time_graphs = [requests_by_time, errors_by_time, requests_by_service_time]
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

        # إحصائيات عن الخدمات
        with gr.Column():
            gr.Markdown(f"### {labels['total_requests']}")
            gr.Textbox(f"Total Requests in Current Plan: {plan_data['current_plan_requests']}")
            gr.Textbox(f"Remaining Requests: {plan_data['remaining_requests']}")

        # مخطط للطلبات حسب نوع الخدمة
        requests_by_service = gr.BarPlot(
            service_data,
            x="service_type",
            y="requests",
            title=labels["requests_by_service"]
        )

        # إحصائيات حول الأخطاء حسب نوع الخدمة
        errors_by_service = gr.BarPlot(
            service_data,
            x="service_type",
            y="errors",
            title=labels["errors_by_service"]
        )

    return service_dashboard

# تشغيل الداشبورد مع اللغة العربية أو الإنجليزية
if __name__ == "__main__":
    language = "en"  # قم بتغيير اللغة هنا
    dashboard = create_dashboard(language)
