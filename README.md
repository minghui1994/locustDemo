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

Reference: [Locust API](https://docs.locust.io/en/stable/api.html#locust.core.Locust)

<h3>class Locust</h3>

* Represent a "user" which is to be hatched and attack the system that is to be load tested.
* Behavior of this user defined by **task_set** attribute, pointed to a **TaskSet** class.
* This class should usually be subclassed by a class that defines some kind of client. When load testing an HTTP system, probably want to use **HttpLocust** class.

|Code           |Description|
|---------------|-----------|
|**max_wait** = 1000|Maximum waiting time between the execution of locust tasks.|
|**min_wait** = 1000|Minimum waiting time between the execution of locust takes.|
|**task_set** = None|TaskSet class that defines the execution behavior of this locust.|
|**wait_function()**|Function used to calculate waiting time between the execution of locust tasks in milliseconds|
|**weight** = 10    |Probability of locust being chosen. The higher the weight, the greater is the chance of it being chosen.|

<br>

<h3>HttpLocust class</h3>

* Represent an HTTP "user" which is to be hatched and attack the system that is to be load tested.
* Behavior of this user is defined by the task_set attribute, which should point to a **TaskSet** class.
* This class creates a client attribute on instantiation which is an HTTP client with support for keeping a user session between requests.

|Code             |Description|
|-----------------|-----------|
|**client** = None|Instance of HttpSession that is created upon instantiation of Locust. The client support cookies, and therefore keeps the session between HTTP requests.|

<br>

<h3>TaskSet Class</h3>

* Class defining a set of tasks that a Locust user will execute.
* When a TaskSet starts running, it will pick a task from the *tasks* attribute, execute it, and call its **wait_function** which will define a time to sleep for.
* This defaults to a uniformly distributed random number between **min_wait** and **max_wait** milliseconds. It will then schedule another task for execution and so on.

|Code                          |Description|
|------------------------------|-----------|
|**client**                    |Reference to the *client* attribute of the root Locust instance.|
|**interrupt(reschedule=True)**|Interrupt the TaskSet and hand over execution control back to the parent TaskSet. If *reschedule* is True(default), the parent Locust will immediately reschedule, and execute, a new task. For nested TaskSet only.|
|**locust=None**               |Will reffer to the root Locust class instance when the TaskSet has been instantiated.|
|**max_wait**=None             |Max waiting time between execution of locust task. Can be used to override the max_wait defined in root Locust class.|
|**min_wait**=None             |Min waiting time between execution of Locust task. Can be used to override the min_wait defined in the root Locust class.|
|**parent=None**               |Will refer to the parent TaskSet, or Locust, class instance when the TaskSet has been instantiated. Useful for nested TaskSet classes.|
|**schedule_task(task_callable, args=None, Kwargs=None, first=False**|Add a task to the Locust's task execution queue.|
|**tasks=**[]|List with python callables that represents a locust user task. If tasks is a list, task to perform will be picked randomly.|
|**wait_function**=None|Function to calculate waiting time between the execution of locust taks in milliseconds. Can be used to override the wait_function defined in the root Locust class.|