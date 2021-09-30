from django.shortcuts import render
from . forms import PredictCreateForm
from .models import PredictCancer
import pickle
from django.views.generic.list import ListView
from django.contrib.auth.forms import UserCreationForm
from django.views.generic.edit import CreateView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin


# Create your views here.

class SignUp(CreateView):
  form_class = UserCreationForm
  success_url = reverse_lazy("login")
  template_name = "registration/signup.html"


def PredictCreate(request):
    form = PredictCreateForm()

    # collect input from client
    context = {'prediction': ""}
    if request.method == 'POST':
        age = request.POST.get('age')
        menopause = request.POST.get('menopause')
        tumor_size = request.POST.get('tumor_size')
        inv_nodes = request.POST.get('inv_nodes')
        node_caps = request.POST.get('node_caps')
        deg_malig = int(request.POST.get('deg_malig'))
        breast = request.POST.get('breast')
        breast_quad = request.POST.get('breast_quad')
        irradiat = request.POST.get('irradiat')

        #umpickle save labels from the LabelEncoder
        age_p = pickle.load(open('age_label.pkl', 'rb'))
        meno = pickle.load(open('menopause_label.pkl', 'rb'))
        tumor = pickle.load(open('tumor_size_label.pkl', 'rb'))
        nodes = pickle.load(open('inv_node_label.pkl', 'rb'))
        caps = pickle.load(open('node_caps_label.pkl', 'rb'))
        brst = pickle.load(open('breast_label.pkl', 'rb'))
        quadrant = pickle.load(open('breast_quad_label.pkl', 'rb'))
        radd = pickle.load(open('irradiat_label.pkl', 'rb'))

        #get value of selected variable
        age_val = age_p.transform([age])
        meno_val = meno.transform([menopause])
        tumor_val = tumor.transform([tumor_size])
        nodes_val = nodes.transform([inv_nodes])
        caps_val = caps.transform([node_caps])
        brst_val = brst.transform([breast])
        quadrant_val = quadrant.transform([breast_quad])
        radd_val = radd.transform([irradiat])

        #make predictions
        scaled= pickle.load(open('scaling.pkl', 'rb'))
        model = pickle.load(open('cancer_model.sav', 'rb'))

        classification = model.predict(scaled.transform([[age_val, meno_val, tumor_val, nodes_val, caps_val, deg_malig, brst_val, quadrant_val, radd_val]]))

        #saving prediction in database
        result = classification[0]
        if result == 0:
            context['prediction'] =  "No Recurrence Events"
        elif result == 1:
            context['prediction'] =  "Recurrence Events"
        else:
            return 'error'
        
        PredictCancer.objects.create(age=age, menopause=menopause, tumor_size=tumor_size, inv_nodes=inv_nodes,
                 node_caps=node_caps, deg_malig=deg_malig, breast=breast, breast_quad=breast_quad, irradiat=irradiat, classification=context['prediction'])
        
        return render(request, "result.html", context)

    return render(request, 'home.html', {'form':form})

class PredictionList(LoginRequiredMixin, ListView):
   model = PredictCancer
   template_name = 'dashboard.html'

