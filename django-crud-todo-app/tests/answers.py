all_lists = [
{
  "model": "list_app.list",
  "pk": 3,
  "fields": {
    "list_name": "Tuesday"
  }
},
{
  "model": "list_app.list",
  "pk": 4,
  "fields": {
    "list_name": "testingname"
  }
},
{
  "model": "list_app.list",
  "pk": 5,
  "fields": {
    "list_name": "Thursday"
  }
},
{
  "model": "list_app.list",
  "pk": 6,
  "fields": {
    "list_name": "Friday"
  }
},
{
  "model": "list_app.list",
  "pk": 7,
  "fields": {
    "list_name": "New list test"
  }
}
]

all_tasks = [
{
  "model": "task_app.task",
  "pk": 3,
  "fields": {
    "task_name": "Take out trash",
    "completed": True,
    "parent_list": 'Tuesday'
  }
},
{
  "model": "task_app.task",
  "pk": 8,
  "fields": {
    "task_name": "add1",
    "completed": False,
    "parent_list": 'Tuesday'
  }
},
{
  "model": "task_app.task",
  "pk": 9,
  "fields": {
    "task_name": "add2",
    "completed": False,
    "parent_list": 'Tuesday'
  }
},
{
  "model": "task_app.task",
  "pk": 10,
  "fields": {
    "task_name": "willthiswork",
    "completed": False,
    "parent_list": 'Tuesday'
  }
},
{
  "model": "task_app.task",
  "pk": 11,
  "fields": {
    "task_name": "anothertest",
    "completed": False,
    "parent_list": 'Tuesday'
  }
},
{
  "model": "task_app.task",
  "pk": 12,
  "fields": {
    "task_name": "anothertest",
    "completed": False,
    "parent_list": 'Tuesday'
  }
}
]

all_sub_tasks = [
{
  "model": "sub_task_app.sub_task",
  "pk": 15,
  "fields": {
    "sub_task_name": "grab leashes",
    "completed": True,
    "parent_task": "Walk Dogs"
  }
},
{
  "model": "sub_task_app.sub_task",
  "pk": 16,
  "fields": {
    "sub_task_name": "grab poop bags",
    "completed": True,
    "parent_task": "Walk Dogs"
  }
},
{
  "model": "sub_task_app.sub_task",
  "pk": 17,
  "fields": {
    "sub_task_name": "grab water bottle",
    "completed": True,
    "parent_task": "Walk Dogs"
  }
},
{
  "model": "sub_task_app.sub_task",
  "pk": 18,
  "fields": {
    "sub_task_name": "grab bowl",
    "completed": True,
    "parent_task": "Walk Dogs"
  }
},
{
  "model": "sub_task_app.sub_task",
  "pk": 21,
  "fields": {
    "sub_task_name": "letussee",
    "completed": False,
    "parent_task": "Walk Dogs"
  }
},
{
  "model": "sub_task_app.sub_task",
  "pk": 22,
  "fields": {
    "sub_task_name": "letussee2",
    "completed": False,
    "parent_task": "Walk Dogs"
  }
}
]

