# django-material-icons

A quick way to add Material Icons with Django template tags.

## Installing

`django-material-icons` can be found on pypi. Run `pip install django-material-icons` to install the package on your machine.

## Getting Started

Using django-material-icons is easy. First, install the `django_material_icons` Django app in your settings file.

```
INSTALLED_APPS = [
    'django_material_icons'
]
```

Also, include the following tags in your base template file. It includes the CDN link to the material icons web font. If you have your own source for the web font, feel free to opt out of this tag!
```
{% load django_material_icons %}

{% include_material_icons %}
```

Then, add an icon with the following tag. Give the name icon's name as the first parameter, and that's all that's required.
```
{% load django_material_icons %}

{% material_icon 'face' %}
```

## Contributing

Please read [CONTRIBUTING.md](https://gist.github.com/PurpleBooth/b24679402957c63ec426) for details on our code of conduct, and the process for submitting pull requests to us.

## Authors

* **Doug Dresser** - *Creator* - [dwdresser](https://github.com/dwdresser)

See also the list of [contributors](https://github.com/your/project/contributors) who participated in this project.

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details

## Acknowledgments

* Thanks Material Icons!
