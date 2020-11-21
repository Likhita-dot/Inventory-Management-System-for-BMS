from django.urls import path

from . import views

urlpatterns = [path("index.html", views.index, name="index"),
	       path('Login.html', views.Login, name="Login"), 
	       path('Admin.html', views.Admin, name="Admin"),
	       path('Register.html', views.Register, name="Register"),
	       path('Signup', views.Signup, name="Signup"),
	       path('UserLogin', views.UserLogin, name="UserLogin"),
	       path('AddProduct.html', views.AddProduct, name="AddProduct"),
	       path('AddProductData', views.AddProductData, name="AddProductData"),
	       path('ViewOrders.html', views.ViewOrders, name="ViewOrders"),
	       path('BookOrder.html', views.BookOrder, name="BookOrder"),
	       path('BookOrderAction', views.BookOrderAction, name="BookOrderAction"),
	       path('AdminLogin', views.AdminLogin, name="AdminLogin"),
	       path('UpdateInventory.html', views.UpdateInventory, name="UpdateInventory"),
	       path('UpdateInventoryAction', views.UpdateInventoryAction, name="UpdateInventoryAction"),
	       path('ViewInventory.html', views.ViewInventory, name="ViewInventory"),
	       path('ViewPurchase.html', views.ViewPurchase, name="ViewPurchase"),
	       path('CompleteOrder', views.CompleteOrder, name="CompleteOrder"),
	       path('CompleteOrderAction', views.CompleteOrderAction, name="CompleteOrderAction"),
]