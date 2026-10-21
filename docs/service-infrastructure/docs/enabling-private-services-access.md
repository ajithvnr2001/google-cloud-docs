---
url: https://docs.cloud.google.com/service-infrastructure/docs/enabling-private-services-access/
title: Enabling private services access \u00a0|\u00a0 Service Infrastructure \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T05:40:24.415910+00:00
---

# Enabling private services access  |  Service Infrastructure  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/service-infrastructure/docs/enabling-private-services-access/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Service Infrastructure ](https://docs.cloud.google.com/service-infrastructure/docs)
  * [ Guides ](https://docs.cloud.google.com/service-infrastructure/docs/how-to)



Send feedback 

#  Enabling private services access Stay organized with collections  Save and categorize content based on your preferences. 

As a service producer, you can allow service consumers to provision resources with private (RFC 1918) or public IP addresses. If service consumers want to use private IP addresses, they must use [private services access](https://docs.cloud.google.com/vpc/docs/private-services-access). However, service consumers can only use private service access if your managed service offers it. To offer private connectivity, you must complete a one-time onboarding process.

The onboarding process requires you to use the Service Networking API and tenancy units. For detailed step-by-step instructions, contact your Google representative.

## Overview

The following sections describe the components and general network topology required to enable private services access for your managed service.

### Tenancy units

When a service consumer enables your managed service, the service create a [tenancy unit](https://docs.cloud.google.com/service-infrastructure/docs/tenancy-units-tutorial) to formalize a relationship between your Google Cloud organization and the service consumer's project. Tenancy units isolate resources and billing costs between different service consumers.

For each service consumer, you will have two tenancy units. One for your managed service and another for the private access management service. The managed service is the external service that you're offering to service consumers, and the private access management service manages private connections with service consumer VPC networks. These tenancy units must be in the same Google Cloud organization where your managed service lives.

### Service Networking

Service Networking automates the private connectivity set up (using VPC Network Peering) between you and the service consumer. You enable and use Service Networking in the same project in which you created the private access management service. This is a different project from the one that contains your managed service.

When a service consumer creates a private connection with your managed service, Service Networking creates a _Shared VPC host project_ and a _Shared VPC network_ for you. The host project and network are created in a predesignated Google Cloud folder in your organization. You specify this folder name as part of the onboarding process. The project and network are contained in a tenancy unit, so they are isolated and can only be used by that service consumer.

After Service Networking creates the Shared VPC network, Service Networking automatically creates a VPC Networking Peering connection between the Shared VPC network and the service consumer-specified VPC network.

Service consumers must also supply an allocated IP address range when they create the private connection. This allocation reserves IP addresses that can only be used by you, a service producer. For example, when a service consumer provisions a resource, you use Service Networking to create subnets in the Shared VPC network. For the subnet's IP address range, Service Networking automatically selects a range from the allocated range. This process prevents collisions between the Shared VPC network and service consumer VPC network.

**Note:** Creating a subnet is a long running operation. You can [poll](https://docs.cloud.google.com/service-infrastructure/docs/polling-operations) it regularly to check the status of the operation.

#### Shared VPC service projects

When your service provisions a service consumer's resource for the first time, your managed service provisions it in a [Shared VPC service project](https://docs.cloud.google.com/vpc/docs/shared-vpc), which is attached to the Service Networking host project. This Shared VPC relationship enables resources in the service project to use subnets in the Shared VPC network.

Your managed service creates the service project in a tenancy unit and predesignated folder, specified during the onboarding process. The folder and tenancy unit are related to your managed service and are different from the ones that Service Networking uses.

### Network topology

The following example shows a single service consumer that has private connectivity to a single service producer. The service consumer provisioned two resources in different regions. Because each resource is in a different region, they are in different subnets.

[ ![](https://docs.cloud.google.com/static/service-infrastructure/images/service-networking-overview.svg)](https://docs.cloud.google.com/static/service-infrastructure/images/service-networking-overview.svg) Overview of Service Networking for service producers (click to enlarge)

  * There are two Endpoints projects: one for the managed service and another one for the private access management service. These must be in the same Google Cloud organization.

  * Within the Google Cloud organization, there are two folders, one for each of the Endpoints services. The private access management service folder contains a Shared VPC host project for the private connection. The managed service folder contains a service project for service consumer resources.

    * In each folder, the service consumer-related projects are contained in tenancy units. Both tenancy units are associated with `consumer-project-a`.
  * Service consumers must initiate the private connection (which is also a VPC Network Peering connection). They must supply an allocated IP address range for the private connection from which the subnet IP addresses come. For more information about the service consumer steps, see [Configuring Private Services Access](https://docs.cloud.google.com/vpc/docs/configure-private-services-access).

    * If you offer multiple services, service consumers only need one private connection. All traffic to and from the service consumer goes through the Shared VPC host project.
  * In a single service consumer project, multiple VPC networks can privately connect to your services. This requires a Shared VPC host project for each connected VPC network. However, all of those projects can be contained in the same `consumer-project-a` tenancy unit.

  * In the host project, you must configure firewall rules and routes to enable connectivity to new resources. Because other services can use the same Shared VPC network, these rules can allow or deny connectivity between your different services.




## Onboarding process

The following list is a general outline of the onboarding process. You must complete this process for each managed service that will offer private connectivity. Contact your Google representative for more information.

  1. Create a peering management service.

This is a managed service that a service producer builds through the Service Management and Endpoints API. For more information, contact your Google representative.

  2. Provide the following configuration information to your Google representative:

     * The minimum IP address range that service consumers must allocate when they connect to you, specified as an IPv4 prefix length. If you offer multiple services, you might want users to allocate a larger IP address range, such as `/16`.
     * The folder ID where your private access management service creates Shared VPC hosts projects. Use Resource Manager to find the folder ID.
     * The billing account that's associated with the organization where your private access management service creates Shared VPC host projects.
     * The principals (typically these are service account IDs) that manage the host project's network firewall rules.
  3. Activate the Compute Engine API.

For each Shared VPC host project, activate the `compute.googleapis.com` API, which you can do by using the Service Usage APIs or in the project configuration.

After resources have been provisioned, configure firewall rules for the Shared VPC network in the host project. You must use the identity that you provided during the onboarding process to access the VPC network. If you offer other services, those services might use the same VPC network. Don't create rules that might inadvertently allow or deny traffic to other services.

  4. Inform service consumers.

Inform service consumers that they must establish a private connection. For more information, see [Configuring Private Services Access](https://docs.cloud.google.com/vpc/docs/private-access-options). Service consumers must provide the following information:

     * The name of their project and network where they want to establish private connectivity.
     * The Cloud region where the resource must be provisioned.



## What's next

  * To enable Service Networking APIs, see [Getting Started with the Service Networking API](https://docs.cloud.google.com/service-infrastructure/docs/service-networking/getting-started).
  * For information about Service Networking private connection limits, see [Quotas and Limits](https://docs.cloud.google.com/service-infrastructure/docs/quotas#networking).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
