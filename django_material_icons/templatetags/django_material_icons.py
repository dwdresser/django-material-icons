from django.template import Library

MATERIAL_CLASS = 'material-icons'

register = Library()

@register.inclusion_tag('django_material_icons/icon.html')
def material_icon(icon_name, extra_classes=None):
    '''
    Template tag for rendering a material icon

    :param str icon_name: Name of material icon to render
    :param str extr_classes: String of classes to add to icon
    '''
    # add extra classes onto material class tag
    class_str = MATERIAL_CLASS
    if extra_classes:
        class_str += ' {}'.format(extra_classes)

    return {
        'classes': class_str,
        'icon_name': icon_name,
    }

@register.inclusion_tag('django_material_icons/include_material_icons.html')
def include_material_icons():
    '''
    Template tag for loading the stylesheet for the icon web font
    '''
    return {}
