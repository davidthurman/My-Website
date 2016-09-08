from django.db import models

# Create your models here.
class Topic(models.Model):
	"""A topic that I am writing about"""
	text = models.CharField(max_length = 200)
	date_added = models.DateTimeField(auto_now_add = True)

	def __str__(self):
		"""Return a string representation of the model."""
		return self.text
		
class Entry(models.Model):
	"""A post in a section of my blog"""
	topic = models.ForeignKey(Topic)
	title = models.TextField(default="Title")
	text = models.TextField()
	date_added = models.DateTimeField(auto_now_add = True)

	class Meta:
		verbose_name_plural = 'entries'

	def __str__(self):
		"""Return a string representation of the model. Make it limited to 50 characters"""
		if len(self.text) > 50:
			return self.text[:50] + "..."
		else:
			return self.text