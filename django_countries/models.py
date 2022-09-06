from django.contrib.staticfiles.storage import staticfiles_storage
from django.db import models
from django_datatables.columns import DatatableColumn
from django_datatables.helpers import render_replace
from django_datatables.model_def import DatatableModel


class Country(models.Model):
    name = models.CharField(max_length=600)
    iso_code = models.CharField(max_length=4, unique=True, primary_key=True)

    class Meta:
        verbose_name_plural = u'Countries'

    def __str__(self):
        return self.name

    class Datatable(DatatableModel):
        name = {'title': 'Country'}

        class Flag(DatatableColumn):
            def row_result(self, data, _page_results):
                if type(data.get(self.field)) == str:
                    return data.get(self.field).replace(' ', '-')

            def col_setup(self):
                self.field = 'name'
                self.title = 'Flag'
                self.options['render'] = [render_replace(
                    var='999999',
                    html=f'<img src="{staticfiles_storage.url("country/flags/999999.png")}">'
                )]
