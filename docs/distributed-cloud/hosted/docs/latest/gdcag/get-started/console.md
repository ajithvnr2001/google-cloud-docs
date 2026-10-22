---
url: https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/get-started/console/
title: GDC console access \u00a0|\u00a0 Google Distributed Cloud air-gapped \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T12:58:42.829666+00:00
---

# GDC console access  |  Google Distributed Cloud air-gapped  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/get-started/console/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Distributed, hybrid, and multicloud ](https://docs.cloud.google.com/docs/dhm-cloud)
  * [ Google Distributed Cloud ](https://docs.cloud.google.com/distributed-cloud/docs)
  * [ Air-gapped ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdch)
  * [ 1.16.2 (Latest) ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag)



Send feedback 

#  GDC console access Stay organized with collections  Save and categorize content based on your preferences. 

This document provides an overview of the GDC console and how to access it. The GDC console is a graphical interface dedicated for Google Distributed Cloud (GDC) air-gapped that is fundamentally different compared to the Google Cloud console. The GDC console is only accessible within your organization's network and isn't available on the public internet.

The GDC console is available to all audience groups that manage projects and resources of the GDC organization. For more information, see [Audiences for GDC air-gapped documentation](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/resources/audiences).

## Access to the GDC console

To access the GDC console, you must first connect to your GDC environment's network and then navigate to the GDC console URL in a web browser. Based on your universe's settings, the GDC console URL can provide access to the global view or zonal view:

  * For a global GDC console URL, use the syntax `https://console.ORG_NAME.SUFFIX`, such as `https://console.org-1.gdc.google.com`.
  * For a zonal GDC console URL, use the syntax `https://console.ORG_NAME.ZONE.SUFFIX`, such as `https://console.org-1.zone-1.gdc.google.com`.



Reach out to your infrastructure operator group for the GDC console URL for your organization if you don't know it. For more information about global and zonal access with the GDC console, see [Global and zonal resources](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/resources/multi-zone/api-servers#console).

After [signing in with your identity provider](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/platform/pa-user/iam/sign-in), the GDC console interface is displayed.

## GDC console navigation

The GDC console provides access to various management and observability features. The layout consists of a header bar, a navigation menu, and a main view for displaying and managing resources.

### Header bar

The header bar at the top of the page includes a project picker. Use the project picker to select a project and switch the GDC console context. The resources available in the navigation menu and displayed in the main work area are scoped to the project you select. For organization-scoped resources, you must select the organization to view resources scoped outside your project. For more information, see [Select a project or organization](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/platform/pa-user/manage-projects#select-project).

Additionally, the header bar provides a _help_ **Help** option that points to documentation hosted in your air-gapped environment.

If you need to log out of your selected identity, click _logout_ **Logout**.

### Navigation menu

The navigation menu, accessible by clicking _menu_ **Menu** , provides access to services and resources available within the selected project or organization, such as the following:

  * Marketplace
  * Identity & Access
  * Compute
  * Storage
  * Backup & Restore
  * Databases
  * Networking
  * Artificial Intelligence



The options available from the navigation menu depend on your Identity and Access Management (IAM) roles. For more information, see [Predefined role descriptions](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/platform/pa-user/iam/role-descriptions).

## What's next

  * [Access zones with your tools](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/resources/multi-zone/access-zones)
  * [Resource hierarchy](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/resources/resource-hierarchy)
  * [Connect to an identity provider](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/platform/pa-user/iam/connect-identity)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
