---
url: https://docs.cloud.google.com/apigee/docs/api-platform/architecture/overview/
title: Apigee architecture overview \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T12:55:40.174289+00:00
---

# Apigee architecture overview  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/apigee/docs/api-platform/architecture/overview/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Apigee ](https://docs.cloud.google.com/apigee/docs)
  * [ Guides ](https://docs.cloud.google.com/apigee/docs/api-platform/get-started/what-apigee)



Send feedback 

#  Apigee architecture overview Stay organized with collections  Save and categorize content based on your preferences. 

_This page applies to**Apigee** and **Apigee hybrid**._

_View[ Apigee Edge](https://docs.apigee.com/api-platform/get-started/what-apigee-edge) documentation._ ![](https://fonts.gstatic.com/s/i/googlematerialicons/help/v13/gm_grey-24dp/1x/gm_help_gm_grey_24dp.png)

This topic provides an overview of the Apigee system architecture. It is intended to help you understand which components are created during [provisioning](https://docs.cloud.google.com/apigee/docs/api-platform/get-started/overview) and their purpose in the overall system.

Apigee provides two options for provisioning: [with VPC peering](https://docs.cloud.google.com/apigee/docs/api-platform/get-started/install-cli) and [without VPC peering](https://docs.cloud.google.com/apigee/docs/api-platform/get-started/install-cli-non-peered). Both options are described in the sections that follow.

  * Architecture with VPC peering enabled
  * Architecture with VPC peering disabled



## Architecture with VPC peering enabled

This section describes the Apigee system architecture when Apigee is [provisioned with the VPC peering option](https://docs.cloud.google.com/apigee/docs/api-platform/get-started/install-cli).

### Provisioning overview

During provisioning, components are configured and created that allow bidirectional communication between a virtual private cloud network (VPC) managed by you and a VPC network managed by Apigee. After you complete the first few provisioning steps, the two VPCs exist, but as yet cannot communicate back and forth. Further configuration is needed to allow bidirectional communication. See Figure 1.

![](https://docs.cloud.google.com/static/apigee/docs/api-platform/images/apigee-arch-diagrams/apigee-arch-b.png)**Figure 1** : Your VPC and Apigee's VPC cannot communicate with each other without further configuration.

To enable communication between VPCs, we use [VPC network peering](https://docs.cloud.google.com/vpc/docs/vpc-peering). Network peering allows internal IP address connectivity across two Virtual Private Cloud (VPC) networks regardless of whether they belong to the same project or the same Google Cloud organization. After the network peering step is completed, communication is possible between the two VPCs. See Figure 2.

![](https://docs.cloud.google.com/static/apigee/docs/api-platform/images/apigee-arch-diagrams/apigee-arch-c.png)**Figure 2** : VPC network peering enables communication between VPCs.

To route traffic from client apps on the internet to Apigee, we use an external Application Load Balancer (XLB). An XLB can communicate across Google Cloud projects, such as between the customer Google Cloud project and the Apigee Google Cloud Project, using [cross-project service referencing](https://cloud.google.com/load-balancing/docs/https#cross-project).

You could also provision a [ managed instance group](https://docs.cloud.google.com/compute/docs/instance-groups#managed_instance_groups) (MIG) of virtual machines (VM) that serve as a network bridge. The MIG VMs have the capability to communicate bidirectionally across the peered networks. When provisioning is complete, apps on the internet talk to the XLB, the XLB talks to the bridge VM, and the bridge VM talks to the Apigee network. See Figure 3 and Figure 4.

![](https://docs.cloud.google.com/static/apigee/docs/api-platform/images/apigee-arch-diagrams/apigee-arch-a.png)**Figure 3** : Managed VMs allow requests and responses to flow between the peered networks.

In this configuration, traffic is routed from Apigee (for example, from the MessageLogging policy) to a workload running in your internal VPC. In this case, communication to your internal VPC does not go through a NAT IP of the Egress. Instead, you can route the traffic through one of the Apigee instance IPs. 

![](https://docs.cloud.google.com/static/apigee/docs/api-platform/images/apigee-arch-diagrams/apigee-arch-d.png)**Figure 4** : Traffic routed privately to a workload in your internal VPC.

### API proxy call lifecycle

The following illustration shows the lifecycle of an API proxy call as it moves through the provisioned Apigee system components (Figure 5):

![](https://docs.cloud.google.com/static/apigee/docs/api-platform/images/apigee-arch-diagrams/apigee-arch-e.png)**Figure 5** : Traffic routed privately to a workload in your internal VPC.

  1. A client app calls an Apigee API proxy.
  2. The request lands on a global L7 external HTTPS load balancer (XLB). The XLB is configured with an external/public IP and a TLS certificate.
  3. The XLB sends the request to a virtual machine (VM). The VM serves as a bridge between your VPC and Google's VPC (managed by Apigee). **Note:** The XLB is not capable of communicating across the peered networks. A VM, on the other hand, can be configured to talk to Apigee across the peered network. This is why you provision a [ managed instance group](https://docs.cloud.google.com/compute/docs/instance-groups#managed_instance_groups) (MIG) of VMs to function as a network bridge. These VMs are managed by you, not by Apigee. You are responsible for scaling, patching, and maintaining these VMs. Apigee only provides the startup script used to configure the VMs to route traffic.
  4. The VM sends the request to Apigee, which processes the API proxy request.
  5. Apigee sends the request to the backend service, and the response is sent back to the client.



## Architecture with VPC peering disabled

This section describes the Apigee system architecture when Apigee is [not provisioned with the VPC peering option](https://docs.cloud.google.com/apigee/docs/api-platform/get-started/install-cli-non-peered).

During provisioning, components are configured and created that allow bidirectional communication between a virtual private cloud network (VPC) managed by you and a VPC network managed by Apigee. After you complete the first few provisioning steps, the two VPCs exist, but as yet cannot communicate back and forth. Further configuration is needed to allow bidirectional communication. See Figure 6.

![](https://docs.cloud.google.com/static/apigee/docs/images/star-ark-empty-arch.png)**Figure 6** : Your VPC and Apigee's VPC cannot communicate with each other without further configuration.

To enable communication between VPCs, we use [Private Service Connect](https://cloud.google.com/vpc/docs/private-service-connect) for routing northbound traffic to Apigee and southbound traffic to target services running in your Google Cloud projects. 

Private Service Connect enables private connection between a service producer (Apigee) and a service consumer (one or more other Cloud projects that you control). With this method (Figure 7), requests pass through either an external Application Load Balancer or a regional external load balancer to a single point of attachment, called a [service attachment](https://docs.cloud.google.com/vpc/docs/private-service-connect#service-attachments). 

To privately connect Apigee to a backend target, you must create two entities: a [service attachment](https://docs.cloud.google.com/vpc/docs/private-service-connect#service-attachments) in the VPC network where the target is deployed and an [endpoint attachment](https://docs.cloud.google.com/apigee/docs/reference/apis/apigee/rest/v1/organizations.endpointAttachments/create) in the Apigee VPC. These two entities allow Apigee to connect to the target service. See [Southbound networking patterns](https://docs.cloud.google.com/apigee/docs/api-platform/architecture/southbound-networking-patterns-endpoints).

The steps for provisioning Apigee with Private Service Connect (without VPC peering) are described in [Command line provisioning without VPC peering](https://docs.cloud.google.com/apigee/docs/api-platform/get-started/install-cli-non-peered). 

![](https://docs.cloud.google.com/static/apigee/docs/api-platform/images/non-vpc-peered-arch.png)**Figure 7.** Apigee architecture without VPC peering. For details of this architecture, see [ Apigee architecture overview](https://docs.cloud.google.com/apigee/docs/api-platform/architecture/overview).![](https://docs.cloud.google.com/static/apigee/docs/api-platform/images/non-vpc-peered-arch.png)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
