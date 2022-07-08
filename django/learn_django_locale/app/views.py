from django.shortcuts import render
from django.utils.translation import gettext as _

def indexx(request):
    view_trans = _('これはビューの翻訳です。')
    context = {'view_trans': view_trans}
    return render(request, 'app/index.html', context)
