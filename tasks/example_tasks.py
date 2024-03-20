from robocorp.tasks import task, setup
from robocorp.log import debug
from .logconfig import setup_log


class TaskData:
    message = ""
    count = 0

    def __str__(self) -> str:
        returnable = ""
        for name, value in self.items():
            returnable += f"Logging: {self.__name__}.{name} = {value}"
        return returnable


@setup(scope="session")
def task_setup(tasks):
    setup_log()


@task
def example():
    message = "Hello"
    message = message + " World!"
    data = {"message": message, "count": 0}
    td = TaskData()
    td.message = message
    for x in range(3):
        data["count"] = x
        td.count = x
        debug(data)
        td = td
