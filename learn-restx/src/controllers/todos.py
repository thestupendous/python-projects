from flask_restx import Namespace, fields, Resource

todosCtrlr = Namespace("todos", path="/todos/", description="todos api controller")

todosDB = []

createTodoCommand = todosCtrlr.model("createTaskCommand",{
    'task' : fields.String(required=True, description="task to do")
})

todoDTO = todosCtrlr.model("todoDTO",{      # Data Transfer Object
    'task' : fields.String(required=True, description="About the Todo")
})

@todosCtrlr.route("/")
class Todos(Resource):
    @todosCtrlr.marshal_list_with(todoDTO)
    def get(self):
        return todosDB

    @todosCtrlr.expect(createTodoCommand)
    def post(self):
        # use the Api payload and return the created item with status 201
        newTodo = todosCtrlr.payload
        newId = 1 if len(todosDB) == 0 else 1 + max([x["id"] for x in todosDB])
        todo = {"id": newId, "task": newTodo["task"]}
        todosDB.append(todo)
        return todo, 201

@todosCtrlr.route("/<int:id>")
class Todo(Resource):
    @todosCtrlr.marshal_with(todoDTO)
    def get(self, id):
        requiredTodo = [x for x in todosDB if x['id'] == id]
        if len(requiredTodo) == 0:
            todosCtrlr.abort(404, "Todo with id {} doesn't exist".format(id))
        return requiredTodo[0], 200
    
    def delete(self, id):
        global todosDB
        todosDB = [x for x in todosDB if x['id'] != id]
        return '', 204
    
    @todosCtrlr.expect(createTodoCommand)
    @todosCtrlr.marshal_with(todoDTO)
    def put(self, id):
        updatedTodo = todosCtrlr.payload
        for todo in todosDB:
            if todo['id'] == id:
                todo['task'] = updatedTodo['task']
                return todo, 200
        todosCtrlr.abort(404, "Todo with id {} doesn't exist".format(id))
