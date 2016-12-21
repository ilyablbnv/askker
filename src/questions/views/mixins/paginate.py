from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage


class QuestionPaginationMixin(object):
    _questions_per_page = 5

    def paginate_questions(self, queryset, page_number):
        paginator = Paginator(queryset, self._questions_per_page)

        try:
            page = paginator.page(page_number)
        except PageNotAnInteger:
            page = paginator.page(1)
        except EmptyPage:
            page = paginator.page(paginator.num_pages)

        return page, page.object_list