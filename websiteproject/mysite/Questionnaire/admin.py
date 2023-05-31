from django.contrib import admin

from .models import Question, Answer

class Questionadmin(admin.ModelAdmin):
    fields = ["text"]

class AnswerAdmin(admin.ModelAdmin):
    fields = ["question","text","is_correct"]

admin.site.register(Question,Questionadmin)
admin.site.register(Answer,AnswerAdmin)
