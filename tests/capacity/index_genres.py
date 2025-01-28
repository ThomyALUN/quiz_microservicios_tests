from locust import HttpUser, task

class ApiUser(HttpUser):
  @task
  def get_genres(self):
    self.client.get("/api/genres")
