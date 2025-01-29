
from clients import DashAPI

class  BuilderDashAPI:
    def __init__(self,url,token,isDev=False) -> None:
         self.api=DashAPI(url,token)
    def  get_data_byservices(self):
        if self.isDev==True:
            return plot_plan_data_services()

        data=self.api.get_plot_plan_data_services()
        labels=[]
        values=[]
        for i in data:
            labels.append(i["serviceType"])
            values.append(i["usageCount"])
        return values,labels



    def  get_data_byplan(self):
        labels=[]
        values=[]
        for i in data:
            labels.append(i["serviceType"])
            values.append(i["usageCount"])
        data=self.api.get_plot_plan_data()
        return data

    def  get_data_byplan_services(self):
        data=self.api.get_plot_plan_data_services()
        return data

    def  get_data_byerrors_by_time(self):
        data=self.api.get_errors_by_time()
        return data

    def  get_data_byrequests_by_time(self):
        data=self.api.get_requests_by_time()
        return data

    def  filter_service(self,service_type="ALL"):
        data=self.api.filter_service(service_type)
        return data

    def  get_by_token(self,token):
        data=self.api.get_by_token(token)
        return data

    def  get_by_subscription_id(self,subscription_id):
        data=self.api.get_by_subscription_id(subscription_id)
        return data

    def  get_spaces_by_ram_async(self,ram):
        data=self.api.get_spaces_by_ram_async(ram)
        return data
    def  ge_by_filter(self,start,end):
        return service_data


    def  get_data_by_time(self,start,end):
        data=self.api.get_data_by_time(start,end)
        return data
    def  get_stateerrors(self):
       return service_data

    def  get_staterequests(self):
        return service_data

    def  get_data_byplan_services(self):
        return service_data_tod
