from django.shortcuts import render
from .models import *

def home_page(Request):
    return render(Request,'index.html')

def blog_video(Request):
    return render(Request,'blog-video.html')

def blog(Request):
    return render(Request,'blog.html')

def bloglist(Request):
    return render(Request,'bloglist.html')

def connectmembership(Request):
    return render(Request,'connectmembership.html')

def contact(Request):
    msg=''
    if(Request.method=="POST"):
        c=Contact()
        c.name=Request.POST.get('name')
        c.email=Request.POST.get('email')
        c.phone=Request.POST.get('phone')
        c.message=Request.POST.get('message')
        c.save()
        msg="Done"
    return render(Request,'contact.html',{'msg':msg})

def donate(Request):
    return render(Request,'donate.html')

def familymakerawards(Request):
    return render(Request,'familymakerawards.html')

def happyhome(Request):
    return render(Request,'happyhome.html')

def leadershipskills(Request):
    return render(Request,'leadershipskills.html')

def media(Request):
    return render(Request,'media.html')

def nomination_form(Request):
    msg=''
    if Request.method=="POST":
        n=Nomination_Form()
        n.name=Request.POST.get('name')
        n.email=Request.POST.get('email')
        n.age=Request.POST.get('age')
        n.mobile=Request.POST.get('mobile')
        n.location=Request.POST.get('location')
        n.nominate_name=Request.POST.get('nominate_name')
        n.q1=Request.POST.get('q1')
        n.q1_others=Request.POST.get('q1_others')
        n.q2=Request.POST.get('q2')
        n.q3=Request.POST.getlist('q3')
        n.q4=Request.POST.get('q4')
        n.q5=Request.POST.getlist('q5')
        n.q6=Request.POST.get('q6')
        n.q7=Request.POST.getlist('q7')
        n.q7_others=Request.POST.get('q7_others')
        n.q8=Request.POST.get('q8')
        n.q9=Request.POST.getlist('q2')
        n.q10=Request.POST.get('q2')
        n.q11=Request.POST.getlist('q11')
        n.q12=Request.POST.get('q12')
        n.q13=Request.POST.getlist('q13')
        n.q14=Request.POST.getlist('q14')
        n.q15=Request.POST.get('q15')
        n.q16=Request.POST.get('q16')
        n.q17=Request.POST.getlist('q17')
        n.q18=Request.POST.get('q18')
        n.q19=Request.POST.get('q19')
        n.q20=Request.POST.get('q20')
        n.q21=Request.POST.get('q21')
        n.q22=Request.POST.get('q22')
        n.q23=Request.POST.get('q23')
        n.picture=Request.FILES.get('picture')
        n.save()
        msg="Done"
        
        
    return render(Request,'nomination-form.html',{'msg':msg})

def nomination(Request):
    return render(Request,'nomination.html')

def ourachivements(Request):
    return render(Request,'ourachivements.html')

def ourmission(Request):
    return render(Request,'ourmission.html')

def ourvision(Request):
    return render(Request,'ourvision.html')

def panelvideo(Request):
    return render(Request,'panelvideo.html')

def post(Request):
    return render(Request,'post.html')

def publicspeaking(Request):
    return render(Request,'publicspeaking.html')

def relationshipworkshop(Request):
    return render(Request,'relationshipworkshop.html')

def resources(Request):
    return render(Request,'resources.html')

def riskmanagement(Request):
    return render(Request,'riskmanagement.html')

def sponsership(Request):
    return render(Request,'sponsership.html')
