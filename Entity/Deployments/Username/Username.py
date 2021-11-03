import os
from Entity.Entity import Entity

KEY_USERNAME = "username"

class Username(Entity):
    name = "Username"

    def Initialize(self):
        self.AddKey(KEY_USERNAME)
        self.SetValue(KEY_USERNAME, str(self.GetUsername())) # Fixed value

    def Update(self):
        pass

    def GetUsername(self):
        # Gives user's home directory
        userhome = os.path.expanduser('~')

        # Gives username by splitting path based on OS
        return os.path.split(userhome)[-1] 

