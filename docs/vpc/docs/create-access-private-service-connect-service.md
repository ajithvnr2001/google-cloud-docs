---
url: https://docs.cloud.google.com/vpc/docs/create-access-private-service-connect-service/
title: Create and access services \u00a0|\u00a0 Virtual Private Cloud \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T03:27:12.244030+00:00
---

# Create and access services  |  Virtual Private Cloud  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/vpc/docs/create-access-private-service-connect-service/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Networking ](https://docs.cloud.google.com/docs/networking)
  * [ Virtual Private Cloud ](https://docs.cloud.google.com/vpc/docs)
  * [ Guides ](https://docs.cloud.google.com/vpc/docs/overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Create and access services

Private Service Connect provides multiple ways to connect _service consumers_ to _service producers_. A common configuration is to make a load-balanced service available by creating a Private Service Connect published service. After the service is published, service consumers in another VPC network can access the service through a Private Service Connect endpoint. The following tutorials explain how to complete these steps:

  1. [Create a load-balanced service](https://docs.cloud.google.com/vpc/docs/create-load-balanced-service)
  2. [Make the service accessible from other VPC networks](https://docs.cloud.google.com/vpc/docs/make-service-accessible-other-vpc-networks)
  3. [Access the service from another VPC network](https://docs.cloud.google.com/vpc/docs/access-service-other-vpc-network)



Connecting service consumers to service producers creates the following configuration.

[ ![A Private Service Connect endpoint connects a service consumer VPC network to a service producer VPC network.](https://docs.cloud.google.com/static/vpc/images/load-balancer-published-service-endpoint.svg)](https://docs.cloud.google.com/static/vpc/images/load-balancer-published-service-endpoint.svg)

An endpoint lets service consumers send traffic from the consumer's VPC network to services in the service producer's VPC network (click to enlarge). 

Client VMs send requests to the internal IP address of the endpoint, which is local to the consumer's VPC network. Private Service Connect directs the traffic to the load balancer backend VMs.

Private Service Connect endpoints, Private Service Connect service attachments, and load balancers are logical constructs. From a physical perspective, traffic goes directly from the physical server that hosts the client VM to the physical server that hosts the producer load balancer VM. For more information, see [Private Service Connect architecture and performance](https://docs.cloud.google.com/vpc/docs/private-service-connect-architecture).

## What's next

  * [Create a load-balanced service](https://docs.cloud.google.com/vpc/docs/create-load-balanced-service)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
