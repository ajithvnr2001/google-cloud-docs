---
url: https://docs.cloud.google.com/confidential-computing/confidential-vm/docs/restrict-confidential-vm-interaction/
title: Restrict VM interaction to Confidential VM only \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T09:11:28.466937+00:00
---

# Restrict VM interaction to Confidential VM only  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/confidential-computing/confidential-vm/docs/restrict-confidential-vm-interaction/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Compute ](https://docs.cloud.google.com/docs/compute-area)
  * [ Compute Engine ](https://docs.cloud.google.com/compute/docs)
  * [ Confidential VM ](https://docs.cloud.google.com/confidential-computing/confidential-vm/docs)
  * [ Guides ](https://docs.cloud.google.com/confidential-computing/confidential-vm/docs/confidential-vm-overview)



Send feedback 

#  Restrict VM interaction to Confidential VM only Stay organized with collections  Save and categorize content based on your preferences. 

You can set up a security perimeter that makes sure your Confidential VM instances can only interact with other Confidential VM instances. This is achieved with the following services:

  * [Shared Virtual Private Cloud (VPC) networks](https://docs.cloud.google.com/vpc/docs/shared-vpc)

  * [Organization policy constraints](https://docs.cloud.google.com/resource-manager/docs/organization-policy/using-constraints)

  * [Firewall rules](https://docs.cloud.google.com/vpc/docs/using-firewalls)




A security perimeter can be established around Confidential VM instances that reside inside the same project, or in separate projects.

## Required roles

To get the permissions that you need to create a security perimeter, ask your administrator to grant you the following IAM roles on the organization: 

  * [Organization Administrator ](https://docs.cloud.google.com/iam/docs/roles-permissions/resourcemanager#resourcemanager.organizationAdmin) (`roles/resourcemanager.organizationAdmin`)
  * [Compute Shared VPC Admin ](https://docs.cloud.google.com/iam/docs/roles-permissions/compute#compute.xpnAdmin) (`roles/compute.xpnAdmin`)
  * [Project IAM Admin ](https://docs.cloud.google.com/iam/docs/roles-permissions/resourcemanager#resourcemanager.projectIamAdmin) (`roles/resourcemanager.projectIamAdmin`)
  * [Compute Network User ](https://docs.cloud.google.com/iam/docs/roles-permissions/compute#compute.networkUser) (`roles/compute.networkUser`)
  * [Compute Instance Admin ](https://docs.cloud.google.com/iam/docs/roles-permissions/compute#compute.instanceAdmin) (`roles/compute.instanceAdmin`)



For more information about granting roles, see [Manage access to projects, folders, and organizations](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

You might also be able to get the required permissions through [custom roles](https://docs.cloud.google.com/iam/docs/creating-custom-roles) or other [predefined roles](https://docs.cloud.google.com/iam/docs/roles-overview#predefined). 

To learn more about these roles, see [Required administrative roles](https://docs.cloud.google.com/vpc/docs/shared-vpc#iam_roles_required_for_shared_vpc) in the [Shared VPC overview](https://docs.cloud.google.com/vpc/docs/shared-vpc).

## Create a Confidential VM perimeter

To create a security perimeter around your Confidential VM instances, complete the following instructions:

  1. Create a [folder](https://docs.cloud.google.com/resource-manager/docs/creating-managing-folders) in your organization called `confidential-perimeter`.

  2. Inside the folder, [create a shared VPC host project](https://docs.cloud.google.com/vpc/docs/provisioning-shared-vpc). This defines the Confidential VM perimeter.




After you've created a VPC host project, share the project by granting your networking team access.

## Enforce the perimeter

To prevent [service projects](https://docs.cloud.google.com/vpc/docs/shared-vpc#shared_vpc_host_project_and_service_project_associations) from allowing non-Confidential VM instances from interacting with the perimeter, [apply the following organization policy constraints](https://docs.cloud.google.com/resource-manager/docs/organization-policy/using-constraints) to your `confidential-perimeter` folder as indicated.

Constraint | Value | Description  
---|---|---  
`constraints/compute.restrictNonConfidentialComputing` | `deny compute.googleapis.com` | Forces all service projects to create Confidential VM instances only.  
`constraints/compute.restrictSharedVpcHostProjects` | `under: FOLDER_ID` | Prevents projects inside the perimeter from creating another Shared VPC host project. Replace FOLDER_ID with the [ ID](https://docs.cloud.google.com/resource-manager/docs/creating-managing-folders#viewing_or_listing_folders_and_projects) of your `confidential-perimeter` folder.  
`constraints/compute.restrictVpcPeering` | `is: []` | Prevents service projects from peering network and network connections outside of the perimeter.  
`constraints/compute.vmExternalIpAccess` | `is: []` | Forces all Confidential VM instances in service projects to use internal IPs.  
`constraints/compute.restrictLoadBalancerCreationForTypes` |  `allowedValues: ["INTERNAL_TCP_UDP", "INTERNAL_HTTP_HTTPS",]` | Prevents all VM instances from defining an internet-visible ingress point. You may override this for specific projects in your perimeter that should have ingress—for example, your perimeter network.  
  
To control network data transfer outside of the perimeter, use [VPC firewall rules](https://docs.cloud.google.com/vpc/docs/using-firewalls).

## What's next

You can use VPC Service Controls to extend the security perimeter to cover Google Cloud resources. To learn more, see [Overview of VPC Service Controls](https://docs.cloud.google.com/vpc-service-controls/docs/overview).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
