from django.contrib.contenttypes.models import ContentType
from django.core.urlresolvers   import reverse

symbols = (u"абвгдеёжзийклмнопрстуфхцчшщъыьэюяАБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ",
           u"abvgdeejzijklmnoprstufhzcss_y_euaABVGDEEJZIJKLMNOPRSTUFHZCSS_Y_EUA")
tr = dict([(ord(a), ord(b)) for (a, b) in zip(*symbols)])

symbols_reverse = (u"abvgdeejzijklmnoprstufhzcss_y_euaABVGDEEJZIJKLMNOPRSTUFHZCSS_Y_EUA",
                   u"абвгдеёжзийклмнопрстуфхцчшщъыьэюяАБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ")
tr_reverse = dict([(ord(a), ord(b)) for (a, b) in zip(*symbols_reverse)])


def fix_code(code):
    return code.translate(tr).upper()

def fix_code_reverse(code):
    return code.translate(tr_reverse).upper()


def nvl(data, val=''):
    if data is None:
        return val
    return data


class AdminURLMixin(object):

    def get_admin_url(self):
        content_type = ContentType.objects.get_for_model(self.__class__)

        return reverse("admin:%s_%s_change" % (
            content_type.app_label,
            content_type.model),
                       args=(self.id,))