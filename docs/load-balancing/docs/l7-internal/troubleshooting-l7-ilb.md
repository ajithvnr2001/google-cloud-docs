---
url: https://docs.cloud.google.com/load-balancing/docs/l7-internal/troubleshooting-l7-ilb/
title: Troubleshoot issues with internal Application Load Balancers \u00a0|\u00a0 Cloud Load Balancing \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:33:28.122909+00:00
---

# Troubleshoot issues with internal Application Load Balancers  |  Cloud Load Balancing  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/load-balancing/docs/l7-internal/troubleshooting-l7-ilb/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Networking ](https://docs.cloud.google.com/docs/networking)
  * [ Load Balancing ](https://docs.cloud.google.com/load-balancing/docs)
  * [ Guides ](https://docs.cloud.google.com/load-balancing/docs/load-balancing-overview)



Send feedback 

#  Troubleshoot issues with internal Application Load Balancers Stay organized with collections  Save and categorize content based on your preferences. 

This guide describes how to troubleshoot configuration issues for a Google Cloud internal Application Load Balancer. Before following this guide, familiarize yourself with the following:

  * [Internal Application Load Balancer overview](https://docs.cloud.google.com/load-balancing/docs/l7-internal)
  * [Proxy-only subnets](https://docs.cloud.google.com/load-balancing/docs/proxy-only-subnets)
  * [Internal Application Load Balancer logging and monitoring](https://docs.cloud.google.com/load-balancing/docs/l7-internal/monitoring)



## Troubleshoot common issues with Network Analyzer

[Network Analyzer](https://docs.cloud.google.com/network-intelligence-center/docs/network-analyzer/overview) automatically monitors your VPC network configuration and detects both suboptimal configurations and misconfigurations. It identifies network failures, provides root cause information, and suggests possible resolutions. To learn about the different misconfiguration scenarios that are automatically detected by Network Analyzer, see [Load balancer insights](https://docs.cloud.google.com/network-intelligence-center/docs/network-analyzer/insights/network-services/load-balancer) in the Network Analyzer documentation.

Network Analyzer is available in the Google Cloud console as a part of Network Intelligence Center.

[Go to Network Analyzer](https://console.cloud.google.com/net-intelligence/network-analyzer)

## Backends have incompatible balancing modes

When creating a load balancer, you might see the error:
    
    
    Validation failed for instance group INSTANCE_GROUP:
    
    backend services 1 and 2 point to the same instance group
    but the backends have incompatible balancing_mode. Values should be the same.
    

This happens when you try to use the same backend in two different load balancers, and the backends don't have compatible balancing modes.

For more information, see the following:

  * [Restrictions and guidance for instance groups](https://docs.cloud.google.com/load-balancing/docs/backend-service#restrictions_and_guidance)
  * [Change the balancing mode of a load balancer](https://docs.cloud.google.com/load-balancing/docs/backend-service#change_balancing_mode)



## Load balanced traffic does not have the source address of the original client

This is expected behavior. An internal Application Load Balancer operates as an HTTP(S) reverse proxy (gateway). When a client program opens a connection to the IP address of an INTERNAL_MANAGED forwarding rule, the connection terminates at a proxy. The proxy processes the requests that arrive over that connection. For each request, the proxy selects a backend to receive the request based on the URL map and other factors. The proxy then sends the request to the selected backend. As a result, from the point of view of the backend, the source of an incoming packet is an IP address from the region's [proxy-only subnet](https://docs.cloud.google.com/load-balancing/docs/proxy-only-subnets).

## Load balancer doesn't connect to backends

The firewalls protecting your backend servers need to be configured to allow ingress traffic from the proxies in the [proxy-only subnet range](https://docs.cloud.google.com/load-balancing/docs/l7-internal/proxy-only-subnets) that you allocated to your internal HTTP(S) load balancer's region.

The proxies connect to backends using the connection settings specified by the configuration of your backend service. If these values don't match the configuration of the server(s) running on your backends, the proxy cannot forward requests to the backends.

## Health check probes can't reach the backends

To verify that health check traffic reaches your backend VMs, [enable health check logging](https://docs.cloud.google.com/load-balancing/docs/health-check-logging) and search for successful log entries.

## Clients cannot connect to the load balancer

The proxies listen for connections to the load balancer's IP address and port configured in the forwarding rule (for example, `10.1.2.3:80`), and with the protocol specified in the forwarding rule (HTTP or HTTPS). If your clients can't connect, ensure that they are using the correct address, port, and protocol.

Ensure that a firewall isn't blocking traffic between your client instances and the load balanced IP address.

Ensure that the clients are in the same region as the load balancer. Internal HTTP(S) Load Balancing is a regional product, so all clients (and backends) must be in the same region as the load balancer resource.

## Organizational policy restriction for Shared VPC

If you are using Shared VPC and you cannot create a new internal Application Load Balancer in a particular subnet, an organization policy might be the cause. In the organization policy, add the subnet to the list of allowed subnets or contact your organization administrator. For more information, see [`constraints/compute.restrictSharedVpcSubnetworks`](https://docs.cloud.google.com/resource-manager/docs/organization-policy/org-policy-constraints).

## Load balancer doesn't distribute traffic evenly across zones

You might observe an imbalance in your internal Application Load Balancer traffic across zones. This can happen especially when there is low utilization (< 10%) of your backend capacity.

Such behavior can affect overall latency due to traffic being sent to only a few servers in one zone.

To even out the traffic distribution across zones, you can make the following configuration changes:

  * Use the `RATE` [balancing mode](https://docs.cloud.google.com/load-balancing/docs/backend-service#bmtc-rate-max-per-endpoint) with a low `max-rate-per-instance` target capacity.
  * Use the `LocalityLbPolicy` backend [traffic policy](https://docs.cloud.google.com/load-balancing/docs/l7-internal/traffic-management#traffic_policies) with a load balancing algorithm of `LEAST_REQUEST`.



## Unexplained `5xx` errors

For error conditions caused by a communications issue between the load balancer proxy and its backends, the load balancer generates an HTTP status code (`5xx`) and returns that status code to the client. Not all HTTP `5xx` errors are generated by the load balancer—for example, if a backend sends an HTTP `5xx` response to the load balancer, the load balancer relays that response to its client. To determine whether an HTTP `5xx` response was relayed from a backend or if it was generated by the load balancer proxy, see the `proxyStatus` field of the [load balancer logs](https://docs.cloud.google.com/load-balancing/docs/l7-internal/monitoring#what_is_logged).

Configuration changes to the internal Application Load Balancer, such as addition or removal of a backend service, can result in a brief period of time where users see the HTTP status code `503`. While these configuration changes propagate to [Envoys](https://www.envoyproxy.io/) globally, you see log entries where the `proxyStatus` field matches the `connection_refused` log string.

If HTTP `5xx` status codes persist longer than a few minutes after you complete the load balancer configuration, take the following steps to troubleshoot HTTP `5xx` responses:

  1. Verify that there is a [firewall rule configured to allow health checks](https://docs.cloud.google.com/load-balancing/docs/l7-internal/setting-up-l7-internal#configure_firewall_rules). In the absence of one, load balancer logs typically have a `proxyStatus` matching `destination_unavailable`, which indicates that the load balancer considers the backend to be unavailable.

  2. Verify that health check traffic reaches your backend VMs. To do this, [enable health check logging](https://docs.cloud.google.com/load-balancing/docs/health-check-logging) and search for successful log entries.

For new load balancers, the lack of successful health check log entries doesn't mean that health check traffic is not reaching your backends. It might mean that the backend's initial health state has not yet changed from `UNHEALTHY` to a different state. You see successful health check log entries only after the health check prober receives an HTTP `200 OK` response from the backend.

  3. Verify that the keepalive configuration parameter for the HTTP server software running on the backend instance is not less than the keepalive timeout of the load balancer, whose value is fixed at 10 minutes (600 seconds) and is not configurable.

The load balancer generates an HTTP `5xx` status code when the connection to the backend has unexpectedly closed while sending the HTTP request or before the complete HTTP response has been received. This can happen because the keepalive configuration parameter for the web server software running on the backend instance is less than the fixed keepalive timeout of the load balancer. Ensure that the keepalive timeout configuration for HTTP server software on each backend is set to slightly greater than 10 minutes (the recommended value is 620 seconds).




## Forwarding rule creation fails with "Address is not an RFC 1918 address"

When creating an internal forwarding rule with a literal IP address in a subnet that uses a non-RFC 1918 range, you see an error similar to the following:
    
    
    ERROR: (gcloud.compute.forwarding-rules.create) Could not fetch resource:
     - Invalid value for field 'resource.IPAddress': '100.71.1.88'. Address '100.71.1.88' is not an RFC1918 address.
    

The API validator strictly checks literal values against RFC 1918 standards to prevent accidental public routable IP routing. However, it does not dynamically evaluate if a literal address is VPC-managed, and therefore fails when you provide a non-RFC 1918 IP directly.

To resolve this issue, use one of the following workarounds:

  * Omit the `--address` flag from your [`gcloud compute forwarding-rules create` command](https://docs.cloud.google.com/sdk/gcloud/reference/compute/forwarding-rules/create#--address). Google Cloud automatically allocates a safe, valid IP address directly from your subnet.
  * Reserve a named IP address resource first using the [`gcloud compute addresses create` command](https://docs.cloud.google.com/sdk/gcloud/reference/compute/addresses/create#--purpose). You must then reference the reserved name using the `--address` flag: 
    1. Reserve the static IP address as a named resource: `bash gcloud compute addresses create ADDRESS_NAME \ --addresses=IP_ADDRESS \ --region=REGION \ --subnet=SUBNET \ --purpose=SHARED_LOADBALANCER_VIP`
    2. Reference the reserved IP address by name in your forwarding rule creation command: `--address=ADDRESS_NAME`.



## Limitations

If you are having trouble using an internal Application Load Balancer with other Google Cloud networking features, note the current compatibility [limitations](https://docs.cloud.google.com/load-balancing/docs/l7-internal#limitations).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
