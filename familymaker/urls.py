from django.contrib import admin
from django.urls import path
from mainApp import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.home_page),
    path('blog-video/',views.blog_video),
    path('blog/',views.blog),
    path('bloglist/',views.bloglist),
    path('connectmembership/',views.connectmembership),
    path('contact/',views.contact),
    path('donate/',views.donate),
    path('familymakerawards/',views.familymakerawards),
    path('happyhome/',views.happyhome),
    path('leadershipskills/',views.leadershipskills),
    path('media/',views.media),
    path('nomination-form/',views.nomination_form),
    path('nomination/',views.nomination),
    path('ourachivements/',views.ourachivements),
    path('ourmission/',views.ourmission),
    path('ourvision/',views.ourvision),
    path('panelvideo/',views.panelvideo),
    path('post/',views.post),
    path('publicspeaking/',views.publicspeaking),
    path('relationshipworkshop/',views.relationshipworkshop),
    path('resources/',views.resources),
    path('riskmanagement/',views.riskmanagement),
    path('sponsership/',views.sponsership),
    
]+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
