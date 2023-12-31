from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^register$', views.UserRegistrationView.as_view(), name="register"),
    url(r'^login$', views.UserLoginView.as_view(), name="login"),
    url(r'^profile$', views.UserProfileView.as_view(), name="profile"),
    url(r'^changepassword$', views.UserChangePasswordView.as_view(), name="changepassword"),
    url(r'^income$', views.IncomeCreate.as_view(), name="income"),
    url(r'^income/(?P<pk>\d+)$', views.IncomeDetailView.as_view(), name="income"),
    url(r'^expense$', views.ExpenseCreate.as_view(), name="expense"),
    url(r'^expense/(?P<pk>\d+)$', views.ExpenseDetailView.as_view(), name="expense"),
    url(r'^goal$', views.GoalsCreate.as_view(), name="goal"),
    url(r'^goal/(?P<pk>\d+)$', views.GoalsDetailView.as_view(), name="goal"),
    url(r'^source$', views.SourceIncomeView.as_view(), name="source"),
    url(r'^source/(?P<pk>\d+)$', views.SourceIncomeDetailView.as_view(), name="source"),
    url(r'^home$', views.HomeView.as_view(), name="home"),
    url(r'^exchange-rate/$', views.ExchangerateCreate.as_view(), name="exchangerate"),
    url(r'^exchange-rate/(?P<pk>\d+)$', views.ExchangerateCreate.as_view(), name="exchangerate"),
    url(r'^location$', views.LocationDetailView.as_view(), name="location"),
    url(r'^periodic$', views.PeriodicDetailView.as_view(), name="periodic"),
    url(r'^tag/$', views.TagView.as_view(), name="tag"),
    url(r'^tag/(?P<pk>\d+)$', views.TagView.as_view(), name="tag"),
    url(r'^debt$', views.DebtView.as_view(), name="debt"),
    url(r'^debt/(?P<pk>\d+)$', views.DebtDetailView.as_view(), name="debt"),
    url(r'^setting$', views.SettingView.as_view(), name="setting"),
    url(r'^setting/(?P<pk>\d+)$', views.SettingDetailView.as_view(), name="setting"),
    url(r'^transaction/$', views.TransactionView.as_view(), name="transaction"),
    url(r'^transaction/(?P<pk>\d+)$', views.TransactionView.as_view(), name="transaction"),
    url(r'^user/subscription$', views.UserSubscriptionView.as_view(), name="user_subscription"),
    url(r'^admin/subscription/$', views.AdminSubscriptionView.as_view(), name="admin_subscription"),
    url(r'^admin/subscription/(?P<pk>\d+)$', views.AdminSubscriptionView.as_view(), name="admin_subscription"),
    url(r'^report$', views.ReportView.as_view(), name="report"),
]
