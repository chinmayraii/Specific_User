from django.db import models
from django.contrib.auth.models import User

class Chatbot(models.Model):
    user_id = models.CharField(max_length=100)
    user_input = models.TextField()
    bot_response = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'User: {self.user_input} | Bot: {self.bot_response}'




def add_chat(request):
    if 'user_id' not in request.session:
        # Generate a unique user ID and store it in the session
        request.session['user_id'] = str(uuid.uuid4())

    user_id = request.session['user_id']

    if request.method=='POST':
        if 'change_user' in request.POST:
            # Clear the current user's session
            request.session.flush()
            return render(request, 'chatbot.html') 