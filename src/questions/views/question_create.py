from django.core.urlresolvers import reverse
from django.db.models import Count
from django.utils import timezone
from django.views.generic import CreateView

from questions.forms import QuestionForm
from questions.models import Question, Topic
from questions.utils import slugify

__all__ = ["QuestionCreateView"]


class QuestionCreateView(CreateView):
    template_name = "questions/question_create.html"
    model = Question
    form_class = QuestionForm

    def form_valid(self, form):
        form.instance.author = self.request.user
        form.instance.created_at = timezone.now()
        form.instance.slug = slugify(form.instance.title[:50])
        return super(QuestionCreateView, self).form_valid(form)

    def form_invalid(self, form):
        return super(QuestionCreateView, self).form_invalid(form)

    def get_context_data(self, **kwargs):
        data = super(QuestionCreateView, self).get_context_data(**kwargs)
        data["topic_list"] = Topic.objects.all().annotate(question_count=Count("questions"))
        return data

    def get_success_url(self):
        return reverse(
            "question_detail",
            kwargs={
                "question_slug": self.object.slug
            }
        )
