---
url: https://docs.cloud.google.com/chrome-enterprise-premium/docs/intune-overview/
title: Overview of Chrome Enterprise Premium integration with Microsoft Intune \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T08:57:45.910987+00:00
---

# Overview of Chrome Enterprise Premium integration with Microsoft Intune  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chrome-enterprise-premium/docs/intune-overview/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Chrome Enterprise Premium ](https://docs.cloud.google.com/chrome-enterprise-premium/docs)
  * [ Guides ](https://docs.cloud.google.com/chrome-enterprise-premium/docs/overview)



Send feedback 

#  Overview of Chrome Enterprise Premium integration with Microsoft Intune Stay organized with collections  Save and categorize content based on your preferences. 

Microsoft Intune is a cloud-based service that focuses on mobile device management (MDM) and mobile application management (MAM). Microsoft Intune helps administrators assess the security posture of managed devices within their organization. Google's Chrome Enterprise Premium integrates with Microsoft Intune to let you ensure that the devices connecting to your organization's web resources and applications are authorized, secured, and managed as per your organization's policies. 

## When to use Chrome Enterprise Premium integration with Intune

Use this integration when you want to collect the real-time information about the devices in your organization using Intune, and use this information to manage your devices and control access to your organizational resources using Chrome Enterprise Premium.

## How Chrome Enterprise Premium works with Intune

Chrome Enterprise Premium uses a zero trust model to grant access to your organizational resources based on a user's device identity and context of the request.

In this integration, Intune collects the real-time device information and provides this information to Chrome Enterprise Premium. The BCE Intune connector collects data from Intune using Microsoft Graph APIs. [Access Context Manager](https://docs.cloud.google.com/access-context-manager/docs/overview), which is a part of Chrome Enterprise Premium, uses the device information collected by the BCE Intune connector, and provides security-based access control to your resources by using access levels. **Note:** Creating custom access levels in Access Context Manager is available in Chrome Enterprise Premium , which is the paid subscription of Chrome Enterprise Premium. To upgrade, [contact our sales team](https://go.chronicle.security/beyondcorp-enterprise-upgrade). 

The following diagram shows how Chrome Enterprise Premium works with Intune:

![Architecture diagram](https://docs.cloud.google.com/static/chrome-enterprise-premium/images/intune-overview.svg)![](https://docs.cloud.google.com/static/chrome-enterprise-premium/images/intune-overview.svg)

## What's next

  * [Set up Chrome Enterprise Premium integration with Intune](https://docs.cloud.google.com/chrome-enterprise-premium/docs/setting-up-intune)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
