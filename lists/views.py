from django.http import HttpResponse
from django.shortcuts import redirect,render
from lists.models import Item,List
# Create your views here.


def home_page(request):

    # return HttpResponse('<html><title>To-Do lists</title></html>')
    # if request.method == 'POST':
    #     return HttpResponse(request.POST['item_text'])
    # return render(request,'home.html')

        # if request.method == 'POST':
        #     new_item_text = request.POST['item_text']
        #     Item.objects.create(text=new_item_text)
        #     return redirect('/lists/the-only-list-in-the-world/')

        #create not requiring saving
    # else :
    #     new_item_text= ''
    #     items = Item.objects.all()
        return render(request, 'home.html')
                      # , {'items': items})

    #
    #     'new_item_text' : new_item_text
    # })\


def view_list(request, list_id):
    plist = List.objects.get(id=list_id)
    # items = Item.objects.filter(list=plist)
    # except ValueError :
    #     plist.delete()
    # error = "You can't have an empty list item"

    return render(request, 'list.html', {'list': plist})
    # except ValidationError :
    #     list.delete()
    #     error = "You can't have an empty list item"
    #     return render (request, 'home.html', {"error": error})


def new_list(request):
    plist = List.objects.create()
    Item.objects.create(text=request.POST['item_text'], list=plist)
    return redirect('/lists/%d/' % (plist.id,),follow=True)

def add_item(request,list_id):
    plist = List.objects.get(id=list_id)
    Item.objects.create(text=request.POST['item_text'], list=plist)
    return redirect('/lists/%d/' % (plist.id,), follow=True)