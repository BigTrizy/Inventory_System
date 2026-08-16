import tomllib

with open("scripts/standards/policy.toml", "rb") as file:
        policies = tomllib.load(file)

def normalize_username(username):
    username = username.lower().strip()
    return username

def validate_username(username):
        username = normalize_username(username)
        if len(username) > policies["username"]["max_length"]:
            return (False, f"Error: Username is longer than the allowed length of {policies['username']['max_length']}", username)
        if len(username) < policies["username"]["min_length"]:
            return (False, f"Error: Username is shorter than the minimum required length of {policies['username']['min_length']}", username)
        if not policies["username"]["spaces"]:
            if " " in username:
                 return (False, f"Username cannot contain spaces", username)
        return(True, f"Username: {username} is valid", username)

def validate_password(password):
     if len(password) > policies["password"]["max_length"]:
          return (False, f"Error: Password is longer than the allowed length of {policies["password"]["max_length"]}")
     if len(password) < policies["password"]["min_length"]:
               return (False, f"Error: Password is shorter than the minimum required length of {policies["password"]["min_length"]}")
     return (True, f"Password is valid")
     

    