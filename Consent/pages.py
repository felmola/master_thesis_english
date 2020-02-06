from otree.api import Currency as c, currency_range
from ._builtin import Page, WaitPage
from .models import Constants

class Bienvenido(Page):
    pass


class Consent(Page):

    form_model = 'player'
    form_fields = ['nombre', 'id_number']

    def before_next_page(self):
        self.player.consent_admin()


class NormalWaitPage(WaitPage):
    title_text = "Please wait"
    body_text = "Waiting for the other participants."
    pass


page_sequence = [
    Bienvenido,
    NormalWaitPage,
    Consent,
    NormalWaitPage,
]
