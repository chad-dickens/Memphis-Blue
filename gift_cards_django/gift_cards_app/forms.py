from django import forms
from gift_cards_app.models import Orders

class OrderForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # Setting up html stuff
        my_dict = {'first_name': ('First Name', '30'),
                   'last_name': ('Last Name', '30'),
                   'phone': ('Phone', '12'),
                   'email': ('Email', None),
                   'company': ('Company', '200'),
                   'address': ('Address', '400')}

        for key in my_dict:
            self.fields[key].widget.attrs['placeholder'] = my_dict[key][0]
            self.fields[key].widget.attrs['class'] = 'form-control'
            if my_dict[key][1]:
                self.fields[key].widget.attrs['maxlength'] = my_dict[key][1]

        for name in ('val', 'qty'):
            for i in range(1, 9):
                key = name + '_' + str(i)
                self.fields[key].widget.attrs['class'] = 'form-control input-' + name
                self.fields[key].widget.attrs['step'] = '1'

                if name == 'val':
                    self.fields[key].widget.attrs['placeholder'] = '$AUD'
                    self.fields[key].widget.attrs['min'] = '50'
                    self.fields[key].widget.attrs['max'] = '500'
                else:
                    self.fields[key].widget.attrs['placeholder'] = 'Qty'
                    self.fields[key].widget.attrs['min'] = '1'

    class Meta:
        model = Orders
        fields = '__all__'
