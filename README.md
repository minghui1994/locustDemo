<h1>Locust Demo</h1>

A repo to learn Locust load testing tool.

<h2>Basics</h2>

```python
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
```

|Code    |Description|
|--------|-----------|
|on_start|Called when a locust start before any task is scheduled|
|on_stop |Called when the TaskSet is stopping|

<br>
<br>

<h2>API</h2>

<h3>class Locust</h3>

* Represent a "user" which is to be hatched and attack the system that is to be load tested.
* Behavior of this user defined by **task_set** attribute, pointed to a **TaskSet** class.
* This class should usually be subclassed by a class that defines some kind of client. When load testing an HTTP system, probably want to use **HttpLocust** class.

|Code           |Description|
|---------------|-----------|
|max_wait = 1000|Maximum waiting time between the execution of locust tasks.|
|min_wait = 1000|Minimum waiting time between the execution of locust takes.|
|task_set = None|TaskSet class that defines the execution behavior of this locust.|
|wait_function()|Function used to calculate waiting time between the execution of locust tasks in milliseconds|
|weight = 10    |Probability of locust being chosen. The higher the weight, the greater is the chance of it being chosen.|