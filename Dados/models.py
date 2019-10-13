from otree.api import (
    models, widgets, BaseConstants, BaseSubsession, BaseGroup, BasePlayer,
    Currency as c, currency_range
)


author = 'Felipe Montealegre'

doc = """
Dados
"""


class Constants(BaseConstants):
    name_in_url = 'Dados'
    players_per_group = None
    num_rounds = 1


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):

    reporte_numero = models.IntegerField(
        choices=[
            (1, '1'),
            (2, '2'),
            (3, '3'),
            (4, '4'),
            (5, '5'),
            (6, '6'),
        ],
        verbose_name='Please select the number you rolled on the first try from the list below:',
    )

    reporte_pago = models.IntegerField(
        choices=[
            (2, '2 ECU'),
            (4, '4 ECU'),
            (6, '6 ECU'),
            (8, '8 ECU'),
            (10, '10 ECU'),
            (0, '0 ECU'),
        ],
        verbose_name='Now select the payment according to the table above from the list below:',
    )

    total_payoff = models.IntegerField()

    def set_payoff(self):
        if self.reporte_numero == 1:
            self.total_payoff = 2
        elif self.reporte_numero == 2:
            self.total_payoff = 4
        elif self.reporte_numero == 3:
            self.total_payoff = 6
        elif self.reporte_numero == 4:
            self.total_payoff = 8
        elif self.reporte_numero == 5:
            self.total_payoff = 10
        elif self.reporte_numero == 6:
            self.total_payoff = 0

        self.payoff = self.total_payoff
        print("[[ DADOS ]] - PLAYER - SET_PAYOFF.............TOTAL_PAYOFF IS", self.total_payoff)
        print("[[ DADOS ]] - PLAYER - SET_PAYOFF.............PAYOFF IS", self.payoff)

    def memory_admin(self):
        self.participant.vars['dados_reporte_numero'] = self.reporte_numero
        self.participant.vars['dados_payoff'] = self.total_payoff
        print("[[ DADOS ]] - PLAYER - DADOS_ADMIN.............ROUND NUMBER", self.round_number)
        print("[[ DADOS ]] - PLAYER - DADOS_ADMIN.............PVARS ARE", self.participant.vars)
