from locust import HttpUser, between, task
import urllib3

HOST = "http://107.22.65.34:8080"

# https://urllib3.readthedocs.io/en/latest/advanced-usage.html#ssl-warnings
urllib3.disable_warnings()


class FibbServ(HttpUser):
    wait_time = between(5, 15)
    host = HOST

    def on_start(self):
        pass

    @task
    def fib_100(self):
        self.client.get("/fib/100")

    @task
    def fib_1000(self):
        self.client.get("/fib/1000")
