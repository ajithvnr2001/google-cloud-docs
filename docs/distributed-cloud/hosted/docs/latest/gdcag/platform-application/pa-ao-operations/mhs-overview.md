---
url: https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/platform-application/pa-ao-operations/mhs-overview/
title: Managed Harbor Service overview \u00a0|\u00a0 Google Distributed Cloud air-gapped \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T12:58:55.615085+00:00
---

# Managed Harbor Service overview  |  Google Distributed Cloud air-gapped  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/platform-application/pa-ao-operations/mhs-overview/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Distributed, hybrid, and multicloud ](https://docs.cloud.google.com/docs/dhm-cloud)
  * [ Google Distributed Cloud ](https://docs.cloud.google.com/distributed-cloud/docs)
  * [ Air-gapped ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdch)
  * [ 1.16.2 (Latest) ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag)



Send feedback 

#  Managed Harbor Service overview Stay organized with collections  Save and categorize content based on your preferences. 

This document provides an overview of Managed Harbor Service (MHS) in Google Distributed Cloud (GDC) air-gapped.

MHS is a fully managed container registry based on the open-source Harbor project. Integrating MHS into your GDC environment provides a secure, scalable way to manage the lifecycle of your container artifacts in isolated environments without manual maintenance.

This overview introduces the foundational concepts required to work with MHS in GDC air-gapped, including the relationship between GDC projects and Harbor instance projects. It also details the administrative boundaries between infrastructure-level Identity and Access Management (IAM) roles and registry-level Role-based access control (RBAC), as well as core features such as automated garbage collection and service performance limits.

This document is for developers in platform administrator or application operator groups that use and administer MHS in GDC. For more information, see [Audiences for GDC air-gapped](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/resources/audiences) documentation.

## How Managed Harbor Service in GDC works

### Operational planes

GDC MHS operates on two distinct functional layers of network architecture. Each layer enables specific operations:

  * Management-plane layer: lets you create and delete Harbor registry instances.
  * Data-plane layer: lets you push and pull container images in your Harbor instance.



### Differences between GDC projects and Harbor instance projects

Managed Harbor Service involves two distinct project types. Understanding the interaction between these entities ensures you manage resources and access controls at the appropriate layer:

  * **GDC project** : The organizational unit for infrastructure management. Use this to manage the Harbor registry instance along with other GDC resources like VMs and clusters.

    * **Limits** : A GDC project can contain only one Harbor instance. However, that single instance can be shared across multiple GDC projects to provide a centralized registry for your environment.
    * **Access** : Requires GDC project-level IAM roles for instance creation, management, and administrative tasks.
  * **Harbor instance project** : A logical grouping for artifact management that exists within a Harbor instance. Use this to organize container images and repository-level access.

    * **Limits** : A Harbor instance supports multiple Harbor projects. These can be allocated to individual teams or users to enable multi-tenancy within a shared registry.
    * **Access** : Requires registry-specific RBAC roles to manage repositories, perform administrative tasks, and control artifact access within the project.



### Features

Harbor is a Cloud Native Computing Foundation (CNCF) graduated open source project that provides a built-in cloud container registry solution for Kubernetes and Docker. With managed service integration, you can deploy a Harbor instance to store and manage artifacts on GDC. MHS offers the following features:

  * Harbor instances are automatically provisioned and managed by GDC.
  * Harbor is integrated with IAM for authentication.
  * Harbor supports programmatic access through project service accounts to enable automated workloads.
  * Harbor instances can be upgraded to the newer stable version.
  * Harbor is enhanced to meet GDC's compliance and quality requirements.
  * A Harbor instance is a zonal resource; it's deployed in one zone, but it's accessible from any zones within the GDC deployment universe.



## Role-based access control for MHS

GDC enforces role-based access control (RBAC) for Managed Harbor Service (MHS) at two distinct layers: the GDC project level and the Harbor registry project level.

Project service accounts authenticate programmatically using short-lived identity tokens issued by IAM. This removes the need to manually create and manage Harbor robot accounts. While a service account's IAM role permits interaction with the Harbor instance, you must still assign it a corresponding Harbor registry project role to authorize specific data operations.

To control access to your registries, configure permissions at both the platform and repository levels.

**Note:** When assigning any roles in Distributed Cloud, always follow the [IAM principle of least privilege](https://docs.cloud.google.com/iam/docs/using-iam-securely#least_privilege).

### IAM roles for GDC project access

GDC manages project-level permissions using IAM roles. You can assign these roles to both users and project service accounts to control access to your Harbor instances.

  * **For platform administrators and users** : identify the required roles related to your specific task in the procedural documentation and request access from your Organization IAM Admin. For more information, see [Grant and revoke access](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/platform/pa-user/iam/set-up-role-bindings).
  * **For service accounts** : grant these same IAM roles to project service accounts to enable programmatic authentication for automated workloads, such as registry instance management and artifact deployment.
  * **For infrastructure operators** : consult the GDC MHS service manuals to determine the exact IAM roles required for your specific operational tasks.



### Registry roles for Harbor project access

A Harbor project uses its own set of RBAC mechanisms that operate independently from IAM roles. To manage repositories and artifacts, both users and project service accounts must have the required role assigned directly at the Harbor project level.

For more information about Harbor's specific roles and permissions, see the Harbor documentation for [Managing user access](https://goharbor.io/docs/2.8.0/administration/managing-users/).

## Performance

Google has tested and verified MHS to support the limits specified in [System limits](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/resources/system-limits#mhs).

The actual performance limits might be higher.

## Garbage collection

When you use MHS to add and delete images from the registry, unused data can build up over time. To avoid straining storage resources, MHS automatically performs garbage collection every 12 hours. You don't have to configure garbage collection manually.

## What's next

Configure your workspace and projects to start managing container images:

  * [Create Harbor registry instances](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/platform-application/pa-ao-operations/create-harbor-instances).
  * [Create Harbor instance projects](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/platform-application/pa-ao-operations/create-harbor-projects).
  * [Manage Harbor registry instances](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/platform-application/pa-ao-operations/manage-harbor-instances).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
