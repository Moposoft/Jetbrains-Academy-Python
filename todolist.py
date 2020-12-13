from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, Date
from sqlalchemy.orm import sessionmaker
from datetime import datetime, timedelta, date

engine = create_engine('sqlite:///todo.db?check_same_thread=False')
Base = declarative_base()


class Table(Base):
    __tablename__ = 'task'
    id = Column(Integer, primary_key=True)
    task = Column(String, name='task', default='default_value')
    deadline = Column(Date, name='deadline', default=datetime.today())

    def __repr__(self):
        return self.task


Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)
session = Session()


def todays_tasks():
    d = date.today()
    print("Today {} {}".format(d.day, d.strftime("%b")))
    rows = session.query(Table).filter(Table.deadline == d.today()).order_by(Table.deadline).all()
    if not rows:
        print("Nothing to do!\n")
    else:
        for x in range(len(rows)):
            print("{}. {}".format(x+1, rows[x]))
        print()


def weeks_tasks():
    d = date.today()
    days = [d + timedelta(days=n) for n in range(0, 7)]
    for i in days:
        print("{} {} {}:".format(i.strftime("%A"), i.day, i.strftime("%b")))
        rows = session.query(Table).filter(Table.deadline == i).order_by(Table.deadline).all()
        if not rows:
            print("Nothing to do!\n")
        else:
            for x in range(len(rows)):
                print("{}. {}".format(x, rows[x]))
            print()


def missed_tasks():
    print("Missed tasks:")
    rows = session.query(Table, Table.deadline).filter(Table.deadline < datetime.today().date()).all()
    if not rows:
        print("Nothing is missed!\n")
    else:
        for x in range(len(rows)):
            task = rows[x][0]
            day = rows[x][1].day
            month = rows[x][1].strftime("%b")
            print("{}. {}. {} {}".format(x + 1, task, day, month))
        print()


def all_tasks():
    print("All tasks:")
    rows = session.query(Table, Table.deadline).order_by(Table.deadline).all()
    if not rows:
        print("Nothing to do!\n")
    else:
        for x in range(len(rows)):
            task = rows[x][0]
            day = rows[x][1].day
            month = rows[x][1].strftime("%b")
            print("{}. {}. {} {}".format(x + 1, task, day, month))
        print()


def delete_task():
    rows = session.query(Table).all()
    if not rows:
        print("Nothing to delete\n")
    else:
        print("Choose the number of the task you want to delete:")
        rows = session.query(Table, Table.deadline, Table.id).order_by(Table.deadline).all()
        for x in range(len(rows)):
            task = rows[x][0]
            day = rows[x][1].day
            month = rows[x][1].strftime("%b")
            print("{}. {}. {} {}".format(x + 1, task, day, month))
    task = int(input())
    task_id = rows[task-1].id
    session.query(Table).filter(Table.id == task_id).delete()
    session.commit()
    print("The task has been deleted!\n")


def add_task():
    print("Enter task")
    task = input()
    print("Enter deadline")
    dl = datetime.strptime(input(), '%Y-%m-%d')
    new_row = Table(task=task, deadline=dl)
    session.add(new_row)
    session.commit()
    print("The task has been added!\n")


options = {"1": todays_tasks, "2": weeks_tasks, "3": all_tasks,
           "4": missed_tasks, "5": add_task, "6": delete_task, "0": exit}

while True:
    print("1) Today's tasks\n2) Week's tasks\n3) All tasks\n"
          "4) Missed tasks\n5) Add task\n6) Delete task\n0) Exit")
    options[input()]()
