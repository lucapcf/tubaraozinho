from django.shortcuts import render, redirect, get_object_or_404
from .forms import InvestmentForm
from ideas.models import Idea
from .models import Investment
from django.contrib.auth.decorators import login_required

@login_required
def make_investment(request, idea_id):
    idea = get_object_or_404(Idea, id=idea_id)
    
    if request.method == 'POST':
        form = InvestmentForm(request.POST)
        if form.is_valid():
            investment = form.save(commit=False)
            investment.investor = request.user.userprofile
            investment.idea = idea
            investment.save()
            return redirect("investments:invested")
    else:
        form = InvestmentForm(initial={'idea': idea})
    
    return render(request, 'investments/make_investment.html', {'form': form, 'idea': idea})


@login_required
def invested(request):
    return render(request, 'investments/invested.html')


@login_required
def edit_investment(request, investment_id):
    investment = get_object_or_404(Investment, id=investment_id)
    idea = investment.idea

    # Update the status of the accepted investment
    investment.status = 'aprovado'
    investment.save()

    # Set all other investments in the same idea to 'rejeitado'
    Investment.objects.filter(idea=idea).exclude(id=investment_id).update(status='rejeitado')

    return redirect("ideas:idea", idea_id=idea.id)