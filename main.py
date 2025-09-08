import requests
import os
from utils.email import generate_mail_body, send_email
try:
    from dotenv import load_dotenv
    load_dotenv()
except ImportError:
    print("python-dotenv no está instalado, no se cargarán las variables de entorno, salvo que se usen en el .env.")

DOMAINS = os.getenv("DOMAINS", "").split("|")
TIMEOUT_REQUEST = int(os.getenv("TIMEOUT_REQUEST", 30))
RECEPTORES = os.getenv("RECEPTORES", "").split(";")

def check_health(domain):
    
    try:
        response = requests.get(domain, timeout=TIMEOUT_REQUEST)
        if response.status_code == 200:
            return True, f"{domain} está saludable."
        else:
            return False, f"{domain} retornó el código de estado {response.status_code}."
    except requests.RequestException as e:
        return False, f"{domain} es inalcanzable. Error: {e}"

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
        print("Todos los servicios están saludables.")
        
if __name__ == "__main__":
    main()
