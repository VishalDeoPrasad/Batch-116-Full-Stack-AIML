from django.shortcuts import render
import os
import joblib
from django.conf import settings
# Create your views here.

model_path = os.path.join(settings.BASE_DIR, 'model.pkl')
model = joblib.load(model_path)

def home(request):
    result = None
    if request.method == "POST":
        hours = float(request.POST['hours'])
        attendance = float(request.POST['attendance'])
        assignments = float(request.POST['assignments'])
        score = float(request.POST['score'])

        new_data = [[hours, attendance, assignments, score]]
        pred = model.predict(new_data)[0]
        if pred == 1:
            result = "Student Will Pass"
        else:
            result = "Student Will Fail"

    return render(request, 'home.html', {'result':result})
