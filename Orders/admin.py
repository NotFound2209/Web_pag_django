from django.contrib import admin
from . import models


# Register your models here.


admin.site.register([models.Orders, models.Order_line])