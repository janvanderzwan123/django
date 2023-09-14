
from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def home(response):
	return render(response, "calculator.html", {})

from django.shortcuts import render

def calculate(request):
    if request.method == 'POST':
        expression = request.POST.get('expression', '')
        value = request.POST.get('value')
        operator = request.POST.get('operator')
        calculate = request.POST.get('calculate')

        if value:
            expression += value
        elif operator:
            expression += operator
        elif calculate:
            try:
                result = eval(expression)
                expression = str(result)
            except Exception as e:
                expression = f"Error: {str(e)}"

    return render(request, 'calculator.html', {'expression': expression})




