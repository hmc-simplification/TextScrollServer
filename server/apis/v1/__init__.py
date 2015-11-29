from users import User, Users#, Setting, Settings, Library, Libraries
#from trials import Trials, Trial


endpoints = [
	(User, "users/<string:user_id>"),
	(Users, "users")
]
