
from unicodedata import name
from django.urls import path
from.views import register_card, register_customer, register_notifications,register_transaction, register_wallet,register_reward,register_receipt,register_loan,register_account,register_thirdparty,register_currency


urlpatterns=[path("register/",register_customer,name="registration")]
urlpatterns=[path("register/",register_wallet,name="wallet")]
urlpatterns=[path("register/",register_account,name="account")]
urlpatterns=[path("register/",register_card,name="card")]
urlpatterns=[path("register/",register_thirdparty,name="thirdparty")]
urlpatterns=[path("register/",register_notifications,name="notifications")]
urlpatterns=[path("register/",register_receipt,name="receipts")]
urlpatterns=[path("register/",register_loan,name="loan")]
urlpatterns=[path("register/",register_reward,name="reward")]
urlpatterns=[path("register/",register_transaction,name="transaction")]
urlpatterns=[path("register/",register_currency,name="currency")    ]
