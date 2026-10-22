---
url: https://docs.cloud.google.com/load-balancing/docs/metrics/
title: Load balancing metrics \u00a0|\u00a0 Cloud Load Balancing \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T12:29:23.827807+00:00
---

# Load balancing metrics  |  Cloud Load Balancing  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/load-balancing/docs/metrics/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Networking ](https://docs.cloud.google.com/docs/networking)
  * [ Load Balancing ](https://docs.cloud.google.com/load-balancing/docs)
  * [ Resources ](https://docs.cloud.google.com/load-balancing/docs/resources)



Send feedback 

#  Load balancing metrics Stay organized with collections  Save and categorize content based on your preferences. 

You can monitor the performance and health of your Google Cloud load-balanced applications and services using metrics provided by Cloud Monitoring. These metrics represent collections of measurements that help you maintain optimal operations. In Cloud Monitoring, each service or component under observation is called a _monitored resource_.

Use the following resources to find details about supported metric types, units used, and their metadata:

  * For a general explanation of the entries in the tables, see [Metric types](https://docs.cloud.google.com/monitoring/api/v3/kinds-and-types).

  * For information about the units used in the metric lists, see the [`unit` field](https://docs.cloud.google.com/monitoring/api/ref_v3/rest/v3/projects.metricDescriptors#MetricDescriptor.FIELDS.unit) in the `MetricDescriptor` reference.

  * For information about statements of the form “Sampled every _x_ seconds” and “After sampling, data is not visible for up to _y_ seconds”, see [Additional information: metadata](https://docs.cloud.google.com/monitoring/api/metrics#metadata).

  * For a set of complete, current lists of supported metric types, see [Metrics list](https://docs.cloud.google.com/monitoring/api/metrics).

  * For pricing information, see [Monitoring pricing](https://cloud.google.com/stackdriver/pricing#monitoring-costs).




The following table maps metric path prefixes to the load balancer types:

Metric path | Load balancer  
---|---  
`https/` | Global external Application Load Balancer  
  
Classic Application Load Balancer  
`https/external/regional` | Regional external Application Load Balancer  
`https/internal/` |  Cross-region internal Application Load Balancer  
  
Regional internal Application Load Balancer  
`l3/external/` | External passthrough Network Load Balancer  
`l3/internal/` | Internal passthrough Network Load Balancer  
`tcp_ssl_proxy/` | Classic proxy Network Load Balancer  
`l4_proxy/` |  Global external proxy Network Load Balancer  
  
Cross-region internal proxy Network Load Balancer  
  
Regional internal proxy Network Load Balancer  
  
Regional external proxy Network Load Balancer  
  
The "metric type" strings in this table must be prefixed with `loadbalancing.googleapis.com/`. That prefix has been omitted from the entries in the table. When querying a label, use the `metric.labels.` prefix; for example, `metric.labels.LABEL="VALUE"`. 

Metric type Launch stage  _(Resource hierarchy levels)_  
Display name  
---  
Kind, Type, Unit  
Monitored resources | _Description_  
Labels  
`application_lb/backend_latencies` BETA ** _(project)_**   
Backend latencies   
`DELTA`, `DISTRIBUTION`, `ms`   
**[gce_backend_service](https://docs.cloud.google.com/monitoring/api/resources#tag_gce_backend_service)** |  _A distribution of the latency calculated from when the request was sent by the Application Load Balancer proxy to the backend until the proxy received from the backend the last byte of response. For Service Extensions, this value represents the sum of latencies of each ProcessingRequest/ProcessingResponse pair between the load balancer and the extension backend._   
`protocol`: Protocol used by the client: 'HTTP/1.0', 'HTTP/1.1', 'HTTP/2.0', 'QUIC/HTTP/2.0' or 'UNKNOWN'.   
`response_code`: (INT64) HTTP response code.   
`response_code_class`: (INT64) HTTP response code class: 200, 300, 400, 500 or 0 for none.   
`cache_result`: Cache result for serving HTTP request by proxy: 'HIT', 'MISS', 'DISABLED' or 'UNKNOWN'.   
`matcher_type`: The type of rule matched for the request: 'PATH_MATCHER' or 'DEFAULT_MATCH'. 'DEFAULT_MATCH' indicates that the default route rule or action was matched to the request.   
`matcher_name`: Matched rule for the request. Label value is based on matcher_type. PATH_MATCHER type will be the name of the path matcher. DEFAULT_MATCH types will be empty.   
`matched_path`: The prefix, exact, regex, or template URL path matcher that matched the request. 'UNMATCHED' for the sink default rule.   
`load_balancing_scheme`: Load balancing scheme used by the Application Load Balancer: 'EXTERNAL_MANAGED' or 'INTERNAL_MANAGED'.   
`client_country`: Country of the client where the traffic originated from, such as 'United States' or 'Germany'.   
`proxy_continent`: Continent of the proxy where the traffic originated from, such as 'North America' or 'Europe'.   
`application_lb/backend_request_bytes_count` BETA ** _(project)_**   
Backend request bytes count per application load balancer   
`DELTA`, `INT64`, `By`   
**[gce_backend_service](https://docs.cloud.google.com/monitoring/api/resources#tag_gce_backend_service)** |  _The number of bytes sent as requests from the application load balancer to backends. For Service Extensions, this value represents the total number of bytes sent from the load balancer to the extension backend._   
`protocol`: Protocol used by the client: 'HTTP/1.0', 'HTTP/1.1', 'HTTP/2.0', 'QUIC/HTTP/2.0' or 'UNKNOWN'.   
`response_code`: (INT64) HTTP response code.   
`response_code_class`: (INT64) HTTP response code class: 200, 300, 400, 500 or 0 for none.   
`cache_result`: Cache result for serving HTTP request by proxy: 'HIT', 'MISS', 'DISABLED' or 'UNKNOWN'.   
`matcher_type`: The type of rule matched for the request: 'PATH_MATCHER' or 'DEFAULT_MATCH'. 'DEFAULT_MATCH' indicates that the default route rule or action was matched to the request.   
`matcher_name`: Matched rule for the request. Label value is based on matcher_type. PATH_MATCHER type will be the name of the path matcher. DEFAULT_MATCH types will be empty.   
`matched_path`: The prefix, exact, regex, or template URL path matcher that matched the request. 'UNMATCHED' for the sink default rule.   
`load_balancing_scheme`: Load balancing scheme used by the Application Load Balancer: 'EXTERNAL_MANAGED' or 'INTERNAL_MANAGED'.   
`client_country`: Country of the client where the traffic originated from, such as 'United States' or 'Germany'.   
`proxy_continent`: Continent of the proxy where the traffic originated from, such as 'North America' or 'Europe'.   
`application_lb/backend_request_count` BETA ** _(project)_**   
Backend request count per application load balancer   
`DELTA`, `INT64`, `1`   
**[gce_backend_service](https://docs.cloud.google.com/monitoring/api/resources#tag_gce_backend_service)** |  _The number of requests served by backends of the application load balancer. For Service Extensions, this value represents the number of gRPC streams between the load balancer and the extension backend._   
`protocol`: Protocol used by the client: 'HTTP/1.0', 'HTTP/1.1', 'HTTP/2.0', 'QUIC/HTTP/2.0' or 'UNKNOWN'.   
`response_code`: (INT64) HTTP response code.   
`response_code_class`: (INT64) HTTP response code class: 200, 300, 400, 500 or 0 for none.   
`cache_result`: Cache result for serving HTTP request by proxy: 'HIT', 'MISS', 'DISABLED' or 'UNKNOWN'.   
`matcher_type`: The type of rule matched for the request: 'PATH_MATCHER' or 'DEFAULT_MATCH'. 'DEFAULT_MATCH' indicates that the default route rule or action was matched to the request.   
`matcher_name`: Matched rule for the request. Label value is based on matcher_type. PATH_MATCHER type will be the name of the path matcher. DEFAULT_MATCH types will be empty.   
`matched_path`: The prefix, exact, regex, or template URL path matcher that matched the request. 'UNMATCHED' for the sink default rule.   
`load_balancing_scheme`: Load balancing scheme used by the Application Load Balancer: 'EXTERNAL_MANAGED' or 'INTERNAL_MANAGED'.   
`client_country`: Country of the client where the traffic originated from, such as 'United States' or 'Germany'.   
`proxy_continent`: Continent of the proxy where the traffic originated from, such as 'North America' or 'Europe'.   
`application_lb/backend_response_bytes_count` BETA ** _(project)_**   
Backend response bytes count per application load balancer   
`DELTA`, `INT64`, `By`   
**[gce_backend_service](https://docs.cloud.google.com/monitoring/api/resources#tag_gce_backend_service)** |  _The number of bytes sent as response from backends to the application load balancer. For Service Extensions, this value represents the total number of bytes received by the load balancer from the extension backend._   
`protocol`: Protocol used by the client: 'HTTP/1.0', 'HTTP/1.1', 'HTTP/2.0', 'QUIC/HTTP/2.0' or 'UNKNOWN'.   
`response_code`: (INT64) HTTP response code.   
`response_code_class`: (INT64) HTTP response code class: 200, 300, 400, 500 or 0 for none.   
`cache_result`: Cache result for serving HTTP request by proxy: 'HIT', 'MISS', 'DISABLED' or 'UNKNOWN'.   
`matcher_type`: The type of rule matched for the request: 'PATH_MATCHER' or 'DEFAULT_MATCH'. 'DEFAULT_MATCH' indicates that the default route rule or action was matched to the request.   
`matcher_name`: Matched rule for the request. Label value is based on matcher_type. PATH_MATCHER type will be the name of the path matcher. DEFAULT_MATCH types will be empty.   
`matched_path`: The prefix, exact, regex, or template URL path matcher that matched the request. 'UNMATCHED' for the sink default rule.   
`load_balancing_scheme`: Load balancing scheme used by the Application Load Balancer: 'EXTERNAL_MANAGED' or 'INTERNAL_MANAGED'.   
`client_country`: Country of the client where the traffic originated from, such as 'United States' or 'Germany'.   
`proxy_continent`: Continent of the proxy where the traffic originated from, such as 'North America' or 'Europe'.   
`application_lb/request_bytes_count` BETA ** _(project)_**   
Request bytes   
`DELTA`, `INT64`, `By`   
**[gce_forwarding_rule](https://docs.cloud.google.com/monitoring/api/resources#tag_gce_forwarding_rule)** |  _The number of request bytes received by the application load balancer. For Service Extensions, this value represents the total number of bytes sent from the load balancer to the extension backend._   
`protocol`: Protocol used by the client: 'HTTP/1.0', 'HTTP/1.1', 'HTTP/2.0', 'QUIC/HTTP/2.0' or 'UNKNOWN'.   
`response_code`: (INT64) HTTP response code.   
`response_code_class`: (INT64) HTTP response code class: 200, 300, 400, 500 or 0 for none.   
`cache_result`: Cache result for serving HTTP request by proxy: 'HIT', 'MISS', 'DISABLED' or 'UNKNOWN'.   
`matcher_type`: The type of rule matched for the request: 'PATH_MATCHER' or 'DEFAULT_MATCH'. 'DEFAULT_MATCH' indicates that the default route rule or action was matched to the request.   
`matcher_name`: Matched rule for the request. Label value is based on matcher_type. PATH_MATCHER type will be the name of the path matcher. DEFAULT_MATCH types will be empty.   
`matched_path`: The prefix, exact, regex, or template URL path matcher that matched the request. 'UNMATCHED' for the sink default rule.   
`load_balancing_scheme`: Load balancing scheme used by the Application Load Balancer: 'EXTERNAL_MANAGED' or 'INTERNAL_MANAGED'.   
`client_country`: Country of the client where the traffic originated from, such as 'United States' or 'Germany'.   
`proxy_continent`: Continent of the proxy where the traffic originated from, such as 'North America' or 'Europe'.   
`application_lb/request_count` BETA ** _(project)_**   
Request count   
`DELTA`, `INT64`, `1`   
**[gce_forwarding_rule](https://docs.cloud.google.com/monitoring/api/resources#tag_gce_forwarding_rule)** |  _The number of requests served by the application load balancer._   
`protocol`: Protocol used by the client: 'HTTP/1.0', 'HTTP/1.1', 'HTTP/2.0', 'QUIC/HTTP/2.0' or 'UNKNOWN'.   
`response_code`: (INT64) HTTP response code.   
`response_code_class`: (INT64) HTTP response code class: 200, 300, 400, 500 or 0 for none.   
`cache_result`: Cache result for serving HTTP request by proxy: 'HIT', 'MISS', 'DISABLED' or 'UNKNOWN'.   
`matcher_type`: The type of rule matched for the request: 'PATH_MATCHER' or 'DEFAULT_MATCH'. 'DEFAULT_MATCH' indicates that the default route rule or action was matched to the request.   
`matcher_name`: Matched rule for the request. Label value is based on matcher_type. PATH_MATCHER type will be the name of the path matcher. DEFAULT_MATCH types will be empty.   
`matched_path`: The prefix, exact, regex, or template URL path matcher that matched the request. 'UNMATCHED' for the sink default rule.   
`load_balancing_scheme`: Load balancing scheme used by the Application Load Balancer: 'EXTERNAL_MANAGED' or 'INTERNAL_MANAGED'.   
`client_country`: Country of the client where the traffic originated from, such as 'United States' or 'Germany'.   
`proxy_continent`: Continent of the proxy where the traffic originated from, such as 'North America' or 'Europe'.   
`application_lb/response_bytes_count` BETA ** _(project)_**   
Response bytes   
`DELTA`, `INT64`, `By`   
**[gce_forwarding_rule](https://docs.cloud.google.com/monitoring/api/resources#tag_gce_forwarding_rule)** |  _The number of bytes sent as responses from the application load balancer to clients._   
`protocol`: Protocol used by the client: 'HTTP/1.0', 'HTTP/1.1', 'HTTP/2.0', 'QUIC/HTTP/2.0' or 'UNKNOWN'.   
`response_code`: (INT64) HTTP response code.   
`response_code_class`: (INT64) HTTP response code class: 200, 300, 400, 500 or 0 for none.   
`cache_result`: Cache result for serving HTTP request by proxy: 'HIT', 'MISS', 'DISABLED' or 'UNKNOWN'.   
`matcher_type`: The type of rule matched for the request: 'PATH_MATCHER' or 'DEFAULT_MATCH'. 'DEFAULT_MATCH' indicates that the default route rule or action was matched to the request.   
`matcher_name`: Matched rule for the request. Label value is based on matcher_type. PATH_MATCHER type will be the name of the path matcher. DEFAULT_MATCH types will be empty.   
`matched_path`: The prefix, exact, regex, or template URL path matcher that matched the request. 'UNMATCHED' for the sink default rule.   
`load_balancing_scheme`: Load balancing scheme used by the Application Load Balancer: 'EXTERNAL_MANAGED' or 'INTERNAL_MANAGED'.   
`client_country`: Country of the client where the traffic originated from, such as 'United States' or 'Germany'.   
`proxy_continent`: Continent of the proxy where the traffic originated from, such as 'North America' or 'Europe'.   
`application_lb/total_latencies` BETA ** _(project)_**   
Total latencies   
`DELTA`, `DISTRIBUTION`, `ms`   
**[gce_forwarding_rule](https://docs.cloud.google.com/monitoring/api/resources#tag_gce_forwarding_rule)** |  _A distribution of the latency calculated from when the request was received by the proxy until the proxy got ACK from client on last response byte._   
`protocol`: Protocol used by the client: 'HTTP/1.0', 'HTTP/1.1', 'HTTP/2.0', 'QUIC/HTTP/2.0' or 'UNKNOWN'.   
`response_code`: (INT64) HTTP response code.   
`response_code_class`: (INT64) HTTP response code class: 200, 300, 400, 500 or 0 for none.   
`cache_result`: Cache result for serving HTTP request by proxy: 'HIT', 'MISS', 'DISABLED' or 'UNKNOWN'.   
`matcher_type`: The type of rule matched for the request: 'PATH_MATCHER' or 'DEFAULT_MATCH'. 'DEFAULT_MATCH' indicates that the default route rule or action was matched to the request.   
`matcher_name`: Matched rule for the request. Label value is based on matcher_type. PATH_MATCHER type will be the name of the path matcher. DEFAULT_MATCH types will be empty.   
`matched_path`: The prefix, exact, regex, or template URL path matcher that matched the request. 'UNMATCHED' when a default (empty) path was matched.   
`load_balancing_scheme`: Load balancing scheme used by the Application Load Balancer: 'EXTERNAL_MANAGED' or 'INTERNAL_MANAGED'.   
`client_country`: Country of the client where the traffic originated from, such as 'United States' or 'Germany'.   
`proxy_continent`: Continent of the proxy where the traffic originated from, such as 'North America' or 'Europe'.   
`https/backend_latencies` GA ** _(project)_**   
Backend latency   
`DELTA`, `DISTRIBUTION`, `ms`   
**[https_lb_rule](https://docs.cloud.google.com/monitoring/api/resources#tag_https_lb_rule)** |  _A distribution of the latency calculated from when the request was sent by the proxy to the backend until the proxy received from the backend the last byte of response. For Service Extensions, this value represents the sum of latencies of each ProcessingRequest/ProcessingResponse pair between the load balancer and the extension backend. Sampled every 60 seconds. After sampling, data is not visible for up to 210 seconds._   
`protocol`: Protocol used by the client, one of [HTTP/1.0, HTTP/1.1, HTTP/2.0, SPDY, UNKNOWN].   
`response_code`: (INT64) HTTP response code.   
`load_balancing_scheme`: Load balancing scheme: EXTERNAL or EXTERNAL_MANAGED.   
`response_code_class`: (INT64) HTTP response code class: 200, 300, 400, 500 or 0 for none.   
`proxy_continent`: Continent of the HTTP proxy that handled the hit: 'America', 'Europe' or 'Asia'.   
`cache_result`: Cache result for serving HTTP request by proxy: 'HIT', 'MISS', 'DISABLED' or 'UNKNOWN'.   
`client_country`: Country of the client that issued the HTTP request (for example, 'United States', 'Germany').   
`https/backend_request_bytes_count` GA ** _(project)_**   
Backend Request Bytes   
`DELTA`, `INT64`, `By`   
**[https_lb_rule](https://docs.cloud.google.com/monitoring/api/resources#tag_https_lb_rule)** |  _The number of bytes sent as requests from external HTTP(S) load balancer to backends. For Service Extensions, this value represents the total number of bytes sent from the load balancer to the extension backend. Sampled every 60 seconds. After sampling, data is not visible for up to 210 seconds._   
`response_code`: (INT64) HTTP backend response code.   
`load_balancing_scheme`: Load balancing scheme: EXTERNAL or EXTERNAL_MANAGED.   
`response_code_class`: (INT64) HTTP backend response code class: 200, 300, 400, 500 or 0 for none.   
`proxy_continent`: Continent of the HTTP proxy that handled the request: 'America', 'Europe' or 'Asia'.   
`cache_result`: Cache result for serving the HTTP request by backends (cache hits are abstracted as backend requests): 'HIT', 'MISS', 'DISABLED' or 'UNKNOWN'.   
`https/backend_request_count` GA ** _(project)_**   
Backend Request Count   
`DELTA`, `INT64`, `1`   
**[https_lb_rule](https://docs.cloud.google.com/monitoring/api/resources#tag_https_lb_rule)** |  _The number of requests served by backends of external HTTP(S) load balancer. For Service Extensions, this value represents the total number of gRPC streams between the load balancer to the extension backend. Sampled every 60 seconds. After sampling, data is not visible for up to 210 seconds._   
`response_code`: (INT64) HTTP backend response code.   
`load_balancing_scheme`: Load balancing scheme: EXTERNAL or EXTERNAL_MANAGED.   
`response_code_class`: (INT64) HTTP backend response code class: 200, 300, 400, 500 or 0 for none.   
`proxy_continent`: Continent of the HTTP proxy that handled the request: 'America', 'Europe' or 'Asia'.   
`cache_result`: Cache result for serving the HTTP request by backends (cache hits are abstracted as backend requests): 'HIT', 'MISS', 'DISABLED' or 'UNKNOWN'.   
`https/backend_response_bytes_count` GA ** _(project)_**   
Backend Response Bytes   
`DELTA`, `INT64`, `By`   
**[https_lb_rule](https://docs.cloud.google.com/monitoring/api/resources#tag_https_lb_rule)** |  _The number of bytes sent as responses from backends (or cache) to external HTTP(S) load balancer. For Service Extensions, this value represents the total number of bytes received by the load balancer from the extension backend. Sampled every 60 seconds. After sampling, data is not visible for up to 210 seconds._   
`response_code`: (INT64) HTTP backend response code.   
`load_balancing_scheme`: Load balancing scheme: EXTERNAL or EXTERNAL_MANAGED.   
`response_code_class`: (INT64) HTTP backend response code class: 200, 300, 400, 500 or 0 for none.   
`proxy_continent`: Continent of the HTTP proxy that handled the request: 'America', 'Europe' or 'Asia'.   
`cache_result`: Cache result for serving the HTTP request by backends (cache hits are abstracted as backend requests): 'HIT', 'MISS', 'DISABLED' or 'UNKNOWN'.   
`https/external/regional/backend_latencies` GA ** _(project)_**   
Backend latencies   
`DELTA`, `DISTRIBUTION`, `ms`   
**[http_external_regional_lb_rule](https://docs.cloud.google.com/monitoring/api/resources#tag_http_external_regional_lb_rule)** |  _A distribution of the latency calculated from when the request was sent by the proxy to the backend until the proxy received from the backend the last byte of response. For Service Extensions, this value represents the sum of latencies of each ProcessingRequest/ProcessingResponse pair between the load balancer and the extension backend. Sampled every 60 seconds. After sampling, data is not visible for up to 210 seconds._   
`protocol`: Protocol used by the client: 'HTTP/1.0', 'HTTP/1.1', 'HTTP/2.0', 'QUIC/HTTP/2.0' or 'UNKNOWN'.   
`response_code`: (INT64) HTTP response code.   
`response_code_class`: (INT64) HTTP response code class: 200, 300, 400, 500 or 0 for none.   
`cache_result`: Cache result for serving HTTP request by proxy: 'HIT', 'MISS', 'DISABLED' or 'UNKNOWN'.   
`client_country`: Country of the client that issued the HTTP request (e.g. 'United States', 'Germany').   
`https/external/regional/backend_request_bytes_count` GA ** _(project)_**   
Backend request bytes count per external regional https load balancer   
`DELTA`, `INT64`, `By`   
**[http_external_regional_lb_rule](https://docs.cloud.google.com/monitoring/api/resources#tag_http_external_regional_lb_rule)** |  _The number of bytes sent as requests from Regional External HTTP(S) load balancer to backends. For Service Extensions, this value represents the total number of bytes sent from the load balancer to the extension backend. Sampled every 60 seconds. After sampling, data is not visible for up to 90 seconds._   
`response_code`: (INT64) HTTP response code.   
`response_code_class`: (INT64) HTTP response code class: 200, 300, 400, 500 or 0 for none.   
`https/external/regional/backend_request_count` GA ** _(project)_**   
Backend request count per external regional https load balancer   
`DELTA`, `INT64`, `1`   
**[http_external_regional_lb_rule](https://docs.cloud.google.com/monitoring/api/resources#tag_http_external_regional_lb_rule)** |  _The number of requests served by backends of Regional External HTTP(S) load balancer. For Service Extensions, this value represents the total number of gRPC streams between the load balancer to the extension backend. Sampled every 60 seconds. After sampling, data is not visible for up to 90 seconds._   
`response_code`: (INT64) HTTP response code.   
`response_code_class`: (INT64) HTTP response code class: 200, 300, 400, 500 or 0 for none.   
`https/external/regional/backend_response_bytes_count` GA ** _(project)_**   
Backend response bytes count per external regional https load balancer   
`DELTA`, `INT64`, `By`   
**[http_external_regional_lb_rule](https://docs.cloud.google.com/monitoring/api/resources#tag_http_external_regional_lb_rule)** |  _The number of bytes sent as response from backends to Regional External HTTP(S) load balancer. For Service Extensions, this value represents the total number of bytes received by the load balancer from the extension backend. Sampled every 60 seconds. After sampling, data is not visible for up to 90 seconds._   
`response_code`: (INT64) HTTP response code.   
`response_code_class`: (INT64) HTTP response code class: 200, 300, 400, 500 or 0 for none.   
`https/external/regional/request_bytes_count` GA ** _(project)_**   
Request bytes   
`DELTA`, `INT64`, `By`   
**[http_external_regional_lb_rule](https://docs.cloud.google.com/monitoring/api/resources#tag_http_external_regional_lb_rule)** |  _The number of bytes sent as requests from clients to HTTP/S load balancer. Sampled every 60 seconds. After sampling, data is not visible for up to 90 seconds._   
`protocol`: Protocol used by the client: 'HTTP/1.0', 'HTTP/1.1', 'HTTP/2.0', 'QUIC/HTTP/2.0' or 'UNKNOWN'.   
`response_code`: (INT64) HTTP response code.   
`response_code_class`: (INT64) HTTP response code class: 200, 300, 400, 500 or 0 for none.   
`cache_result`: Cache result for serving HTTP request by proxy: 'HIT', 'MISS', 'DISABLED' or 'UNKNOWN'.   
`client_country`: Country of the client that issued the HTTP request (e.g. 'United States', 'Germany').   
`https/external/regional/request_count` GA ** _(project)_**   
Request count   
`DELTA`, `INT64`, `1`   
**[http_external_regional_lb_rule](https://docs.cloud.google.com/monitoring/api/resources#tag_http_external_regional_lb_rule)** |  _The number of requests served by HTTP/S load balancer. Sampled every 60 seconds. After sampling, data is not visible for up to 90 seconds._   
`protocol`: Protocol used by the client: 'HTTP/1.0', 'HTTP/1.1', 'HTTP/2.0', 'QUIC/HTTP/2.0' or 'UNKNOWN'.   
`response_code`: (INT64) HTTP response code.   
`response_code_class`: (INT64) HTTP response code class: 200, 300, 400, 500 or 0 for none.   
`cache_result`: Cache result for serving HTTP request by proxy: 'HIT', 'MISS', 'DISABLED' or 'UNKNOWN'.   
`client_country`: Country of the client that issued the HTTP request (e.g. 'United States', 'Germany').   
`https/external/regional/response_bytes_count` GA ** _(project)_**   
Response bytes   
`DELTA`, `INT64`, `By`   
**[http_external_regional_lb_rule](https://docs.cloud.google.com/monitoring/api/resources#tag_http_external_regional_lb_rule)** |  _The number of bytes sent as responses from HTTP/S load balancer to clients. Sampled every 60 seconds. After sampling, data is not visible for up to 90 seconds._   
`protocol`: Protocol used by the client: 'HTTP/1.0', 'HTTP/1.1', 'HTTP/2.0', 'QUIC/HTTP/2.0' or 'UNKNOWN'.   
`response_code`: (INT64) HTTP response code.   
`response_code_class`: (INT64) HTTP response code class: 200, 300, 400, 500 or 0 for none.   
`cache_result`: Cache result for serving HTTP request by proxy: 'HIT', 'MISS', 'DISABLED' or 'UNKNOWN'.   
`client_country`: Country of the client that issued the HTTP request (e.g. 'United States', 'Germany').   
`https/external/regional/total_latencies` GA ** _(project)_**   
Total latencies   
`DELTA`, `DISTRIBUTION`, `ms`   
**[http_external_regional_lb_rule](https://docs.cloud.google.com/monitoring/api/resources#tag_http_external_regional_lb_rule)** |  _A distribution of the latency calculated from when the request was received by the proxy until the proxy got ACK from client on last response byte. Sampled every 60 seconds. After sampling, data is not visible for up to 90 seconds._   
`protocol`: Protocol used by the client: 'HTTP/1.0', 'HTTP/1.1', 'HTTP/2.0', 'QUIC/HTTP/2.0' or 'UNKNOWN'.   
`response_code`: (INT64) HTTP response code.   
`response_code_class`: (INT64) HTTP response code class: 200, 300, 400, 500 or 0 for none.   
`cache_result`: Cache result for serving HTTP request by proxy: 'HIT', 'MISS', 'DISABLED' or 'UNKNOWN'.   
`client_country`: Country of the client that issued the HTTP request (e.g. 'United States', 'Germany').   
`https/frontend_tcp_rtt` GA ** _(project)_**   
Frontend RTT   
`DELTA`, `DISTRIBUTION`, `ms`   
**[https_lb_rule](https://docs.cloud.google.com/monitoring/api/resources#tag_https_lb_rule)** |  _A distribution of the RTT measured for each connection between client and proxy. Sampled every 60 seconds. After sampling, data is not visible for up to 210 seconds._   
`load_balancing_scheme`: Load balancing scheme: EXTERNAL or EXTERNAL_MANAGED.   
`proxy_continent`: Continent of the HTTP proxy that handled the hit: 'America', 'Europe' or 'Asia'.   
`client_country`: Country of the client that issued the HTTP request (for example, 'United States', 'Germany').   
`https/internal/backend_latencies` GA ** _(project)_**   
Backend latencies   
`DELTA`, `DISTRIBUTION`, `ms`   
**[internal_http_lb_rule](https://docs.cloud.google.com/monitoring/api/resources#tag_internal_http_lb_rule)** |  _A distribution of the latency calculated from when the request was sent by the internal Application Load Balancer proxy to the backend until the proxy received from the backend the last byte of response. For Service Extensions, this value represents the sum of latencies of each ProcessingRequest/ProcessingResponse pair between the load balancer and the extension backend. Sampled every 60 seconds. After sampling, data is not visible for up to 90 seconds._   
`protocol`: Protocol used by the client: 'HTTP/1.0', 'HTTP/1.1', 'HTTP/2.0', 'SPDY' or 'UNKNOWN'.   
`response_code`: (INT64) HTTP response code.   
`response_code_class`: (INT64) HTTP response code class: 200, 300, 400, 500 or 0 for none.   
`cache_result`: Cache result for serving HTTP request by proxy: 'HIT', 'MISS', 'DISABLED' or 'UNKNOWN'.   
`https/internal/backend_request_bytes_count` GA ** _(project)_**   
Backend request bytes count per internal https load balancer   
`DELTA`, `INT64`, `By`   
**[internal_http_lb_rule](https://docs.cloud.google.com/monitoring/api/resources#tag_internal_http_lb_rule)** |  _The number of bytes sent as requests from Internal HTTP(S) load balancer to backends. For Service Extensions, this value represents the total number of bytes sent from the load balancer to the extension backend. Sampled every 60 seconds. After sampling, data is not visible for up to 90 seconds._   
`response_code`: (INT64) HTTP response code.   
`response_code_class`: (INT64) HTTP response code class: 200, 300, 400, 500 or 0 for none.   
`https/internal/backend_request_count` GA ** _(project)_**   
Backend request count per internal https load balancer   
`DELTA`, `INT64`, `1`   
**[internal_http_lb_rule](https://docs.cloud.google.com/monitoring/api/resources#tag_internal_http_lb_rule)** |  _The number of requests served by backends of Internal HTTP(S) load balancer. For Service Extensions, this value represents the number of gRPC streams between the load balancer and the extension backend. Sampled every 60 seconds. After sampling, data is not visible for up to 90 seconds._   
`response_code`: (INT64) HTTP response code.   
`response_code_class`: (INT64) HTTP response code class: 200, 300, 400, 500 or 0 for none.   
`https/internal/backend_response_bytes_count` GA ** _(project)_**   
Backend response bytes count per internal https load balancer   
`DELTA`, `INT64`, `By`   
**[internal_http_lb_rule](https://docs.cloud.google.com/monitoring/api/resources#tag_internal_http_lb_rule)** |  _The number of bytes sent as response from backends to Internal HTTP(S) load balancer. For Service Extensions, this value represents the total number of bytes received by the load balancer from the extension backend. Sampled every 60 seconds. After sampling, data is not visible for up to 90 seconds._   
`response_code`: (INT64) HTTP response code.   
`response_code_class`: (INT64) HTTP response code class: 200, 300, 400, 500 or 0 for none.   
`https/internal/request_bytes_count` GA ** _(project)_**   
Request bytes   
`DELTA`, `INT64`, `By`   
**[internal_http_lb_rule](https://docs.cloud.google.com/monitoring/api/resources#tag_internal_http_lb_rule)** |  _The number of bytes sent as requests from clients to internal Application Load Balancer. Sampled every 60 seconds. After sampling, data is not visible for up to 90 seconds._   
`protocol`: Protocol used by the client: 'HTTP/1.0', 'HTTP/1.1', 'HTTP/2.0', 'SPDY' or 'UNKNOWN'.   
`response_code`: (INT64) HTTP response code.   
`response_code_class`: (INT64) HTTP response code class: 200, 300, 400, 500 or 0 for none.   
`cache_result`: Cache result for serving HTTP request by proxy: 'HIT', 'MISS', 'DISABLED' or 'UNKNOWN'.   
`https/internal/request_count` GA ** _(project)_**   
Request count   
`DELTA`, `INT64`, `1`   
**[internal_http_lb_rule](https://docs.cloud.google.com/monitoring/api/resources#tag_internal_http_lb_rule)** |  _The number of requests served by internal Application Load Balancer. Sampled every 60 seconds. After sampling, data is not visible for up to 90 seconds._   
`protocol`: Protocol used by the client: 'HTTP/1.0', 'HTTP/1.1', 'HTTP/2.0', 'QUIC/HTTP/2.0' or 'UNKNOWN'.   
`response_code`: (INT64) HTTP response code.   
`response_code_class`: (INT64) HTTP response code class: 200, 300, 400, 500 or 0 for none.   
`cache_result`: Cache result for serving HTTP request by proxy: 'HIT', 'MISS', 'DISABLED' or 'UNKNOWN'.   
`https/internal/response_bytes_count` GA ** _(project)_**   
Response bytes   
`DELTA`, `INT64`, `By`   
**[internal_http_lb_rule](https://docs.cloud.google.com/monitoring/api/resources#tag_internal_http_lb_rule)** |  _The number of bytes sent as responses from internal Application Load Balancer to clients. Sampled every 60 seconds. After sampling, data is not visible for up to 90 seconds._   
`protocol`: Protocol used by the client: 'HTTP/1.0', 'HTTP/1.1', 'HTTP/2.0', 'SPDY' or 'UNKNOWN'.   
`response_code`: (INT64) HTTP response code.   
`response_code_class`: (INT64) HTTP response code class: 200, 300, 400, 500 or 0 for none.   
`cache_result`: Cache result for serving HTTP request by proxy: 'HIT', 'MISS', 'DISABLED' or 'UNKNOWN'.   
`https/internal/total_latencies` GA ** _(project)_**   
Total latencies   
`DELTA`, `DISTRIBUTION`, `ms`   
**[internal_http_lb_rule](https://docs.cloud.google.com/monitoring/api/resources#tag_internal_http_lb_rule)** |  _A distribution of the latency calculated from when the request was received by the internal Application Load Balancer proxy until the proxy got ACK from client on last response byte. Sampled every 60 seconds. After sampling, data is not visible for up to 90 seconds._   
`protocol`: Protocol used by the client: 'HTTP/1.0', 'HTTP/1.1', 'HTTP/2.0', 'SPDY' or 'UNKNOWN'.   
`response_code`: (INT64) HTTP response code.   
`response_code_class`: (INT64) HTTP response code class: 200, 300, 400, 500 or 0 for none.   
`cache_result`: Cache result for serving HTTP request by proxy: 'HIT', 'MISS', 'DISABLED' or 'UNKNOWN'.   
`https/request_bytes_count` GA ** _(project)_**   
Request bytes   
`DELTA`, `INT64`, `By`   
**[https_lb_rule](https://docs.cloud.google.com/monitoring/api/resources#tag_https_lb_rule)** |  _The number of bytes sent as requests from clients to external HTTP(S) load balancer. Sampled every 60 seconds. After sampling, data is not visible for up to 210 seconds._   
`protocol`: Protocol used by the client, one of [HTTP/1.0, HTTP/1.1, HTTP/2.0, SPDY, UNKNOWN].   
`response_code`: (INT64) HTTP response code.   
`load_balancing_scheme`: Load balancing scheme: EXTERNAL or EXTERNAL_MANAGED.   
`response_code_class`: (INT64) HTTP response code class: 200, 300, 400, 500 or 0 for none.   
`proxy_continent`: Continent of the HTTP proxy that handled the hit: 'America', 'Europe' or 'Asia'.   
`cache_result`: Cache result for serving HTTP request by proxy: 'HIT', 'MISS', 'DISABLED', 'PARTIAL_HIT' (for a request served partially from cache and partially from backend) or 'UNKNOWN'.   
`client_country`: Country of the client that issued the HTTP request (for example, 'United States', 'Germany').   
`https/request_count` GA ** _(project)_**   
Request count   
`DELTA`, `INT64`, `1`   
**[https_lb_rule](https://docs.cloud.google.com/monitoring/api/resources#tag_https_lb_rule)** |  _The number of requests served by external HTTP(S) load balancer. Sampled every 60 seconds. After sampling, data is not visible for up to 210 seconds._   
`protocol`: Protocol used by the client, one of [HTTP/1.0, HTTP/1.1, HTTP/2.0, QUIC/HTTP/2.0, UNKNOWN].   
`response_code`: (INT64) HTTP response code.   
`load_balancing_scheme`: Load balancing scheme: EXTERNAL or EXTERNAL_MANAGED.   
`response_code_class`: (INT64) HTTP response code class: 200, 300, 400, 500 or 0 for none.   
`proxy_continent`: Continent of the HTTP proxy that handled the hit: 'America', 'Europe' or 'Asia'.   
`cache_result`: Cache result for serving HTTP request by proxy: 'HIT', 'MISS', 'DISABLED', 'PARTIAL_HIT' (for a request served partially from cache and partially from backend) or 'UNKNOWN'.   
`client_country`: Country of the client that issued the HTTP request (for example, 'United States', 'Germany').   
`https/response_bytes_count` GA ** _(project)_**   
Response bytes   
`DELTA`, `INT64`, `By`   
**[https_lb_rule](https://docs.cloud.google.com/monitoring/api/resources#tag_https_lb_rule)** |  _The number of bytes sent as responses from external HTTP(S) load balancer to clients. Sampled every 60 seconds. After sampling, data is not visible for up to 210 seconds._   
`protocol`: Protocol used by the client, one of [HTTP/1.0, HTTP/1.1, HTTP/2.0, SPDY, UNKNOWN].   
`response_code`: (INT64) HTTP response code.   
`load_balancing_scheme`: Load balancing scheme: EXTERNAL or EXTERNAL_MANAGED.   
`response_code_class`: (INT64) HTTP response code class: 200, 300, 400, 500 or 0 for none.   
`proxy_continent`: Continent of the HTTP proxy that handled the hit: 'America', 'Europe' or 'Asia'.   
`cache_result`: Cache result for serving HTTP request by proxy: 'HIT', 'MISS', 'DISABLED', 'PARTIAL_HIT' (for a request served partially from cache and partially from backend) or 'UNKNOWN'.   
`client_country`: Country of the client that issued the HTTP request (for example, 'United States', 'Germany').   
`https/total_latencies` GA ** _(project)_**   
Total latency   
`DELTA`, `DISTRIBUTION`, `ms`   
**[https_lb_rule](https://docs.cloud.google.com/monitoring/api/resources#tag_https_lb_rule)** |  _A distribution of the latency calculated from when the request was received by the external HTTP(S) load balancer proxy until the proxy got ACK from client on last response byte. Sampled every 60 seconds. After sampling, data is not visible for up to 210 seconds._   
`protocol`: Protocol used by the client, one of [HTTP/1.0, HTTP/1.1, HTTP/2.0, SPDY, UNKNOWN].   
`response_code`: (INT64) HTTP response code.   
`load_balancing_scheme`: Load balancing scheme: EXTERNAL or EXTERNAL_MANAGED.   
`response_code_class`: (INT64) HTTP response code class: 200, 300, 400, 500 or 0 for none.   
`proxy_continent`: Continent of the HTTP proxy that handled the hit: 'America', 'Europe' or 'Asia'.   
`cache_result`: Cache result for serving HTTP request by proxy: 'HIT', 'MISS', 'DISABLED', 'PARTIAL_HIT' (for a request served partially from cache and partially from backend) or 'UNKNOWN'.   
`client_country`: Country of the client that issued the HTTP request (for example, 'United States', 'Germany').   
`l3/external/egress_bytes_count` GA ** _(project)_**   
Egress bytes count   
`DELTA`, `INT64`, `By`   
**[loadbalancing.googleapis.com/ExternalNetworkLoadBalancerRule](https://docs.cloud.google.com/monitoring/api/resources#tag_loadbalancing.googleapis.com/ExternalNetworkLoadBalancerRule)**   
**[tcp_lb_rule](https://docs.cloud.google.com/monitoring/api/resources#tag_tcp_lb_rule)**   
**[udp_lb_rule](https://docs.cloud.google.com/monitoring/api/resources#tag_udp_lb_rule)** |  _The number of bytes sent from the backend of the external network load balancer to the client. For TCP flows, this metric counts the bytes on the application stream only. Sampled every 60 seconds. After sampling, data is not visible for up to 150 seconds._   
`client_continent`: Continent of the client that initiated the flow to the external network load balancer.   
`client_country`: Country of the client that initiated the flow to the external network load balancer.   
`protocol`: Protocol of the connection, one of [TCP, UDP, GRE, ICMP, ICMPV6, ESP]. This field remains empty for all resources other than loadbalancing.googleapis.com/ExternalNetworkLoadBalancerRule.   
`l3/external/egress_packets_count` GA ** _(project)_**   
Egress packets count   
`DELTA`, `INT64`, `1`   
**[loadbalancing.googleapis.com/ExternalNetworkLoadBalancerRule](https://docs.cloud.google.com/monitoring/api/resources#tag_loadbalancing.googleapis.com/ExternalNetworkLoadBalancerRule)**   
**[tcp_lb_rule](https://docs.cloud.google.com/monitoring/api/resources#tag_tcp_lb_rule)**   
**[udp_lb_rule](https://docs.cloud.google.com/monitoring/api/resources#tag_udp_lb_rule)** |  _The number of packets sent from the backend of the external network load balancer to the client. Sampled every 60 seconds. After sampling, data is not visible for up to 150 seconds._   
`client_continent`: Continent of the client that initiated the flow to the external network load balancer.   
`client_country`: Country of the client that initiated the flow to the external network load balancer.   
`protocol`: Protocol of the connection, one of [TCP, UDP, GRE, ICMP, ICMPV6, ESP]. This field remains empty for all resources other than loadbalancing.googleapis.com/ExternalNetworkLoadBalancerRule.   
`l3/external/ingress_bytes_count` GA ** _(project)_**   
Ingress bytes count   
`DELTA`, `INT64`, `By`   
**[loadbalancing.googleapis.com/ExternalNetworkLoadBalancerRule](https://docs.cloud.google.com/monitoring/api/resources#tag_loadbalancing.googleapis.com/ExternalNetworkLoadBalancerRule)**   
**[tcp_lb_rule](https://docs.cloud.google.com/monitoring/api/resources#tag_tcp_lb_rule)**   
**[udp_lb_rule](https://docs.cloud.google.com/monitoring/api/resources#tag_udp_lb_rule)** |  _The number of bytes sent from the client to the backend of the external network load balancer. For TCP flows, this metric counts the bytes on the application stream only. Sampled every 60 seconds. After sampling, data is not visible for up to 150 seconds._   
`client_continent`: Continent of the client that initiated the flow to the external network load balancer.   
`client_country`: Country of the client that initiated the flow to the external network load balancer.   
`protocol`: Protocol of the connection, one of [TCP, UDP, GRE, ICMP, ICMPV6, ESP]. This field remains empty for all resources other than loadbalancing.googleapis.com/ExternalNetworkLoadBalancerRule.   
`l3/external/ingress_packets_count` GA ** _(project)_**   
Ingress packets count   
`DELTA`, `INT64`, `1`   
**[loadbalancing.googleapis.com/ExternalNetworkLoadBalancerRule](https://docs.cloud.google.com/monitoring/api/resources#tag_loadbalancing.googleapis.com/ExternalNetworkLoadBalancerRule)**   
**[tcp_lb_rule](https://docs.cloud.google.com/monitoring/api/resources#tag_tcp_lb_rule)**   
**[udp_lb_rule](https://docs.cloud.google.com/monitoring/api/resources#tag_udp_lb_rule)** |  _The number of packets sent from the client to the backend of the external network load balancer. Sampled every 60 seconds. After sampling, data is not visible for up to 150 seconds._   
`client_continent`: Continent of the client that initiated the flow to the external network load balancer.   
`client_country`: Country of the client that initiated the flow to the external network load balancer.   
`protocol`: Protocol of the connection, one of [TCP, UDP, GRE, ICMP, ICMPV6, ESP]. This field remains empty for all resources other than loadbalancing.googleapis.com/ExternalNetworkLoadBalancerRule.   
`l3/external/rtt_latencies` GA ** _(project)_**   
RTT latencies   
`DELTA`, `DISTRIBUTION`, `ms`   
**[loadbalancing.googleapis.com/ExternalNetworkLoadBalancerRule](https://docs.cloud.google.com/monitoring/api/resources#tag_loadbalancing.googleapis.com/ExternalNetworkLoadBalancerRule)**   
**[tcp_lb_rule](https://docs.cloud.google.com/monitoring/api/resources#tag_tcp_lb_rule)** |  _A distribution of the round trip time latency, measured over TCP connections for the external network load balancer. Sampled every 60 seconds. After sampling, data is not visible for up to 150 seconds._   
`client_continent`: Continent of the client that initiated the flow to the external network load balancer.   
`client_country`: Country of the client that initiated the flow to the external network load balancer.   
`protocol`: Protocol of the connection, set to TCP if the resource is loadbalancing.googleapis.com/ExternalNetworkLoadBalancerRule, otherwise empty.   
`l3/internal/egress_bytes_count` GA ** _(project)_**   
Egress bytes per internal TCP/UDP load balancer   
`DELTA`, `INT64`, `By`   
**[internal_tcp_lb_rule](https://docs.cloud.google.com/monitoring/api/resources#tag_internal_tcp_lb_rule)**   
**[internal_udp_lb_rule](https://docs.cloud.google.com/monitoring/api/resources#tag_internal_udp_lb_rule)** |  _The number of bytes sent from the internal TCP/UDP load balancer backend to the client (for TCP flows it's counting bytes on application stream only). Sampled every 60 seconds. After sampling, data is not visible for up to 150 seconds._   
`client_project_id`: Project ID of the client instance communicating with the internal TCP/UDP load balancer. If the client instance belongs to a different project, the field is set with the correct value only if all of the following hold: 1) the projects are in the same organization, 2) the communication was via Shared VPC or VPC Peering, 3) cross project metrics were not disabled. Otherwise the field is set to CLIENT_IS_EXTERNAL.   
`client_network`: Network of the client instance communicating with the internal TCP/UDP load balancer. If the client instance belongs to a different project, the field is set with the correct value only if all of the following hold: 1) the projects are in the same organization, 2) the communication was via Shared VPC or VPC Peering, 3) cross project metrics were not disabled. Otherwise the field is set to CLIENT_IS_EXTERNAL.   
`client_subnetwork`: Subnetwork of the client instance communicating with the internal TCP/UDP load balancer. If the client instance belongs to a different project, the field is set with the correct value only if all of the following hold: 1) the projects are in the same organization, 2) the communication was via Shared VPC or VPC Peering, 3) cross project metrics were not disabled. Otherwise the field is set to CLIENT_IS_EXTERNAL.   
`client_zone`: Zone of the client instance communicating with the internal TCP/UDP load balancer. If the client instance belongs to a different project, the field is set with the correct value only if all of the following hold: 1) the projects are in the same organization, 2) the communication was via Shared VPC or VPC Peering, 3) cross project metrics were not disabled. Otherwise the field is set to CLIENT_IS_EXTERNAL.   
`l3/internal/egress_packets_count` GA ** _(project)_**   
Egress packets per internal TCP/UDP load balancer   
`DELTA`, `INT64`, `1`   
**[internal_tcp_lb_rule](https://docs.cloud.google.com/monitoring/api/resources#tag_internal_tcp_lb_rule)**   
**[internal_udp_lb_rule](https://docs.cloud.google.com/monitoring/api/resources#tag_internal_udp_lb_rule)** |  _The number of packets sent from the internal TCP/UDP load balancer to the client. Sampled every 60 seconds. After sampling, data is not visible for up to 150 seconds._   
`client_project_id`: Project ID of the client instance communicating with the internal TCP/UDP load balancer. If the client instance belongs to a different project, the field is set with the correct value only if all of the following hold: 1) the projects are in the same organization, 2) the communication was via Shared VPC or VPC Peering, 3) cross project metrics were not disabled. Otherwise the field is set to CLIENT_IS_EXTERNAL.   
`client_network`: Network of the client instance communicating with the internal TCP/UDP load balancer. If the client instance belongs to a different project, the field is set with the correct value only if all of the following hold: 1) the projects are in the same organization, 2) the communication was via Shared VPC or VPC Peering, 3) cross project metrics were not disabled. Otherwise the field is set to CLIENT_IS_EXTERNAL.   
`client_subnetwork`: Subnetwork of the client instance communicating with the internal TCP/UDP load balancer. If the client instance belongs to a different project, the field is set with the correct value only if all of the following hold: 1) the projects are in the same organization, 2) the communication was via Shared VPC or VPC Peering, 3) cross project metrics were not disabled. Otherwise the field is set to CLIENT_IS_EXTERNAL.   
`client_zone`: Zone of the client instance communicating with the internal TCP/UDP load balancer. If the client instance belongs to a different project, the field is set with the correct value only if all of the following hold: 1) the projects are in the same organization, 2) the communication was via Shared VPC or VPC Peering, 3) cross project metrics were not disabled. Otherwise the field is set to CLIENT_IS_EXTERNAL.   
`l3/internal/ingress_bytes_count` GA ** _(project)_**   
Ingress bytes per internal TCP/UDP load balancer   
`DELTA`, `INT64`, `By`   
**[internal_tcp_lb_rule](https://docs.cloud.google.com/monitoring/api/resources#tag_internal_tcp_lb_rule)**   
**[internal_udp_lb_rule](https://docs.cloud.google.com/monitoring/api/resources#tag_internal_udp_lb_rule)** |  _The number of bytes sent from the client to the internal TCP/UDP load balancer backend (for TCP flows it's counting bytes on application stream only). Sampled every 60 seconds. After sampling, data is not visible for up to 150 seconds._   
`client_project_id`: Project ID of the client instance communicating with the internal TCP/UDP load balancer. If the client instance belongs to a different project, the field is set with the correct value only if all of the following hold: 1) the projects are in the same organization, 2) the communication was via Shared VPC or VPC Peering, 3) cross project metrics were not disabled. Otherwise the field is set to CLIENT_IS_EXTERNAL.   
`client_network`: Network of the client instance communicating with the internal TCP/UDP load balancer. If the client instance belongs to a different project, the field is set with the correct value only if all of the following hold: 1) the projects are in the same organization, 2) the communication was via Shared VPC or VPC Peering, 3) cross project metrics were not disabled. Otherwise the field is set to CLIENT_IS_EXTERNAL.   
`client_subnetwork`: Subnetwork of the client instance communicating with the internal TCP/UDP load balancer. If the client instance belongs to a different project, the field is set with the correct value only if all of the following hold: 1) the projects are in the same organization, 2) the communication was via Shared VPC or VPC Peering, 3) cross project metrics were not disabled. Otherwise the field is set to CLIENT_IS_EXTERNAL.   
`client_zone`: Zone of the client instance communicating with the internal TCP/UDP load balancer. If the client instance belongs to a different project, the field is set with the correct value only if all of the following hold: 1) the projects are in the same organization, 2) the communication was via Shared VPC or VPC Peering, 3) cross project metrics were not disabled. Otherwise the field is set to CLIENT_IS_EXTERNAL.   
`l3/internal/ingress_packets_count` GA ** _(project)_**   
Ingress packets per internal TCP/UDP load balancer   
`DELTA`, `INT64`, `1`   
**[internal_tcp_lb_rule](https://docs.cloud.google.com/monitoring/api/resources#tag_internal_tcp_lb_rule)**   
**[internal_udp_lb_rule](https://docs.cloud.google.com/monitoring/api/resources#tag_internal_udp_lb_rule)** |  _The number of packets sent from the client to the internal TCP/UDP load balancer backend. Sampled every 60 seconds. After sampling, data is not visible for up to 150 seconds._   
`client_project_id`: Project ID of the client instance communicating with the internal TCP/UDP load balancer. If the client instance belongs to a different project, the field is set with the correct value only if all of the following hold: 1) the projects are in the same organization, 2) the communication was via Shared VPC or VPC Peering, 3) cross project metrics were not disabled. Otherwise the field is set to CLIENT_IS_EXTERNAL.   
`client_network`: Network of the client instance communicating with the internal TCP/UDP load balancer. If the client instance belongs to a different project, the field is set with the correct value only if all of the following hold: 1) the projects are in the same organization, 2) the communication was via Shared VPC or VPC Peering, 3) cross project metrics were not disabled. Otherwise the field is set to CLIENT_IS_EXTERNAL.   
`client_subnetwork`: Subnetwork of the client instance communicating with the internal TCP/UDP load balancer. If the client instance belongs to a different project, the field is set with the correct value only if all of the following hold: 1) the projects are in the same organization, 2) the communication was via Shared VPC or VPC Peering, 3) cross project metrics were not disabled. Otherwise the field is set to CLIENT_IS_EXTERNAL.   
`client_zone`: Zone of the client instance communicating with the internal TCP/UDP load balancer. If the client instance belongs to a different project, the field is set with the correct value only if all of the following hold: 1) the projects are in the same organization, 2) the communication was via Shared VPC or VPC Peering, 3) cross project metrics were not disabled. Otherwise the field is set to CLIENT_IS_EXTERNAL.   
`l3/internal/rtt_latencies` GA ** _(project)_**   
RTT latencies per internal TCP/UDP load balancer   
`DELTA`, `DISTRIBUTION`, `ms`   
**[internal_tcp_lb_rule](https://docs.cloud.google.com/monitoring/api/resources#tag_internal_tcp_lb_rule)** |  _A distribution of RTT measured over TCP connections for internal TCP/UDP load balancer flows. Sampled every 60 seconds. After sampling, data is not visible for up to 150 seconds._   
`client_project_id`: Project ID of the client instance communicating with the internal TCP/UDP load balancer. If the client instance belongs to a different project, the field is set with the correct value only if all of the following hold: 1) the projects are in the same organization, 2) the communication was via Shared VPC or VPC Peering, 3) cross project metrics were not disabled. Otherwise the field is set to CLIENT_IS_EXTERNAL.   
`client_network`: Network of the client instance communicating with the internal TCP/UDP load balancer. If the client instance belongs to a different project, the field is set with the correct value only if all of the following hold: 1) the projects are in the same organization, 2) the communication was via Shared VPC or VPC Peering, 3) cross project metrics were not disabled. Otherwise the field is set to CLIENT_IS_EXTERNAL.   
`client_subnetwork`: Subnetwork of the client instance communicating with the internal TCP/UDP load balancer. If the client instance belongs to a different project, the field is set with the correct value only if all of the following hold: 1) the projects are in the same organization, 2) the communication was via Shared VPC or VPC Peering, 3) cross project metrics were not disabled. Otherwise the field is set to CLIENT_IS_EXTERNAL.   
`client_zone`: Zone of the client instance communicating with the internal TCP/UDP load balancer. If the client instance belongs to a different project, the field is set with the correct value only if all of the following hold: 1) the projects are in the same organization, 2) the communication was via Shared VPC or VPC Peering, 3) cross project metrics were not disabled. Otherwise the field is set to CLIENT_IS_EXTERNAL.   
`l4_proxy/egress_bytes_count` GA ** _(project)_**   
Egress bytes   
`DELTA`, `INT64`, `By`   
**[l4_proxy_rule](https://docs.cloud.google.com/monitoring/api/resources#tag_l4_proxy_rule)** |  _Number of bytes sent from VM to client using proxy. Sampled every 60 seconds. After sampling, data is not visible for up to 210 seconds._   
`client_country`: Country of the client where the traffic originated from, such as 'United States' or 'Germany'.   
`l4_proxy/ingress_bytes_count` GA ** _(project)_**   
Ingress bytes   
`DELTA`, `INT64`, `By`   
**[l4_proxy_rule](https://docs.cloud.google.com/monitoring/api/resources#tag_l4_proxy_rule)** |  _Number of bytes sent from client to VM using proxy. Sampled every 60 seconds. After sampling, data is not visible for up to 210 seconds._   
`client_country`: Country of the client where the traffic originated from, such as 'United States' or 'Germany'.   
`l4_proxy/tcp/closed_connections_count` GA ** _(project)_**   
Closed connections   
`DELTA`, `INT64`, `1`   
**[l4_proxy_rule](https://docs.cloud.google.com/monitoring/api/resources#tag_l4_proxy_rule)** |  _Number of connections that were terminated over TCP proxy or SSL proxy load balancer. Sampled every 60 seconds. After sampling, data is not visible for up to 210 seconds._   
`client_country`: Country of the client where the traffic originated from, such as 'United States' or 'Germany'.   
`l4_proxy/tcp/new_connections_count` GA ** _(project)_**   
New connections   
`DELTA`, `INT64`, `1`   
**[l4_proxy_rule](https://docs.cloud.google.com/monitoring/api/resources#tag_l4_proxy_rule)** |  _Number of connections that were opened over TCP proxy or SSL proxy load balancer. Sampled every 60 seconds. After sampling, data is not visible for up to 210 seconds._   
`client_country`: Country of the client where the traffic originated from, such as 'United States' or 'Germany'.   
`subnet/proxy_only/addresses` GA ** _(project)_**   
Proxy-only addresses   
`GAUGE`, `INT64`, `1`   
**[gce_subnetwork](https://docs.cloud.google.com/monitoring/api/resources#tag_gce_subnetwork)** |  _The current number of proxy-only addresses by state. Sampled every 60 seconds. After sampling, data is not visible for up to 120 seconds._   
`state`: State of the address, one of [used, free].   
`tcp_ssl_proxy/closed_connections` GA ** _(project)_**   
Closed connections   
`DELTA`, `INT64`, `1`   
**[tcp_ssl_proxy_rule](https://docs.cloud.google.com/monitoring/api/resources#tag_tcp_ssl_proxy_rule)** |  _Number of connections that were terminated over TCP proxy or SSL proxy load balancer. Sampled every 60 seconds. After sampling, data is not visible for up to 210 seconds._   
`proxy_continent`: Continent of the SSL proxy that handles the connection: 'America', 'Europe' or 'Asia'.   
`client_country`: Country of the client that opened the TCP/SSL connection (for example, 'United States', 'Germany').   
`tcp_ssl_proxy/egress_bytes_count` GA ** _(project)_**   
Egress bytes   
`DELTA`, `INT64`, `By`   
**[tcp_ssl_proxy_rule](https://docs.cloud.google.com/monitoring/api/resources#tag_tcp_ssl_proxy_rule)** |  _Number of bytes sent from VM to client using proxy. Sampled every 60 seconds. After sampling, data is not visible for up to 210 seconds._   
`proxy_continent`: Continent of the proxy that handles the connection: 'America', 'Europe' or 'Asia'.   
`client_country`: Country of the client that opened the TCP/SSL connection (for example, 'United States', 'Germany').   
`tcp_ssl_proxy/frontend_tcp_rtt` GA ** _(project)_**   
Frontend RTT   
`DELTA`, `DISTRIBUTION`, `ms`   
**[tcp_ssl_proxy_rule](https://docs.cloud.google.com/monitoring/api/resources#tag_tcp_ssl_proxy_rule)** |  _A distribution of the smoothed RTT (in ms) measured by the proxy's TCP stack, each minute application layer bytes pass from proxy to client. Sampled every 60 seconds. After sampling, data is not visible for up to 210 seconds._   
`proxy_continent`: Continent of the SSL proxy that handles the connection: 'America', 'Europe' or 'Asia'.   
`client_country`: Country of the client that opened the TCP/SSL connection (for example, 'United States', 'Germany').   
`tcp_ssl_proxy/ingress_bytes_count` GA ** _(project)_**   
Ingress bytes   
`DELTA`, `INT64`, `By`   
**[tcp_ssl_proxy_rule](https://docs.cloud.google.com/monitoring/api/resources#tag_tcp_ssl_proxy_rule)** |  _Number of bytes sent from client to VM using proxy. Sampled every 60 seconds. After sampling, data is not visible for up to 210 seconds._   
`proxy_continent`: Continent of the proxy that handles the connection: 'America', 'Europe' or 'Asia'.   
`client_country`: Country of the client that opened the TCP/SSL connection (for example, 'United States', 'Germany').   
`tcp_ssl_proxy/new_connections` GA ** _(project)_**   
New connections opened   
`DELTA`, `INT64`, `1`   
**[tcp_ssl_proxy_rule](https://docs.cloud.google.com/monitoring/api/resources#tag_tcp_ssl_proxy_rule)** |  _Number of connections that were created over TCP proxy or SSL proxy load balancer. Sampled every 60 seconds. After sampling, data is not visible for up to 210 seconds._   
`proxy_continent`: Continent of the SSL proxy that handles the connection: 'America', 'Europe' or 'Asia'.   
`client_country`: Country of the client that opened the TCP/SSL connection (for example, 'United States', 'Germany').   
`tcp_ssl_proxy/open_connections` GA ** _(project)_**   
Open Connections   
`GAUGE`, `INT64`, `1`   
**[tcp_ssl_proxy_rule](https://docs.cloud.google.com/monitoring/api/resources#tag_tcp_ssl_proxy_rule)** |  _Current number of outstanding connections through the TCP proxy or SSL proxy load balancer. Sampled every 60 seconds. After sampling, data is not visible for up to 210 seconds._   
`proxy_continent`: Continent of the SSL proxy that handles the connection: 'America', 'Europe' or 'Asia'.   
`client_country`: Country of the client that opened the TCP/SSL connection (for example, 'United States', 'Germany').   
  
Table generated at 2026-10-14 20:24:33 UTC.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-15 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-15 UTC."],[],[]] 
