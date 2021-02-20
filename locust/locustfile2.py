from locust import HttpUser, between, task
import urllib3
from random import randint

EMAILS = [
    ["adam@domain.com", "Adam", "Abacki"],
    ["bogdan@domain.com", "Bogdan", "Babacki"],
    ["cecylia@domain.com", "Cecylia", "Cedacka"],
]

HOST = "https://k2lzwh7qzj.execute-api.eu-central-1.amazonaws.com/alpha_3"

# https://urllib3.readthedocs.io/en/latest/advanced-usage.html#ssl-warnings
urllib3.disable_warnings()


class FibbServ(HttpUser):
    wait_time = between(5, 15)
    host = HOST

    def on_start(self):
        pass

    @task
    def place_order(self):
        user_nb = randint(0, len(EMAILS) - 1)
        e_mail = EMAILS[user_nb][0]
        firstname = EMAILS[user_nb][1]
        lastname = EMAILS[user_nb][2]
        fibb_index = randint(1, 300)

        self.client.post(
            "/place_order",
            headers={"Content-Type": "application/json"},
            json={
                "e_mail": e_mail,
                "fibb_index": fibb_index,
                "firstname": firstname,
                "lastname": lastname,
            },
        )

    @task
    def results(self):
        user_nb = randint(0, len(EMAILS) - 1)
        e_mail = EMAILS[user_nb][0]

        self.client.post(
            "/results",
            headers={"Content-Type": "application/json"},
            json={"e_mail": e_mail},
        )