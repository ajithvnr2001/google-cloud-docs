---
url: https://docs.cloud.google.com/load-balancing/docs/firewall-rules/
title: Firewall rules \u00a0|\u00a0 Cloud Load Balancing \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:34:20.744714+00:00
---

# Firewall rules  |  Cloud Load Balancing  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/load-balancing/docs/firewall-rules/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Networking ](https://docs.cloud.google.com/docs/networking)
  * [ Load Balancing ](https://docs.cloud.google.com/load-balancing/docs)
  * [ Guides ](https://docs.cloud.google.com/load-balancing/docs/load-balancing-overview)



Send feedback 

#  Firewall rules Stay organized with collections  Save and categorize content based on your preferences. 

Google Cloud load balancers typically require one or more firewall rules to ensure that traffic from clients reaches the backends.

  * Most load balancers are required to specify a health check for backend instances. For the health check probes to reach your backends, you must create an ingress allow [firewall rule](https://docs.cloud.google.com/firewall/docs/using-firewalls) that allows health check probes to reach your backend instances.

  * Load balancers based on Google Front Ends (GFEs) require an ingress allow firewall rule that permits traffic from the GFE proxy to reach the backend instances. In most cases, GFE proxies use the same source IP ranges as the health check probes and therefore don't require a separate firewall rule. Exceptions are noted in the following table.

  * Load balancers based on the open source Envoy proxy require an ingress allow firewall rule that permits traffic from the _proxy-only subnet_ to reach the backend instances. These load balancers terminate incoming connections and traffic from the load balancer to the backends is then sent from IP addresses in the proxy-only subnet.




The following table summarizes the minimum required firewall rules for each type of load balancer.

Load balancer type | Minimum required ingress allow firewall rules | Overview | Example  
---|---|---|---  
Global external Application Load Balancer  | 

  * Health check ranges: For IPv4 health checks to the backends:
    * `35.191.0.0/16`
For IPv6 health checks to the backends:
    * `2600:2d00:1:b029::/64`
  * GFE proxy ranges: 
    * The following are the proxy ranges if the backends are instance groups, zonal NEGs (`GCE_VM_IP_PORT`), or hybrid connectivity NEGs (`NON_GCP_PRIVATE_IP_PORT`). 
      * For IPv4 traffic: 
        * `35.191.0.0/16`
        * `130.211.0.0/22`
      * For IPv6 traffic: 
        * `2600:2d00:1:1::/64`
    * IP address ranges listed in the `_cloud-eoips.googleusercontent.com` DNS TXT record. You can extract the source IP addresses for global internet NEG backends using the following example command on a Linux system: `dig TXT _cloud-eoips.googleusercontent.com | grep -Eo 'ip4:[^ ]+' | cut -d':' -f2`

| [Overview](https://docs.cloud.google.com/load-balancing/docs/https#firewall-rules) | [Example](https://docs.cloud.google.com/load-balancing/docs/https/setup-global-ext-https-compute)  
Classic Application Load Balancer | 

  * Health check ranges: For IPv4 health checks to the backends:
    * `35.191.0.0/16`
  * GFE proxy ranges: 
    * The following are the proxy ranges if the backends are instance groups, zonal NEGs (`GCE_VM_IP_PORT`), or hybrid connectivity NEGs (`NON_GCP_PRIVATE_IP_PORT`). 
      * For IPv4 traffic: 
        * `35.191.0.0/16`
        * `130.211.0.0/22`
      * For IPv6 traffic: 
        * `2600:2d00:1:1::/64`
    * IP address ranges listed in the `_cloud-eoips.googleusercontent.com` DNS TXT record. You can extract the source IP addresses for global internet NEG backends using the following example command on a Linux system: `dig TXT _cloud-eoips.googleusercontent.com | grep -Eo 'ip4:[^ ]+' | cut -d':' -f2`

| [Overview](https://docs.cloud.google.com/load-balancing/docs/https#firewall-rules) | [Example](https://docs.cloud.google.com/load-balancing/docs/https/ext-https-lb-simple#firewall)  
Regional external Application Load Balancer  | 

  * Health check ranges 1, 2: For IPv4 health checks to the backends:
    * `35.191.0.0/16`
For IPv6 health checks to the backends:
    * `2600:2d00:1:b029::/64`
  * Proxy-only subnet 2

| [Overview](https://docs.cloud.google.com/load-balancing/docs/https#firewall-rules) | [Example](https://docs.cloud.google.com/load-balancing/docs/https/setting-up-reg-ext-https-lb#configure_firewall_rules)  
Cross-region internal Application Load Balancer | 

  * Health check ranges 1, 2: For IPv4 health checks to the backends:
    * `35.191.0.0/16`
For IPv6 health checks to the backends:
    * `2600:2d00:1:b029::/64`
  * Proxy-only subnet 2

| [Overview](https://docs.cloud.google.com/load-balancing/docs/l7-internal#firewall_rules) | [Example](https://docs.cloud.google.com/load-balancing/docs/l7-internal/setting-up-l7-cross-reg-internal#configure_firewall_rules)  
Regional internal Application Load Balancer | 

  * Health check ranges 1, 2: For IPv4 health checks to the backends:
    * `35.191.0.0/16`
For IPv6 health checks to the backends:
    * `2600:2d00:1:b029::/64`
  * Proxy-only subnet 2

| [Overview](https://docs.cloud.google.com/load-balancing/docs/l7-internal#firewall_rules) | [Example](https://docs.cloud.google.com/load-balancing/docs/l7-internal/setting-up-l7-internal#configure_firewall_rules)  
Global external proxy Network Load Balancer | 

  * Health check ranges: For IPv4 health checks to the backends:
    * `35.191.0.0/16`
For IPv6 health checks to the backends:
    * `2600:2d00:1:b029::/64`
  * GFE proxy ranges: 
    * For IPv4 traffic: 
      * `35.191.0.0/16`
      * `130.211.0.0/22`
    * For IPv6 traffic: 
      * `2600:2d00:1:1::/64`

| [Overview](https://docs.cloud.google.com/load-balancing/docs/tcp#firewall_rules) |  [Example](https://docs.cloud.google.com/load-balancing/docs/tcp/set-up-global-ext-proxy-tcp#config-hc-firewall)  
Classic proxy Network Load Balancer | 

  * Health check ranges: For IPv4 health checks to the backends:
    * `35.191.0.0/16`
  * GFE proxy ranges: 
    * For IPv4 traffic: 
      * `35.191.0.0/16`
      * `130.211.0.0/22`
    * For IPv6 traffic: 
      * `2600:2d00:1:1::/64`

| [Overview](https://docs.cloud.google.com/load-balancing/docs/tcp#firewall_rules) |  [Example](https://docs.cloud.google.com/load-balancing/docs/tcp/setting-up-tcp#config-hc-firewall)  
Regional external proxy Network Load Balancer  | 

  * Health check ranges 1, 2: For IPv4 health checks to the backends:
    * `35.191.0.0/16`
For IPv6 health checks to the backends:
    * `2600:2d00:1:b029::/64`
  * Proxy-only subnet 2

| [Overview](https://docs.cloud.google.com/load-balancing/docs/tcp#firewall_rules) | [Example](https://docs.cloud.google.com/load-balancing/docs/tcp/set-up-ext-reg-tcp-proxy-migs#configure_firewall_rules)  
Regional internal proxy Network Load Balancer  | 

  * Health check ranges 1, 2: For IPv4 health checks to the backends:
    * `35.191.0.0/16`
For IPv6 health checks to the backends:
    * `2600:2d00:1:b029::/64`
  * Proxy-only subnet 2

| [Overview](https://docs.cloud.google.com/load-balancing/docs/tcp/internal-proxy#firewall_rules) | [Example](https://docs.cloud.google.com/load-balancing/docs/tcp/set-up-int-tcp-proxy-migs#configure_firewall_rules)  
Cross-region internal proxy Network Load Balancer | 

  * Health check ranges 1, 2: For IPv4 health checks to the backends:
    * `35.191.0.0/16`
For IPv6 health checks to the backends:
    * `2600:2d00:1:b029::/64`
  * Proxy-only subnet 2

| [Overview](https://docs.cloud.google.com/load-balancing/docs/tcp/internal-proxy#firewall_rules) | [Example](https://docs.cloud.google.com/load-balancing/docs/tcp/setup-cross-reg-proxy-migs#configure_firewall_rules)  
Global external passthrough Network Load Balancer | 

  * Health check ranges: For IPv4 traffic to the backends:
    * `136.124.104.0/22`
    * `136.124.108.0/22`
For IPv6 traffic to the backends:
    * `2600:1904:7::/48`
    * `2600:1904:8::/48`
  * External source IP addresses of clients on the internet.   
For example, `0.0.0.0/0` (all IPv4 clients) or `::/0` (all IPv6 clients) or a specific set of IP address ranges.

| [Overview](https://docs.cloud.google.com/load-balancing/docs/network/global-networklb-architecture#firewall-rules) | [Example](https://docs.cloud.google.com/load-balancing/docs/network/set-up-global-ext-passthrough-network-lb-vm-backends#configure_a_firewall_rule)  
Regional external passthrough Network Load Balancer  | 

  * Health check ranges: For IPv4 health checks to the backends:
    * `35.191.0.0/16`
    * `209.85.152.0/22` (for target pools)
    * `209.85.204.0/22`
For IPv6 health checks to the backends:
    * `2600:1901:8001::/48`
  * External source IP addresses of clients on the internet.   
For example, `0.0.0.0/0` (all IPv4 clients) or `::/0` (all IPv6 clients) or a specific set of IP address ranges. Target pool-based load balancers might proxy health checks through the metadata server. In this case, health check probes sources match the IP address of the metadata server: `169.254.169.254`. However, traffic from the metadata server is always allowed to reach VMs. No firewall rule is required.

| Overview  


  * [Backend service-based](https://docs.cloud.google.com/load-balancing/docs/network/networklb-backend-service#firewall_rules)
  * [Target pool-based](https://docs.cloud.google.com/load-balancing/docs/network/networklb-target-pools#firewall_rules)

| Examples  


  * [Backend service-based](https://docs.cloud.google.com/load-balancing/docs/network/setting-up-network-backend-service#configure-firewall-rules)
  * [Target pool-based](https://docs.cloud.google.com/load-balancing/docs/network/setting-up-network#creating_a_firewall_rule_to_allow_external_traffic_to_these_vm_instances)

  
Internal passthrough Network Load Balancer  | 

  * Health check ranges: For IPv4 health checks to the backends:
    * `35.191.0.0/16`
For IPv6 health checks to the backends:
    * `2600:2d00:1:b029::/64`
  * Internal source IP addresses of clients

| [Overview](https://docs.cloud.google.com/load-balancing/docs/internal#firewall_rules) | [single-stack](https://docs.cloud.google.com/load-balancing/docs/internal/setting-up-internal#configure_firewall_rules) [dual-stack](https://docs.cloud.google.com/load-balancing/docs/internal/setting-up-internal#configure_firewall_rules_dual_stack)  
  
1 Allowing traffic from Google's health check probe ranges isn't required for hybrid NEGs. However, if you're using a combination of hybrid and zonal NEGs in a single backend service, you need to allow traffic from the [Google health check probe ranges](https://docs.cloud.google.com/load-balancing/docs/health-check-concepts#ip-ranges) for the zonal NEGs. 

2 For regional internet NEGs, health checks are optional. Traffic from load balancers using _regional_ internet NEGs originates from the [proxy-only subnet](https://docs.cloud.google.com/load-balancing/docs/proxy-only-subnets) and is then NAT-translated (by using Cloud NAT) to either manually or automatically allocated NAT IP addresses. This traffic includes both health check probes and user requests from the load balancer to the backends. For details, see [Regional NEGs: Use a Cloud NAT gateway](https://docs.cloud.google.com/load-balancing/docs/negs/internet-neg-concepts#nat-support).   


Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
