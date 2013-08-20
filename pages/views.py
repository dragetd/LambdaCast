from django.shortcuts import render_to_response, get_object_or_404, redirect
from django import forms
from django.template import RequestContext
from django.http import HttpResponseRedirect, HttpResponse
from pages.models import Page

import lambdaproject.settings as settings


def page(request,slug):
    pag_instance = Page()
    page_list = Page.objects.filter(activated=True)
    page = get_object_or_404(Page, slug=slug)
    return render_to_response('static_pages/page.html', {'page_list':page_list, 'page': page,'settings': settings}, context_instance=RequestContext(request))
