from email.policy import default
from django.dispatch import receiver
from django.shortcuts import render
from .models import  Chat
from users.models import Friend, User
from django.db.models import Q
from django.http import HttpResponse, JsonResponse
from django.contrib.auth.decorators import login_required


# Create your views here.
@login_required
def chat(request, username):
      receiver = User.objects.get(username=username)
      user = request.user
      friends = set(Friend.objects.filter(user=user))
      friend = User.objects.filter(username__in=friends)
     
      #Send massage
      if request.method == "POST":
            massage = request.POST['massage']
            chat = Chat(chat=massage, sender=user, receiver=receiver)
            chat.save()
            try: Friend.objects.get(user=user, friend=receiver)
            except Friend.DoesNotExist:
                  Friend.objects.create(user=user, friend=receiver)
                  Friend.objects.create(user=receiver, friend=user)

      #List of Friends
      for f in friend:
           unread = Chat.objects.filter(sender= f, receiver=user, is_seen="&#10003;").count() 
           fr = Friend.objects.filter(user=user, friend=f)
           fr.update(unread=unread)
           
            
      return render(request, 'chat.html', { 'receiver':receiver, 'friends':friends})

@login_required
def data(request, username):
      receiver = User.objects.get(username=username)
      sender = user = request.user
      massages = Chat.objects.filter(
            Q(receiver=receiver, sender=sender) | Q(receiver=sender, sender=receiver)
      ).order_by("id")
      Chat.objects.filter(sender=receiver, is_seen="&#10003;").update(is_seen="&#10003; &#10003;")
      #Equilize unred to 0 when user see the massages
     
      fr = Friend.objects.filter(user=user, friend=receiver)
      fr.update(unread=0)
      return JsonResponse({"massages" : list(massages.values())})

@login_required      
def friends(request):
      user = request.user
      friends = set(Friend.objects.filter(user=user))
      friend = User.objects.filter(username__in=friends)
      for f in friend:
           unread = Chat.objects.filter(sender= f, receiver=user, is_seen="&#10003;").count() 
           fr = Friend.objects.filter(user=user, friend=f)
           fr.update(unread=unread)
      return render(request, 'home.html',{'friends':friends} )
    
