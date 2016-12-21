from django.db.models import Count
from django.views.generic import DetailView

from questions.models import Topic, Question


__all__ = ["TopicDetailView"]


class TopicDetailView(DetailView):
    template_name = "questions/topic_detail.html"
    model = Topic
    context_object_name = "topic"
    slug_url_kwarg = "topic_slug"

    def get_context_data(self, **kwargs):
        data = super(TopicDetailView, self).get_context_data(**kwargs)
        data['questions'] = self.object.questions.all()
        data['topic_list'] = Topic.objects.all().annotate(question_count=Count("questions"))
        return data
