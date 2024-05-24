from django.shortcuts import render

def homePage(request):

    return render(request, "index.html")

def calculator(request):
    result = 0
    try:
        if request.method=="POST":
            n1 =eval(request.POST.get('num1'))
            n2 =eval(request.POST.get('num2'))
            opr = request.POST.get('opr')
            if opr=="+":
                result = n1+n2
            elif opr=="-":
                result = n1-n2
            elif opr=="*":
                result = n1*n2
            elif opr=="/":
                result = n1/n2       
    except:
        result = "Invalid opr...."   
    return render(request, "calculator.html", {"output":result})

def evenOdd(request):
    answer = ""
    try:
        if request.method=="POST":
            num=int(request.POST.get('num1'))
            if num%2==0:
                answer = "Number is Even"
            else:
                answer= "Number is Odd"
    except:
        answer = "Invide please enter a Integer value..."  

    return render(request, "evenOdd.html", {"output":answer})


def markSheet(request):
    total = 0
    percentage = 0.0
    division = ""
    try:
        if request.method=="POST":
            sub1=int(request.POST.get('num1'))
            sub2=int(request.POST.get('num2'))
            sub3=int(request.POST.get('num3'))
            sub4=int(request.POST.get('num4'))
            sub5=int(request.POST.get('num5'))

            total = sub1+sub2+sub3+sub4+sub5
            percentage = total/5
            if percentage >=33 and percentage < 50:
                division = "Third Division"
            elif percentage >=50 and percentage <60:
                division = "Second Division"
            elif percentage >= 60:
                division = "First Division"       
    except:
        pass  

    return render(request, "marksheet.html", {"total":total, "percentage":percentage, "division":division})