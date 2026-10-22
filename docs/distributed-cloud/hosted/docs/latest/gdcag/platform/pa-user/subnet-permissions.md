---
url: https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/platform/pa-user/subnet-permissions/
title: Prepare IAM permissions \u00a0|\u00a0 Google Distributed Cloud air-gapped \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T12:58:47.312074+00:00
---

# Prepare IAM permissions  |  Google Distributed Cloud air-gapped  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/platform/pa-user/subnet-permissions/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Distributed, hybrid, and multicloud ](https://docs.cloud.google.com/docs/dhm-cloud)
  * [ Google Distributed Cloud ](https://docs.cloud.google.com/distributed-cloud/docs)
  * [ Air-gapped ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdch)
  * [ 1.16.2 (Latest) ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag)



Send feedback 

#  Prepare IAM permissions Stay organized with collections  Save and categorize content based on your preferences. 

This document explains how to prepare your Identity and Access Management (IAM) permissions to effectively manage subnets in Google Distributed Cloud (GDC) air-gapped.

GDC uses IAM for granular access to specific resources. This model helps prevent unauthorized access to other resources.

A role is a collection of permissions that let you perform specific actions on resources. You assign roles to subjects, such as users, groups, or service accounts. To manage subnets in GDC, you must have the required IAM roles.

This document is for network administrators within the platform administrator group who are responsible for managing networking requirements within their organization. For more information, see [Audiences for GDC air-gapped documentation](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/resources/audiences).

## IAM roles for subnets

GDC supports the following IAM roles for managing subnets:

  * **Subnet Org Admin (`subnet-global-org-admin`)**: Manages multiple zone subnets within the organization. This is a global permission.
  * **Subnet Org Admin (`subnet-org-admin`)**: Manages zonal subnets within the organization. This is a zonal permission.
  * **Subnet Project Admin (`subnet-global-project-admin`)**: Manages multiple zone subnets within a project. This is a global permission.
  * **Subnet Project Admin (`subnet-project-admin`)**: Manages zonal subnets within a project. This is a zonal permission. 
    * This role includes permission to read all subnets in the project namespace and to create, update, or delete most subnets in the project namespace.
    * This role doesn't grant permission to create, update, or delete root-type subnets (`subnet.Spec.Type == Root`).
  * **Subnet Project Operator (`subnet-project-operator`)**: Manages leaf type auto-allocated subnets within projects. 
    * This role has permission to read all subnets in the project and to create, update, or delete only the auto-allocated leaf subnets in the project namespaces.
    * This role doesn't grant permission to create, update, or delete the following subnets: 
      * Root or branch type subnets (`subnet.Spec.Type == Root` or `subnet.Spec.Type == Branch`)
      * Network subnets (`subnet.Spec.NetworkSpec != nil`)
      * Subnets with dedicated CIDR blocks (`subnet.Spec.Ipv4Request.CIDR != nil` or `subnet.Spec.Ipv6Request.CIDR != nil`)
  * **Subnet Platform Viewer (`subnet-platform-viewer`)**: Lists subnets in the `platform` namespace.
  * **Shared Subnet User (`shared-subnet-user`)**: Uses a shared subnet in the `platform` namespace as a parent to allocate a subnet inside the project.
  * **SUBNET_NAME User (`SUBNET_NAME-user`)**: Uses specific subnets in the `platform` namespace. 
    * To grant a dedicated subnet in the `platform` namespace for use as a parent to allocate a subnet inside the project, the Subnet Org Admin must create or update a subnet and set the `"ipam.gdc.goog/subnet-delegation-role": auto` annotation for it.
    * To enable a subnet group within the `platform` namespace for project-internal subnet allocation, the Subnet Org Admin must set the `"ipam.gdc.goog/subnet-delegation-role": auto` annotation on all subnets in the group.



## What's next

  * [Provision IP addresses for workloads](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/platform/pa-user/create-internal-subnets)
  * [Bring your own external IP addresses](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/platform/pa-user/create-external-subnets)
  * [Design access boundaries between resources](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/resources/access-boundaries)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
