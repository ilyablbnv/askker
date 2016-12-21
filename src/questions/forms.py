from django import forms
from django.forms import Textarea, SelectMultiple, TextInput
from questions.models import Question, Answer


class QuestionForm(forms.ModelForm):
    class Meta:
        model = Question
        fields = ('title', 'body', 'topics')
        labels = {
            'title': 'Title',
            'body': 'Add some more detail',
            'topics': 'You can choose one or more topics '
        }
        # Temporary solution. Css classes should not be at the backend logic.
        widgets = {
            'title': TextInput(attrs={'class': "form__input form__input--w100"}),
            'body': Textarea(attrs={'rows': 10, 'class': "form__input form__input--w100"}),
            'topics': SelectMultiple(attrs={'class': "form__input form__input--w100 form__input--multiple"})
        }


class AnswerForm(forms.ModelForm):
    class Meta:
        model = Answer
        fields = ["text"]
