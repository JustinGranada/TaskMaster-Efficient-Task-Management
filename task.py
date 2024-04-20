import basic_backend
import mvc_exceptions as mvc_exc
from datetime import datetime
class Task(object):

    def __init__(self, application_tasks):
        self._task_type = 'activities'
        self.create_items(application_tasks)

    @property
    def task_type(self):
        return self._item_type

    @task_type.setter
    def task_type(self, new_task_type):
        self._task_type = new_task_type

    def create_task(self, title, description, deadline, priority):
        basic_backend.create_task(title, description, deadline, priority)

    def create_tasks(self, tasks):
        basic_backend.create_tasks(tasks)

    def read_task(self, title):
        return basic_backend.read_tasks(title)

    def read_tasks(self):
        return basic_backend.read_tasks()

    def update_task(self, title, description, deadline, priority):
        basic_backend.update_task(title, description, deadline, priority)

    def delete_task(self, title):
        basic_backend.delete_task(title)

    def filter_tasks_by_priority(self, priority): 

        return [task for task in self.tasks if task.priority == priority] 

    def filter_tasks_by_deadline(self, deadline): 

        return [task for task in self.tasks if task.deadline == deadline] 
    

class View(object):

    @staticmethod
    def show_bullet_point_list(task_type, tasks):
        print('--- {} LIST ---'.format(task_type.upper()))
        for task in tasks:
            print('* {}'.format(task))

    @staticmethod
    def show_number_point_list(task_type, tasks):
        print('--- {} LIST ---'.format(task_type.upper()))
        for i, task in enumerate(tasks):
            print('{}. {}'.format(i+1, task))

    @staticmethod
    def show_task(task_type, task, task_info):
        print('//////////////////////////////////////////////////////////////')
        print('Tasks Listed: {}'.format(task.upper()))
        print('{} INFO: {}'.format(task_type.upper(), task_info))
        print('//////////////////////////////////////////////////////////////')

    @staticmethod
    def display_missing_task_error(task, err):
        print('**************************************************************')
        print('Sorry, no task in the list{}!'.format(task.upper()))
        print('{}'.format(err.args[0]))
        print('**************************************************************')

    @staticmethod
    def display_task_already_stored_error(task, task_type, err):
        print('**************************************************************')
        print('Task already created {} in the {} list!'
              .format(task.upper(), task_type))
        print('{}'.format(err.args[0]))
        print('**************************************************************')

    @staticmethod
    def display_task_not_yet_stored_error(task, task_type, err):
        print('**************************************************************')
        print('Task {} not in our {} list. Please insert it first!'
              .format(task.upper(), task_type))
        print('{}'.format(err.args[0]))
        print('**************************************************************')

    @staticmethod
    def display_item_stored(task, task_type):
        print('++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++')
        print('Added the task {} to the {} list!'
              .format(task.upper(), task_type))
        print('++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++')

    @staticmethod
    def display_change_task_type(older, newer):
        print('---   ---   ---   ---   ---   ---   ---   ---   ---   ---   --')
        print('Change task type from "{}" to "{}"'.format(older, newer))
        print('---   ---   ---   ---   ---   ---   ---   ---   ---   ---   --')

    @staticmethod
    def display_item_updated(title, o_description, o_deadline, o_priority,n_description, n_deadline, n_priority):
        print('---   ---   ---   ---   ---   ---   ---   ---   ---   ---   --')
        print('Change {} description: {} --> {}'
              .format(title, o_description, n_description))
        print('Change {} deadline: {} --> {}'
              .format(title, o_deadline, n_deadline))
        print('Change {} priority: {} --> {}'
              .format(title, o_priority, n_priority))
        print('---   ---   ---   ---   ---   ---   ---   ---   ---   ---   --')

    @staticmethod
    def display_item_deletion(title):
        print('--------------------------------------------------------------')
        print('We have just removed {} from our list'.format(title))
        print('--------------------------------------------------------------')   

class Controller(object):

    def __init__(self, model, view):
        self.model = model
        self.view = view

    def show_items(self, bullet_points=False):
        tasks = self.model.read_tasks()
        task_type = self.model.task_type
        if bullet_points:
            self.view.show_bullet_point_list(task_type, tasks)
        else:
            self.view.show_number_point_list(task_type, tasks)

    def show_item(self, task_title):
        try:
            task = self.model.read_item(task_title)
            task_type = self.model.item_type
            self.view.show_item(task_type, task_title, task)
        except mvc_exc.ItemNotStored as e:
            self.view.display_missing_item_error(task_title, e)

    def insert_item(self, title, description, deadline, priority):
        assert isinstance(deadline,datetime.date), 'deadline must date'
        task_type = self.model.task_type
        try:
            self.model.create_task(title, description, deadline, priority)
            self.view.display_task_stored(title, task_type)
        except mvc_exc.TaskAlreadyStored as e:
            self.view.display_task_already_stored_error(title, task_type, e)

    def update_task(self, title, description, deadline, priority):
        assert isinstance(deadline,datetime.date), 'deadline must date'
        task_type = self.model.item_type

        try:
            older = self.model.read_task(title)
            self.model.update_task(title, description, deadline, priority)
            self.view.display_item_updated(
                title, older['description'], older['deadline'],older['priority'], description, deadline, priority)
        except mvc_exc.ItemNotStored as e:
            self.view.display_item_not_yet_stored_error(title, task_type, e)
            # if the item is not yet stored and we performed an update, we have
            # 2 options: do nothing or call insert_item to add it.
            # self.insert_item(name, price, quantity)

    def update_task_type(self, new_task_type):
        old_task_type = self.model.task_type
        self.model.task_type = new_task_type
        self.view.display_change_item_type(old_task_type, new_task_type)

    def delete_task(self, title):
        task_type = self.model.task_type
        try:
            self.model.delete_task(title)
            self.view.display_task_deletion(title)
        except mvc_exc.ItemNotStored as e:
            self.view.display_item_not_yet_stored_error(title, task_type, e)