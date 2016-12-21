from django.db.models import Count
from django.views.generic import ListView

from questions.models import Question, Topic

# List of public objects of that module
from questions.views.mixins.paginate import QuestionPaginationMixin

__all__ = ["IndexView"]


class QuestionListView(QuestionPaginationMixin, ListView):
    template_name = "questions/question_list.html"
    # Specify the context variable to use. Make it "friendly"
    context_object_name = "questions"

    _page = None

    def get_context_data(self, **kwargs):
        data = super(QuestionListView, self).get_context_data(**kwargs)
        data["topic_list"] = Topic.objects.all().annotate(question_count=Count("questions"))
        data["page"] = self._page
        return data

    def get_queryset(self):
        q = Question.objects.all().order_by('-created_at')
        q = q.annotate(answers_count=Count("answers"))

        page_number = self.request.GET.get("page")
        page, data = self.paginate_questions(q, page_number)
        self._page = page
        return data
