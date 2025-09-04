import requests
import os
from utils.email import generate_mail_body, send_email
try:
    from dotenv import load_dotenv
    load_dotenv()
except ImportError:
    print("python-dotenv not installed, proceeding without loading .env file")

DOMAINS = os.getenv("DOMAINS", "").split(";")
TIMEOUT = int(os.getenv("TIMEOUT", 10))
RECEPTORES = os.getenv("RECEPTORES", "").split(";")

def check_health(domain):
    
    try:
        response = requests.get(domain, timeout=TIMEOUT)
        if response.status_code == 200:
            return True, f"{domain} is healthy."
        else:
            return False, f"{domain} returned status code {response.status_code}."
    except requests.RequestException as e:
        return False, f"{domain} is unreachable. Error: {e}"
    
def main():
    results = []
    for domain in DOMAINS:
        is_healthy, message = check_health(domain)
        results.append((domain, is_healthy, message))

    unhealthy_services = [msg for domain, healthy, msg in results if not healthy]
    
    if unhealthy_services:
        email_body = generate_mail_body(unhealthy_services)
        subject = "Servicios caídos"
        for recipient in RECEPTORES:
            send_email(recipient, subject, email_body)
            
    else:
        print("All services are healthy.")
        
if __name__ == "__main__":
    main()
