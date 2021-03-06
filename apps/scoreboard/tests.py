import random
import string
from django.test import TestCase, Client, override_settings
from django.urls import reverse

from apps.accounts.models import Account


class ScoreboardTest(TestCase):

    def setUp(self):
        for x in range(0, 10):
            team_name = ''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(10))
            new_account = Account.objects.create(
                username=team_name,
                email="{0}@gmail.com".format(team_name),
            )
            new_account.set_password(team_name)
            new_account.save()

    @override_settings(STATICFILES_STORAGE='')
    def test_scoreboard(self):
        client = Client()

        response = client.get(reverse('scoreboard:scoreboard'))
        self.assertEqual(response.status_code, 200)
