from ajax_helpers.mixins import AjaxHelpers
from django_datatables.datatables import DatatableView
from django_menus.menu import MenuItem

from bookeeper.views.views import BaseMenu
from country.management.commands.initialise_countries import initialise_countries
from country.models import Country


class CountryList(AjaxHelpers, BaseMenu, DatatableView):
    template_name = 'bookeeper/bookeeper_table.html'
    model = Country

    def setup_menu(self):
        self.add_menu('page_menu').add_items(MenuItem('import', 'Import', MenuItem.AJAX_BUTTON))

    def button_import(self, **kwargs):
        initialise_countries()
        return self.command_response('reload')

    def setup_table(self, table):
        table.add_columns(
            'name', 'iso_code', 'Flag',
        )
