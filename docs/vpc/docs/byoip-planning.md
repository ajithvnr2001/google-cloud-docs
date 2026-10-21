---
url: https://docs.cloud.google.com/vpc/docs/byoip-planning/
title: Planning for bring your own IP addresses \u00a0|\u00a0 Virtual Private Cloud \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T02:28:20.629734+00:00
---

# Planning for bring your own IP addresses  |  Virtual Private Cloud  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/vpc/docs/byoip-planning/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Networking ](https://docs.cloud.google.com/docs/networking)
  * [ Virtual Private Cloud ](https://docs.cloud.google.com/vpc/docs)
  * [ Guides ](https://docs.cloud.google.com/vpc/docs/overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Planning for bring your own IP addresses

Bring your own IP addresses (BYOIP) lets you provision and use your own public IPv4 addresses for Google Cloud resources. After the IP addresses are imported, Google Cloud manages them in the same way as Google-provided IP addresses, with these exceptions:

  * The IP addresses are available only to the customer who brought them.

  * There are no charges for idle or in-use IP addresses.




## Planning your deployment

It's important to plan your deployment, because provisioning and deletion processes require multiple weeks to complete. For more information about the provisioning timeline and allowed prefix sizes, see [Limitations](https://docs.cloud.google.com/vpc/docs/using-bring-your-own-ip#limitations).

Here are some decisions that should be considered when you plan your deployment:

  * **Who is responsible for administering BYOIP addresses?** This is typically an administrator or group, but is not typically the same users who manage individual projects. Use IAM roles and permissions to distinguish who has privileges for the public advertised prefixes and public delegated prefixes that you plan to provision.

  * **How are prefixes managed?** It is likely that you want to use your BYOIP addresses in different projects. You can manage prefixes centrally in a project distinct from the ultimate destinations of the IP addresses. We recommend that you isolate prefix administration in a project of its own, including its own users and groups with Public IP Admin permissions. This isolation helps to prevent confusion about prefix administration and inadvertent or unauthorized use of prefixes. For more information, see Project architecture.

  * **How are prefixes named?** Every BYOIP resource (public advertised prefix, public delegated prefix, sub-prefix) requires a name, and the name is used to manage each resource. You assign the name during resource creation, and names can't be changed without deleting and recreating the resource. For this reason, we recommend that you create generic names that won't need to change—for example, `pap-203-0-113-0-24`, `pdp-203-0-113-0-25`, `sub-203-0-113-0-28`, where the letters denote the resource type, and the numbers denote the specific prefix and prefix length.

  * **Where are the IP addresses provisioned?** It's useful to think of the provisioning process as "stocking" IPs into regions (or the global scope). The provisioning process for stocking IP addresses takes multiple weeks to complete, so it's useful to plan and deploy public delegated prefixes long before they are needed.

You don't have to use all IPs in a public delegated prefix immediately. If you aren't sure where you need them, provision only the public delegated prefixes that you're certain you need to use. Moving a public delegated prefix requires complete deletion and then recreation, which can take approximately eight weeks.

After public delegated prefix provisioning is complete, you can delegate sub-prefixes to projects and create addresses for use with resources. If you anticipate needing BYOIP addresses in a region, complete the public delegated prefix provisioning process in advance, so you can later fulfill addressing needs on-demand.

For example, if you need some IP addresses in `us-central1` and some IP addresses for global load balancers, and you want to reserve some IP addresses for the future, you should create the following plan.

Prefix type | Prefix | Scope  
---|---|---  
Public advertised prefix | 203.0.113.0/24 |   
Public delegated prefix | 203.0.113.0/28 | us-central1  
Public delegated prefix | 203.0.113.16/28 | us-east-4  
Public advertised prefix for global load balancers | 192.0.2.0/24 |   
Public delegated prefix | 192.0.2.0/28 | global  
  
The remaining IP addresses are reserved for future use.




## Project architecture

We recommend that you use organizations to benefit from features such as IAM permissions at the organization level and [Shared VPC](https://docs.cloud.google.com/vpc/docs/shared-vpc). See [creating and managing organizations](https://docs.cloud.google.com/resource-manager/docs/creating-managing-organization#creating-projects) for more information about using an organization.

### BYOIP address administration in an organization

In this example of a project belonging to an organization, there is a dedicated project, `Public IP project`, used to manage BYOIP addresses. The Public IP Admin for the organization has created the public advertised prefix and public delegated prefixes in the `Public IP project`.

When the `VPC project` needs public IP addresses, the Public IP Admin for the organization creates the IP addresses in the `VPC project`.

The organization can contain multiple projects, and the Public IP Admin can delegate IP addresses to them all from the `Public IP project`.

[ ![](https://docs.cloud.google.com/static/vpc/images/byoip-vpc-standalone.svg)](https://docs.cloud.google.com/static/vpc/images/byoip-vpc-standalone.svg)

**Figure 1.** You can use organizations and projects to manage BYOIP addresses.

### BYOIP addresses administration with Shared VPC

In this example of an organization that contains Shared VPC, there is a dedicated project, `Public IP project`, used to manage BYOIP addresses. The Public IP Admin for the organization has created the public advertised prefix and public delegated prefixes in the `Public IP project`.

When the `Shared VPC host project` or the related service projects need public IP addresses, the Public IP Admin for the organization creates the IP addresses in the `Shared VPC host project`. The host project and the service projects can access the BYOIP addresses from the host project.

Creating IP addresses in a Shared VPC service project is not supported.

[ ![](https://docs.cloud.google.com/static/vpc/images/byoip-vpc-shared.svg)](https://docs.cloud.google.com/static/vpc/images/byoip-vpc-shared.svg)

**Figure 2.** You can delegate BYOIP addresses to a Shared VPC host project, but not to a Shared VPC service project. However, a service project can use BYOIP addresses that were delegated to the host project.

### BYOIP address administration without an organization

If you use a project that does not belong to an organization, you can't create a separate project for BYOIP address administration. Create the public advertised prefix and public delegated prefixes in the same project that needs the BYOIP addresses.

## What's next

  * [Create a public advertised prefix](https://docs.cloud.google.com/vpc/docs/create-pap)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
