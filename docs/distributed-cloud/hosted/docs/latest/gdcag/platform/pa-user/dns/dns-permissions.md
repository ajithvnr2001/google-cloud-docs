---
url: https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/platform/pa-user/dns/dns-permissions/
title: Prepare IAM permissions \u00a0|\u00a0 Google Distributed Cloud air-gapped \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T23:43:44.973729+00:00
---

# Prepare IAM permissions  |  Google Distributed Cloud air-gapped  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/platform/pa-user/dns/dns-permissions/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Distributed, hybrid, and multicloud ](https://docs.cloud.google.com/docs/dhm-cloud)
  * [ Google Distributed Cloud ](https://docs.cloud.google.com/distributed-cloud/docs)
  * [ Air-gapped ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdch)
  * [ 1.16.2 (Latest) ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag)



Send feedback 

#  Prepare IAM permissions Stay organized with collections  Save and categorize content based on your preferences. 

This document explains how to prepare your Identity and Access Management (IAM) permissions to effectively use Cloud DNS within GDC.

GDC offers IAM for granular access to specific GDC resources and prevents unwanted access to other resources. IAM operates on the security principle of least privilege and controls who can access given resources using IAM roles and permissions.

A role is a collection of specific permissions mapped to certain actions on resources and assigned to individual subjects, such as users, groups of users, or service accounts. Therefore, you must have the proper IAM roles and permissions to use managed DNS services in GDC.

The intended audience for this document is platform administrators and application operators responsible for network administration and managing DNS for their organization within GDC.

## Get IAM permissions

To create DNS zones and records, you must have the necessary identity and access roles. Ask your Project IAM Admin to grant you the roles:

  * Managed DNS Project Viewer (`managed-dns-project-viewer`) role: views existing DNS zones and records.
  * Managed DNS Project Admin (`managed-dns-project-admin`) role: creates and updates DNS zones and records.



For more information on these roles, see [Role definitions](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/application/ao-user/iam/role-definitions).

## What's next

  * [Create DNS zones](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/platform/pa-user/dns/create-dns-zone)
  * [Create DNS records](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/platform/pa-user/dns/create-dns-records)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
