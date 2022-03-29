import django.dispatch


pre_create_historical_record = django.dispatch.Signal()
post_create_historical_record = django.dispatch.Signal()
