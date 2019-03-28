import datetime
import re

from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from django.core.files.storage import default_storage
from django.shortcuts import render, redirect

# Create your views here.

# from django.http import HttpResponse
from fixed_asset.models import AssetRawData


def index(request):
    return render(request, "index.html", locals())
    # return HttpResponse("Hello, world. You're at the polls index.")


def login_view(request):
    """
    system login view

    :param request: username, psw to validate from auth system
    :return: redirecting to home page / session landing page
    """
    if request.method == "POST":
        username = request.POST.get("username", None)
        psw = request.POST.get("psw", None)
        is_auth = authenticate(request, username=username, password=psw)
        if is_auth:
            login(request, is_auth)
            return redirect("/my-app/")
        else:
            error = f"Invalid {username} username."

    return render(request, "login.html", locals())


@login_required(login_url="/login/")
def home(request):
    return render(request, "home.html", locals())


def logout_view(request):
    logout(request)
    return render(request, "logout.html", locals())


def upload_file(request):
    if request.method == "POST":
        af = request.FILES.get("a_file")
        file_name = default_storage.save(af.name, af)
        file = default_storage.open(file_name, "r")

        list_file = []
        for i in file.readlines():
            dctionary_file = {}
            datez = re.findall(
                "\d{2}/\d{2}/\d{2}|\d{1}/\d{2}/\d{2} \d{1}:\d{2} am| \d{2}:\d{2} am|\d{1}:\d{2} pm|\d{2}:\d{2} pm", i)
            # datez = re.findall('(\d+/\d+/\d+),\s(\d{2}\:\d{2}\s(?:AM|PM|am|pm))')
            # read line if it has date in it
            if datez:

                # date_obj1 = datetime.datetime.strptime(" ".join(datez), '%d/%m/%y %I:%M %p ')
                # split the line
                match = i.split("-", 1)

                # read date from list
                try:

                    date_obj1 = datetime.datetime.strptime(match[0], '%d/%m/%y, %H:%M ')
                except:
                    date_obj1 = datetime.datetime.strptime(match[0], '%d/%m/%y, %I:%M %p ')

                if ':' not in match[1]:
                    matchsecual = []
                    matchsecual.append('none')
                    matchsecual.append(match[1])
                else:

                    # split list into two
                    matchsecual = match[1].split(":", 1)

                # add key and values to empty dictionary
                dctionary_file['c_on'] = date_obj1
                dctionary_file['mobile_no'] = matchsecual[0]
                dctionary_file['content'] = matchsecual[1].rstrip()

                list_file.append(AssetRawData(**dctionary_file))

        print(list_file)
        if len(list_file) > 0:
            AssetRawData.objects.bulk_create(list_file)
    return render(request, "upload.html", locals())
