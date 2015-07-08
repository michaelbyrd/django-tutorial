from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.utils import timezone
from django.views import generic

from .models import Choice, Question


class IndexView(generic.ListView):
    context_object_name = 'latest_question_list'

    def get_queryset(self):
        """
        Return the last five published question (not including those set to be
        published in the future).
        """
        return Question.objects.filter(
            pub_date__lte=timezone.now()
        ).order_by('-pub_date')[:5]
        # old return Question.objects.order_by('-pub_date')[:5]


class DetailView(generic.DetailView):
    model = Question

    def get_queryset(self):
        """
        Exclude any questions that aren't published yet.
        """
        return Question.objects.filter(pub_date__lte=timezone.now())


class ResultsView(generic.DetailView):
    model = Question
    # this one requires a temple because we can't gave two DetailViews
    template_name = 'polls/results.html'


def vote(request, question_id):
    p = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = p.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        # Redeisplay the question voting form.
        return render(request, 'polls/detail.html', {
            'question': p,
            'error_message': "Please select a choice.",
        })
    else:
        selected_choice.votes += 1
        selected_choice.save()
        return HttpResponseRedirect(reverse('polls:results', args=(p.id,)))
