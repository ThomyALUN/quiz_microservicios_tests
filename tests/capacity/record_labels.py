from locust import HttpUser, task

class ApiUser(HttpUser):
  @task
  def record_labels(self):
    self.client.get("/api/record_labels")
