from django.db import models

class Chat(models.Model):
    user_id = models.CharField(max_length=100)
    chat_name = models.CharField(max_length=150)
    language = models.CharField(max_length=20)
    llm_version = models.CharField(max_length=50)
    short_description = models.CharField(max_length=200, blank=True)
    content = models.TextField()
    version = models.CharField(max_length=20)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    MSG_SEPARATOR = "\n---MSG---\n"

    def save(self, *args, **kwargs):
        if not self.short_description and self.content:
            self.short_description = self.content[:50]
        super().save(*args, **kwargs)

    def append_content(self, new_text):
        if self.content:
            self.content += self.MSG_SEPARATOR + new_text
        else:
            self.content = new_text
        self.save()

class Message(models.Model):
    chat = models.ForeignKey(Chat, on_delete=models.CASCADE, related_name="messages")
    user_id = models.CharField(max_length=100)
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)