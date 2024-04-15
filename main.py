from prometheus_client import start_http_server, Gauge
import requests
import time

# Define Prometheus metrics
URL_STATUS = Gauge('url_status', 'Status of the URL (1=reachable, 0=unreachable)')

def check_url(url):
    try:
        response = requests.get(url)
        return 1 if response.status_code == 200 else 0
    except:
        return 0

def update_metrics(url):
    status = check_url(url)
    URL_STATUS.set(status)

if __name__ == '__main__':
    # URL to check
    url_to_check = 'http://example.com'

    # Start the Prometheus metrics server
    start_http_server(8000)

    # Main loop to periodically update metrics
    while True:
        update_metrics(url_to_check)
        time.sleep(60)
