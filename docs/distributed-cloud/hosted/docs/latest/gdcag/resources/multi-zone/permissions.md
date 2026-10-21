---
url: https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/resources/multi-zone/permissions/
title: Permissions control for a multi-zone universe \u00a0|\u00a0 Google Distributed Cloud air-gapped \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T23:43:35.579061+00:00
---

# Permissions control for a multi-zone universe  |  Google Distributed Cloud air-gapped  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/resources/multi-zone/permissions/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Distributed, hybrid, and multicloud ](https://docs.cloud.google.com/docs/dhm-cloud)
  * [ Google Distributed Cloud ](https://docs.cloud.google.com/distributed-cloud/docs)
  * [ Air-gapped ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdch)
  * [ 1.16.2 (Latest) ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag)



Send feedback 

#  Permissions control for a multi-zone universe Stay organized with collections  Save and categorize content based on your preferences. 

To maintain access to resources that span multiple zones in a multi-zone Google Distributed Cloud (GDC) air-gapped universe, you must implement a consistent global permissions scheme. GDC provides Identity and Access Management (IAM) features to control your global permissions without having to track and maintain zone-level access.

This document is for IT administrators within the platform administrator group who are responsible for developing and maintaining access control for resources that span across multiple zones in a GDC universe.

For more information, see [Audiences for GDC air-gapped documentation](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/resources/audiences).

## Access that spans a universe

GDC offers several key IAM capabilities to help control access to your zones and the resources within each zone:

  * **[Global role management](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag)** : control roles across your zones with global roles.
  * **[Global user permissions control](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag)** : sign in once and propagate your authentication across all zones.
  * **[Global workload and service permissions control](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag)** : authenticate your workloads and services once and propagate their authentication across all zones.



### Global role management

GDC provides built-in global permissions control that lets you apply and manage IAM roles that span all zones automatically. Global control over your permissions removes segmented use cases where you must manually apply roles in each zone. _Role-based access control (RBAC)_ is global by default, but provides fine-tuned zonal permission allocation, when necessary.

For example, consider you have a new developer that needs to access your project's resources. Since a project is global by default, it spans all zones in your universe. Instead of manually applying and maintaining the roles necessary to access the project in each zone, you apply a global access role for the project, which applies to all zones the project resides within automatically. The new developer's project access now evolves with your universe, and is propagated to new zones automatically if your universe grows.

For more information about role bindings in GDC, see [Grant and revoke access](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/platform/pa-user/iam/set-up-role-bindings).

### Global user permissions control

GDC offers _identity providers (IdP)_ to streamline authenticating users in your universe, without the hassle of signing in to each zone separately. An IdP is a system that centrally manages and secures user identities, providing authentication services. Connecting to an existing IdP lets users access GDC using their organization's credentials, without needing to create or manage separate accounts within GDC. Since an IdP is a global resource that is configured to span multiple zones by default, you can access GDC through the same IdP regardless of the zone you work in.

For more information about IdPs in GDC, see [Connect to an identity provider](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/platform/pa-user/iam/connect-identity).

### Global workload and service permissions control

Just as human users benefit from IdPs to streamline authentication across zones, your workloads and services can also benefit from global authentication in your universe with _service accounts_. Service accounts are the accounts that workloads and services use to programmatically consume resources and access microservices securely. Since a service account is a global resource that is configured to span multiple zones by default, your workloads and services can access resources that span a universe uniformly with a single set of global permissions.

As an example, consider you have a VM that has an attached storage volume. Because a volume can span two zones, if you want to allow the VM to access the volume, it must have access permissions in all zones where the volume resides. With global service accounts, you can provide the VM access to the storage volume once, which propagates to all zones where the volume resides. This capability lets you configure access on a universal scale, without managing zone-specific access.

For more information about service accounts in GDC, see [Authenticate with service accounts](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/platform/pa-user/service-identity).

## What's next

  * [Zones in GDC air-gapped](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/resources/multi-zone/mz-overview)
  * [Access zones with your tools](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/resources/multi-zone/access-zones)
  * [Sign in](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/platform/pa-user/iam/sign-in)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
