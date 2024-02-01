import requests

def fetch_random_user():
    url = 'https://api.freeapi.app/api/v1/public/randomusers/user/random'
    response = requests.get(url)
    data = response.json()
    print(data)
    
    
def main():
    fetch_random_user()   
    
    
if __name__ == '__main__':
    main()     
    