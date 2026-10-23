---
url: https://docs.cloud.google.com/load-balancing/docs/https/request-distribution/
title: Request distribution for external Application Load Balancers \u00a0|\u00a0 Cloud Load Balancing \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:24:58.289259+00:00
---

# Request distribution for external Application Load Balancers  |  Cloud Load Balancing  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/load-balancing/docs/https/request-distribution/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Networking ](https://docs.cloud.google.com/docs/networking)
  * [ Load Balancing ](https://docs.cloud.google.com/load-balancing/docs)
  * [ Guides ](https://docs.cloud.google.com/load-balancing/docs/load-balancing-overview)



Send feedback 

#  Request distribution for external Application Load Balancers Stay organized with collections  Save and categorize content based on your preferences. 

This document delves into the intricacies of how external Application Load Balancers load balancers handle connections, route traffic, and maintain session affinity.

## How connections work

Google Cloud's external Application Load Balancers—global and regional—streamline routing using distributed proxies (GFEs) or Envoy-managed subnets. With configurable timeouts, TLS termination, and built-in security, they ensure compliant, scalable application delivery worldwide or regionally.

### Global external Application Load Balancer connections

The global external Application Load Balancers are implemented by many proxies called Google Front Ends (GFEs). There isn't just a single proxy. In Premium Tier, the same global external IP address is advertised from various points of presence, and client requests are directed to the client's nearest GFE.

Depending on where your clients are, multiple GFEs can initiate HTTP(S) connections to your backends. To learn more about the GFE proxy ranges, see [Firewall rules](https://docs.cloud.google.com/load-balancing/docs/firewall-rules).

**Note:** For internet NEGs, requests from the load balancer come from different IP ranges depending on the type of NEG (global or regional). For more information, see [Authenticating requests](https://docs.cloud.google.com/load-balancing/docs/negs/internet-neg-concepts#authenticating_requests).

Depending on the backend service configuration, the protocol used by each GFE to connect to your backends can be HTTP, HTTPS, or HTTP/2. For HTTP or HTTPS connections, the HTTP version used is HTTP 1.1.

HTTP keepalive is enabled by default, as specified in the HTTP 1.1 specification. HTTP keepalives attempt to efficiently use the same TCP session; however, there's no guarantee. The GFE uses a client HTTP keepalive timeout of 610 seconds and a default backend keepalive timeout value of 600 seconds. You can update the client HTTP keepalive timeout but the backend keepalive timeout value is fixed. You can configure the request and response timeout by setting the backend service timeout. Though closely related, an HTTP keepalive and a TCP idle timeout are not the same thing. For more information, see timeouts and retries.

To ensure that traffic is load balanced evenly, the load balancer might cleanly close a TCP connection either by sending a `FIN ACK` packet after completing a response that included a `Connection: close` header, or it might issue an HTTP/2 `GOAWAY` frame after completing a response. This behavior does not interfere with any active requests or responses.

The numbers of HTTP connections and TCP sessions vary depending on the number of GFEs connecting, the number of clients connecting to the GFEs, the protocol to the backends, and where backends are deployed.

For more information, see [How external Application Load Balancers work](https://docs.cloud.google.com/load-balancing/docs/tutorials/about-capacity-optimization-with-global-lb#how_https_load_balancing_works) in the solutions guide: Application Capacity Optimizations with Global Load Balancing.

### Regional external Application Load Balancer connections

The regional external Application Load Balancer is a managed service implemented on the Envoy proxy. The regional external Application Load Balancer uses a shared subnet called a proxy-only subnet to provision a set of IP addresses that Google uses to run Envoy proxies on your behalf. The `--purpose` flag for this proxy-only subnet is set to `REGIONAL_MANAGED_PROXY`. All [regional Envoy-based load balancers](https://docs.cloud.google.com/load-balancing/docs/proxy-only-subnets#envoy-lb) in a particular network and region share this subnet.

Clients use the load balancer's IP address and port to connect to the load balancer. Client requests are directed to the proxy-only subnet in the same region as the client. The load balancer terminates clients requests and then opens new connections from the proxy-only subnet to your backends. Therefore, packets sent from the load balancer have source IP addresses from the proxy-only subnet.

Depending on the backend service configuration, the protocol used by Envoy proxies to connect to your backends can be HTTP, HTTPS, or HTTP/2. If HTTP or HTTPS, the HTTP version is HTTP 1.1. HTTP keepalive is enabled by default, as specified in the HTTP 1.1 specification. The Envoy proxy sets both the client HTTP keepalive timeout and the backend keepalive timeout to a default value of 600 seconds each. You can update the client HTTP keepalive timeout but the backend keepalive timeout value is fixed. You can configure the request/response timeout by setting the backend service timeout. For more information, see timeouts and retries.

### Client communications with the load balancer

  * Clients can communicate with the load balancer by using the HTTP/1.0, HTTP/1.1, HTTP/2, or HTTP/3 protocol.
  * When HTTPS is used, modern clients default to HTTP/2. This is controlled _on the client_ , not on the HTTPS load balancer.
  * You cannot disable HTTP/2 by making a configuration change on the load balancer. However, you can configure some clients to use HTTP 1.1 instead of HTTP/2. For example, with `curl`, use the `--http1.1` parameter.
  * External Application Load Balancers support the `HTTP/1.1 100 Continue` response.



For the complete list of protocols supported by external Application Load Balancer forwarding rules in each mode, see [Load balancer features](https://docs.cloud.google.com/load-balancing/docs/features#protocols_from_the_clients_to_the_load_balancer).

### Source IP addresses for client packets

The source IP address for packets, as seen by the backends, is _not_ the Google Cloud external IP address of the load balancer. In other words, there are two TCP connections.

**For the global external Application Load Balancers** : 

  * Connection 1, from original client to the load balancer (GFE):

    * **Source IP address** : the original client (or external IP address if the client is behind a NAT gateway or a forward proxy).
    * **Destination IP address** : your load balancer's IP address.
  * Connection 2, from the load balancer (GFE) to the backend VM or endpoint:

    * **Source IP address** : an IP address in one of the ranges specified in Firewall rules.

    * **Destination IP address** : the internal IP address of the backend VM or container in the VPC network.


**Note:** For internet NEGs, requests from the load balancer come from different IP ranges. For more information, see [Authenticating requests](https://docs.cloud.google.com/load-balancing/docs/negs/internet-neg-concepts#authenticating_requests).**For the regional external Application Load Balancers** : 

  * Connection 1, from original client to the load balancer (proxy-only subnet):

    * **Source IP address** : the original client (or external IP address if the client is behind a NAT gateway or a forward proxy).
    * **Destination IP address** : your load balancer's IP address.
  * Connection 2, from the load balancer (proxy-only subnet) to the backend VM or endpoint:

    * **Source IP address** : an IP address in the proxy-only subnet that is shared among all the Envoy-based load balancers deployed in the same region and network as the load balancer.

    * **Destination IP address** : the internal IP address of the backend VM or container in the VPC network.




### Special routing paths

Google Cloud uses special routes not defined in your VPC network to route packets for the following types of traffic:

  * For health checks, except [distributed Envoy health checks](https://docs.cloud.google.com/load-balancing/docs/negs/hybrid-neg-concepts#envoy-health-checks). For more information, see [Paths for health checks](https://docs.cloud.google.com/vpc/docs/routes#health_checks_for_all_load_balancer_types).


  * Between GFEs and backends of global external Application Load Balancers and classic Application Load Balancers. For more information, see [Paths between Google Front Ends and backends](https://docs.cloud.google.com/vpc/docs/routes#paths_between_google_front_end_gfe_proxies_and_backends).



Google Cloud uses subnet routes for [proxy-only subnets](https://docs.cloud.google.com/load-balancing/docs/proxy-only-subnets) to route packets for the following types of traffic:

  * When using distributed Envoy health checks.



For regional external Application Load Balancers, Google Cloud uses open-source Envoy proxies to terminate client requests to the load balancer. The load balancer terminates the TCP session and opens a new TCP session from the region's proxy- only subnet to your backend. Routes defined within your VPC network facilitate communication from Envoy proxies to your backends and from your backends to the Envoy proxies.

### Open ports

GFEs have several open ports to support other Google services that run on the same architecture. When you run a port scan, you might see other open ports for other Google services running on GFEs.

Both GFE-based load balancers—global external Application Load Balancers and classic Application Load Balancers—always show ports 80 and 443 as open (along with any other port you've configured in your load balancer's forwarding rules). However, if you haven't configured a forwarding rule for port 80 or for port 443, any connections sent to those ports are refused. Conversely, regional external Application Load Balancers are implemented using Envoy proxies and don't show extra open ports during a scan. 

Running a port scan on the IP address of a GFE-based load balancer isn't useful from an auditing perspective for the following reasons:

  * A port scan (for example, with `nmap`) generally expects no response packet or a TCP RST packet when performing TCP SYN probing. GFEs send SYN-ACK packets in response to SYN probes only for ports on which you have configured a forwarding rule. GFEs only send packets to your backends in response to packets sent to your load balancer's IP address _and_ the destination port configured on its forwarding rule. Packets that are sent to a different IP address or port aren't sent to your backends.

  * Packets sent to the IP address of your load balancer can be answered by any GFE in Google's fleet; however, scanning a load balancer IP address and destination port combination only interrogates a single GFE per TCP connection. The IP address of your load balancer isn't assigned to a single device or system. Thus, scanning the IP address of a GFE-based load balancer doesn't scan all the GFEs in Google's fleet.




With that in mind, the following are some more effective ways to audit the security of your backend instances:

  * A security auditor should inspect the forwarding rules configuration for the load balancer's configuration. The forwarding rules define the destination port for which your load balancer accepts packets and forwards them to the backends. For GFE-based load balancers, [each external forwarding rule can only reference a single destination TCP port](https://docs.cloud.google.com/load-balancing/docs/forwarding-rule-concepts#port_specifications). For a load balancer using TCP port 443, UDP port 443 is used when the connection is upgraded to QUIC (HTTP/3). 

  * A security auditor should inspect the firewall rule configuration applicable to backend VMs. The firewall rules that you set block traffic from the GFEs to the backend VMs but don't block incoming traffic to the GFEs. For best practices, see the firewall rules section.




### TLS termination

The following table summarizes how TLS termination is handled by external Application Load Balancers.

Load balancer mode | TLS termination  
---|---  
Global external Application Load Balancer | TLS is terminated on a GFE, which can be anywhere in the world.  
Classic Application Load Balancer | TLS is terminated on a GFE, which could be anywhere in the world.  
Regional external Application Load Balancer | TLS is terminated on Envoy proxies located in a proxy-only subnet in a region chosen by the user. Use this load balancer mode if you need geographic control over the region where TLS is terminated.  
  
### Timeouts and retries

External Application Load Balancers support the following types of timeouts for HTTP or HTTPS traffic:

Timeout type and description | Default values | Supports custom timeout values  
---|---|---  
Global | Classic | Regional  
Backend service timeout1

* * *

A request and response timeout. Represents the maximum amount of time allowed between the load balancer sending the first byte of a request to the backend and the backend returning the last byte of the HTTP response to the load balancer. If the backend hasn't returned the entire HTTP response to the load balancer within this time limit, the remaining response data is dropped. | 

  * For serverless NEGs on a backend service: 60 minutes
  * For all other backend types on a backend service: 30 seconds
  * For backend buckets: 24 hours (86,400 seconds)

|  |  |   
Connection setup timeout

* * *

The maximum time allowed for the proxy to establish a connection to the backend. A successful setup includes completing the TCP three-way handshake, and—if the backend protocol is HTTPS—completing the TLS handshake.

  * For global external Application Load Balancers and classic Application Load Balancers, the load balancer's proxy is a second-layer GFE.
  * For regional external Application Load Balancers, the load balancer's proxy is Envoy software.

| 4.5 seconds |  |  |   
Client TLS timeout

* * *

The maximum amount of time that the load balancer's proxy waits for the TLS handshake to complete.

  * For global external Application Load Balancers and classic Application Load Balancers, the load balancer's proxy is a first-layer GFE.
  * For regional external Application Load Balancers, the load balancer's proxy is Envoy software.

| 10 seconds |  |  |   
Client HTTP keepalive timeout

* * *

The maximum amount of time that the TCP connection between a client and the load balancer's proxy can be idle. (The same TCP connection might be used for multiple HTTP requests.)

  * For global external Application Load Balancers and classic Application Load Balancers, the load balancer's proxy is a first-layer GFE.
  * For regional external Application Load Balancers, the load balancer's proxy is Envoy software.

| 610 seconds |  |  |   
Backend HTTP keepalive timeout

* * *

The maximum amount of time that the TCP connection between the load balancer's proxy and a backend can be idle. (The same TCP connection might be used for multiple HTTP requests.)

  * For global external Application Load Balancers and classic Application Load Balancers, the load balancer's proxy is a second-layer GFE.
  * For regional external Application Load Balancers, the load balancer's proxy is Envoy software.

| 

  * For backend services: 10 minutes (600 seconds)
  * For backend buckets: 6 minutes (360 seconds)

|  |  |   
QUIC session idle timeout

* * *

The maximum amount of time that a QUIC session can be idle between the (downstream) client and the GFE of a global external Application Load Balancer or a classic Application Load Balancer. |  For global external Application Load Balancers and classic Application Load Balancers: The QUIC session idle timeout is the minimum of either the client idle timeout or the GFE idle timeout (240 seconds). The GFE idle timeout is fixed at 240 seconds. The client idle timeout can be configured. |  |  |   
  
1Not configurable for serverless NEG backends. Not configurable for backend buckets.

#### Backend service timeout

The configurable _backend service timeout_ represents the maximum amount of time that the load balancer waits for your backend to process an HTTP request and return the corresponding HTTP response. Except for serverless NEGs, the default value for the backend service timeout is 30 seconds.

For example, if you want to download a 500-MB file, and the value of the backend service timeout is 90 seconds, the load balancer expects the backend to deliver the entire 500-MB file within 90 seconds. It is possible to configure the backend service timeout to be insufficient for the backend to send its complete HTTP response. In this situation, if the load balancer has at least received HTTP response headers from the backend, the load balancer returns the complete response headers and as much of the response body as it could obtain within the backend service timeout.

We recommend that you set the backend service timeout to the longest amount of time that you expect your backend to need in order to process an HTTP response. If the software running on your backend needs more time to process an HTTP request and return its entire response, we recommend that you increase the backend service timeout. For example, we recommend that you increase the timeout if you see HTTP `408` status code responses with `jsonPayload.statusDetail client_timed_out` errors. 

The backend service timeout accepts values between `1` and `2,147,483,647` seconds; however, larger values aren't practical configuration options. Google Cloud also doesn't guarantee that an underlying TCP connection can remain open for the entirety of the value of the backend service timeout. In case of the global and classic Application Load Balancers, GFEs impose an effective maximum backend service timeout of `86,400` seconds (1 day). Client systems must implement retry logic instead of relying on a TCP connection to be open for long periods of time.

To configure the backend service timeout, use one of the following methods: 

### Console

Modify the **Timeout** field of the load balancer's backend service.

### gcloud

Use the [ `gcloud compute backend-services update` command](https://docs.cloud.google.com/sdk/gcloud/reference/compute/backend-services/update#--timeout) to modify the `--timeout` parameter of the backend service resource.

### API

For a global external Application Load Balancer or a classic Application Load Balancer, modify the `timeoutSec` parameter for the [global `backendServices` resource](https://docs.cloud.google.com/compute/docs/reference/rest/v1/backendServices).

For a regional external Application Load Balancer, modify the `timeoutSec` parameter for the [ `regionBackendServices` resource](https://docs.cloud.google.com/compute/docs/reference/rest/v1/regionBackendServices).

Websocket connection timeouts aren't always the same as backend service timeouts. Websocket connection timeouts depend on the type of load balancer: Load balancer mode | Default values | Timeout description for websockets  
---|---|---  
Global external Application Load Balancer | backend service timeout: 30 seconds | Active websocket connections don't use the configured backend service timeout of the load balancer. The connections are automatically closed after 24 hours (86,400 seconds). This 24-hour limit is fixed and overrides the backend service timeout if it is greater than 24 hours. Idle websocket connections are closed after the backend service times out. We don't recommend backend service timeout values greater than 24 hours (86,400 seconds) because Google Cloud periodically restarts GFEs for software updates and other routine maintenance. Your backend service timeout value doesn't delay the maintenance activities. The longer the backend service timeout value, the more likely it is that Google Cloud terminates TCP connections for maintenance.  
Classic Application Load Balancer | backend service timeout: 30 seconds | Websocket connections, whether idle or active, automatically close after the backend service times out. We don't recommend backend service timeout values greater than 24 hours (86,400 seconds) because Google Cloud periodically restarts GFEs for software updates and other routine maintenance. Your backend service timeout value doesn't delay the maintenance activities. The longer the backend service timeout value, the more likely it is that Google Cloud terminates TCP connections for maintenance.  
Regional external Application Load Balancer | backend service timeout: 30 seconds | Active websocket connections don't use the backend service timeout of the load balancer. Idle websocket connections are closed after the backend service times out. Google Cloud periodically restarts or changes the number of serving Envoy software tasks. The longer the backend service timeout value is, the more likely it is that Envoy tasks restart or terminate TCP connections.  
  
Regional external Application Load Balancers use the configured [`routeAction.timeout`](https://docs.cloud.google.com/compute/docs/reference/rest/v1/regionUrlMaps) parameter of the URL maps and ignores the backend service timeout. When `routeAction.timeout` isn't configured, the value of the backend service timeout is used. When `routeAction.timeout` is supplied, the backend service timeout is ignored, and the value of `routeAction.timeout` is used as the request and response timeout instead.

#### Client HTTP keepalive timeout

The _client HTTP keepalive timeout_ represents the maximum amount of time that a TCP connection can be idle between the (downstream) client and one of the following types of proxies:

  * For a global external Application Load Balancer or a classic Application Load Balancer: a first-layer Google Front End


  * For a regional external Application Load Balancer: an Envoy proxy



The client HTTP keepalive timeout represents the TCP idle timeout for the underlying TCP connections. The client HTTP keepalive timeout doesn't apply to websockets.

The default value for the client HTTP keepalive timeout is 610 seconds. For global and regional external Application Load Balancers, you can configure the client HTTP keepalive timeout with a value between 5 and 1200 seconds.

To configure the client HTTP keepalive timeout, use one of the following methods:

### Console

Modify the **HTTP keepalive timeout** field of the load balancer's frontend configuration.

### gcloud

For global external Application Load Balancers, use the [`gcloud compute target-http-proxies update` command](https://docs.cloud.google.com/sdk/gcloud/reference/compute/target-http-proxies/update) or the [`gcloud compute target-https-proxies update` command](https://docs.cloud.google.com/sdk/gcloud/reference/compute/target-https-proxies/update) to modify the `--http-keep-alive-timeout-sec` parameter of the target HTTP proxy or the target HTTPS proxy resource.

For a regional external Application Load Balancer, you cannot update the keepalive timeout parameter of a regional target HTTP(S) proxy directly. To update the keepalive timeout parameter of a regional target proxy, you need to do the following:

  1. Create a new target proxy with the intended timeout settings.
  2. Mirror all other settings from the current target proxy on the new one. For target HTTPS proxies, this includes linking any SSL certificates or certificate maps to the new target proxy.
  3. Update the forwarding rules to point to the new target proxy.
  4. Delete the previous target proxy.



### API

For global external Application Load Balancers, modify the `httpKeepAliveTimeoutSec` parameter for the [ `targetHttpProxies` resource](https://docs.cloud.google.com/compute/docs/reference/rest/v1/targetHttpProxies) or the [ `targetHttpsProxies` resource](https://docs.cloud.google.com/compute/docs/reference/rest/v1/targetHttpsProxies).

For a regional external Application Load Balancer, you cannot update the keepalive timeout parameter of a regional target HTTP(S) proxy directly. To update the keepalive timeout parameter of a regional target proxy, you need to do the following:

  1. Create a new target proxy with the intended timeout settings.
  2. Mirror all other settings from the current target proxy on the new one. For target HTTPS proxies, this includes linking any SSL certificates or certificate maps to the new target proxy.
  3. Update the forwarding rules to point to the new target proxy.
  4. Delete the previous target proxy.



The load balancer's client HTTP keepalive timeout must be greater than the HTTP keepalive (TCP idle) timeout used by downstream clients or proxies. If a downstream client has a greater HTTP keepalive (TCP idle) timeout than the load balancer's client HTTP keepalive timeout, it's possible for a race condition to occur. From the perspective of a downstream client, an established TCP connection is permitted to be idle for longer than permitted by the load balancer. This means that the downstream client can send packets after the load balancer considers the TCP connection to be closed. When that happens, the load balancer responds with a TCP reset (RST) packet.

When the client HTTP keepalive timeout expires, either the GFE or the Envoy proxy sends a TCP FIN to the client to gracefully close the connection.

#### Backend HTTP keepalive timeout

External Application Load Balancers are proxies that use at least two TCP connections:

  * For a global external Application Load Balancer or a classic Application Load Balancer, a first TCP connection exists between the (downstream) client and a first-layer GFE. First-layer GFEs connect to second layer GFEs, and then the second-layer GFEs open a second TCP connection to your backends.


  * For a regional external Application Load Balancer, a first TCP connection exists between the (downstream) client and an Envoy proxy. The Envoy proxy then opens a second TCP connection to your backends.



The load balancer's secondary TCP connections might not get closed after each request; they can stay open to handle multiple HTTP requests and responses. The _backend HTTP keepalive timeout_ defines the TCP idle timeout between the load balancer and your backends. The backend HTTP keepalive timeout doesn't apply to websockets.

The backend keepalive timeout is fixed at 10 minutes (600 seconds) and cannot be changed. This helps ensure that the load balancer maintains idle connections for at least 10 minutes. After this period, the load balancer can send termination packets to the backend at any time.

The load balancer's backend keepalive timeout must be less than the keepalive timeout used by software running on your backends. This avoids a race condition where the operating system of your backends might close TCP connections with a TCP reset (RST). Because the backend keepalive timeout for the load balancer isn't configurable, you must configure your backend software so that its HTTP keepalive (TCP idle) timeout value is greater than 600 seconds.

When the backend HTTP keepalive timeout expires, either the GFE or the Envoy proxy sends a TCP FIN to the backend VM to gracefully close the connection.

The following table lists the changes necessary to modify keepalive timeout values for common web server software.

Web server software | Parameter | Default setting | Recommended setting  
---|---|---|---  
[Apache](https://httpd.apache.org) | [KeepAliveTimeout](https://httpd.apache.org/docs/2.4/mod/core.html#keepalivetimeout) | `KeepAliveTimeout 5` | `KeepAliveTimeout 620`  
[nginx](https://nginx.org) | [keepalive_timeout](http://nginx.org/en/docs/http/ngx_http_core_module.html#keepalive_timeout) | `keepalive_timeout 75s;` | `keepalive_timeout 620s;`  
  
#### QUIC session idle timeout

The _QUIC session idle timeout_ represents the maximum amount of time that a QUIC session can be idle between the client and the GFE of a global external Application Load Balancer or a classic Application Load Balancer.

The QUIC session idle timeout value is defined as the minimum of either the client idle timeout or the GFE idle timeout (240 seconds). The GFE idle timeout is fixed at 240 seconds. The client idle timeout can be configured.

#### Retries

Support for retry logic depends on the mode of the external Application Load Balancer.

Load balancer mode | Retry logic  
---|---  
Global external Application Load Balancer  |  Configurable by using a [retry policy](https://docs.cloud.google.com/compute/docs/reference/rest/v1/urlMaps) in the URL map. The maximum number of retries (`numRetries`) that can be configured by using the retry policy is 25. The maximum configurable `perTryTimeout` is 24 hours. If you want to disable retries, you must explicitly set `numRetries` to 1. This is because the `numRetries` parameter specifies the maximum total number of attempts the load balancer makes to send the request to the backend. This total includes the initial request plus any subsequent retry attempts. When you set `numRetries` to 1 in order to disable retries, it means that only the initial request is sent and no additional retries are attempted.  Without a retry policy, unsuccessful requests that have no HTTP body (for example, `GET` requests) that result in HTTP `502`, `503`, or `504` responses (`retryConditions=["gateway-error"]`) are retried once. HTTP `POST` requests aren't retried. Retried requests only generate one log entry for the final response. The following table specifies which backends support default and custom retry policies for a global external Application Load Balancer. | Type of backend | Default retry policy | Custom retry policy  
---|---|---  
Instance groups |  |   
Zonal NEGs |  |   
Hybrid NEGs |  |   
Private Service Connect NEGs |  |   
Internet NEGs |  |   
Serverless NEGs |  |   
**Note:** When a custom retry policy (`routeAction.retryPolicy`) isn't configured, the load balancer automatically creates a default retry policy. The timeout on the default retry policy is equal to the timeout value on the backend service and not on the route. As a result, the load balancer ignores the `routeAction.timeout` value if there is no custom retry policy.   
Classic Application Load Balancer |  The retry policy cannot be changed for connection retries. HTTP `POST` requests aren't retried. HTTP `GET` requests are always retried once as long as 80% or more of the backends are healthy. If there is a single backend instance in a group and the connection to that backend instance fails, the percentage of unhealthy backend instances is 100%, so the GFE doesn't retry the request. The load balancer retries a failed `GET` request if the first request failed before receiving response headers from the backend instance. Retried requests only generate one log entry for the final response. For more information, see [External Application Load Balancer logging and monitoring](https://docs.cloud.google.com/load-balancing/docs/https/https-logging-monitoring). Unsuccessful requests result in the load balancer synthesizing an HTTP `502` response. The following table specifies which backends support a retry policy for a Classic Application Load Balancer. | Type of backend | Default retry policy | Custom retry policy  
---|---|---  
Instance groups |  |   
Zonal NEGs |  |   
Hybrid NEGs |  |   
Internet NEGs |  |   
Serverless NEGs |  |   
Regional external Application Load Balancer |  Configurable by using a [retry policy](https://docs.cloud.google.com/compute/docs/reference/rest/v1/regionUrlMaps) in the URL map. The default number of retries (`numRetries`) is 1. The maximum number of retries that can be configured by using the retry policy is 25. The maximum configurable `perTryTimeout` is 24 hours. Without a retry policy, unsuccessful requests that have no HTTP body (for example, `GET` requests) that result in HTTP `502`, `503`, or `504` responses are retried once. HTTP `POST` requests aren't retried. Retried requests only generate one log entry for the final response.  
  
The WebSocket protocol is [supported with GKE Ingress](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/ingress-xlb#support_for_websocket).

### Illegal request and response handling

The load balancer blocks both client requests and backend responses from reaching the backend or the client, respectively, for a number of reasons. Some reasons are strictly for HTTP/1.1 compliance and others are to avoid unexpected data being passed to or from the backends. None of the checks can be disabled.

The following table specifies the different types of requests that are blocked by external Application Load Balancers for HTTP/1.1 compliance.

In this table,  indicates a request that is blocked by the load balancer, and  indicates a request that is allowed by the load balancer.

Type of request | Global external Application Load Balancer | Classic Application Load Balancer | Regional external Application Load Balancer  
---|---|---|---  
Unparsable first line of the request. |  |  |   
A header is missing the colon (:) delimiter. |  |  |   
Headers or the first line contain invalid characters. |  |  |   
The content length is not a valid number, or there are multiple content length headers.  |  |  |   
There are multiple transfer encoding keys, or there are unrecognized transfer encoding values.  |  |  |   
There's a non-chunked body and no content length specified. |  |  1 |   
Body chunks are unparsable. This is the only case where some data reaches the backend. The load balancer closes the connections to the client and backend when it receives an unparsable chunk.  |  |  |   
  
1 The proxy returns an HTTP `411` response for the request, but then attempts to parse the non-chunked body as a subsequent request. If the non-chunked body itself is a valid HTTP request, then it is parsed and sent to the backend. 

#### Request handling

The following table specifies which external Application Load Balancers blocks a request if it meets any of the conditions listed in the first column of the table.

In this table,  indicates a request that is blocked by the load balancer, and  indicates a request that is allowed by the load balancer.

Condition | Global external Application Load Balancer | Classic Application Load Balancer | Regional external Application Load Balancer  
---|---|---|---  
The total size of the request headers and request URL exceeds the limit for the maximum request [ header size for external Application Load Balancers](https://docs.cloud.google.com/load-balancing/docs/quotas#https-lb-header-limits).  |  |  |   
The request method does not allow a body, but the request has one. |  |  |   
The request contains an `Upgrade` header, and the `Upgrade` header is not used to enable WebSocket connections.  |  |  |   
The HTTP version is unknown. |  |  |   
  
#### Response handling

The following table specifies which external Application Load Balancers blocks a request if it meets any of the conditions listed in the first column of the table.

In this table,  indicates a request that is blocked by the load balancer, and  indicates a request that is allowed by the load balancer.

Condition | Global external Application Load Balancer | Classic Application Load Balancer | Regional external Application Load Balancer  
---|---|---|---  
The total size of response headers exceeds the limit for maximum response header size for the load balancer.  |  |  |   
The HTTP version is unknown. |  |  |   
  
When handling both the request and response, the load balancer might remove or overwrite [hop-by-hop headers](https://datatracker.ietf.org/doc/html/rfc2616#section-13.5.1) in HTTP/1.1 before forwarding them to the intended destination.

## Traffic distribution

When you add a backend instance group or NEG to a backend service, you specify a _balancing mode_ , which defines a method measuring backend load and a target capacity. External Application Load Balancers support two balancing modes:

  * `RATE`, for instance groups or NEGs, is the target maximum number of requests (queries) per second (RPS, QPS). The target maximum RPS/QPS can be exceeded if all backends are at or above capacity.

  * `UTILIZATION` is the backend utilization of VMs in an instance group.




How traffic is distributed among backends depends on the mode of the load balancer.

### Global external Application Load Balancer

Before a Google Front End (GFE) sends requests to backend instances, the GFE estimates which backend instances have capacity to receive requests. This capacity estimation is made proactively, not at the same time as requests are arriving. The GFEs receive periodic information about the available capacity and distribute incoming requests accordingly.

What _capacity_ means depends in part on the balancing mode. For the `RATE` mode, it is relatively simple: a GFE determines exactly how many requests it can assign per second. `UTILIZATION`-based load balancing is more complex: the load balancer checks the instances' current utilization and then estimates a query load that each instance can handle. This estimate changes over time as instance utilization and traffic patterns change.

Both factors—the capacity estimation and the proactive assignment—influence the distribution among instances. Thus, Cloud Load Balancing behaves differently from a simple round-robin load balancer that spreads requests exactly 50:50 between two instances. Instead, Google Cloud load balancing attempts to optimize the backend instance selection for each request.

For the global external Application Load Balancer, load balancing is two tiered. The balancing mode determines the weighting or fraction of traffic to send to each backend (instance group or NEG). Then, the load balancing policy (`LocalityLbPolicy`) determines how traffic is distributed to instances or endpoints within the group. For more information, see the [Load balancing locality policy (backend service API documentation)](https://docs.cloud.google.com/compute/docs/reference/rest/v1/backendServices#BackendService.FIELDS.locality_lb_policy).

For the classic Application Load Balancer, the balancing mode is used to select the most favorable backend (instance group or NEG). Traffic is then distributed in a round robin fashion among instances or endpoints within the backend.

#### How requests are distributed

_GFE-based external Application Load Balancers_ use the following process to distribute incoming requests:

  1. **From client to first-layer GFE**. Edge routers advertise the forwarding rule's external IP address at the borders of Google's network. Each advertisement lists a next hop to a Layer 3 and Layer 4 load balancing system (Maglev). The Maglev systems route traffic to a first-layer Google Front End (GFE). 
     * _When using Premium Tier_ , Google advertises your load balancer's IP address from all points of presence, worldwide. Each load balancer IP address is global anycast.
     * _When using Standard Tier_ , Google advertises your load balancer's IP address from points of presence associated with the forwarding rule's region. The load balancer uses a regional external IP address. Using a Standard Tier forwarding rule limits you to instance group and zonal NEG backends in the same region as the load balancer's forwarding rule.
  2. **From first-layer GFE to second-layer GFE**. The first-layer GFE terminates TLS if required and then routes traffic to second-layer GFEs according to the following process: 
     * First-layer GFEs parse the URL map and select a backend service or backend bucket.
     * For backend services with internet NEGs, the first layer-GFEs select a second-layer external forwarding gateway colocated with the first-layer GFE. The forwarding gateway sends requests to the internet NEG endpoint. This concludes the request distribution process for internet NEGs.
     * For backend services with [serverless NEGs](https://docs.cloud.google.com/load-balancing/docs/negs/serverless-neg-concepts) and [Private Service Connect (PSC) NEGs](https://docs.cloud.google.com/load-balancing/docs/negs#psc-neg), and single-region backend buckets, first-layer GFEs select a second-layer GFE in the region matching the region of the NEG or bucket. For multi-region Cloud Storage buckets, first-layer GFEs select second-layer GFEs either in the region of the bucket, or a region as close as possible to the multi-region bucket (defined by network round trip time).
     * For backend services with instance groups, [zonal NEGs with `GCE_VM_IP_PORT` endpoints](https://docs.cloud.google.com/load-balancing/docs/negs/zonal-neg-concepts), and [hybrid NEGs](https://docs.cloud.google.com/load-balancing/docs/negs/hybrid-neg-concepts), Google's capacity management system informs first-layer GFEs about the used and configured capacity for each backend. The configured capacity for a backend is defined by the [balancing mode](https://docs.cloud.google.com/load-balancing/docs/backend-service#balancing-mode), the [target capacity](https://docs.cloud.google.com/load-balancing/docs/backend-service#target-capacity) of the balancing mode, and the [capacity scaler](https://docs.cloud.google.com/load-balancing/docs/backend-service#capacity_scaler). 
       * _Standard Tier:_ first-layer GFEs select a second layer GFE in the region containing the backends.
       * _Premium Tier:_ first-layer GFEs select second-layer GFEs from a set of applicable regions. Applicable regions are all regions where backends have been configured, excluding those regions with configured backends having zero capacity. First-layer GFEs select the closest second-layer GFE in an applicable region (defined by network round-trip time). If backends are configured in two or more regions, first-layer GFEs can spill requests over to other applicable regions if a first-choice region is full. Spillover to other regions is possible when all backends in the first-choice region are at capacity.
  3. **Second layer GFEs select backends**. Second-layer GFEs are located in zones of a region. They use the following process to select a backend: 
     * For backend services with serverless NEGs, Private Service Connect NEGs, and backend buckets, second-layer GFEs forward requests to Google's production systems. This concludes the request distribution process for these backends.
     * For backend services with instance groups, zonal NEGs with `GCE_VM_IP_PORT` endpoints, and hybrid NEGs, Google's health check probe systems inform second-layer GFEs about the health check status of the backend instances or endpoints.

_Premium Tier only:_ If the second-layer GFE has no healthy backend instances or endpoints in its region, it might send requests to another second-layer GFE in a different applicable region with configured backends. Spillover between second-layer GFEs in different regions doesn't exhaust all possible region-to-region combinations. If you need to direct traffic away from backends in a particular region, instead of configuring backends to fail health checks, [set the capacity scaler of the backend to zero](https://docs.cloud.google.com/load-balancing/docs/backend-service#capacity_scaler) so that the first-layer GFE excludes the region during the previous step.

The second-layer GFE then directs requests to backend instances or endpoints in zones within its region as discussed in the next step.

  4. **Second layer GFE selects a zone.** By default, second-layer GFEs use the `WATERFALL_BY_REGION` algorithm where each second-layer GFE prefers to select backend instances or endpoints in the same zone as the zone that contains the second-layer GFE. Because `WATERFALL_BY_REGION` minimizes traffic between zones, at low request rates, each second-layer GFE might exclusively send requests to backends in the same zone as the second-layer GFE itself.

For global external Application Load Balancers only, second-layer GFEs can be configured to use one of the following alternative algorithms by using a [`serviceLbPolicy`](https://docs.cloud.google.com/load-balancing/docs/service-lb-policy):

     * `SPRAY_TO_REGION`: Second-layer GFEs don't prefer selecting backend instances or endpoints in the same zone as the second-layer GFE. Second-layer GFEs attempt to distribute traffic to all backend instances or endpoints in all zones of the region. This can lead to more even distribution of load at the expense of increased traffic between zones.
     * `WATERFALL_BY_ZONE`: Second-layer GFEs strongly prefer selecting backend instances or endpoints in the same zone as the second-layer GFE. Second-layer GFEs only direct requests to backends in different zones after all backends in the current zone have reached their configured capacities.
  5. **Second layer GFE selects instances or endpoints within the zone.** By default, a second-layer GFE distributes requests among backends in a round-robin fashion. For global external Application Load Balancers only, you can change this by using a load balancing locality policy (`localityLbPolicy`). The load balancing locality policy applies only to backends within the selected zone discussed in the previous step. 



### Regional external Application Load Balancer

For regional external Application Load Balancers, traffic distribution is based on the load balancing mode and the load balancing locality policy.

The balancing mode determines the weight and fraction of traffic to send to each group (instance group or NEG). The load balancing locality policy (`LocalityLbPolicy`) determines how backends within the group are load balanced.

When a backend service receives traffic, it first directs traffic to a backend (instance group or NEG) according to the backend's balancing mode. After a backend is selected, traffic is then distributed among instances or endpoints in that backend group according to the load balancing locality policy.

For more information, see the following:

  * [Balancing modes](https://docs.cloud.google.com/load-balancing/docs/backend-service#traffic_distribution)
  * [Load balancing locality policy (regional backend service API documentation)](https://docs.cloud.google.com/compute/docs/reference/rest/beta/regionBackendServices).



## Session affinity

Session affinity, configured on the backend service of Application Load Balancers, provides a best-effort attempt to send requests from a particular client to the same backend as long as the number of healthy backend instances or endpoints remains constant, and as long as the previously selected backend instance or endpoint is not at capacity. The [target capacity of the balancing mode](https://docs.cloud.google.com/load-balancing/docs/backend-service#traffic_distribution) determines when the backend is at capacity.

The following table outlines the different types of session affinity options supported for the different Application Load Balancers. In the section that follows, Types of session affinity, each session affinity type is discussed in further detail.

**Table:** Supported session affinity settings Product | Session affinity options  
---|---  
[Global external Application Load Balancer](https://docs.cloud.google.com/load-balancing/docs/https) and [Regional external Application Load Balancer](https://docs.cloud.google.com/load-balancing/docs/https) | 

  * None (`NONE`)
  * Client IP (`CLIENT_IP`)
  * Generated cookie (`GENERATED_COOKIE`)
  * Header field (`HEADER_FIELD`)
  * HTTP cookie (`HTTP_COOKIE`)
  * Stateful cookie-based affinity (`STRONG_COOKIE_AFFINITY`)

Also note:

  * The effective default value of the load balancing locality policy (`localityLbPolicy`) changes according to your session affinity settings. If session affinity is not configured—that is, if session affinity remains at the default value of `NONE`—then the default value for `localityLbPolicy` is `ROUND_ROBIN`. If session affinity is set to a value other than `NONE`, then the default value for `localityLbPolicy` is `MAGLEV`. 
  * For the global external Application Load Balancer, don't configure session affinity if you're using weighted traffic splitting. If you do, the weighted traffic splitting configuration takes precedence.

  
[Classic Application Load Balancer](https://docs.cloud.google.com/load-balancing/docs/https) | 

  * None (`NONE`)
  * Client IP (`CLIENT_IP`)
  * Generated cookie (`GENERATED_COOKIE`)

  
  
Keep the following in mind when configuring session affinity:

  * Don't rely on session affinity for authentication or security purposes. Session affinity, except for stateful cookie-based session affinity, can break whenever the number of serving and healthy backends changes. For more details, see Losing session affinity.

  * The default values of the `--session-affinity` and `--subsetting-policy` flags are both `NONE`, and only one of them at a time can be set to a different value.




### Types of session affinity

The session affinity for external Application Load Balancers can be classified into one of the following categories: 

  * Hash-based session affinity (`NONE`, `CLIENT_IP`)
  * HTTP header-based session affinity (`HEADER_FIELD`)
  * Cookie-based session affinity (`GENERATED_COOKIE`, `HTTP_COOKIE`, `STRONG_COOKIE_AFFINITY`)



#### Hash-based session affinity

For hash-based session affinity, the load balancer uses the _consistent hashing algorithm_ to select an eligible backend. The session affinity setting determines which fields from the IP header are used to calculate the hash.

Hash-based session affinity can be of the following types:

  * None
  * Client IP affinity



##### None

A session affinity setting of `NONE` does _not_ mean that there is no session affinity. It means that no session affinity option is explicitly configured.

Hashing is always performed to select a backend. And a session affinity setting of `NONE` means that the load balancer uses a 5-tuple hash to select a backend. The 5-tuple hash consists of the source IP address, the source port, the protocol, the destination IP address, and the destination port.

A session affinity of `NONE` is the default value.

##### Client IP affinity

_Client IP_ session affinity (`CLIENT_IP`) is a 2-tuple hash created from the source and destination IP addresses of the packet. Client IP affinity forwards all requests from the same client IP address to the same backend, as long as that backend has capacity and remains healthy.

When you use client IP affinity, keep the following in mind:

  * The packet destination IP address is only the same as the load balancer forwarding rule's IP address if the packet is sent directly to the load balancer.
  * The packet source IP address might not match an IP address associated with the original client if the packet is processed by an intermediate NAT or proxy system before being delivered to a Google Cloud load balancer. In situations where many clients share the same effective source IP address, some backend VMs might receive more connections or requests than others.



#### HTTP header-based session affinity

With header field affinity (`HEADER_FIELD`), requests are routed to the backends based on the value of the HTTP header in the [`consistentHash.httpHeaderName` field](https://docs.cloud.google.com/compute/docs/reference/rest/v1/backendServices#BackendService.FIELDS.inlinedField_60) of the backend service. To distribute requests across all available backends, each client needs to use a different HTTP header value.

Header field affinity is supported when the following conditions are true:

  * The load balancing locality policy is `RING_HASH` or `MAGLEV`.
  * The backend service's `consistentHash` specifies the name of the HTTP header (`httpHeaderName`).



#### Cookie-based session affinity

Cookie-based session affinity can be of the following types:

  * Generated cookie affinity
  * HTTP cookie affinity
  * Stateful cookie-based session affinity



##### Generated cookie affinity

When you use generated cookie-based affinity (`GENERATED_COOKIE`), the load balancer includes an HTTP cookie in the `Set-Cookie` header in response to the initial HTTP request.

The name of the generated cookie varies depending on the type of the load balancer.

Product | Cookie name  
---|---  
Global external Application Load Balancers | `GCLB`  
Classic Application Load Balancers | `GCLB`  
Regional external Application Load Balancers | `GCILB`  
  
The generated cookie's path attribute is always a forward slash (`/`), so it applies to all backend services on the same URL map, provided that the other backend services also use generated cookie affinity.

You can configure the cookie's time to live (TTL) value between `0` and `1,209,600` seconds (inclusive) by using the `affinityCookieTtlSec` backend service parameter. If `affinityCookieTtlSec` isn't specified, the default TTL value is `0`.

When the client includes the generated session affinity cookie in the `Cookie` request header of HTTP requests, the load balancer directs those requests to the same backend instance or endpoint, as long as the session affinity cookie remains valid. This is done by mapping the cookie value to an index that references a specific backend instance or an endpoint, and by making sure that the generated cookie session affinity requirements are met.

To use generated cookie affinity, configure the following balancing mode and `localityLbPolicy` settings:

  * For backend instance groups, use the `RATE` balancing mode.
  * For the `localityLbPolicy` of the backend service, use either `RING_HASH` or `MAGLEV`. If you don't explicitly set the `localityLbPolicy`, the load balancer uses `MAGLEV` as an implied default.



For more information, see losing session affinity.

##### HTTP cookie affinity

When you use HTTP cookie-based affinity (`HTTP_COOKIE`), the load balancer includes an HTTP cookie in the `Set-Cookie` header in response to the initial HTTP request. You specify the name, path, and time to live (TTL) for the cookie.

All Application Load Balancers support HTTP cookie-based affinity.

You can configure the cookie's TTL values using seconds, fractions of a second (as nanoseconds), or both seconds plus fractions of a second (as nanoseconds) using the following backend service parameters and valid values:

  * `consistentHash.httpCookie.ttl.seconds` can be set to a value between `0` and `315576000000` (inclusive).
  * `consistentHash.httpCookie.ttl.nanos` can be set to a value between `0` and `999999999` (inclusive). Because the units are nanoseconds, `999999999` means `.999999999` seconds.



If both `consistentHash.httpCookie.ttl.seconds` and `consistentHash.httpCookie.ttl.nanos` aren't specified, the value of the `affinityCookieTtlSec` backend service parameter is used instead. If `affinityCookieTtlSec` isn't specified, the default TTL value is `0`.

When the client includes the HTTP session affinity cookie in the `Cookie` request header of HTTP requests, the load balancer directs those requests to the same backend instance or endpoint, as long as the session affinity cookie remains valid. This is done by mapping the cookie value to an index that references a specific backend instance or an endpoint, and by making sure that the generated cookie session affinity requirements are met.

To use HTTP cookie affinity, configure the following balancing mode and `localityLbPolicy` settings:

  * For backend instance groups, use the `RATE` balancing mode.
  * For the `localityLbPolicy` of the backend service, use either `RING_HASH` or `MAGLEV`. If you don't explicitly set the `localityLbPolicy`, the load balancer uses `MAGLEV` as an implied default.



For more information, see losing session affinity.

##### Stateful cookie-based session affinity

When you use stateful cookie-based affinity (`STRONG_COOKIE_AFFINITY`), the load balancer includes an HTTP cookie in the `Set-Cookie` header in response to the initial HTTP request. You specify the name, path, and time to live (TTL) for the cookie.

All Application Load Balancers, except for classic Application Load Balancers, support stateful cookie-based affinity.

You can configure the cookie's TTL values using seconds, fractions of a second (as nanoseconds), or both seconds plus fractions of a second (as nanoseconds). The duration represented by `strongSessionAffinityCookie.ttl` cannot be set to a value representing more than two weeks (1,209,600 seconds).

The value of the cookie identifies a selected backend instance or endpoint by encoding the selected instance or endpoint in the value itself. For as long as the cookie is valid, if the client includes the session affinity cookie in the `Cookie` request header of subsequent HTTP requests, the load balancer directs those requests to selected backend instance or endpoint.

Unlike other session affinity methods:

  * Stateful cookie-based affinity has no specific requirements for the balancing mode or for the load balancing locality policy (`localityLbPolicy`).

  * Stateful cookie-based affinity is not affected when autoscaling adds a new instance to a managed instance group.

  * Stateful cookie-based affinity is not affected when autoscaling removes an instance from a managed instance group _unless_ the selected instance is removed.

  * Stateful cookie-based affinity is not affected when autohealing removes an instance from a managed instance group _unless_ the selected instance is removed.




For more information, see losing session affinity.

#### Meaning of zero TTL for cookie-based affinities

All cookie-based session affinities, such as generated cookie affinity, HTTP cookie affinity, and stateful cookie-based affinity, have a TTL attribute.

A TTL of zero seconds means the load balancer does not assign an `Expires` attribute to the cookie. In this case, the client treats the cookie as a session cookie. The definition of a _session_ varies depending on the client:

  * Some clients, like web browsers, retain the cookie for the entire browsing session. This means that the cookie persists across multiple requests until the application is closed.

  * Other clients treat a session as a single HTTP request, discarding the cookie immediately after.




### Losing session affinity

All session affinity options require the following:

  * The selected backend instance or endpoint must remain configured as a backend. Session affinity can break when one of the following events occurs: 
    * You remove the selected instance from its instance group.
    * Managed instance group autoscaling or autohealing removes the selected instance from its managed instance group.
    * You remove the selected endpoint from its NEG.
    * You remove the instance group or NEG that contains the selected instance or endpoint from the backend service.
  * The selected backend instance or endpoint must remain healthy. Session affinity can break when the selected instance or endpoint fails health checks.
  * For Global external Application Load Balancers and Classic Application Load Balancers, session affinity can break if a different first-layer Google Front End (GFE) is used for subsequent requests or connections after the change in routing path. A different first-layer GFE might be selected if the routing path from a client on the internet to Google changes between requests or connections. 

Except for stateful cookie-based session affinity, all session affinity options have the following additional requirements: 

  * The instance group or NEG that contains the selected instance or endpoint must not be full as defined by its [target capacity](https://docs.cloud.google.com/load-balancing/docs/backend-service#target-capacity). (For regional managed instance groups, the zonal component of the instance group that contains the selected instance must not be full.) Session affinity can break when the instance group or NEG is full and other instance groups or NEGs are not. Because fullness can change in unpredictable ways when using the `UTILIZATION` balancing mode, you should use the `RATE` or `CONNECTION` balancing mode to minimize situations when session affinity can break.

  * The _total number_ of configured backend instances or endpoints must remain constant. When at least one of the following events occurs, the number of configured backend instances or endpoints changes, and session affinity can break:

    * Adding new instances or endpoints:

      * You add instances to an existing instance group on the backend service.
      * Managed instance group autoscaling adds instances to a managed instance group on the backend service.
      * You add endpoints to an existing NEG on the backend service.
      * You add non-empty instance groups or NEGs to the backend service.
    * Removing any instance or endpoint, _not just the selected instance or endpoint_ :

      * You remove any instance from an instance group backend.
      * Managed instance group autoscaling or autohealing removes any instance from a managed instance group backend.
      * You remove any endpoint from a NEG backend.
      * You remove any existing, non-empty backend instance group or NEG from the backend service.
  * The _total number_ of healthy backend instances or endpoints must remain constant. When at least one of the following events occurs, the number of healthy backend instances or endpoints changes, and session affinity can break:

    * Any instance or endpoint passes its health check, transitioning from unhealthy to healthy.
    * Any instance or endpoint fails its health check, transitioning from healthy to unhealthy or timeout.



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
