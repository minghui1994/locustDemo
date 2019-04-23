from locust import HttpLocust, TaskSet, task

class UserBehavior(TaskSet):
    def on_start(self):
        self.login()

    def on_stop(self):
        self.logout()

    def login(l):
        l.client.post("/login", {"username": "ellen_key", "password": "education"})

    def logout(l):
        l.client.post("/logout", {"username": "ellen_key", "password": "education"})

    @task(2)
    def index(l):
        l.client.get("/")

    @task(1)
    def profile(l):
        l.client.get("/profile")


class WebsiteUser(HttpLocust): #Represents a user
    task_set = UserBehavior
    min_wait = 5000
    max_wait = 9000