from django.shortcuts import render, redirect, HttpResponse
from datetime import datetime

def index(request):
    if not 'logs' in request.session:
        request.session['logs'] = []
    return render(request, 'session_words/index.html')

def add(request):
    if request.method == 'POST':
        log = {
            'word': '?' if not request.POST.get('word') else request.POST.get('word'),
            'color': request.POST.get('color'),
            'big': request.POST.get('big'),
            'datetime': datetime.now().strftime('%I:%M:%S%p %b %d %Y')
        }
        request.session['logs'].append(log)
        request.session.modified = True
        return redirect('/session_words')
 
def destroy(request):
  request.session.pop('logs')
  return redirect('/session_words')           
