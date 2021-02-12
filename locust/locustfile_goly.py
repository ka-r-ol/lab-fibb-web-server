from locust import HttpUser, between, task
import urllib3

# HOST = "http://107.22.65.34:8080"
# HOST = "http://localhost:8080"
HOST = "http://3.127.136.141:8080"

# https://urllib3.readthedocs.io/en/latest/advanced-usage.html#ssl-warnings
urllib3.disable_warnings()


class FibbServ(HttpUser):
    wait_time = between(5, 15)
    host = HOST

    def on_start(self):
        pass

    def fib_100(self):
        self.client.get("/fib/100")

    @task
    def fib_300000(self):
        self.client.get("/fib/300000")
