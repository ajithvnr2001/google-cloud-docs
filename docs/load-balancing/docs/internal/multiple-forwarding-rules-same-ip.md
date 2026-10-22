---
url: https://docs.cloud.google.com/load-balancing/docs/internal/multiple-forwarding-rules-same-ip/
title: Internal passthrough Network Load Balancer forwarding rules that use a common IP address \u00a0|\u00a0 Cloud Load Balancing \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T15:10:22.400179+00:00
---

# Internal passthrough Network Load Balancer forwarding rules that use a common IP address  |  Cloud Load Balancing  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/load-balancing/docs/internal/multiple-forwarding-rules-same-ip/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Networking ](https://docs.cloud.google.com/docs/networking)
  * [ Load Balancing ](https://docs.cloud.google.com/load-balancing/docs)
  * [ Guides ](https://docs.cloud.google.com/load-balancing/docs/load-balancing-overview)



Send feedback 

#  Internal passthrough Network Load Balancer forwarding rules that use a common IP address Stay organized with collections  Save and categorize content based on your preferences. 

Internal passthrough Network Load Balancers are regional load balancers that enable you to run and scale your services behind an internal IP address that is accessible only to your internal virtual machine (VM) instances.

This page discusses using multiple forwarding rules with the same IP address. For general information about internal passthrough Network Load Balancers, see the [Internal passthrough Network Load Balancer overview](https://docs.cloud.google.com/load-balancing/docs/internal).

Using internal forwarding rules, you can use a shared internal IP address across up to ten forwarding rules. To share an IP address, you set the purpose of the IP address to `SHARED_LOADBALANCER_VIP`. You can use `TCP`or `UDP` for the forwarding rule protocol and assign up to five ports to the forwarding rule, or specify `--ports=ALL` to use all ports. If you want to use the `L3_DEFAULT` protocol, you must use all ports with the `--ports=ALL` option.

With unique combinations of protocol and ports, you can do the following:

  * Create 50 unique TCP ports with each forwarding rule using the `TCP` protocol.

If a forwarding rule is configured to use the `TCP` protocol and all ports, no other forwarding rule using the `TCP` protocol can use the same shared IP address.

  * Create 50 unique UDP ports with each forwarding rule using the `UDP` protocol.

If a forwarding rule is configured to use the `UDP` protocol and all ports, no other forwarding rule using the `UDP` protocol can use the same shared IP address.

  * Create 50 unique combinations of TCP and UDP ports, with each forwarding rule using either the `TCP` or `UDP` protocol.

  * Reference a common backend service (a single load balancer) or multiple backend services (multiple load balancers that share the same IP address).

  * Use all ports when configuring a forwarding rule with the `L3_DEFAULT` protocol. There can be only one `L3_DEFAULT` forwarding rule for an IP address, which can be shared with other TCP and UDP forwarding rules, if necessary.




When your forwarding rules have different protocols, you must have two different backend services as well. A single internal passthrough Network Load Balancer works for either TCP or UDP traffic—not both—because it has a single backend service that uses only one of these protocols.

## Decision matrices for forwarding rules

Use the following tables to design your deployment.

### Single internal passthrough Network Load Balancer

A single backend service supports TCP or UDP, not both.

When you need multiple forwarding rules, calculate the number of forwarding rules that you need by using the formula `⌈total number of ports / 5⌉`, where `⌈⌉` is the ceiling (least integer) function, and means _round up_ to the nearest whole number.

For example, suppose you need 26 TCP ports on one IP address of your load balancer. If you don't want to create a single forwarding rule by using `--ports=ALL`, you must create six forwarding rules because `26 / 5 = 5 with a remainder of 1`.

Intended frontend configuration | Number of forwarding rules required | `--purpose=SHARED_LOADBALANCER_VIP` flag required for IP address | Forwarding rule port specification  
---|---|---|---  
One IP address, traffic on all ports | One forwarding rule | No | `--ports=ALL`  
One IP address, traffic on specific ports |  For five or fewer ports:  
one forwarding rule For six or more ports:  
multiple forwarding rules |  For five or fewer ports: no For six or more ports: yes | Set `--ports` to a set of up to five contiguous or non-contiguous port numbers.   
Multiple IP addresses, traffic on all ports | One forwarding rule per IP address | No | `--ports=ALL`  
Multiple IP addresses, traffic on specific ports | At least one forwarding rule per IP address |  If using five or fewer ports per IP address: no If using six or more ports per IP address: yes | Set `--ports` to a set of up to five contiguous or non-contiguous port numbers.   
  
### Two internal passthrough Network Load Balancers

When you have two internal passthrough Network Load Balancers, you can have two backend services, where one backend service is for TCP traffic, and the other backend service is for UDP traffic.

When you need multiple forwarding rules, calculate the number of forwarding rules that you need by using the following formula, where `⌈⌉` is the ceiling (least integer) function, and means _round up_ to the nearest whole number:
    
    
     ⌈total number of TCP ports / 5⌉
    
     ⌈total number of UDP ports / 5⌉
    

For example, suppose you need 26 TCP ports and 12 UDP ports. You must create nine forwarding rules:

  * `26 / 5 = 5 with a remainder of 1`, so you need six forwarding rules for your TCP ports.
  * `12 / 5 = 2 with a remainder of 2`, so you need three forwarding rules for your UDP ports.

**Note:** You cannot share a static internal IPv6 address across multiple forwarding rules.Intended frontend configuration | Number of forwarding rules required | `--purpose=SHARED_LOADBALANCER_VIP` flag required for IP address | Forwarding rule port specification  
---|---|---|---  
One IP address, traffic on all ports | Two forwarding rules—one for TCP, one for UDP | Because the TCP forwarding rule and the UDP forwarding rule must share a single IP address: yes | `--ports=ALL`  
One IP address, traffic on specific ports |  For five or fewer TCP ports and five or fewer UDP ports: two forwarding rules—one for TCP, one for UDP For six or more TCP ports or UDP ports: multiple forwarding rules, where each forwarding rule supports one protocol and five or fewer ports | Yes | Set `--ports` to a set of up to five contiguous or non-contiguous port numbers.   
Multiple IP addresses, traffic on all ports, either TCP or UDP |  At least two forwarding rules—one for TCP using one IP address, one for UDP using a different IP address Three or more forwarding rules if you need three or more IP addresses | No | `--ports=ALL`  
Multiple IP addresses, traffic on specific ports, either TCP or UDP |  At least two forwarding rules—one for TCP using one IP address, one for UDP using a different IP address More than two forwarding rules if you need one of the following:

  * More than two IP addresses
  * More than five ports for TCP traffic on an IP address or more than five ports for UDP traffic on an IP address

|  For one IP address with five or fewer TCP ports and one IP address with five or fewer UDP ports: no For six or more TCP ports or UDP ports: yes | Set `--ports` to a set of up to five contiguous or non-contiguous port numbers.   
  
#### Limitations

  * Two or more forwarding rules with the same IP address and protocol cannot have overlapping ports. For example: 
    * When you configure the forwarding rule with protocol TCP and port `80`, you cannot configure another forwarding rule to serve that protocol and port. For example, you cannot create another forwarding rule to serve TCP ports `80`, `81`, and `90`.
    * When you configure the forwarding rule for TCP and ports `80`, `8080`, and `90`, you cannot configure another forwarding rule for TCP that would use all ports.
  * When two or more forwarding rules share the same IP address by using the `--purpose=SHARED_LOADBALANCER_VIP` flag, at most only one of them can have the protocol set to `L3_DEFAULT`.



## Use cases

Many different types of deployments are possible. The following examples use one IP address that accepts traffic on specific ports for two load balancers.

### Example 1

This example uses different forwarding rules with the following parameters:

  * The same IP address (`10.1.1.1`)
  * Different protocols
  * Separate backend services that each forwarding rule points to
  * Matching protocols: the protocol of each backend service matches the protocol of the corresponding forwarding rule

[ ![Different forwarding rules, same IP address, different protocols and ports.](https://docs.cloud.google.com/static/load-balancing/images/ilb-fwd-rules-same-ip-different-protocols.svg)](https://docs.cloud.google.com/static/load-balancing/images/ilb-fwd-rules-same-ip-different-protocols.svg) Different forwarding rules, same IP address, different protocols and ports (click to enlarge).

### Example 2

This example uses different forwarding rules with the following parameters:

  * The same IPv4 address (`10.1.1.1`)
  * The same protocol
  * A different set of numbered ports on each forwarding rule

**Notes:**

  * This configuration option is an alternative to creating a single forwarding rule that specifies all ports.
  * You cannot share a static internal IPv6 address across multiple forwarding rules.

[ ![Different forwarding rules, same IP address, same protocol, more than five numbered ports.](https://docs.cloud.google.com/static/load-balancing/images/ilb-fwd-rules-same-ip-different-ports.svg)](https://docs.cloud.google.com/static/load-balancing/images/ilb-fwd-rules-same-ip-different-ports.svg) Different forwarding rules, same IP address, same protocol, more than five numbered ports (click to enlarge).

## Configuration steps

You can create multiple internal forwarding rules that have the same IP address if you do both of the following:

  1. [Create a static (reserved) internal IP address](https://docs.cloud.google.com/vpc/docs/reserve-static-internal-ip-address) for the forwarding rules to use.
  2. Set the [`--purpose` flag](https://docs.cloud.google.com/sdk/gcloud/reference/compute/addresses/create#--purpose) on the shared internal IP address to the value `SHARED_LOADBALANCER_VIP`.



For an example setup, see [Accepting traffic on multiple ports using two forwarding rules](https://docs.cloud.google.com/load-balancing/docs/internal/setting-up-internal#multiple-ports-two-fwd-rules).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
