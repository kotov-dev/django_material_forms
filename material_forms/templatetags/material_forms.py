from django import template
from django.forms import widgets
from django.utils.html import conditional_escape
import material_forms.widgets as material_widgets


register = template.Library()
try:
    from django.utils.encoding import force_text
except ImportError:
    from django.utils.encoding import force_unicode as force_text


def text_value(value):
    """
    Force a value to text, render None as an empty string
    """
    if value is None:
        return ''
    return force_text(value)


@register.simple_tag
def material_field(field, **kwargs):
    field_errors = [conditional_escape(text_value(error)) for error in field.errors]
    kwargs['field_errors'] = field_errors
    kwargs['label'] = kwargs.get('label', field.label)
    kwargs['help_text'] = kwargs.get('help_text', field.help_text)

    if field_errors:
        field.field.widget.attrs['class'] = field.field.widget.attrs.get('class', '') + ' is-invalid'
    elif field.form.is_bound:
        field.field.widget.attrs['class'] = field.field.widget.attrs.get('class', '') + ' is-valid'

    if isinstance(field.field.widget, widgets.TextInput):
        field.field.widget = material_widgets.MaterialTextInput(attrs=field.field.widget.attrs, material_attrs=kwargs)
    elif isinstance(field.field.widget, widgets.NumberInput):
        field.field.widget = material_widgets.MaterialNumberInput(attrs=field.field.widget.attrs, material_attrs=kwargs)
    elif isinstance(field.field.widget, widgets.EmailInput):
        field.field.widget = material_widgets.MaterialEmailInput(attrs=field.field.widget.attrs, material_attrs=kwargs)
    elif isinstance(field.field.widget, widgets.URLInput):
        field.field.widget = material_widgets.MaterialURLInput(attrs=field.field.widget.attrs, material_attrs=kwargs)
    elif isinstance(field.field.widget, widgets.PasswordInput):
        field.field.widget = material_widgets.MaterialPasswordInput(attrs=field.field.widget.attrs, material_attrs=kwargs,
                                                                    render_value=field.field.widget.render_value)
    elif isinstance(field.field.widget, widgets.CheckboxInput):
        field.field.widget = material_widgets.MaterialCheckboxInput(attrs=field.field.widget.attrs, material_attrs=kwargs)
    elif isinstance(field.field.widget, widgets.Textarea):
        if field_errors or field.form.is_bound:
            field.field.widget.attrs['style'] = 'box-shadow:none;' + field.field.widget.attrs.get('class', '')
        field.field.widget = material_widgets.MaterialTextarea(attrs=field.field.widget.attrs, material_attrs=kwargs)

    elif isinstance(field.field.widget, widgets.Select):
        field.field.widget = material_widgets.MaterialSelect(attrs=field.field.widget.attrs, choices=field.field.widget.choices, material_attrs=kwargs)

    elif isinstance(field.field.widget, widgets.RadioSelect):
        field.field.widget = material_widgets.MaterialRadioSelect(attrs=field.field.widget.attrs, choices=field.field.widget.choices, material_attrs=kwargs)
    return field