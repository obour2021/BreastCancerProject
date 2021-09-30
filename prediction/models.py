from django.db import models

# Create your models here.

class PredictCancer(models.Model):
    TWENTY = '20-29'
    THIRTY = '30-39'
    FOURTY = '40-49'
    FIFTY = '50-59'
    SIXTY = '60-69'
    SEVENTY = '70-79'
    AGE_CHOICES = [
        (TWENTY, '20-29'),
        (THIRTY, '30-39'),
        (FOURTY, '40-49'),
        (FIFTY, '50-59'),
        (SIXTY, '60-69'),
        (SEVENTY, '70-79'),
    ]
    age = models.CharField(
        max_length=50,
        choices=AGE_CHOICES,
    )

    LOW = 'ge40'
    MEDIUM = 'lt40'
    HIGH = 'premeno'
    MENOPAUSE_CHOICES =[
        (LOW, 'ge40'),
        (MEDIUM, 'lt40'),
        (HIGH, 'premeno'),
    ]

    menopause = models.CharField(
        max_length=50,
        choices=MENOPAUSE_CHOICES,
    )

    ONE = '0-4'
    TWO = '5-9'
    THREE = '10-14'
    FOUR = '15-19'
    FIVE = '20-24'
    SIX = '25-29'
    SEVEN = '30-34'
    EIGHT = '35-39'
    NINE = '40-44'
    TEN = '45-49'
    ELEVEN = '50-54'
    TUMOR_SIZE_CHOICES = [
        (ONE, '0-4'),
        (TWO, '5-9'),
        (THREE, '10-14'),
        (FOUR, '15-19'),
        (FIVE, '20-24'),
        (SIX, '25-29'),
        (SEVEN, '30-34'),
        (EIGHT, '35-39'),
        (NINE, '40-44'),
        (TEN, '45-49'),
        (ELEVEN, '50-54'),
    ]

    tumor_size = models.CharField(
        max_length=50,
        choices=TUMOR_SIZE_CHOICES,
    )

    FIRST = '0-2'
    SECOND = '3-5'
    THIRD = '6-8'
    FOURTH = '9-11'
    FIVETH = '12-14'
    SIXTH = '15-17'
    SEVENTH = '24-26'
    INV_NODES_CHOICES = [
        (FIRST, '0-2'),
        (SECOND, '3-5'),
        (THIRD, '6-8'),
        (FOURTH, '9-11'),
        (FIVETH, '12-14'),
        (SIXTH, '15-17'),
        (SEVENTH, '24-26'),
    ]

    inv_nodes = models.CharField(
        max_length=50,
        choices=INV_NODES_CHOICES,
    )

    NO = 'no'
    YES = 'yes'
    NODE_CAPS_CHOICES = [
        (NO, 'no'),
        (YES, 'yes'),
    ]

    node_caps = models.CharField(
        max_length=50,
        choices=NODE_CAPS_CHOICES,
    )

    deg_malig = models.IntegerField()

    LEFT = 'left'
    RIGHT = 'right'
    BREAST_CHOICES = [
        (LEFT, 'left'),
        (RIGHT, 'right'),
    ]

    breast = models.CharField(
        max_length=50,
        choices=BREAST_CHOICES,
    )

    CENTRAL = 'central'
    LEFTLOW = 'left_low'
    LEFTUP = 'left_up'
    RIGHTLOW = 'right_low'
    RIGHTUP = 'right_up'
    BREAST_QUAD_CHOICES = [
        (CENTRAL, 'central'),
        (LEFTLOW, 'left_low'),
        (LEFTUP, 'left_up'),
        (RIGHTLOW, 'right_low'),
        (RIGHTUP, 'right_up'),
    ]

    breast_quad = models.CharField(
        max_length=50,
        choices=BREAST_QUAD_CHOICES,
    )


    NO = 'no'
    YES = 'yes'
    IRRADIAT_CHOICES = [
        (NO, 'no'),
        (YES, 'yes'),
    ]

    irradiat = models.CharField(
        max_length=50,
        choices=IRRADIAT_CHOICES,
    )

    classification = models.CharField(max_length=50)

    def __str__(self):
        return self.classification

    def get_absolute_url(self):
        return "list"
    



    



