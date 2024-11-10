from locust import HttpUser, task, between

class TestItems(HttpUser):
    @task
    def test_get_items(self):
        self.client.get("/api/items")

