from django import forms
try:
    import json
except ImportError:
    from django.utils import simplejson as json
from jsonate.utils import jsonate

class JsonateWidget(forms.Textarea):
    
    def render(self, name, value, attrs=None):
        if not isinstance(value, basestring):
            value = jsonate(value, indent=2)
        return super(JsonateWidget, self).render(name, value, attrs)