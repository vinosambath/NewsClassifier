from newsClassifier import login_manager
from newsClassifier.Models.user import User

@login_manager.user_loader
def load_user(id):
	return User(id)
