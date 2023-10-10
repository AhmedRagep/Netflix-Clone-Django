from django.shortcuts import render,redirect
from django.views import View
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
# Create your views here.

class Home(View):
  def get(self, request, *args, **kwargs):
    # اذا كان اليوزر مسجل ادخل لصفحة البروفيل
    if request.user.is_authenticated:
      return redirect('profile_list')
    return render(request, 'index.html', {})
  


method_decorator(login_required, name="dispatch")
class ProfileList(View):
  def get(self, request, *args, **kwargs):
    profiles = request.user.profiles.all()
    return render(request, 'profilelist.html', {'profiles':profiles})