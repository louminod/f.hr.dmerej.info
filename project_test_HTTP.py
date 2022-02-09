import requests

def add_employee() :
    payload = {'employee': {'name': 'a', 'email': 'a', 'basic_info': {'address_line1': 'a', 'address_line2': 'a', 'city': 'a', 'zip_code': 7}, 'contract': {'hiring_date': 'a', 'job_title': 'a'}}}
    r = requests.get('http://127.0.0.1:5678/add_employee', 
        params=payload,
        headers={'Accept': 'application/json'})
    
    r2 = requests.post('http://127.0.0.1:5678/add_employee', 
        params=payload,
        headers={'Accept': 'application/json'})
    

def add_employee_empty() :
    
    r = requests.post('http://127.0.0.1:5678/add_employee', 
        headers={'Accept': 'application/json'})
    

    assert r.status_code == 400


def add_team_empty() :

    r = requests.post('http://127.0.0.1:5678/add_team', 
        headers={'Accept': 'application/json'})

    assert r.status_code == 400

def reset_database() :
    r = requests.post('http://127.0.0.1:5678/reset_db',
        headers={'Accept': 'application/json'})

    r2 = requests.get('http://127.0.0.1:5678/employees',
        headers={'Accept': 'application/json'})

    assert r.status_code == 200



#add_employee()
#add_employee_empty()
add_team_empty()
#reset_database()