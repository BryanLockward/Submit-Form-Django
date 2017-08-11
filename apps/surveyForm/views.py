from django.shortcuts import render, redirect

def index(request):
    return render(request, 'surveyForm/index.html')

def process(request):
    try:
        request.session['attempts']
    except KeyError:
        request.session['attempts'] = 0
    request.session['name'] = request.POST['name']
    request.session['location'] = request.POST['location']
    request.session['language'] = request.POST['language']
    request.session['comment'] = request.POST['comment']
    request.session['attempts'] += 1
    return redirect('/result')

def results(request):
    return render(request, 'surveyForm/results.html')
