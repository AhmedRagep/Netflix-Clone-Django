from django.shortcuts import render,redirect
from django.views import View
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from .forms import ProfileForm
from .models import Profile,Movie, Video
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



# تزيين الدالة dispatch لتتطلب تسجيل الدخول قبل تنفيذ الطلب
method_decorator(login_required, name="dispatch")

# تعريف كلاس ProfileCreate الذي يورث من View
class ProfileCreate(View):

  # الدالة التي تنفذ عند طلب GET
  def get(self, request, *args, **kwargs):
    
    # إنشاء نموذج فارغ 
    form = ProfileForm()
    
    # عرض النموذج مع قالب profileCreate.html
    return render(request,'profileCreate.html' ,{'form':form})

  # الدالة التي تنفذ عند طلب POST
  def post(self, request, *args, **kwargs):

    # إنشاء نموذج وملؤه بالبيانات المرسلة
    form = ProfileForm(request.POST or None) 

    # التحقق من صحة بيانات النموذج
    if form.is_valid():
      
      # إنشاء ملف شخصي جديد ببيانات النموذج
      profile = Profile.objects.create(**form.cleaned_data)  

      # إضافة الملف الشخصي للمستخدم
      if profile:
        request.user.profiles.add(profile)
        
        # إعادة توجيه لعرض قائمة الملفات الشخصية
        return redirect('profile_list')

    # عرض النموذج مرة أخرى إذا كان غير صالح
    return render(request,'profileCreate.html' ,{'form':form})
  



# تزيين الدالة dispatch لتتطلب تسجيل الدخول قبل تنفيذ الطلب
method_decorator(login_required, name="dispatch")

# تعريف كلاس ProfileCreate الذي يورث من View
class MovieList(View):

  # الدالة التي تنفذ عند طلب GET
  def get(self, request,profile_id, *args, **kwargs):

    try:
      # هاتلي البروفايل اللي الايدي بتاعه هوا الايدي بتاع البروفايل الحالي
      profile = Profile.objects.get(uuid=profile_id)
      # فلتر الافلام علي حسب عمر البروفايل الحالي
      movies = Movie.objects.filter(age_limit=profile.age_limit)
      # لو البرفايل مش موجود 
      if profile not in request.user.profiles.all():
        # روح لصفحة البروفايل
        return redirect('profile-list')
      # اما لو موجود روح للافلام الخاصة بعمره
      return render(request,'movieList.html' ,{'movies':movies})
    # لو فيه مشكلة في الصفحة 
    except Profile.DoesNotExist:
      # روح لصفحة البروفايل
      return redirect('profile-list')
    




# تزيين الدالة dispatch لتتطلب تسجيل الدخول قبل تنفيذ الطلب
method_decorator(login_required, name="dispatch")

# تعريف كلاس ProfileCreate الذي يورث من View
class MovieDetail(View):

  # الدالة التي تنفذ عند طلب GET
  def get(self, request,movie_id, *args, **kwargs):

    try:
      
      # فلتر الافلام علي حسب ايدي البروفايل
      movie = Movie.objects.get(uuid=movie_id)
    
      # اما لو موجود روح للافلام الخاصة بعمره
      return render(request,'movieDetail.html' ,{'movie':movie})
    # لو فيه مشكلة في الصفحة 
    except Movie.DoesNotExist:
      # روح لصفحة البروفايل
      return redirect('profile-list')
    




# تزيين الدالة dispatch لتتطلب تسجيل الدخول قبل تنفيذ الطلب
method_decorator(login_required, name="dispatch")

# تعريف كلاس ProfileCreate الذي يورث من View
class PlayMovie(View):

  # الدالة التي تنفذ عند طلب GET
  def get(self, request,movie_id, *args, **kwargs):

    try:
      
      # فلتر الافلام علي حسب ايدي البروفايل
      movie = Movie.objects.get(uuid=movie_id)
      # هاتلي قيم الافلام 
      movie = movie.video.values()
    
      # اما لو موجود روح للافلام الخاصة بعمره
      return render(request,'showMovie.html' ,{'movie':list(movie)})
    # لو فيه مشكلة في الصفحة 
    except Movie.DoesNotExist:
      # روح لصفحة التفاصيل
      return redirect('movie-detail')