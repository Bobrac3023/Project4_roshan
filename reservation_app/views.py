from django.shortcuts import render
from django.views import generic
from .models import Reservation
#from .forms import ReservationForm

# Create your views here.

class PostList(generic.ListView):
    model = Reservation
    queryset = Reservation.objects.all()
    template_name="reservation/index.html"
    #paginate_by = 6

def index(request, slug):
    # …
    if request.method == "POST":
        ReservationForm = ReservationForm(data=request.POST)
    if ReservationForm.is_valid():
        comment = ReservationForm.save(commit=False)
        comment.author = request.user
        comment.post = post
        comment.save()
    ReservationForm = ReservationForm()

    return render(
        request,
        "reservation_app/index.html",
        {
            "ReservationForm": ReservationForm,
        },
    )