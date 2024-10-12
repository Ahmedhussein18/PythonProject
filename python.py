import socket
import time

# Define the DNS name of the nginx service
NGINX_SERVICE_NAME = "nginx-service"
NGINX_NAMESPACE = "default"  # Replace with your nginx namespace if different
DNS_NAME = f"{NGINX_SERVICE_NAME}.{NGINX_NAMESPACE}.svc.cluster.local"

# Time interval (in seconds) between DNS resolution attempts
RESOLVE_INTERVAL = 10

def resolve_dns():
    try:
        # Resolve the DNS name to an IP address
        ip_addresses = socket.gethostbyname_ex(DNS_NAME)[2]
        print(f"Resolved {DNS_NAME} to IP addresses: {ip_addresses}")
    except socket.gaierror:
        print(f"Failed to resolve {DNS_NAME}. It might not be available.")
        
if __name__ == "__main__":
    while True:
        print("edit")
        resolve_dns()
        time.sleep(RESOLVE_INTERVAL)
