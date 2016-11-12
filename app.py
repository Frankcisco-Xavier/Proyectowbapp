import web
import json

render = web.template.render('views/')

urls = (
    '/index','index',
    '/informacion','informacion',
    '/registros','registros'
)

class index:
    def GET (datos):
        return render.index()

class informacion:
    def GET (datos):
        return render.informacion()

class registros:
    def GET (datos):
        datos=[]
        with open("registro.json","r")as file:
            datos=json.load(file)
        return render.registros(datos)

if __name__ == '__main__':
    app=web.application(urls, globals())
    web.config.debug=True
    app.run()