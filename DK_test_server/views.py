from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from .forms import Player, DateForms
from .models import Player as Pl
from django.views.generic import TemplateView
from datetime import datetime
from .models import *


class HomePageView(TemplateView):
    template_name = 'home.html'


class TablePageView(TemplateView):
    template_name = 'table.html'


class TrainingRequestHandler():
    def __init__(self, request):
        self.username = request.user
        self.date = datetime.today().strftime('%Y-%m-%d')
        for key, val in request.POST.items():
            exec('self.' + key + '=val')
    def create_single_training(self):
        single_training = DateTraning.objects.create(id=self.username, date=self.date)
        Pull.objects.create(id=single_training.tranings_id, pull1=self.pull1, pull2=self.pull2)
        Push.objects.create(id=single_training.tranings_id, push1=self.push1, push2=self.push2)
        Sit.objects.create(id=single_training.tranings_id, sit1=self.sit1, sit2=self.sit2)
        Jumping.objects.create(id=single_training.tranings_id, jumping1=self.jumping1)
        Entrance.objects.create(id=single_training.tranings_id, entrance1=self.entrance1)
        Press.objects.create(id=single_training.tranings_id, press1=self.press1, press2=self.press2)
        Weight.objects.create(id=single_training.tranings_id, weight1=self.weight1)
        Weightcategory.objects.create(id=single_training.tranings_id, weightcategory1=self.weightcategory1)
        Bars.objects.create(id=single_training.tranings_id, bars1=self.bars1, bars2=self.bars2)
        Stadium.objects.create(id=single_training.tranings_id, stadium1=self.stadium1, stadium2=self.stadium2)


def index(request):

    return HttpResponse("gg.")
# Create your views here.


def DK_test(request, id):
    address = request.GET.get('address', 'qqqqqqqqqqqqqq')
    name = request.GET.get('name', 'Abobus')

    slovar = {'Abobus': 14,
              'Nikola': 15,
              "german": 16,
              }
    data = {
        'address': address,
        'name': name,
        'age': id,
    }

    return render(request, 'DK_new.html', context=data)


def test(request):
    return render(request, 'form_DK.html')


def DK_form(request):
    if request.method == 'POST':
        data = {
            'address': request.POST.get('address'),
            'name': request.POST.get('name'),
            'age': request.POST.get('age'),
        }
        player = Pl.objects.create(name=data['name'], age=data['age'], address=data['address'])
        return render(request, 'DK_new.html', context=data)

    else:
        player = Player()
        return render(request, "Form_DK.html", {"form": player})

def DK_list(request):
    count = Pl.objects.count()
    player = Pl.objects.filter(name='nikola')
    count = player.count()
    return render(request, "DK_list.html", {"people": player, "count": count})


def DK_user(request, name):
    user = Pl.objects.filter(name=name)

    return render(request, 'DK_new.html', {"user": user})


def DK_table(request):
    if request.method == 'POST':
        form = DateForms(request.POST)
        print(request.user.username)
        tranings = TrainingRequestHandler(request)
        tranings.create_single_training()
        if form.is_valid():
            return HttpResponseRedirect('/')
    else:
        form = DateForms()
    return render(request, 'table2.html', {"form": form})


def push():
    pass