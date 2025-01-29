from builders import BuilderDashAPI
from seeds import  BuilderDashAPISeed
from  components import  *
class  TamplateDashBuilder:
       __translation__={}


       def __init__(self,url,token,isDev=False) -> None:
         self.builder=BuilderDashAPI(url,token) if isDev==False else BuilderDashAPISeed()
         self.token=token





       def  get_data_byservices(self):
            values,labels=self.builder.get_data_byservices()
            return plotpie(values,labels)


       def  get_data_byplan(self):
            values,labels=self.builder.get_data_byservices()

            return plotpie(values,labels)

       def  get_data_byplan_services(self):
            return self.builder.get_data_byplan_services()

       def get_staterequests(self):
            return self.builder.get_staterequests()
       def get_stateerrors(self):
            return self.builder.get_stateerrors()

       def get_data_byplan_services(self):
            return self.builder.get_data_byplan_services()

       def  ge_by_filter(self,start,end):
            return self.builder.ge_by_filter(start,end)




       def  createapp(self,data=None,language="en"):
            labels = translations[language]
            gr.HTML(Style)
            with gr.Column() as service_dashboard:
                  # tokenauth=gr.State(value=self.token)

                  #-----1------#
                  create_section_state(self,labels)

                  #-----2------#

                  create_section_bytime(self,labels)

                  #-----3------#
                  create_section_by_all_services(self,labels)








            return service_dashboard
