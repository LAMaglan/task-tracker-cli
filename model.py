import datetime

class Todo:
    def __init__(self, task, category, date_added=None, date_completed=None, status=1, position=None):
        self.task = task
        self.category = category
        self.date_added = date_added if date_added is not None else datetime.datetime.now().isoformat()
        self.date_completed = date_completed
        self.status = status # 1 = open, 2 = completed
        self.position = position
    
    # wrapper function for "prettier" printing
    def __repr__(self) -> str:
        return f"({self.task}, {self.category}, {self.date_added}, {self.date_completed}, {self.status}, {self.position})"