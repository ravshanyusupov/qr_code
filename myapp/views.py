from django.shortcuts import render


def main(request):
    return render(request, 'base.html')


def qr_code(request):
    return render(request, 'qr_code.html')