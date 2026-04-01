
"""
    POST/PUT requests required data
"""

def get_user_payload(email, password="Password123!"):
    return {
        "name": "AFL Automation",
        "email": email,
        "password": password,
        "title": "Mr",
        "birth_date": "10",
        "birth_month": "October",
        "birth_year": "1995",
        "firstname": "AFL",
        "lastname": "Tester",
        "company": "AFL Tech",
        "address1": "123 Main Street",
        "address2": "Apt 4B",
        "country": "India",
        "zipcode": "500001",
        "state": "Telangana",
        "city": "Hyderabad",
        "mobile_number": "9876543210"
    }

def data_driven():
    # List of tuples format: (email, password, expected_status)
    return [
        ("dinesh8897@gmail.com", "Ange949161@", 200),    # Positive Case
        ("invalid_user@test.com", "wrong_pass", 404),   # Negative Case
        ("", "any_pass", 400),                          # Empty Email Case
        ("user@test.com", "", 400)                      # Empty Password Case
    ]