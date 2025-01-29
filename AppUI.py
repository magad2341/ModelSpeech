import gradio as gr
def cheack_token(token):
    return True

def  get_appsetting():
     data={
         "token":"""CfDJ8JLuH1pG0YlDsCUBLhkja-kmpJ3miKTglCi_X7wqGyt_H-ZPTudyN3wBbQDnAhb27CZ5JDJKh113wvoIkrZ6C6eoHLnsZzVDood2W71noI66sKuYG-o0W5Yw-9jo4Yk7dYlGSd914dxfez-miMizdqZ2coXy3N7UxX_lehhvUIRzBKFRli39mlOoJINwLKprVU_IC6tvKMlsxx5JSG_sqC7xrlesIw0420wDNVPczLA33Lgp38YgwLr4f62r10CTfb4x81cBwgmPZETjahdk2tCBTmFA59JbhqLH62PVJrsJmo7vbOOIMXZ4ATZqYgGq4jyV1LnaXHy820WwYUCURxMPrXuVgPopwTA47UIrQ_A6FWXFsrAV5UuIKekUEqIflMFyaksXmEF1rpIMru7DYPx8sD22LsUtlFBF33h1_sqiJ3tOq38o-9FCEthjNBqwlpukp0b_abiajyJ--ouc3g6BcQXYOytCzfpzwplR6SU0BZxQqXxwIx0rqG1kXuC5du0g6PsjmZ46ojmeAjJNtAyplwjuWbeoPxSdWHD_l88mBJsirh53AW6HWeE9-mY7Wwnck-T_zzYL7TnOitlaV034T3it-PU1DzrQT3LUILP06iLWC6DsYiGMYxI3LYq7sGJ1YeoiV7gxSkJiOLLgPBfJqFWdouxbUujjarD0bwbDRFipUT_ovX47SEypqL2mVoa62WkVepncPPdFy_z9E8w_uxA6wz9cwQd9So610IpHI2xJI6aQlDzMaQJovheNMLMhSRiLuGdT7Y-h919yRjn3QdjAugumhPTv42ybgjXJ3d4ufVXxlyi7QYAkkQ7PuGMmj8z0ELVBQ-Xodgg4tsXCpe6XZJYfHe_1P4DEkab-"""
          ,
         "urlapi":"http://lahjaapi.runasp.net/",
         "lg":"ar",
         "data":None

         }
     return data

def  get_appsetting_serile(data):

     return  data


class  APPException:
     def  catchwithAuth(self):

          return True

     def  catchwithAuthUI(self):
         gr.Markdown("#خطا في المصادقة")

     def catchStartUp(self):
          gr.Markdown("## هنا استدعاء  دالة  اعاده التوجية  او رسالة خطا او اي شي ")







def  create_app(tamplate,isDev=True,inputs=[],outputs=[],exception=APPException()):

     with gr.Blocks() as demo:
          state=gr.State(value=None)

          @gr.render()
          def main(request: gr.Request):

              if    isDev==False:
                  if request:
                     appsettingdata=dict(request.query_params)
              else:
                     appsettingdata=get_appsetting()
              try:
                   token=appsettingdata["token"]

                   if cheack_token(token):
                      urlapi=appsettingdata["urlapi"]
                      lg=appsettingdata["lg"]
                      data=appsettingdata["data"]
                      tamplate(urlapi,token,isDev).createapp(data,lg)

                   else:
                          exception.catchwithAuthUI()
              except:
                    exception.catchStartUp()
          demo.load(fn=main, inputs=inputs, outputs=outputs)
          return demo

