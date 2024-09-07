from django.shortcuts import render
from django.http import HttpRequest, HttpResponse


def index(request: HttpRequest, msg: str) -> HttpResponse:
    return(HttpResponse(f"<h1>You said:</h1><h2>{msg}</h2><h2>!!!</h2>"))