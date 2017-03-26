from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.views.decorators.clickjacking import xframe_options_exempt
import json
def dumpJsonp(request, data):
    if('sendback' in request.GET):
        data['sendback']=request.GET['sendback']
    if('callback' in request.GET):
        return '%s(%s)'%(request.GET["callback"], json.dumps(data))

@xframe_options_exempt
def quote_list(request):
    if('dashboard_request' in request.GET):
        return HttpResponse(dumpJsonp(request,{'load_current_page':'true','fullscreen_on_click':'false', 'is_interactive_tile':'true', 'get_parameter':'isdash'}), content_type='application/javascript');
    return render(request, 'random_quote/base.html')
