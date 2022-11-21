from django.shortcuts import render


def main(request):
    return render(request, 'base.html')


def qr_code(request):
    return render(request, 'qr_code.html')


def qr_code_1(request):
    return render(request, 'qr_code_2.html')


def qr_code_2(request):
    return render(request, 'qr_code_3.html')
