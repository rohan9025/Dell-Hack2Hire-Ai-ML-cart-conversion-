from django.shortcuts import render
from django.http import HttpResponse
from products.core.jsparser.parser import parser
from products.core.jsparser.parser import calcPercentage

# Create your views here.

posts=[
    {
        'model':'inspiron',
        'device':'laptop',
        'type':'college',
    },
    {
        'model':'legion',
        'device':'laptop',
        'type':'gaming',
    },
    {
        'model':'alienware',
        'device':'laptop',
        'type':'gaming',
    }

]
def index(request):
    
    return render(request,'products/index.html')
def about(request):
    context ={
        'title':"about"
    }
    return render(request,'products/about.html',context)

def xps(request):
    # This handles the AJAX POST from xps-webpage.html

    data = dict(request.POST)

    try:
        """
            This is for the first pass. For some reason, when the page loads
            it goes through this function. data['Screen[]'] isn't defined as
            data is empty.
        """
        screen = data['Screen[]']
    except:
        """
            If this is the first pass, then exit the function
        """
        return render(request,'products/xps-webpage.html')

    parsedData = {}

    parser_screen = parser(data['Screen[]'])
    parsedData['screen'] = parser_screen.parse()

    parser_price = parser(data['Price[]'])
    parsedData['price'] = parser_price.parse()

    parser_memory = parser(data['Memory[]'])
    parsedData['memory'] = parser_memory.parse()

    parser_cpu = parser(data['Cpu[]'])
    parsedData['cpu'] = parser_cpu.parse()

    parsedData['gpu'] = 0

    calcP_Obj = calcPercentage(parsedData)
    print (calcP_Obj.calculate_percentage())

    # TODO: send to calcP_Obj.calculate_percentage() to core...

    return render(request,'products/xps-webpage.html')

def latitude(request):
    # This handles the AJAX POST from latitude-webpage.html

    data = dict(request.POST)

    try:
        """
            This is for the first pass. For some reason, when the page loads
            it goes through this function. data['Screen[]'] isn't defined as
            data is empty.
        """
        screen = data['Screen[]']
    except:
        """
            If this is the first pass, then exit the function
        """
        return render(request,'products/latitude-webpage.html')

    parsedData = {}

    parser_screen = parser(data['Screen[]'])
    parsedData['screen'] = parser_screen.parse()

    parser_price = parser(data['Price[]'])
    parsedData['price'] = parser_price.parse()

    parser_memory = parser(data['Memory[]'])
    parsedData['memory'] = parser_memory.parse()

    parser_cpu = parser(data['Cpu[]'])
    parsedData['cpu'] = parser_cpu.parse()

    parsedData['gpu'] = 0

    calcP_Obj = calcPercentage(parsedData)
    print (calcP_Obj.calculate_percentage())

    # TODO: send to calcP_Obj.calculate_percentage() to core...

    return render(request,'products/latitude-webpage.html')


def inspiron(request):
    # This handles the AJAX POST from xps-webpage.html

    data = dict(request.POST)

    try:
        """
            This is for the first pass. For some reason, when the page loads
            it goes through this function. data['Screen[]'] isn't defined as
            data is empty.
        """
        screen = data['Screen[]']
    except:
        """
            If this is the first pass, then exit the function
        """
        return render(request,'products/inspiron-webpage.html')

    parsedData = {}

    parser_screen = parser(data['Screen[]'])
    parsedData['screen'] = parser_screen.parse()

    parser_price = parser(data['Price[]'])
    parsedData['price'] = parser_price.parse()

    parser_memory = parser(data['Memory[]'])
    parsedData['memory'] = parser_memory.parse()

    parser_cpu = parser(data['Cpu[]'])
    parsedData['cpu'] = parser_cpu.parse()

    parsed_GPU = parser(data['Gpu[]'])
    parsedData['gpu'] = parser_GPU.parse()

    calcP_Obj = calcPercentage(parsedData)
    print (calcP_Obj.calculate_percentage())

    # TODO: send to calcP_Obj.calculate_percentage() to core...

    return render(request,'products/inspiron-webpage.html')


def alienware(request):
    # This handles the AJAX POST from xps-webpage.html

    data = dict(request.POST)

    try:
        """
            This is for the first pass. For some reason, when the page loads
            it goes through this function. data['Screen[]'] isn't defined as
            data is empty.
        """
        screen = data['Screen[]']
    except:
        """
            If this is the first pass, then exit the function
        """
        return render(request,'products/alienware-webpage.html')

    parsedData = {}

    parser_screen = parser(data['Screen[]'])
    parsedData['screen'] = parser_screen.parse()

    parser_price = parser(data['Price[]'])
    parsedData['price'] = parser_price.parse()

    parser_memory = parser(data['Memory[]'])
    parsedData['memory'] = parser_memory.parse()

    parser_cpu = parser(data['Cpu[]'])
    parsedData['cpu'] = parser_cpu.parse()

    parsed_GPU = parser(data['Gpu[]'])
    parsedData['gpu'] = parser_GPU.parse()

    calcP_Obj = calcPercentage(parsedData)
    print (calcP_Obj.calculate_percentage())

    # TODO: send to calcP_Obj.calculate_percentage() to core...

    return render(request,'products/alienware-webpage.html')

def xps13_series(request):
    return render(request,'products/xps13-series.html')

def xps15_series(request):
    return render(request,'products/xps15-series.html')

def inspiron15_series(request):
    return render(request,'products/inspiron15-series.html')

def inspiron17_series(request):
    return render(request,'products/inspiron17-series.html')

def latitude_series(request):
    return render(request,'products/latitude-series.html')

def alienware15_series(request):
    return render(request,'products/alienware15-series.html')

def alienware17_series(request):
    return render(request,'products/alienware17-series.html')






