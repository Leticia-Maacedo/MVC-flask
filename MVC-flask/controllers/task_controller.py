from flask import render_template, request, redirect, url_for
from models import db
from models.task import Task
from models.user import User

class TaskController:

    @staticmethod
    def list_tasks():
        tasks = Task.query.all()   
        return render_template('tasks.html', tasks=tasks)

    @staticmethod
    def create_task():
        if request.method == 'POST':
            title = request.form['title']
            description = request.form['description']
            user_id = request.form['user_id']

            nova_tarefa = Task(title=title, description=description, user_id=user_id)

            db.session.add(nova_tarefa)
            db.session.commit()

            return redirect('/tasks')

        else:
            usuarios = User.query.all()
            return render_template('create_task.html', users=usuarios)


    @staticmethod
    def update_task_status(task_id):
        tarefa = Task.query.get(task_id)
        if tarefa:
            if tarefa.status == 'Pendente':
                tarefa.status = 'Concluído'
            else:
                tarefa.status = 'Pendente'
            db.session.commit()
        return redirect('/tasks')


    @staticmethod
    def delete_task(task_id):
        tarefa = Task.query.get(task_id)
        if tarefa:
            db.session.delete(tarefa)
            db.session.commit()
        return redirect('/tasks')

