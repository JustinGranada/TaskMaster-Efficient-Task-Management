import mvc_exceptions as mvc_exc

tasks = list()

def create_tasks(app_tasks):
    global tasks
    tasks = app_tasks


def create_task(title, description, deadline, priority):
    global tasks
    results = list(filter(lambda x: x['title'] == title, tasks))
    if results:
        raise mvc_exc.ItemAlreadyStored('"{}" already stored!'.format(title))
    else:
        tasks.append({'title': title, 'description': description, 'deadline': deadline, 'priority':priority })

def read_task(title):
    global tasks
    mytasks = list(filter(lambda x: x['title'] == title, tasks))
    if mytasks:
        return mytasks[0]
    else:
        raise mvc_exc.ItemNotStored(
            'Can\'t read "{}" because it\'s not stored'.format(title))

def read_tasks():
    global tasks
    return [task for task in tasks]

def update_task(title, description, deadline, priority):
    global tasks
    # Python 3.x removed tuple parameters unpacking (PEP 3113), so we have to do it manually (i_x is a tuple, idxs_items is a list of tuples)
    idxs_tasks = list(
        filter(lambda i_x: i_x[1]['title'] == title, enumerate(tasks)))
    if idxs_tasks:
        i, task_to_update = idxs_tasks[0][0], idxs_tasks[0][1]
        tasks[i] = {'title': title, 'description': description, 'deadline': deadline, 'priority':priority}
    else:
        raise mvc_exc.ItemNotStored(
            'Can\'t update "{}" because it\'s not stored'.format(title))


def delete_task(title):
    global tasks
    # Python 3.x removed tuple parameters unpacking (PEP 3113), so we have to do it manually (i_x is a tuple, idxs_items is a list of tuples)
    idxs_tasks = list(
        filter(lambda i_x: i_x[1]['title'] == title, enumerate(tasks)))
    if idxs_tasks:
        i, task_to_delete = idxs_tasks[0][0], idxs_tasks[0][1]
        del tasks[i]
    else:
        raise mvc_exc.ItemNotStored(
            'Can\'t delete "{}" because it\'s not stored'.format(title))

