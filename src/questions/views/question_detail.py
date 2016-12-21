from django.db.models import Count
from django.views.generic import DetailView

from questions.forms import AnswerForm
from questions.models import Question, Topic, Answer

__all__ = ["QuestionDetailView"]


class QuestionDetailView(DetailView):
    model = Question
    # The name of the URLConf keyword argument that contains the slug.
    slug_url_kwarg = "question_slug"
    template_name = "questions/question_detail.html"
    context_object_name = "question"

    def get_context_data(self, **kwargs):
        data = super(QuestionDetailView, self).get_context_data(**kwargs)
        data["topic_list"] = Topic.objects.all().annotate(question_count=Count("questions"))
        data['form'] = AnswerForm(initial={"question": self.object})
        return data
