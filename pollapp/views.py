from django.shortcuts import render,redirect,HttpResponse
from .models import Poll
from .forms import PollForm

def home(request):
    polls = Poll.objects.all()
    context = {'polls' : polls}
    return render(request,'poll/home.html',context)

def create(request):
    if request.method == 'POST':
        form = PollForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = PollForm()
    context = {
        'form':form
    }
    return render(request,'poll/create.html',context)

def base(request):
    context = {}
    return render(request,'poll/base.html',context)

def results(request,poll_id):
    poll = Poll.objects.get(pk=poll_id)
    context = {'poll' : poll}
    return render(request,'poll/results.html',context)

def vote(request, poll_id):
    poll = Poll.objects.get(pk=poll_id)

    if request.method == 'POST':

        selected_option = request.POST['poll']
        if selected_option == 'option1':
            poll.option_one_count += 1
        elif selected_option == 'option2':
            poll.option_two_count += 1
        elif selected_option == 'option3':
            poll.option_three_count += 1
        else:
            return HttpResponse(400, 'Invalid form')

        poll.save()

        return redirect('results', poll.id)

    context = {
        'poll' : poll
    }
    return render(request, 'poll/vote.html', context)