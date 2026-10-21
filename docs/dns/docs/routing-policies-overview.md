---
url: https://docs.cloud.google.com/dns/docs/routing-policies-overview/
title: DNS routing policies and health checks \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T12:38:57.711929+00:00
---

# DNS routing policies and health checks  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dns/docs/routing-policies-overview/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Networking ](https://docs.cloud.google.com/docs/networking)
  * [ Cloud DNS ](https://docs.cloud.google.com/dns/docs)
  * [ Guides ](https://docs.cloud.google.com/dns/docs/set-up-dns-records-domain-name)



Send feedback 

#  DNS routing policies and health checks Stay organized with collections  Save and categorize content based on your preferences. 

You can configure DNS routing policies for resource record sets in private or public zones to steer traffic based on specific criteria. Create resource record sets with specific routing policy values to set up these policies. These values determine how Cloud DNS routes query traffic.

Cloud DNS supports the following routing policies:

  * **Weighted round robin (WRR) routing policy** : Use a WRR routing policy to assign different weights to each resource record set for a DNS name. A WRR routing policy helps ensure that traffic is distributed according to the configured weights. Combining WRR and geolocation routing policies is not supported.

**Note:** Resolvers might cache and serve responses to multiple clients until the resource record's time to live (TTL) expires. This inherent behavior of DNS traffic steering might sometimes lead to inexact traffic steering.


  * **Geolocation routing policy** : Use the geolocation routing policy to specify source geolocations and to provide corresponding responses to those geographies. The geolocation routing policy applies a nearest match for the source location when no policy items exactly match the traffic source.

    * **Geolocation routing policy with a geofence** : Use geolocation routing policy with a geofence to restrict traffic to a specific geolocation even if all endpoints in that geolocation are unhealthy.


  * **Failover routing policy** : Use the failover routing policy to set up active backup configurations.



DNS routing policies can't be configured for the following private zones:

  * Forwarding zones
  * DNS peering zones
  * Managed reverse lookup zones
  * Service Directory zones



## WRR routing policies

A WRR routing policy lets you specify different weights per DNS target, and Cloud DNS ensures that your traffic is distributed according to the weights. You can use this policy to support [manual `active-active` or `active-passive` configurations](https://wikipedia.org/wiki/High-availability_cluster). You can also split traffic between production and experimental versions of your service.

Cloud DNS supports health checking and failovers within routing policies for internal load balancers and external endpoints. Cloud DNS enables automatic failover when the endpoints fail their health checks. During a failover, Cloud DNS automatically adjusts the traffic split among the remaining healthy endpoints. For more information, see Health checks.

## Geolocation routing policies

A geolocation routing policy lets you map traffic originating from source geographies (Google Cloud regions) to specific DNS targets. Use this policy to distribute incoming requests to different service instances based on the traffic's origin. You can use this feature with traffic from outside Google Cloud or with traffic originating within Google Cloud and bound for internal passthrough Network Load Balancers. Cloud DNS uses the region where the queries enter Google Cloud as the source geography.

A geolocation routing policy maps the source differently for public and private DNS in the following ways:

  * For public DNS, the source IP address or the [extension mechanism for DNS (EDNS)](https://wikipedia.org/wiki/Extension_Mechanisms_for_DNS) client subnet of the query is used.
  * For private DNS, the EDNS client subnet is not used. Instead, the location of the query is the location of the system that sends the packets for the query: 
    * For queries from a Compute Engine virtual machine (VM) instance with a network interface in a VPC network, the location of the query is the region that contains the VM instance.
    * For queries received by an [inbound server policy entry point](https://docs.cloud.google.com/dns/docs/server-policies-overview#dns-server-policy-in), the location of the query is the region of the Cloud VPN tunnel, Cloud Interconnect VLAN attachment, or Router appliance that received the packets for the query. The region of the IP address of the entry point is not relevant. For more information, see [Network and region for inbound queries](https://docs.cloud.google.com/dns/docs/server-policies-overview#policy-in-support).



Cloud DNS supports health checking and failovers within routing policies for internal load balancers and external endpoints. Cloud DNS enables automatic failover when the endpoints fail their health checks. When you use geolocation routing policies, the traffic fails over to the next closest geolocation to the source traffic.

### Geolocation routing policy with geofence

A geofence helps ensure that traffic is directed to a specific region, even if all endpoints within that region fail the health checks.

When geofencing is disabled and a health check failure occurs for a specific geolocation, traffic automatically fails over to the next closest geolocation. However, when geofencing is enabled, this automatic failover doesn't occur. As an authoritative server, Cloud DNS must return a value, and in this scenario, Cloud DNS returns all the IP addresses unaltered when the endpoints fail the health checks. 

## Failover routing policies

The failover routing policy lets you set up active backup configurations to provide high availability for internal resources within your VPC network.

In normal operation, Cloud DNS always returns the IP addresses from the `active` set. When all IP addresses in the `active` set become unhealthy, Cloud DNS serves the IP addresses from the `backup` set. If you configure the `backup` set as a geolocation routing policy, it operates as described in the Geolocation routing policies section. If you configure the `backup` set for an internal load balancer, Cloud DNS health checks all backup virtual IP (VIP) addresses.

Cloud DNS lets you gradually _trickle_ traffic to the backup VIP addresses so that you can verify that the backup VIP addresses are functioning. You can configure the percentage of the traffic sent to the backup as a fraction from 0 to 1. You can manually trigger a failover by sending 100% of the traffic to the backup VIP addresses. The typical value is 0.1. Health checks can be applied only to internal load balancers and external endpoints.

## Health checks

Cloud DNS supports health checking and failovers within routing policies for the following internal load balancers and external endpoints:

  * [Internal Application Load Balancers](https://docs.cloud.google.com/load-balancing/docs/l7-internal) (regional and cross-region)
  * [Internal passthrough Network Load Balancers](https://docs.cloud.google.com/load-balancing/docs/internal)
  * [Internal proxy Network Load Balancers](https://docs.cloud.google.com/load-balancing/docs/tcp/internal-proxy) ([Preview](https://cloud.google.com/products#product-launch-stages))
  * External endpoints

**Important:** Make sure that you enable global access for regional load balancers.

When you want to use health checking with a managed zone and [DNS Security Extensions (DNSSEC)](https://docs.cloud.google.com/dns/docs/dnssec) is enabled, only a single IP address can be used within each policy item (a WRR or geolocation). You cannot mix health-checked IP addresses and non-health-checked IP addresses in a specific policy.

For information about best practices to keep in mind when you configure the Cloud DNS record and health checks, see [Best practices](https://docs.cloud.google.com/load-balancing/docs/https/reg-applb-ha-overview#dns-hc-best-practices).

### Health checks for internal load balancers

Health checks for internal load balancers are only available in private zones.

For internal Application Load Balancers and internal proxy Network Load Balancers, Cloud DNS considers the health of the load balancer itself during the routing decision. When a load balancer receives a query, it distributes traffic only to the healthy backend services. To help ensure that there are healthy backends, you can manage the lifecycle of the backends by using services such as managed instance groups (MIGs). Cloud DNS doesn't need to be aware of the health status of individual backends; the load balancer handles this task.

For internal passthrough Network Load Balancers, Cloud DNS checks the health information on the load balancer's individual backend instances. Cloud DNS applies a default 20% threshold, and if at least 20% of backend instances are healthy, the load balancer endpoint is considered healthy. DNS routing policies mark the endpoint as healthy or unhealthy based on this threshold, and route traffic accordingly.

A single internal passthrough Network Load Balancer virtual IP address (VIP) can have multiple backend instances. If an internal passthrough Network Load Balancer doesn't have any backend instances, Cloud DNS still considers it healthy. For health checking to work correctly, specify at least one backend instance within the load balancer configuration.

When the endpoint is marked unhealthy, the following conditions can occur:

  * If there are multiple VIP addresses programmed against a policy, then only healthy VIP addresses are returned.
  * If all the VIP addresses programmed against a policy bucket are unhealthy, that policy line has failed. The following behavior applies:

    * For a WRR policy, Cloud DNS distributes the traffic proportionally among the remaining healthy endpoints defined in the policy. 
    * For a geolocation policy that doesn't have fencing enabled, the traffic switches to endpoints in the next closest geography to the source Google Cloud region defined in the policy.
    * For a geolocation policy that has geofencing enabled, Cloud DNS distributes the traffic to the VIP address that is closest to the source Google Cloud region defined in the policy. 
    * For a failover policy, Cloud DNS switches the traffic to the backup endpoints defined in the policy.
    * If all policy buckets are unhealthy, Cloud DNS behaves as if all endpoints are healthy. This scenario might potentially lead to traffic distributed to unresponsive endpoints.



For more information about health checks for internal load balancers, see [Health checks overview](https://docs.cloud.google.com/load-balancing/docs/health-check-concepts).

### Health checks for external endpoints

Health checks for external endpoints are only available in public zones. The endpoints that you want to health check must be accessible over the public internet. The specified endpoint could be any external IP address and port, including a global external Application Load Balancer VIP, Regional external Application Load Balancer VIP, global external proxy Network Load Balancer VIP, on-premises endpoints, or any other endpoint that is accessible over the public internet.

Use health checks for external endpoints in the following scenarios:

  * To reroute traffic to a regional external Application Load Balancer if a global external Application Load Balancer backend or a global external proxy Network Load Balancer backend becomes unhealthy.
  * To reroute traffic to another regional external Application Load Balancer if a specific regional external Application Load Balancer's backend becomes unhealthy.
  * To monitor the health of on-premises endpoints or other endpoints that are reachable on the public internet.



When you create DNS routing policy with health checks for external endpoints, Cloud DNS sends health check probes to your endpoints. These health check probes originate from three Google Cloud source regions that you specify. Each region's health check probers run independently, and Cloud DNS aggregates their results to determine the endpoint's overall health. Within each region, three health check prober instances probe each endpoint. If one probe fails, Cloud DNS can still determine the endpoint's health by using the remaining probes. This means that you have nine probers in total for each endpoint, and each probe occurs at the frequency that you specify in the health check's check interval. Based on the parameters of the routing policy and the health information, Cloud DNS selects an endpoint and routes traffic to the selected endpoint.

Cloud DNS supports the TCP, HTTP, and HTTPS protocols with the following caveats:

  * The TCP request field is not supported.
  * The `proxyHeader` field for HTTP, HTTPS, and TCP is not supported.



SSL, HTTP/2, and gRPC protocols are not supported.

For the TCP protocol, Cloud DNS attempts to connect to the endpoint. For the HTTP and HTTPS protocols, Cloud DNS verifies that the endpoint returns an HTTP response code `200`. You can also configure content-based health checking, where Cloud DNS checks that the response contains a specific string.

Unlike health checking for internal load balancers, Cloud DNS health checks for external endpoints don't originate from fixed IP address ranges. The probe source IP address ranges are subject to change over time.

The protocol and port that you specify when creating the health check determine how health check probes are done. If you don't specify a port, Cloud DNS uses port `80`. To help ensure that health checks work correctly, configure your firewall rules to allow health check probes from any source IP address and on the specific port configured in the health check.

If you haven't configured your firewall to allow health check probes, the probes fail, so Cloud DNS considers the blocked endpoints as unhealthy. If every endpoint is returned as unhealthy, Cloud DNS still provides all of them as a result, even though they are unhealthy. 

### Health check interval

Cloud DNS periodically sends health check probes according to the health check interval. For example, if the health check interval is 30 seconds, Cloud DNS sends one health check probe every 30 seconds.

For Cloud DNS external endpoint health checking, the health check interval must be between 30 and 300 seconds.

### Weighted round robin routing policies and health checks

Cloud DNS supports weights from 0 to 1000, inclusive of both. When health checks are included, the following occurs:

  * If you configure multiple targets, all with weight 0, traffic is distributed equally among the targets.
  * If you configure a new, non-zero weighted target, it then becomes the primary target, and all traffic shifts to that target.
  * As you add more targets with nonzero weights, Cloud DNS dynamically computes the traffic split among the targets (with each request) and distributes the traffic appropriately. For example, if you have configured three targets with weights of 0, 25, and 75, the target with the 0 weight gets no traffic, the target with a weight of 25 gets one-fourth of the traffic, and the remaining target gets three-fourths of the incoming traffic.
  * If health checks are associated with non-zero weighted targets but not with zero weighted targets, the zero weighted targets are always considered healthy. If all the non-zero records are unhealthy, Cloud DNS returns the zero weighted records.
  * If health checks are associated with both non-zero and zero weighted records, and if all the records are failing health checks, Cloud DNS returns any non-zero weighted targets and ignores the zero weighted targets.
  * When Cloud DNS chooses a weight bucket to return to the requestor (a single policy item), only the IP address in that weight bucket is returned. If you only specify one IP address in the weight bucket, only that IP address is in the response. If there is more than one IP address in the weight bucket, Cloud DNS returns all the IP addresses in a randomized order.



### Geolocation routing policies and health checks

For geolocation routing policies with health checks enabled, the following occurs:

  * When a policy has multiple IP addresses configured, and all the IP addresses have health checking, only the healthy IP addresses are returned.
  * When there's a mix and match of health-checked and non-health-checked IP addresses, and all the health-checked IP addresses fail, Cloud DNS returns all the IP addresses that don't have health checking configured. In this scenario, automatic failover to the next nearest geography doesn't occur. 



## Health check logging

Cloud DNS supports health check logging and logs the health status of your health-check-enabled IP addresses when you query the DNS name that refers to those IP addresses.

Health check logging lets you do the following:

  * Validate whether the routing policies are performing as expected. For example: 
    * For geolocation policies, it lets you validate whether the policies detect the correct geography and return the correct resource record dataset. 
    * For WRR policies, it lets you validate if the policies are returning the IP addresses in the correct weightage.
  * Identify infrastructure issues with specific backends and IP addresses that have failures.
  * Troubleshoot why specific backends are never included or are the only ones that are being returned.



For more information, see [health check logging information](https://docs.cloud.google.com/load-balancing/docs/health-check-logging).

## Supported record types for DNS routing policies

DNS routing policies don't support all the [record types that are supported by Cloud DNS](https://docs.cloud.google.com/dns/docs/records#record_type).

The following record types are supported:

**Record type** | **Description**  
---|---  
A  | IPv4 addresses for internal (private zone) and external (public zone) health checks.   
AAAA  | IPv6 addresses for external (public zone) health checks.   
CNAME  | Canonical names. Health checks are not supported.   
MX  | Mail exchange records. Health checks are not supported.   
SRV  | Host/port ([RFC 2782](https://tools.ietf.org/html/rfc2782)). Health checks are not supported.   
TXT  | Text data. Health checks are not supported.   
  
## What's next

  * [Configure DNS routing policies and health checks](https://docs.cloud.google.com/dns/docs/configure-routing-policies)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
