from prometheus_client import start_http_server, Gauge
import requests
import time
import argparse

# Define Arguments
parser = argparse.ArgumentParser(description='A simple HTTP connection tester written in Python.')
parser.add_argument("-u", "--url", help="A URL to test against", required=True)
args = parser.parse_args()

# Define Prometheus metrics
URL_STATUS = Gauge('url_status', 'Status of the URL (1=reachable, 0=unreachable)')
# Define parameters of URL Check
def check_url(url):
    try:
        response = requests.get(url)
        return 1 if response.status_code == 200 else 0
    except:
        return 0
# Define Updating Metrics
def update_metrics(url):
    status = check_url(url)
    URL_STATUS.set(status)

# Main function to update metrics
if __name__ == '__main__':
    url_to_check = str(args.url)
    start_http_server(8000)
    while True:
        update_metrics(url_to_check)
        time.sleep(60)
