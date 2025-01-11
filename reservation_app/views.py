from django.shortcuts import render,get_object_or_404, reverse
from django.http import HttpResponseRedirect
from django.views import generic
from django.contrib import messages
from .models import Reservation
from .forms import ReservationForm

# Create your views here.

class PostList(generic.ListView):
    model = Reservation
    queryset = Reservation.objects.all()
    template_name="reservation/index.html"
    #paginate_by = 6



def about_me(request):

    """
        Renders the index.html page
        """
    if request.method == "POST":
        reservation_form = ReservationForm(data=request.POST)
        if reservation_form.is_valid():
            reservation_form.save()
            messages.add_message(request, messages.SUCCESS, "Reservation request received. Please check your inbox for an confirmation email")
        
    about = Reservation.objects.all()
    #about = Reservation.objects.all().order_by('-updated_on').first()
    reservation_form = ReservationForm()

    return render(
        request,
        "reservation/index.html",
            {
            """
            adding reservation an reservation form variables to the context in the render helper function
            """
            "about": about,
            "reservation_form": reservation_form
            },
    )

#def comment_edit(request, slug, comment_id):
def comment_edit(request,name_id):
    """
    view to edit comments
    """
    if request.method == "POST":

        #queryset = Post.objects.filter(status=1)
        queryset = Reservation.objects.filter(status=1)
        #post = get_object_or_404(queryset, slug=slug)
        post = get_object_or_404(queryset,name=name)
        #comment = get_object_or_404(Comment, pk=comment_id)
        comment = get_object_or_404(Reservation, pk=name_id)
        #reservation_form = ReservationForm(data=request.Reservation, instance=comment)
        """
        ensure reservation_form variable is connected to the correct database record instance to be edited?
        """
        reservation_form = ReservationForm(data=request.Reservation, instance=Reservation)

        #if reservation_form.is_valid() and comment.author == request.user:
        if reservation_form.is_valid() and comment.name == request.user:
            comment = reservation_form.save(commit=False)
            comment.post = post
            comment.approved = False
            comment.save()
            #messages.add_message(request, messages.SUCCESS, 'Comment Updated!')
            messages.add_message(request, messages.SUCCESS, 'Reservation Updated!')
        else:
            messages.add_message(request, messages.ERROR, 'Error updating comment!')

    #return HttpResponseRedirect(reverse('post_detail', args=[slug]))
    return HttpResponseRedirect(reverse('index.html', args=[messages]))

