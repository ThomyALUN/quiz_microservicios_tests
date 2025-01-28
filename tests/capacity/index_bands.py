from locust import HttpUser, task

class ApiUser(HttpUser):
  @task
  def get_bands(self):
    self.client.get("/api/bands")
