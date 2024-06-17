from user import User
from user1 import Privileges,Admin

user = User('sudip','basnet',20,'male')
user.describe_user()

admin = Admin('kailash','panth',25,'male')
admin.describe_user()
admin.privileges.show_privileges()