users_db = []

def register_user(username, email, age):
    # Checking if user is underage
    if age < 18:
        return "Registration failed: age must be 18 or older."
    
    # Body of the function 
    user = {"username": username, "email": email, "age": age}
    users_db.append(user)
    
    # The output 
    return f"User {username} registered successfully!"

# Pass the parameters in any way to register a user
result1 = register_user('Starbucks', 'starbucks.com', 20)

# Testing the result
print(result1)
print(users_db)  # List of registered users
