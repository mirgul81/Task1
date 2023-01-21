from django.shortcuts import render



def indexView(request):
    # news = News.objects.all()
    # students = Students.objects.all()
    # abouts = Abouts.objects.all
    # context = {
    #     'news': news,
    #     'students': students,
    #     'abouts': abouts
    # }
    return render(request, 'main/index.html')

def newsView(request, pk):
    # news = News.objects.all()
    # news = News.objects.get(id=pk)
    # students = Students.objects.all()
    # abouts = Abouts.objects.all()
    # context = {
    #     'info': news.info,
    #     'name': news.name,
    #     'news': news,
    #     'students': students,
    #     'abouts': abouts
    # }
    return render(request, 'main/news.html')


def studentView(request, pk):
    # student = Students.objects.get(id=pk)
    # students = Students.objects.all()
    # news = News.objects.all()
    # abouts = Abouts.objects.all()
    #
    # context={
    #     'name': student.name,
    #     'info': student.info,
    #     'students': students,
    #     'news': news,
    #     'abouts': abouts,
    # }
     return render(request, 'main/student.html')



def aboutView(request, pk):
    # about = Abouts.objects.get(id=pk)
    # abouts = Abouts.objects.all()
    # students = Students.objects.all()
    # news = News.objects.all()
    #
    # context={
    #     'name': about.name,
    #     'info': about.info,
    #     'abouts': abouts,
    #     'students': students,
    #     'news': news,
    # }
    return render(request, 'main/about.html')


# Create your views here.
