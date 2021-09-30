from django import forms
from .models import PredictCancer

class PredictCreateForm(forms.ModelForm):
    class Meta:
        model = PredictCancer
        fields = ('age', 'menopause', 'tumor_size', 'inv_nodes', 'node_caps', 'deg_malig', 'breast', 'breast_quad', 'irradiat')