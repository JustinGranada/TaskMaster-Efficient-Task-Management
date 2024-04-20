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
    # if we try to re-create an object we get an ItemAlreadyStored exception
    # create_item('beer', price=2.0, quantity=10)

    # READ
    print('Read All Tasks')
    print(read_tasks())
    # if we try to read an object not stored we get an ItemNotStored exception
    # print('READ chocolate')
    # print(read_item('chocolate'))
    print('READ quiz')
    print(read_task('review quiz'))

    # UPDATE
    print('UPDATE exam')
    update_task('Complete project', 'chapter 1 - 3',datetime(2024,5,2),'High' )
    print(read_task('Complete project'))
    # if we try to update an object not stored we get an ItemNotStored exception
    # print('UPDATE chocolate')
    # update_item('chocolate', price=10.0, quantity=20)

    # DELETE
    print('DELETE review quiz')
    delete_task('review quiz')
    # if we try to delete an object not stored we get an ItemNotStored exception
    # print('DELETE chocolate')
    # delete_item('chocolate')

    print('READ tasks')
    print(read_tasks())
    

if __name__ == '__main__':
    main()