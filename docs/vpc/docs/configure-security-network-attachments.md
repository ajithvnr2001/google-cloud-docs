---
url: https://docs.cloud.google.com/vpc/docs/configure-security-network-attachments/
title: Configure security for network attachments \u00a0|\u00a0 Virtual Private Cloud \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T09:36:52.206511+00:00
---

# Configure security for network attachments  |  Virtual Private Cloud  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/vpc/docs/configure-security-network-attachments/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Networking ](https://docs.cloud.google.com/docs/networking)
  * [ Virtual Private Cloud ](https://docs.cloud.google.com/vpc/docs)
  * [ Guides ](https://docs.cloud.google.com/vpc/docs/overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Configure security for network attachments 

This page describes how consumer network administrators can manage security in VPC networks that use network attachments.

Private Service Connect interfaces are created and managed by a producer organization, but they are located in a consumer VPC network. For consumer-side security, we recommend firewall rules that are based on IP address ranges from the consumer VPC network. This approach lets the consumer control traffic that comes from Private Service Connect interfaces without relying on the producer's [network tags](https://docs.cloud.google.com/vpc/docs/add-remove-network-tags).

Using network tags with firewall rules is supported, but not recommended, because the consumer does not control those tags.

## Limit producer-to-consumer ingress

Consider the example configuration in figure 1, where the consumer wants to grant the producer access to `producer-ingress-subnet` and block the producer from accessing `restricted-subnet`.

[ ![](https://docs.cloud.google.com/static/vpc/images/psc-interfaces/limit-producer-to-consumer-ingress.svg)](https://docs.cloud.google.com/static/vpc/images/psc-interfaces/limit-producer-to-consumer-ingress.svg)

**Figure 1.** Firewall rules help ensure that traffic from the producer subnet can only reach VMs in the `attachment-subnet` and `producer-ingress-subnet` subnets. 

The following firewall rules allow limited producer-to-consumer ingress:

  1. A low-priority rule denies all egress traffic from the IP address range of the network attachment's subnet, `attachment-subnet`.
         
         gcloud compute firewall-rules create deny-all-egress \
             --network=consumer-vpc \
             --action=DENY \
             --rules=ALL \
             --direction=EGRESS \
             --priority=65534 \
             --source-ranges="10.0.1.48/28" \
             --destination-ranges="0.0.0.0/0"
         

  2. A higher priority rule allows egress from the IP address range of `attachment-subnet` to destinations in the address range of `producer-ingress-subnet`.
         
         gcloud compute firewall-rules create allow-limited-egress \
             --network=consumer-vpc \
             --action=ALLOW \
             --rules=ALL \
             --direction=EGRESS \
             --priority=1000 \
             --source-ranges="10.0.1.48/28" \
             --destination-ranges="10.10.2.0/24"
         

  3. An allow ingress rule overrides the implied deny ingress rule for traffic from `attachment-subnet`.
         
         gcloud compute firewall-rules create allow-ingress \
         --network=consumer-vpc \
         --action=ALLOW \
         --rules=ALL \
         --direction=INGRESS \
         --priority=1000 \
         --source-ranges="10.0.1.48/28"
         




## Allow consumer-to-producer egress

If you want to let a consumer network initiate traffic to a producer network, you can use ingress firewall rules.

Consider the example configuration in figure 2, where the consumer wants to let `subnet-1` access the producer network through the Private Service Connect connection.

[ ![](https://docs.cloud.google.com/static/vpc/images/psc-interfaces/allow-consumer-to-producer-egress.svg)](https://docs.cloud.google.com/static/vpc/images/psc-interfaces/allow-consumer-to-producer-egress.svg)

**Figure 2.** An allow ingress firewall rule lets `subnet-1` access the producer network through a Private Service Connect connection, while `subnet-2` is blocked by the implied deny ingress rule (click to enlarge). 

The following firewall rule ensures that only `subnet-1` can access the producer network through the Private Service Connect connection:
    
    
    gcloud compute firewall-rules create vm-subnet-allow-ingress \
        --network=consumer-vpc \
        --action=ALLOW \
        --rules=ALL \
        --direction=INGRESS \
        --priority=1000 \
        --source-ranges="10.10.2.0/24" \
        --destination-ranges="10.0.1.48/28"
    

## Configure producer-to-producer security

You can use VPC firewall rules for security in scenarios where a producer application needs to access another producer application.

Consider a scenario where a consumer uses two different third-party managed services that are hosted in different VPC networks. One service is a database, and the other service provides analytics. The analytics service must connect to the database service to analyze its data. One approach is for the services to create a direct connection. However, if the two third-party services are directly connected, the consumer loses control and visibility over their data.

A more secure approach is to use Private Service Connect interfaces, [Private Service Connect endpoints](https://docs.cloud.google.com/vpc/docs/about-accessing-vpc-hosted-services-endpoints), and [VPC firewall rules](https://docs.cloud.google.com/vpc/docs/firewalls), as shown in figure 3.

[ ![](https://docs.cloud.google.com/static/vpc/images/psc-interfaces/producer-to-producer-security.svg)](https://docs.cloud.google.com/static/vpc/images/psc-interfaces/producer-to-producer-security.svg)

**Figure 3.** Traffic from the analytics application that's bound for the database application passes through the consumer VPC network. VPC firewall rules limit egress traffic based on source IP address range (click to enlarge). 

In this approach, the consumer network connects to the database application through an endpoint in one subnet and connects to the analytics application through a network attachment in a different subnet. Traffic from the analytics application can reach the database application by passing through the Private Service Connect interface and network attachment, transiting the consumer network, and egressing through the endpoint in `endpoint-subnet`.

In the consumer VPC network, a VPC firewall rule denies all egress traffic from `attachment-subnet`. Another firewall rule that has a higher priority allows egress traffic from `attachment-subnet` and `consumer-private-subnet` to the endpoint. Consequently, traffic from the analytics application can reach the database application's VPC network, and this traffic must flow through the endpoint in the consumer.

The following firewall rules create the configuration described in figure 4.

  1. A firewall rule blocks all egress traffic from `attachment-subnet`:
         
         gcloud compute firewall-rules create consumer-deny-all-egress \
             --network=consumer-vpc \
             --action=DENY \
             --rules=all \
             --direction=EGRESS \
             --priority=65534 \
             --source-ranges="10.0.1.48/28" \
             --destination-ranges="0.0.0.0/0"
         

  2. A firewall rule allows egress TCP traffic on port 80 from `attachment-subnet` and `consumer-private-subnet` to the endpoint:
         
         gcloud compute firewall-rules create consumer-allow-80-egress \
             --network=intf-consumer-vpc \
             --allow=tcp:80 \
             --direction=EGRESS \
             --source-ranges="10.0.1.48/28,10.10.2.0/24" \
             --destination-ranges="10.0.1.66/32" \
             --priority=1000
         




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
