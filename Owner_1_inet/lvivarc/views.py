from django.shortcuts import render, get_object_or_404
from .models import ArcType
from .models import ArcObj

def index(request):
    typelist = ArcType.objects.all()
    context = {"typelist": typelist}
    return render(request, 'index.html', context)


def arclist(request, type_id):
    type_obj = get_object_or_404(ArcType, id=type_id)
    obj_list = type_obj.arcobj_set.all()
    context = {
        'type': type_obj,
        'objects': obj_list,
    }
    return render(request, 'arclist.html', context)


def arcobj(request, obj_id):
    obj = get_object_or_404(ArcObj, id=obj_id)
    return render(request, "arcobj.html", {"obj": obj})
