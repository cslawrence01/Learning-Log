from django import forms

from .models import Topic, Entry

class TopicForm(forms.ModelForm):
	class Meta:
		model = Topic # create the form based on the Topic model
		fields = ['text'] # only include the text field
		labels = {'text': ''} # do not include any labels on the text field

class EntryForm(forms.ModelForm):
	class Meta:
		model = Entry
		fields = ['text']
		labels = {'text': ''}
		widgets = {'text': forms.Textarea(attrs={'cols': 80})}
