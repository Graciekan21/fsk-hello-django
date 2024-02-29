from django.shortcuts import render

# Create your views here.


def get_todo_list(request):
    items = Item.objects.all()
    context = {
        'items': Items
    }
    return render(request, 'todo/todo_list.html', context)
 