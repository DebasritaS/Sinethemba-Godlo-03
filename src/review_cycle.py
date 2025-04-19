class ReviewCycle:
    def __init__(self, cycle_id, start_date, end_date):
        self.__cycle_id = cycle_id
        self.__start_date = start_date
        self.__end_date = end_date
        self.__tasks = []  # Composition of ReviewTasks

    def add_task(self, task):
        self.__tasks.append(task)

    def get_pending_tasks(self):
        return [task for task in self.__tasks if not task._ReviewTask__completed]
