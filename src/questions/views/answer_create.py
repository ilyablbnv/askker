from django.core.urlresolvers import reverse
from django.db.models import Count
from django.utils import timezone
from django.views.generic import CreateView

from questions.forms import AnswerForm
from questions.models import Answer, Question, Topic

__all__ = ["AnswerCreateView"]


class AnswerCreateView(CreateView):
    template_name = "questions/answer_create.html"
    model = Answer
    form_class = AnswerForm

    def _get_question(self):
        return Question.objects.get(slug=self.kwargs.get("question_slug"))

    # Returns context data for displaying the list of objects.
    def get_context_data(self, **kwargs):
        data = super(AnswerCreateView, self).get_context_data(**kwargs)
        question_slug = self.kwargs.get("question_slug")
        data['question'] = Question.objects.get(slug=question_slug)
        data["topic_list"] = Topic.objects.all().annotate(question_count=Count("questions"))
        return data

    # Redirects to get_success_url()
    def form_valid(self, form):
        question = Question.objects.get(slug=self.kwargs.get("question_slug"))
        form.instance.question = question
        form.instance.author = self.request.user
        form.instance.created_at = timezone.now()
        return super(AnswerCreateView, self).form_valid(form)

    # Renders a response, providing the invalid form as context.
    def form_invalid(self, form):
        return super(AnswerCreateView, self).form_invalid(form)

    # Determine the URL to redirect to when the form is successfully validated.
    def get_success_url(self):
        return reverse(
            "question_detail",
            kwargs={
                "question_slug": self.object.question.slug
            }
        )
