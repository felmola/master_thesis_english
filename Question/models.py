from otree.api import (
    models, widgets, BaseConstants, BaseSubsession, BaseGroup, BasePlayer,
    Currency as c, currency_range
)


author = 'Felipe Montealegre'

doc = """
Question
"""


class Constants(BaseConstants):
    name_in_url = 'Question'
    players_per_group = None
    num_rounds = 1


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):

    sexo = models.CharField(
        choices=['Masculine', 'Femenine', 'Other'],
        verbose_name='What is your sex?',
#        widget=widgets.RadioSelect()
    )

    edad = models.PositiveIntegerField(
        verbose_name='How old are you?',
        min=18, max=125
    )

    estado_civil = models.CharField(
        choices=['Single', 'Married', 'Cohabiting', 'Widowed'],
        verbose_name='What is your marital status?',
#        widget=widgets.RadioSelect()
    )

    carrera = models.StringField(
        verbose_name='What is your current undergraduate program?'
    )

    matricula = models.IntegerField(
        verbose_name='How many semesters have you paid counting the current one?'
    )

    estrato = models.IntegerField(
        choices=[
            (1, 'SES 1'),
            (2, 'SES 2'),
            (3, 'SES 3'),
            (4, 'SES 4'),
            (5, 'SES 5'),
            (6, 'SES 6'),
        ],
        verbose_name='According to your utility bills, what is the Socioeconomic Stratum (SES) of the dwelling you currently live in?',
#        widget=widgets.RadioSelect()
    )

    ingreso = models.IntegerField(
        choices=[
            (0, 'Less than 1 SMMLV'),
            (1, '1 SMMLV'),
            (2, '2 SMMLV'),
            (3, '3 SMMLV'),
            (4, '4 SMMLV'),
            (5, '5 SMMLV'),
            (6, '6 SMMLV'),
            (7, 'More than 6 SMMLV'),
        ],
        verbose_name='What is the approximate salary you earn in Monthly Legal Minimum Wages (SMMLV)?',
#        widget=widgets.RadioSelect()
    )

    localidad = models.IntegerField(
        choices=[
            (1, 'Kennedy'),
            (2, 'Suba'),
            (3, 'Engativá'),
            (4, 'Ciudad Bolívar'),
            (5, 'Bosa'),
            (6, 'Usaquén'),
            (7, 'San Cristobal'),
            (8, 'Rafael Uribe'),
            (9, 'Fontibón'),
            (10, 'Usme'),
            (11, 'Puente Aranda'),
            (12, 'Barrios Unidos'),
            (13, 'Tunjuelito'),
            (14, 'Teusaquillo'),
            (15, 'Chapinero'),
            (16, 'Antonio Nariño'),
            (17, 'Santa Fe'),
            (18, 'Los Mártires'),
            (19, 'La Candelaria'),
            ],
        verbose_name='In which urban district do you live in?',
#        widget=widgets.RadioSelect()
    )

    edu_padre = models.CharField(
        choices=['None', 'Elementary school', 'High school', 'Some university degree', 'Technical school', 'Higher education',
                 'Graduate education'],
        verbose_name='What is your father´s maximum degree of education?',
#        widget=widgets.RadioSelect()
    )

    edu_madre = models.CharField(
        choices=['None', 'Elementary school', 'High school', 'Some university degree', 'Technical school', 'Higher education',
                 'Graduate education'],
        verbose_name='What is your mothers´s maximum degree of education?',
#        widget=widgets.RadioSelect()
    )

    peso = models.IntegerField(
        verbose_name='What is your weight in Kilograms?'
    )

    altura = models.IntegerField(
        verbose_name='What is your height in centimeters'
    )

    fehr_1 = models.IntegerField(
        choices=[1, 2, 3, 4, 5,])

    fehr_2 = models.IntegerField(
        choices=[1, 2, 3, 4, 5,])

#    fehr_1 = models.IntegerField(
#        choices=[
#            (1, '1'),
#            (2, '2'),
#            (3, '3'),
#            (4, '4'),
#            (5, '5'),
#        ],
#        label= ' ¿Cómo se considera usted? Normalmente ¿es usted una persona totalmente dispuesta a tomar riesgos o'
#               ' intenta evitar tomar riesgos? Por favor conteste usando la siguiente escala de uno (1) a cinco (5), donde'
#               ' uno (1) indica “totalmente dispuesto a tomar riesgos” y cinco (1) “Totalmente contrario a tomar riesgos”',
#        widget=widgets.RadioSelectHorizontal
#    )
#
#    fehr_2 = models.IntegerField(
#        choices=[
#            (1, '1'),
#            (2, '2'),
#            (3, '3'),
#            (4, '4'),
#            (5, '5'),
#        ],
#        label= 'Normalmente ¿es usted una persona totalmente dispuesta a tomar riesgos de carácter financiero o intenta'
#               ' evitar tomar riesgos financieros? Por favor conteste usando la siguiente escala de uno (1) a cinco (5), donde'
#               ' uno (1) indica “totalmente dispuesto a tomar riesgos” y cinco (5) “Totalmente contrario a tomar riesgos”',
#        widget=widgets.RadioSelectHorizontal
#    )


    seicientos = models.CharField(
        choices=['I will not have any difficulty.', 'I will have some difficulty, but will get it.', 'I do not know if I will get it.',
                 'Definitely, I will not get it.'],
        verbose_name='If you need to find $600000 in a week, to cover an unexpected expenditure, how much difficult'
                     ' would it be to get the money?',
        widget=widgets.RadioSelect()
    )

    #def question_admin(self):
    #    self.participant.vars['consent_nombre'] = self.nombre
    #    self.participant.vars['consent_id_number'] = self.id_number
    #    print("[[ CONSENT ]] - PLAYER - CONSENT_ADMIN.............ROUND NUMBER", self.round_number)
    #    print("[[ CONSENT ]] - PLAYER - CONSENT_ADMIN.............PVARS ARE", self.participant.vars)

