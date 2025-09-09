from models import db

class Task(db.Model):
    __tablename__ = "tasks"

    id = db.Column(db.Integer, primary_key=True) 
    title = db.Column(db.String(120), nullable=False) 
    description = db.Column(db.String(500), nullable=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    status = db.Column(db.String(20), nullable=False, default='Pendente') 
    user = db.relationship('User', back_populates='tasks')

    def __repr__(self):
        return f"<Task {self.title} - {self.status}>"
