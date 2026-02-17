import time
from locust import HttpUser, task, between

class WebsiteUser(HttpUser):
    wait_time = between(1, 5)

    @task
    def benchmarkApi(self):
        self.client.post(url="/testing/benchmark?presidentId=2403-03-01_cit_1&selectedDate=2025-10-18")