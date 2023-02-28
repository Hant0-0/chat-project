from chat_app.models import Rooms
from django.forms import ModelForm


class RoomForm(ModelForm):
    class Meta:
        model = Rooms
        fields = ['title', 'slug']