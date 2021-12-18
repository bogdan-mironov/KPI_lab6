from locust import HttpUser, task, between


class QuickstartUser(HttpUser):
    wait_time = between(5, 20)
    host = 'http://www.boredapi.com/api/'

    @task
    def GetRandomEvent(self):
        self.client.get("activity/")

    @task
    def FindActivityByItsKey(self):
        self.client.get("activity?key=5881028")

    @task
    def FindRandomActivityWithGivenType(self):
        self.client.get("activity?type=recreational")

    @task
    def FindRandomActivityWithGivenNumberOfParticipants(self):
        self.client.get("activity?participants=1")