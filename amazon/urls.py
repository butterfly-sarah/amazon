from django.urls import path
from amazon.views import home,about,contact,base,info,search,add,delete,edit
urlpatterns = [

    path("home",home,name="home"),
    path("about",about,name="about"),
    path("contact",contact,name="contact"),
    path("base",base,name="base"),
    path("home/<int:pro_info>",info,name="info"),
    path("search",search,name="search"),
    path("add",add,name="add"),
    path("delete/<int:pro_id>",delete,name="delete"),
    path("edit/<int:pro_id>",edit,name="edit")
]
