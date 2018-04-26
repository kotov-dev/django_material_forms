from django.forms import widgets


class MaterialInput(widgets.Input):
    template_name = 'material_forms/widgets/input.html'
    input_class = 'form-control'

    def __init__(self, attrs=None, material_attrs=None):
        attrs['class'] = ' '.join(attrs.get('class', '').split(' ') + [self.input_class])
        super().__init__(attrs)
        if material_attrs is None:
            self.material_attrs = {}
        else:
            self.material_attrs = material_attrs

    def get_context(self, name, value, attrs):
        context = super().get_context(name, value, attrs)
        context['material_attrs'] = self.material_attrs
        return context


class MaterialSelect(widgets.Select):
    template_name = 'material_forms/widgets/select.html'
    input_class = 'form-control'

    def __init__(self, attrs=None, choices=(), material_attrs=None):
        attrs['class'] = ' '.join(attrs.get('class', '').split(' ') + [self.input_class])
        super().__init__(attrs, choices)
        if material_attrs is None:
            self.material_attrs = {}
        else:
            self.material_attrs = material_attrs

    def get_context(self, name, value, attrs):
        context = super().get_context(name, value, attrs)
        context['material_attrs'] = self.material_attrs
        return context


class MaterialTextarea(MaterialInput):
    template_name = 'material_forms/widgets/textarea.html'


class MaterialCheckboxInput(MaterialInput, widgets.CheckboxInput):
    input_type = 'checkbox'
    template_name = 'material_forms/widgets/checkbox.html'
    input_class = 'custom-control-input'


class MaterialTextInput(MaterialInput):
    input_type = 'text'


class MaterialNumberInput(MaterialInput):
    input_type = 'number'


class MaterialEmailInput(MaterialInput):
    input_type = 'email'


class MaterialURLInput(MaterialInput):
    input_type = 'url'


class MaterialPasswordInput(MaterialInput):
    input_type = 'password'

    def __init__(self, attrs=None, material_attrs=None, render_value=False):
        super().__init__(attrs, material_attrs)
        self.render_value = render_value

    def get_context(self, name, value, attrs):
        if not self.render_value:
            value = None
        return super().get_context(name, value, attrs)


class MaterialRadioSelect(widgets.RadioSelect):
    input_type = 'radio'
    template_name = 'material_forms/widgets/radio.html'
    material_attrs = None

    def __init__(self, attrs=None, choices=(), material_attrs=None):
        super().__init__(attrs, choices)
        if material_attrs is None:
            self.material_attrs = {}
        else:
            self.material_attrs = material_attrs

    def get_context(self, name, value, attrs):
        context = super().get_context(name, value, attrs)
        for group, options, index in context['widget']['optgroups']:
            for option in options:
                if 'class' not in option['attrs']:
                    option['attrs']['class'] = {}
                option['attrs']['class'] += ' custom-control-input'
        context['material_attrs'] = self.material_attrs
        return context
