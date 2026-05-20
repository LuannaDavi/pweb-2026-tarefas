from django.shortcuts import render

def index(request):
    return render(request,"app/index.html")


def usuario(request):
    dados_usuarios = [{"nome":"Ibrahim","matricula": "5687235678", "idade":"17","Cidade":"SPP"},
    {"nome":"Lucas Cruz","matricula":"82635735","idade":"18","Cidade":"santa maria"},
    {"nome":"Lucas carlos","matricula":"75543573","idade":"18","Cidade":"bom jesus"},
    {"nome":"Ísis","matricula":"4685354988","idade":"19","Cidade":"Serra caiada"},
    {"nome":"paulo gabriel","matricula":"78483568","idade":"18","Cidade":"SPP"}]

    context = {
        "usuarios": dados_usuarios,
    }
    return render(request, "app/usuarios", context)