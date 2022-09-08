
from unicodedata import name
from django.urls import path
from.views import register_card, register_customer, register_notifications,register_transaction, register_wallet,register_reward,register_receipt,register_loan,register_account,register_thirdparty,register_currency


urlpatterns=[
    path("registercustomer/",register_customer,name="Customer"),
    path("registerwallet/",register_wallet,name="wallet"),
    path("registeraccount/",register_account,name="account"),
    path("registercard/",register_card,name="card"),
    path("registerthirdparty/",register_thirdparty,name="thirdparty"),
    path("registernotify/",register_notifications,name="notifications"),
    path("registerreceipts/",register_receipt,name="receipts"),
    path("registerloan/",register_loan,name="loan"),
    path("registerreward/",register_reward,name="reward"),
    path("registertransact/",register_transaction,name="transaction"),
    path("registercurrency/",register_currency,name="currency")
]
