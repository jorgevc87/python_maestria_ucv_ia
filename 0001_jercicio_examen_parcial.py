# Sistema de control de acceso

# Simulacion de la base de datos de usuarios
USER_DATABASE = {
    "jorge_dev": {"password": "secure123", "role": "admin"},
    "maria_user": {"password": "pass456", "role": "user"},
    "guest": {"password": "guest", "role": "guest"},
}

# Revisa si el usuario existe y si la contraseña es correcta
def check_credentials(username, password):
    user = USER_DATABASE.get(username)
    return user and user["password"] == password

# Obtiene el nivel de acceso del usuario
def get_access_level(username):
    return USER_DATABASE[username]["role"]

# Otorga acceso basado en el nivel de acceso
def grant_access(role):
    if role == "admin":
        return "Welcome, admin: Full access to the system."
    elif role == "user":
        return "Welcome user: Limited access to user features."
    elif role == "guest":
        return "User access granted: Read-only access."
    else:
        return "Access denied: Unknown role."

# Función principal de control de acceso
def access_control(username, password):
    if check_credentials(username, password):
        level = get_access_level(username)
        grant_access(level)
    else:
        return "Access denied: Invalid credentials."

# Reintentos
def login_with_retries(max_attemps = 3):
    attempts = 0
    while attempts < max_attemps:
        username = input("Enter username: ")
        password = input("Enter password: ")
        if check_credentials(username, password):
            access_control(username, password)
            return
        else:
            attempts += 1
            print("Invalid credentials. Please try again.")
    print(f"Attempt {attempts} of {max_attemps}.")


    # Ejecutar
if __name__ == "__main__":
    login_with_retries()
        