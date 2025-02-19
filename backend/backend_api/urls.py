from django.urls import path
from backend_api.app_routes import views

urlpatterns = [
    path('signup/', views.user_signup, name='signup'),
    path('login/', views.user_login, name='login'),
    path('logout/', views.user_logout, name='logout'),
    path('get_email/', views.get_email, name='get_email'),
    path('clear_transaction_history/', views.clear_transaction_history, name='clear_transaction_history'),
    path('delete_transactions/', views.delete_transactions, name='delete_transactions'),
    path('delete_account/', views.delete_account, name='delete_account'),
    path('make_transaction/', views.make_transaction, name='make_transaction'),
    path('reset_request/', views.reset_request, name='reset_request'),
    path('reset_password/', views.reset_password, name='reset_password'),
    path('update_username/', views.update_username, name='update_username'),
    path('update_email/', views.update_email, name='update_email'),
    path('get_transaction_history/', views.get_transaction_history, name='get_transaction_history'),
    path('flag_predictions/', views.flag_predictions, name='flag_predictions'),
    path('process_transaction_log/', views.process_transaction_log, name='process_transaction_log'),
    path('detect_anomalies/', views.detect_anomalies, name='detect_anomalies'),
    path('retrain_model/', views.retrain_model, name='retrain_model'),
    path('agg_by_cc_num/', views.agg_by_cc_num, name='agg_by_cc_num')
]
