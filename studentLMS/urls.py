
from django.contrib import admin
from django.urls import path, include
from App import views

urlpatterns = [
    # path to admin page
    path('admin/', admin.site.urls),
    # path to  render home page
    path('', views.frontend, name="frontend"),
    # path login / logout
    path('login/', include('django.contrib.auth.urls')),

    #backend section
    path('backend/', views.backend, name="backend"),
    # Path to add student
    path('add_student', views.add_student, name="add_student"),
    #ㅔpath to delete patient
    path('delete_student/<str:student_id>', views.delete_student, name="delete_student"),
    # path to access the student individually    
    path('student/<str:student_id>', views.student, name="student"),
    # path to add the student    
    path('edit_student', views.edit_student, name="edit_student")


]
 