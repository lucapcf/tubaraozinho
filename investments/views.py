from django.shortcuts import render, redirect, get_object_or_404
from .forms import InvestmentForm
from ideas.models import Idea
from .models import Investment
from django.contrib.auth.decorators import login_required

from django.contrib import messages

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
            messages.success(request, 'Investimento realizado com sucesso!')
            return redirect("ideas:idea", idea_id=idea_id)
    else:
        form = InvestmentForm(initial={'idea': idea})
    
    return render(request, 'investments/make_investment.html', {'form': form, 'idea': idea})


@login_required
def invested(request):
    return render(request, 'investments/invested.html')


@login_required
def accept_investment(request, investment_id):
    investment = get_object_or_404(Investment, id=investment_id)
    idea = investment.idea

    investment.status = 'aprovado'
    investment.save()

    Investment.objects.filter(idea=idea).exclude(id=investment_id).update(status='rejeitado')

    any_accepted_investment = idea.investments.filter(status='aprovado').exists()

    return render(request, 'ideas/idea.html', {
        'idea': idea,
        'any_accepted_investment': any_accepted_investment,
    })