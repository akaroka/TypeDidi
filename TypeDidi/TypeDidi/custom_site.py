from django.contrib.admin import AdminSite


class CustomSite(AdminSite):
    site_header = 'TypeDidi'
    site_title = 'TypeDidi 管理后台> <'
    index_title = '首页'


custome_site = CustomSite(name='cus_admin')
