from task import *
from datetime import datetime
from  basic_backend import *


def main():

    my_items = [
        {'title': 'Complete project', 'description': 'Finish the project report', 'deadline': datetime(2024,5,1),'priority': 'High'},
        {'title': 'Complete activities', 'description': 'Finish the project report', 'deadline': datetime(2024,5,1),'priority': 'High'}
    ]
    # CREATE
    create_tasks(my_items)
    create_task('review quiz', 'chapter 1 - 3',datetime(2024,5,1),'Low' )


    # READ
    print('Read All Tasks')
    print(read_tasks())

    print('READ quiz')
    print(read_task('review quiz'))

    # UPDATE
    print('UPDATE exam')
    update_task('Complete project', 'chapter 1 - 3',datetime(2024,5,2),'High' )
    print(read_task('Complete project'))


    # DELETE
    print('DELETE review quiz')
    delete_task('review quiz')


    print('READ tasks')
    print(read_tasks())
    

if __name__ == '__main__':
    main()
