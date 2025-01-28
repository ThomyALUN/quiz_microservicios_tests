from locust import HttpUser, task
from random import randint

def getRandom():
  return randint(1, 3)

class ApiUser(HttpUser):
  @task
  def generate_labels(self):
    self.client.post("/api/generate_labels", json={"n": getRandom()})
