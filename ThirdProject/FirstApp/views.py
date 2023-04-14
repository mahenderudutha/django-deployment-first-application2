from django.shortcuts import render
import datetime
def wishes3(request):
    date1=datetime.datetime.now()
    msg1='Hello User/Client...GOOD'
    hr=int(date1.strftime('%H'))
    imgs='image1.jpg'
    if hr<12:
        msg1+=' Morning!!'
        imgs = 'img1.jpg'
    elif hr<16:
        msg1+=' Afternoon!!'
        imgs = 'img2.jpg'
    elif hr<20:
        msg1+=' Evening!!'
        imgs = 'img3.jpg'
    else:
        msg1='Hello User/Client...Very Good Night!!'
        imgs = 'img4.jpg'
    dict1={'date1':date1,'msg1':msg1,'imgs':imgs}
    return render(request,'FirstApp/wishes3.html',context=dict1)

from django.shortcuts import render
import datetime

def imgsgall(request):
    date1 = datetime.datetime.now()
    msg1 = '***DJango-Image-Gallery***'
    dict1 = {'date1': date1, 'msg1': msg1}
    return render(request, 'First' 'App/imgsgallery.html', context=dict1)



from django.shortcuts import render
import datetime


def imgsgallery2(request):
    date1 = datetime.datetime.now()
    msg1 = '***DJango-Image-Gallery(Product)***'
    dict1 = {'date1': date1, 'msg1': msg1}
    return render(request, 'FirstApp/imgsgallery2.html', context=dict1)

from django.shortcuts import render
import datetime
def hyperlinks(request):
    date1 = datetime.datetime.now()
    msg1 = '***DJango-Hyperlinks***';
    dict1 = {'date1': date1, 'msg1': msg1}
    return render(request, 'FirstApp/hyperlinks.html', context=dict1);



