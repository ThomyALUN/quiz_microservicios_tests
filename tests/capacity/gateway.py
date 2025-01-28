from locust import HttpUser, task
from random import randint

def getRandom():
  return randint(1, 3)

class ApiUser(HttpUser):
  @task
  def get_bands(self):
    self.client.get("/api/bands")

  @task
  def get_band(self):
    self.client.get(f"/api/bands/{getRandom()}")

  @task
  def get_genres(self):
    self.client.get("/api/genres")

  @task
  def get_genre(self):
    self.client.get(f"/api/genres/{getRandom()}")
    
  @task
  def generate_labels(self):
    self.client.post("/api/generate_labels", json={"n": getRandom()})

  @task
  def record_labels(self):
    self.client.get("/api/record_labels")