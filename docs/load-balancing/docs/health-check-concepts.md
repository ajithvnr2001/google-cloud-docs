---
url: https://docs.cloud.google.com/load-balancing/docs/health-check-concepts/
title: Health checks overview \u00a0|\u00a0 Cloud Load Balancing \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T04:41:18.464115+00:00
---

# Health checks overview  |  Cloud Load Balancing  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/load-balancing/docs/health-check-concepts/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Networking ](https://docs.cloud.google.com/docs/networking)
  * [ Load Balancing ](https://docs.cloud.google.com/load-balancing/docs)
  * [ Guides ](https://docs.cloud.google.com/load-balancing/docs/load-balancing-overview)



Send feedback 

#  Health checks overview Stay organized with collections  Save and categorize content based on your preferences. 

Google Cloud offers configurable health checks for [Google Cloud load balancer](https://docs.cloud.google.com/load-balancing/docs/load-balancing-overview) backends, Cloud Service Mesh backends, and [application-based autohealing for managed instance groups](https://docs.cloud.google.com/compute/docs/instance-groups#autohealing). This document covers key health checking concepts.

Unless otherwise noted, Google Cloud health checks are implemented by dedicated software tasks that connect to backends according to parameters specified in a health check resource. Each connection attempt is called a _probe_. Google Cloud records the success or failure of each probe.

Based on a configurable number of sequential successful or failed probes, an overall health state is computed for each backend. Backends that respond successfully for the configured number of times are considered _healthy_. Backends that fail to respond successfully for a separately configurable number of times are _unhealthy_.

The overall health state of each backend determines eligibility to receive new requests or connections. You can configure the criteria that define a successful probe. This is discussed in detail in the section How health checks work.

Health checks implemented by dedicated software tasks use special routes that aren't defined in your Virtual Private Cloud (VPC) network. For more information, see [Paths for health checks](https://docs.cloud.google.com/vpc/docs/routes#health_checks_for_all_load_balancer_types).

### Health check categories, protocols, and ports

Health checks have a _category_ and a _protocol_. The two categories are _health checks_ and _legacy health checks_ and their supported protocols are as follows:

  * Health checks

    * [Regional (gRPC, gRPC (with TLS), TCP, SSL, HTTP, HTTPS, or HTTP/2)](https://docs.cloud.google.com/compute/docs/reference/rest/v1/regionHealthChecks)
    * [Global (gRPC, gRPC (with TLS), TCP, SSL, HTTP, HTTPS, or HTTP/2)](https://docs.cloud.google.com/compute/docs/reference/rest/v1/healthChecks)
  * Legacy health checks:

    * [Legacy global (HTTP)](https://docs.cloud.google.com/compute/docs/reference/rest/v1/httpHealthChecks)
    * [Legacy global (HTTPS)](https://docs.cloud.google.com/compute/docs/reference/rest/v1/httpsHealthChecks)



The protocol and port determine how health check probes are done. For example, a health check can use the HTTP protocol on TCP port 80, or it can use the TCP protocol for a named port in an instance group.

You cannot convert a legacy health check to a health check, and you cannot convert a health check to a legacy health check.

**Note:** The term _health check_ does not refer to legacy health checks. In this document, legacy health checks are explicitly called _legacy health checks_. Also note that this document uses the term _instance group_ to refer to unmanaged instance groups, zonal managed instance groups, and regional managed instance groups.

## Select a health check

Health checks must be compatible with the type of load balancer (or Cloud Service Mesh) and the backend types. The factors to consider when you select a health check are as follows:

  * **Category:** health check or legacy health check. Only [target pool-based regional external passthrough Network Load Balancers](https://docs.cloud.google.com/load-balancing/docs/network/networklb-target-pools) require legacy health checks. For all other products, you'll use regular health checks.
  * **Protocol:** protocol that Google Cloud uses to probe the backends. It's _best_ to use a health check (or legacy health check) whose protocol matches the protocol used by the load balancer's backend service or target pool. However, the health check protocols and load balancer protocols do **not** need to be the same.
  * **Port specification:** ports that Google Cloud uses with the protocol. You must specify a port for your health check. Health checks have two port specification methods: `--port` and `--use-serving-port`. For legacy health checks, there is one method: `--port`. For more information about health check port requirements per load balancer, see [Port specification flags](https://docs.cloud.google.com/load-balancing/docs/health-checks#hc-port-flags).



The next section describes valid health check selections for each type of load balancer and backend.

### Load balancer guide

This table shows the supported health check category and scope for each load balancer type.

Load balancer | Health check category and scope  
---|---  
[Global external Application Load Balancer](https://docs.cloud.google.com/load-balancing/docs/https)  
  
[Classic Application Load Balancer](https://docs.cloud.google.com/load-balancing/docs/https) [*](https://docs.cloud.google.com/load-balancing/docs/health-check-concepts#http-lb-legacy-hc-note)  
  
[Global external proxy Network Load Balancer](https://docs.cloud.google.com/load-balancing/docs/tcp)  
  
[Classic proxy Network Load Balancer](https://docs.cloud.google.com/load-balancing/docs/tcp)  
  
[Cross-region internal Application Load Balancer](https://docs.cloud.google.com/load-balancing/docs/l7-internal)  
  
[Cross-region internal proxy Network Load Balancer](https://docs.cloud.google.com/load-balancing/docs/tcp/internal-proxy) | Health check ([global](https://docs.cloud.google.com/compute/docs/reference/rest/v1/healthChecks))  
[Regional external Application Load Balancer](https://docs.cloud.google.com/load-balancing/docs/https)  
  
[Regional internal Application Load Balancer](https://docs.cloud.google.com/load-balancing/docs/l7-internal)  
  
[Regional internal proxy Network Load Balancer](https://docs.cloud.google.com/load-balancing/docs/tcp/internal-proxy)  
  
[Regional external proxy Network Load Balancer](https://docs.cloud.google.com/load-balancing/docs/tcp) | Health check ([regional](https://docs.cloud.google.com/compute/docs/reference/rest/v1/regionHealthChecks))  
[Global external passthrough Network Load Balancer](https://docs.cloud.google.com/load-balancing/docs/network/global-networklb-architecture) | Health check ([global](https://docs.cloud.google.com/compute/docs/reference/rest/v1/healthChecks))   
[Regional external passthrough Network Load Balancer](https://docs.cloud.google.com/load-balancing/docs/network) | Backend service-based load balancer: Health check ([regional](https://docs.cloud.google.com/compute/docs/reference/rest/v1/regionHealthChecks)) Target pool-based load balancer: Legacy health check   
([global with the HTTP protocol](https://docs.cloud.google.com/compute/docs/reference/rest/v1/httpHealthChecks))  
[Internal passthrough Network Load Balancer](https://docs.cloud.google.com/load-balancing/docs/internal) | Health check ([global](https://docs.cloud.google.com/compute/docs/reference/rest/v1/healthChecks) or [regional](https://docs.cloud.google.com/compute/docs/reference/rest/v1/regionHealthChecks))  
  
* For external Application Load Balancers, legacy health checks are _not_ recommended but are sometimes supported, depending on the load balancer mode. Load balancer mode | Legacy health checks supported  
---|---  
Global external Application Load Balancer  Classic Application Load Balancer | Yes, if both of the following are true:  


  * The backends are instance groups.
  * The backend VMs serve traffic that uses the HTTP or HTTPS protocol.

  
Regional external Application Load Balancer | No  
  
#### Additional usage notes

  * For backend instance groups, zonal NEGs with `GCE_VM_IP` endpoints, and zonal NEGs with `GCE_VM_IP_PORT` endpoints, probers only attempt to connect to VM instances (or VM instances that contain endpoints) if the VMs are running. Probers don't attempt to connect to instances (or VM instances that contain endpoints) if they are stopped.

  * A target pool-based regional external passthrough Network Load Balancer must use a legacy HTTP health check. It cannot use a legacy HTTPS health check or any non-legacy health check. If you use a target pool-based regional external passthrough Network Load Balancer to balance TCP traffic, you need to run an HTTP service on the VMs being load balanced so that they can respond to health check probes.   
  
For [ almost all other load balancer types](https://docs.cloud.google.com/load-balancing/docs/health-check-concepts#http-lb-legacy-hc-note), you _must_ use regular, non-legacy health checks where the protocol matches the load balancer's backend service protocol.

  * For backend services that use the gRPC protocol, use only gRPC or TCP health checks. Don't use HTTP(S) or HTTP/2 health checks.

  * Certain Envoy-based load balancers that use hybrid NEG backends don't support gRPC health checks. For more information, see the [Hybrid NEGs overview](https://docs.cloud.google.com/load-balancing/docs/negs/hybrid-neg-concepts#envoy-health-checks).




### Health checking with Cloud Service Mesh

Note the following differences in behavior when you're using health checks with Cloud Service Mesh.

  * With Cloud Service Mesh, health checking behavior for network endpoints of the type `INTERNET_FQDN_PORT` and `NON_GCP_PRIVATE_IP_PORT` differs from health checking behavior for other types of network endpoints. Instead of using the dedicated software tasks, Cloud Service Mesh programs Envoy proxies to perform health checks for internet NEGs (`INTERNET_FQDN_PORT` endpoints) and hybrid NEGs (`NON_GCP_PRIVATE_IP_PORT` endpoints).

Envoy supports the following protocols for health checking:

    * HTTP
    * HTTPS
    * HTTP/2
    * TCP
  * When Cloud Service Mesh is integrated with Service Directory and you bind a Service Directory service to a Cloud Service Mesh backend service, you cannot set a health check on the backend service.




## Probe IP ranges

Google Cloud requires that you create the necessary ingress `allow` firewall rules to permit traffic from probers to your backends or other resources. Note the following when you create these firewall rules:

  * The probe IP ranges are a complete set of _possible_ IP addresses used by Google Cloud probers. If you use `tcpdump` or a similar tool, you might not observe traffic from all IP addresses in all probe IP ranges. As a best practice, create ingress firewall rules that allow _all of the probe IP ranges as sources_. Google Cloud can implement new probers automatically without notification.

  * As a best practice, limit these rules to just the protocols and ports that match those used by your health checks.




If you don't have ingress `allow` firewall rules that permit health check probers to connect to your load balancer backends, the implied deny ingress firewall action blocks traffic, causing your backends to be unhealthy. For more information, see [Firewall policies and rules](https://docs.cloud.google.com/firewall/docs/firewall-policies-overview#default-rule-evaluation).

### Probe IP ranges for GFE-based load balancer backends

External Application Load Balancers and external proxy Network Load Balancers that use Google Front Ends (GFEs) are:

  * Global external Application Load Balancers
  * Classic Application Load Balancers
  * Global external proxy Network Load Balancers
  * Classic proxy Network Load Balancers



Health checks for backends of these load balancers come from the IP address ranges in the following table:

Backend type | Health check probe source IP ranges  
---|---  
  
  * Instance groups
  * Zonal NEGs with `GCE_VM_IP_PORT` endpoints
  * Hybrid connectivity NEGs (`NON_GCP_PRIVATE_IP_PORT` endpoints)

|  For IPv4 health checks to the backends:

  * `35.191.0.0/16`

For IPv6 health checks to the backends:

  * `2600:2d00:1:b029::/64`

  
  
  * Global internet NEG (with either `INTERNET_IP_PORT` or `INTERNET_FQDN_PORT` endpoints)
  * Serverless NEG (`SERVERLESS` endpoint)
  * Private Service Connect NEG (`PRIVATE_SERVICE_CONNECT` endpoint)

| Not applicable (these backends don't support health checks)  
  
### Probe IP ranges for Cloud Service Mesh backends

Health checks for Cloud Service Mesh backends come from the IP address ranges in the following table:

Backend type | Health check probe source IP ranges  
---|---  
  
  * Instance groups
  * Zonal NEGs with `GCE_VM_IP_PORT` endpoints

|  For IPv4 health checks to the backends:

  * `35.191.0.0/16`

For IPv6 health checks to the backends:

  * `2600:2d00:1:b029::/64`

  
  
  * Global internet NEG (with either `INTERNET_IP_PORT` or `INTERNET_FQDN_PORT` endpoints)
  * Hybrid connectivity NEGs (`NON_GCP_PRIVATE_IP_PORT` endpoints)

| Distributed Envoy health checks from the IP addresses of your self-managed Envoy proxies  
  
### Probe IP ranges for managed Envoy-based load balancer backends

Application Load Balancers and proxy Network Load Balancers that use managed Envoy proxies are:

  * Regional external Application Load Balancers

  * Regional internal Application Load Balancers



  * Cross-region internal Application Load Balancers


  * Regional external proxy Network Load Balancers

  * Regional internal proxy Network Load Balancers



  * Cross-region internal proxy Network Load Balancers



Health checks for backends of these load balancers come from the IP address ranges in the following table:

Backend type | Health check probe source IP ranges  
---|---  
  
  * Instance groups
  * Zonal NEGs with `GCE_VM_IP_PORT` endpoints

|  For IPv4 health checks to the backends:

  * `35.191.0.0/16`

For IPv6 health checks to the backends:

  * `2600:2d00:1:b029::/64`

  
  
  * Hybrid connectivity NEGs (`NON_GCP_PRIVATE_IP_PORT` endpoints)
  * Regional internet NEG (with either `INTERNET_IP_PORT` or `INTERNET_FQDN_PORT` endpoints)

| Distributed Envoy health checks from the IP addresses of the [Proxy-only subnet](https://docs.cloud.google.com/load-balancing/docs/proxy-only-subnets)  
  
  * Serverless NEG (`SERVERLESS` endpoint)
  * Private Service Connect NEG (`PRIVATE_SERVICE_CONNECT` endpoint)

| Not applicable (these backends don't support health checks)  
  
### Probe IP ranges for select managed Envoy-based load balancer frontends

The following Application Load Balancers and proxy Network Load Balancers use managed Envoy proxies and also support firewall rules that control access to the managed Envoy proxies themselves:

  * Regional internal Application Load Balancers


  * Cross-region internal Application Load Balancers


  * Regional internal proxy Network Load Balancers


  * Cross-region internal proxy Network Load Balancers



For more information about this option, see [Use regional network firewall policies to protect internal Application Load Balancers and internal proxy Network Load Balancers](https://docs.cloud.google.com/firewall/docs/regional-network-app-lb).

If you choose to create ingress deny and ingress allow firewall rules to control access to a forwarding rule of one of these load balancers, you must create ingress allow firewall rules to allow Google systems to monitor the health of the managed Envoy proxies.

For IPv4 health checks to the forwarding rule: 

  * `35.191.0.0/16`



For IPv6 health checks to the forwarding rule: 

  * `2600:2d00:1:b029::/64`



The health checks that Google uses to monitor the managed Envoy proxies are an internal implementation detail, not a user-configurable health check.

### Probe IP ranges for passthrough Network Load Balancer backends

Health checks for backends of passthrough Network Load Balancers come from the IP address ranges in the following table:

Load balancer and backend type | Health check probe source IP ranges  
---|---  
Global external passthrough Network Load Balancers using one of the following backends:

  * Instance groups
  * Zonal NEGs with `GCE_VM_IP` endpoints

|  For IPv4 health checks to the backends:

  * `136.124.104.0/22`
  * `136.124.108.0/22`

For IPv6 health checks to the backends:

  * `2600:1904:7::/48`
  * `2600:1904:8::/48`

  
Regional external passthrough Network Load Balancers using one of the following backends1:

  * Instance groups
  * Zonal NEGs with `GCE_VM_IP` endpoints

|  For IPv4 health checks to the backends:

  * `35.191.0.0/16`
  * `209.85.152.0/22` (for target pools)
  * `209.85.204.0/22`

For IPv6 health checks to the backends:

  * `2600:1901:8001::/48`

  
Internal passthrough Network Load Balancers using one of the following backends:

  * Instance groups
  * Zonal NEGs with `GCE_VM_IP` endpoints

|  For IPv4 health checks to the backends:

  * `35.191.0.0/16`

For IPv6 health checks to the backends:

  * `2600:2d00:1:b029::/64`

  
  
1 Target pool-based external passthrough Network Load Balancers support only IPv4 traffic and might proxy health checks through the metadata server. In this case, health check packet sources match the IP address of the metadata server: `169.254.169.254`. You don't have to create firewall rules to permit traffic from the metadata server. Packets from the metadata server are [always allowed](https://docs.cloud.google.com/vpc/docs/firewalls#alwaysallowed).

## How health checks work

The following sections describe how health checks work.

### Probes

When you [create a health check](https://docs.cloud.google.com/load-balancing/docs/health-checks#create_a_health_check) or [a legacy health check](https://docs.cloud.google.com/load-balancing/docs/health-checks#legacy-health-checks), you specify the following flags or accept their default values. Each health check or legacy health check that you create is implemented by multiple probes. These flags control how frequently _each_ probe evaluates instances in instance groups or endpoints in zonal NEGs.

A health check's settings cannot be configured on a per-backend basis. Health checks are associated with an entire backend service. For a target pool-based regional external passthrough Network Load Balancer, a legacy HTTP health check is associated with the entire target pool. Thus, the parameters for the probe are the same for all backends referenced by a given backend service or target pool.

Configuration flag | Purpose | Default value  
---|---|---  
Check interval  
`check-interval` | The check interval is the amount of time from the start of one probe _issued by one prober_ to the start of the next probe _issued by the same prober_. Units are seconds. | `5s` (5 seconds)  
Timeout  
`timeout` | The timeout is the amount of time that Google Cloud waits for a response to a probe. Its value must be less than or equal to the check interval. Units are seconds. | `5s` (5 seconds)  
  
### Security considerations for probe IP ranges

Consider the following information when planning health checks and the necessary firewall rules:

  * The probe IP ranges belong to Google. Google Cloud uses [special routes](https://docs.cloud.google.com/vpc/docs/routes#special-lb-paths) outside of your VPC network, but within Google's production network, for communicating between health check probers and backend VMs.

  * The probe IP ranges are used exclusively within Google's production network for health check and load balancing. Google Cloud and Google's production network prevent the probe IP ranges from being used for any other purpose by enforcing the following:

    * Google edge routers drop packets from the internet if the packets spoof source IP addresses from a probe IP range.

    * You can't use the probe IP ranges for subnets in your VPC networks. For more information, see [Prohibited IPv4 subnet ranges](https://docs.cloud.google.com/vpc/docs/subnets#restricted-ranges) and [IPv6 specifications](https://docs.cloud.google.com/vpc/docs/subnets#ipv6-specifications).




#### Importance of firewall rules

Google Cloud requires that you create the necessary ingress `allow` firewall rules to permit traffic from probers to your backends:

  * The probe IP ranges are a complete set of _possible_ IP addresses used by Google Cloud probers. If you use `tcpdump` or a similar tool, you might not observe traffic from all IP addresses in all probe IP ranges. As a best practice, create ingress firewall rules that allow _all of the probe IP ranges as sources_. Google Cloud can implement new probers automatically without notification.

  * As a best practice, limit these rules to just the protocols and ports that match those used by your health checks.




If you don't have ingress `allow` firewall rules that permit the health check, the [implied `deny` ingress rule](https://docs.cloud.google.com/firewall/docs/firewall-policies-rule-eval-order#default-rule-evaluation) blocks inbound traffic. When probers can't contact your backends, the load balancer considers your backends to be unhealthy.

### Multiple probes and frequency

Google Cloud sends health check probes from multiple redundant systems called probers. Probers use specific source IP ranges. Google Cloud does not rely on just one prober to implement a health check—multiple probers simultaneously evaluate the instances in instance group backends or the endpoints in zonal NEG backends. If one prober fails, Google Cloud continues to track backend health states.

The interval and timeout settings that you configure for a health check are applied to each prober. For a given backend, software access logs and `tcpdump` show more frequent probes than your configured settings.

This is expected behavior, and you cannot configure the number of probers that Google Cloud uses for health checks. However, you can estimate the effect of multiple simultaneous probes by considering the following factors.

  * To estimate the probe frequency per backend service, consider the following:

    * **Base frequency per backend service.** Each health check has an associated check frequency, inversely proportional to the configured check interval:

1⁄(check interval)

When you associate a health check with a backend service, you establish a base frequency used by each prober for backends on that backend service.

    * **Probe scale factor.** The backend service's base frequency is multiplied by the number of simultaneous probers that Google Cloud uses. This number can vary, but is generally between 5 and 10.

  * **Multiple forwarding rules for passthrough Network Load Balancers.** If you have configured multiple forwarding rules (with different IP addresses) that have the same instance group or zonal NEG as a backend, Google Cloud uses multiple probers to check the health of each IP address on the backend. The probe frequency on each backend instance or endpoint is multiplied by the number of unique forwarding rule IP addresses it is serving. For example:

    * If you create two regional external passthrough Network Load Balancer forwarding rules with different IP addresses that point to the same backend service, the probe frequency on each backend instance or endpoint of the backend service is multiplied by 2.

    * If you create one global external passthrough Network Load Balancer, one regional external passthrough Network Load Balancer and one internal passthrough Network Load Balancer forwarding rule that share the same instance group as a backend, the probe frequency on each backend instance of the instance group is multiplied by 4. This is because a global external passthrough Network Load Balancer forwarding rule is assigned two IP addresses and, therefore, the probe frequency of its backend instances or endpoints are always twice that of the configured health check frequency.

  * **Multiple target proxies for external Application Load Balancers.** If you have multiple target proxies that direct traffic to the same URL map, Google Cloud uses multiple probers to check the IP address associated with each target proxy. The probe frequency per backend service is multiplied by the number of configured target proxies.

  * **Multiple target proxies for external proxy Network Load Balancers and regional internal proxy Network Load Balancers.** If you have configured multiple target proxies that direct traffic to the same backend service, Google Cloud uses multiple probers to check the IP address associated with each target proxy. The probe frequency per backend service is multiplied by the number of configured target proxies.

  * **Sum over backend services.** If a backend is used by multiple backend services, the backend instances are contacted as frequently as the sum of frequencies for each backend service's health check.

With zonal NEG backends, it's more difficult to determine the exact number of health check probes. For example, the same endpoint can be in multiple zonal NEGs. Those zonal NEGs don't necessarily have the same set of endpoints, and different endpoints can point to the same backend.




### Destination for probe packets

The following table shows the network interface and destination IP addresses to which health check probers send packets, depending on the type of load balancer.

For passthrough Network Load Balancers, the application must bind to the load balancer's IP address (or any IP address `0.0.0.0`).

Load balancer | Destination network interface | Destination IP address  
---|---|---  
  
  * Global external Application Load Balancer
  * Global external proxy Network Load Balancer

| 

  * For instance group backends, the primary network interface (`nic0`).
  * For zonal NEG backends with `GCE_VM_IP_PORT` endpoints, the network interface in the VPC network that's associated with the NEG.
  * For zonal NEG backends with `NON_GCP_PRIVATE_IP_PORT` endpoints, the endpoint must represent an interface of an on-premises resource that's reachable by way of a route in the VPC network associated with the NEG _and in the region that contains the NEG_.

| 

  * For instance group backends, the primary internal IPv4 or IPv6 address associated with the primary network interface (`nic0`) of each instance.
  * For zonal NEG backends with `GCE_VM_IP_PORT` endpoints, the IP address of the endpoint: either a primary internal IPv4 or IPv6 address of the network interface or an internal IPv4 or IPv6 address from an alias IP range of the network interface.
  * For zonal NEG backends with `NON_GCP_PRIVATE_IP_PORT` endpoints, the IP address of the endpoint.

  
  
  * Classic Application Load Balancer
  * Regional external Application Load Balancer
  * Cross-region internal Application Load Balancer
  * Regional internal Application Load Balancer
  * Classic proxy Network Load Balancer
  * Regional external proxy Network Load Balancer
  * Cross-region internal proxy Network Load Balancer 1
  * Regional internal proxy Network Load Balancer
  * Cloud Service Mesh

| 

  * For instance group backends, the primary network interface (`nic0`).
  * For zonal NEG backends with `GCE_VM_IP_PORT` endpoints, the network interface in the VPC network that's associated with the NEG.
  * For zonal NEG backends with `NON_GCP_PRIVATE_IP_PORT` endpoints, the endpoint must represent an interface of an on-premises resource that's reachable by way of a route in the VPC network associated with the NEG _and in the region that contains the NEG_.

| 

  * For instance group backends, the primary internal IPv4 address associated with the primary network interface (`nic0`) of each instance.
  * For zonal NEG backends with `GCE_VM_IP_PORT` endpoints, the IP address of the endpoint: either a primary internal IPv4 address of the network interface or an internal IPv4 address from an alias IP range of the network interface.
  * For zonal NEG backends with `NON_GCP_PRIVATE_IP_PORT` endpoints, the IP address of the endpoint.

  
  
  * Global external passthrough Network Load Balancer
  * Regional external passthrough Network Load Balancer

|  For instance group backends, the primary network interface (`nic0`). For zonal NEG backends with `GCE_VM_IP` endpoints, the network interface in the VPC subnetwork that's associated with the NEG. | The IP address(es) associated with the forwarding rule. If you configure multiple forwarding rules (with different IP addresses) that have the same instance group or zonal NEG as a backend, Google Cloud uses multiple probers to check the health of each IP address, increasing the probe frequency on each backend instance or endpoint of the backend. For details, see [Multiple probes and frequency](https://docs.cloud.google.com/load-balancing/docs/health-check-concepts#multiple-probers).  
  
  * Internal passthrough Network Load Balancer

|  The network interface in the VPC network that matches the [ Backend service network specification](https://docs.cloud.google.com/load-balancing/docs/internal#backend-service-network-spec). | The IP address associated with the forwarding rule. If you configure multiple forwarding rules (with different IP addresses) that have the same instance group or zonal NEG as a backend, Google Cloud uses multiple probers to check the health of each IP address, increasing the probe frequency on each backend instance or endpoint of the backend. For details, see [Multiple probes and frequency](https://docs.cloud.google.com/load-balancing/docs/health-check-concepts#multiple-probers).   
  
### Success criteria for HTTP, HTTPS, and HTTP/2

HTTP, HTTPS, and HTTP/2 health checks always require an HTTP `200 (OK)` response code to be received before the health check timeout. All other HTTP response codes, including redirect response codes like `301` and `302`, are considered unhealthy.

In addition to requiring an HTTP `200 (OK)` response code, you can:

  * Configure each health check prober to send HTTP requests to a specific request path instead of the default request path, `/`.

  * Configure each health check prober to check for the presence of an expected response string in the HTTP response body. The expected response string must consist only of single-byte, printable ASCII characters, located within the first 1,024 bytes of the HTTP response body.




The following table lists valid combinations of request path and response flags that are available for HTTP, HTTPS, and HTTP/2 health checks.

Configuration flags | Prober behavior | Success criteria  
---|---|---  
Neither `--request-path` nor `--response` specified  | The prober uses `/` as the request path. | HTTP `200 (OK)` response code only.  
Both `--request-path` and `--response` specified  | The prober uses the configured request path. | HTTP `200 (OK)` response code _and_ up to the first 1,024 ASCII characters of the HTTP response body must match the expected response string.  
Only `--response` specified  | The prober uses `/` as the request path. | HTTP `200 (OK)` response code _and_ up to the first 1,024 ASCII characters of the HTTP response body must match the expected response string.  
Only `--request-path` specified  | The prober uses the configured request path. | HTTP `200 (OK)` response code only.  
  
### Success criteria for SSL and TCP

TCP and SSL health checks have the following base success criteria:

  * For TCP health checks, a health check prober must successfully open a TCP connection to the backend before the health check timeout.

  * For SSL health checks, a health check prober must successfully open a TCP connection to the backend _and_ complete the TLS/SSL handshake before the health check timeout.

  * For TCP health checks, the TCP connection must be closed in one of the following ways:

    * By the health check prober sending either a FIN _or_ RST (reset) packet, or
    * By the backend sending a FIN packet. If a backend sends a TCP RST packet, the probe _might_ be considered unsuccessful if the health check prober has already sent a FIN packet.



The following table lists valid combinations of request and response flags that are available for TCP and SSL health checks. Both request and response flags must consist only of single-byte, printable ASCII characters, each string being no more than 1,024 characters long.

Configuration flags | Prober behavior | Success criteria  
---|---|---  
Neither `--request` nor `--response` specified  | The prober doesn't send any request string. | Base success criteria only.  
Both `--request` and `--response` specified  | The prober sends the configured request string. | Base success criteria and the response string received by the prober must _exactly match_ the expected response string.  
Only `--response` specified  | The prober doesn't send any request string. | Base success criteria and the response string received by the prober must _exactly match_ the expected response string.  
Only `--request` specified  | The prober sends the configured request string. | Base success criteria only (any response string is not checked).  
  
### Success criteria for gRPC

gRPC health checks are used only with gRPC applications, Google Cloud load balancers, and Cloud Service Mesh. Google Cloud supports two types of gRPC health checks:

  * `grpc_with_tls` health checks are used for health checking gRPC backends with TLS enabled. They support unauthenticated TLS encryption, which means that the health checks don't verify the server's identity.
  * `grpc` health checks are used for health checking insecure gRPC backends. They don't support authentication and encryption, so they can't be used for gRPC backends with TLS enabled.



If you are using gRPC health checks (with or without TLS), make sure that the gRPC service sends the RPC response with the status `OK` and the status field set to `SERVING` or `NOT_SERVING` accordingly.

For more information, see the following:

  * [Additional flag for gRPC health checks](https://docs.cloud.google.com/load-balancing/docs/health-checks#optional-flags-hc-protocol-grpc)
  * [gRPC documentation for health checks](https://github.com/grpc/grpc/blob/master/doc/health-checking.md)



### Success criteria for legacy health checks

If the response received by the legacy health check probe is `HTTP 200 OK`, the probe is considered successful. All other HTTP response codes, including a redirect (`301`, `302`), are considered unhealthy.

### Health state

Google Cloud uses the following healthy and unhealthy threshold configuration flags to determine the overall health state of each backend to which traffic is load balanced.

Configuration flag | Purpose | Default value  
---|---|---  
Healthy threshold  
`healthy-threshold` | The healthy threshold specifies the number of sequential successful probe results for a _previously unhealthy backend_ 1 to be considered healthy. Previously unhealthy backends can become healthy if they are able to meet the healthy threshold again. Google Cloud considers backends to be healthy after this healthy threshold has been met. Healthy backends are eligible to receive new connections. Newly added backends might be considered healthy after a single successful probe. | A threshold of `2` probes.  
Unhealthy threshold  
`unhealthy-threshold` | The unhealthy threshold specifies the number of sequential failed probe results for a _previously healthy backend_ 2 to be considered unhealthy. Google Cloud considers backends to be unhealthy when the unhealthy threshold has been met. Unhealthy backends are not eligible to receive new connections; however, existing connections are *not* immediately terminated. Instead, the connection remains open until a timeout occurs or until traffic is dropped. | A threshold of `2` probes.  
  
1 _Previously unhealthy backend_ refers to backends that were in the `UNHEALTHY` or `TIMEOUT` [detailed health check states](https://docs.cloud.google.com/load-balancing/docs/health-check-logging#health-check-states).

2 _Previously healthy backend_ refers to backends that were in the `HEALTHY` or `DRAINING` [detailed health check states](https://docs.cloud.google.com/load-balancing/docs/health-check-logging#health-check-states).

The specific behavior when all backends are unhealthy differs depending on the type of load balancer that you're using:

Load balancer | Behavior when all backends are unhealthy  
---|---  
Classic Application Load Balancer | Returns an HTTP `502` status code to clients when all backends are unhealthy.  
Global external Application Load Balancer  
  
Cross-region internal Application Load Balancer  
  
Regional external Application Load Balancer  
  
Regional internal Application Load Balancer  | Returns an HTTP `503` status code to clients when all backends are unhealthy.  
Proxy Network Load Balancers | Terminates new client TCP connections when all backends are unhealthy.   
Global external passthrough Network Load Balancers |  If all backends are unhealthy in the closest region to the user, automatically fail over traffic to the next closest region with healthy backends and available capacity. If all backends are unhealthy globally, as a last resort, distribute traffic among unhealthy backends according to [ target capacities](https://docs.cloud.google.com/load-balancing/docs/backend-service#target-capacity-global-netlb).  
Internal passthrough Network Load Balancer  
  
Backend service-based regional external passthrough Network Load Balancers | If the failover policy is configured to drop new connections when all primary and failover backends are unhealthy, then drop all incoming traffic. Otherwise, as a last resort, distribute traffic among unhealthy backends according to failover configuration and backend weights. For details, see:

  * [ Traffic distribution for internal passthrough Network Load Balancers](https://docs.cloud.google.com/load-balancing/docs/internal/int-netlb-traffic-distribution)
  * [ Traffic distribution for backend service-based regional external passthrough Network Load Balancers](https://docs.cloud.google.com/load-balancing/docs/network/ext-netlb-traffic-distribution)

  
Target pool-based regional external passthrough Network Load Balancers | [ As a last resort, distribute traffic among all unhealthy backends](https://docs.cloud.google.com/load-balancing/docs/network/networklb-target-pools#health_checks).  
  
## Additional notes

The following sections include some more notes about using health checks on Google Cloud.

### Certificates and health checks

Google Cloud health check probers don't perform certificate validation, even for protocols that require that your backends use certificates (SSL, HTTPS, and HTTP/2)—for example:

  * You can use self-signed certificates or certificates signed by any certificate authority (CA).
  * Certificates that have expired or that are not yet valid are acceptable.
  * Neither the `CN` nor the `subjectAlternativeName` attributes need to match a `Host` header or DNS PTR record.



### Headers

Health checks that use any protocol, but not legacy health checks, allow you to set a proxy header by using the `--proxy-header` flag.

Health checks that use HTTP, HTTPS, or HTTP/2 protocols and legacy health checks allow you to specify an HTTP `Host` header by using the `--host` flag.

If you're using any custom request headers, note that the load balancer adds these headers only to the client requests, not to the health check probes. If your backend requires a specific header for authorization that is missing from the health check packet, the health check might fail.

## Example health check

Suppose you set up a health check with the following settings:

  * Interval: 30 seconds
  * Timeout: 5 seconds
  * Protocol: HTTP
  * Unhealthy threshold: 2 (default)
  * Healthy threshold: 2 (default)



With these settings, the health check behaves as follows:

  1. Multiple redundant systems are simultaneously configured with the health check parameters. Interval and timeout settings are applied _to each system_. For more information, see [Multiple probes and frequency](https://docs.cloud.google.com/load-balancing/docs/health-check-concepts#multiple-probers).
  2. Each health check prober does the following:

     1. Initiates an HTTP connection from one of the source IP addresses to the backend instance every 30 seconds.
     2. Waits up to five seconds for an HTTP `200 (OK)` status code (the success criteria for HTTP, HTTPS, and HTTP/2 protocols).
  3. A backend is considered unhealthy when at least one health check probe system does the following:

     1. Does not receive an `HTTP 200 (OK)` response code for two consecutive probes. For example, the connection might be refused, or there might be a connection or socket timeout.
     2. Receives two consecutive responses that don't match the protocol-specific success criteria.
  4. A backend is considered healthy when at least one health check probe system receives two consecutive responses that match the protocol-specific success criteria.




In this example, each prober initiates a connection every 30 seconds. Thirty seconds elapses between a prober's connection attempts regardless of the duration of the timeout (whether or not the connection timed out). In other words, the timeout must always be less than or equal to the interval, and the timeout never increases the interval.

In this example, each prober's timing looks like the following, in seconds:

  1. t=0: Start probe A.
  2. t=5: Stop probe A.
  3. t=30: Start probe B.
  4. t=35: Stop probe B.
  5. t=60: Start probe C.
  6. t=65: Stop probe C.



## What's next

  * To create, modify, and use health checks, see [Use health checks](https://docs.cloud.google.com/load-balancing/docs/health-checks).
  * To troubleshoot health checks, enable [health check logging](https://docs.cloud.google.com/load-balancing/docs/health-check-logging).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
