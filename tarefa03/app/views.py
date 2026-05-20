from django.shortcuts import render

def index(request):
    return render(request,"app/index.html")


def usuario(request):
    dados_usuarios = [{'nome':'Ibrahim','matricula': '5687235678', 'idade':'17','cidade':'SPP'},
    {'nome':'Lucas Cruz','matricula':'82635735','idade':'18','cidade':'santa maria'},
    {'nome':'Lucas carlos','matricula':'75543573','idade':'18','cidade':'bom jesus'},
    {'nome':'Ísis','matricula':'4685354988','idade':'19','cidade':'Serra caiada'},
    {'nome':'paulo gabriel','matricula':'78483568','idade':'18','cidade':'SPP'}]

    context = {
        "usuarios": dados_usuarios,
    }
    return render(request, "app/usuarios.html", context)