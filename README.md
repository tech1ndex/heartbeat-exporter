# heartbeat-exporter
A Simple Prometheus Exporter that checks the status of an HTTP Endpoint and reports it to Prometheus for Availability.

### Usage

Docker Example:

```
docker run -d -v /log:/log ghcr.io/tech1ndex/heartbeat-exporter:<tag> -u "https://example.com"
```

A `--url` will need to be passed to Docker run/compose, the script will accept as many as required.


##### Parameters:

   `-u [URL]`, `--url [URL]` - This is a required parameter, it is the URL to check and report it's heartbeat.

##### Architecture: 

Current available versions are:
  - amd64
  - arm64

They are version tagged accordingly and can be pulled using `version-arch` tag format.

```
docker pull ghcr.io/tech1ndex/heartbeat-exporter:<tag>
```