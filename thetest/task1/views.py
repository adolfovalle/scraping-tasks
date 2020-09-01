from django.shortcuts import render
from django.http import HttpResponse
from django.utils.timezone import make_aware
from task1.models import Post, Profile
import subprocess
import instaloader

def index(request):
    
    loader = instaloader.Instaloader(compress_json=False)
    lista_usernames= [}
    #lista_usernames= ["adasdas_studio","poco"]
    lista_profiles = []

    for username in lista_usernames:
        profile = instaloader.Profile.from_username(loader.context, username)            
        lista_profiles.append(profile)
        p = Profile(username = profile.username, user_id = profile.userid, n_followers = profile.followers, n_followees = profile.followees)
        p.save()

        for post in profile.get_posts():

            aware_datetime = make_aware(post.date_utc)

            t = Post(profile=p,mediaid=post.mediaid,date_utc=aware_datetime,caption=post.caption,video_view_count=post.video_view_count,likes=post.likes,comments=post.comments)
            t.save()

    loader.download_profiles(lista_profiles)

    return HttpResponse("Hecho")
