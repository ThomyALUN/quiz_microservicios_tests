from locust import HttpUser, task
from random import randint

def getRandom():
  return randint(1, 3)

class ApiUser(HttpUser):
  @task
  def get_genre(self):
    self.client.get(f"/api/genres/{getRandom()}")
    