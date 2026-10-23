---
url: https://docs.cloud.google.com/risk-manager/docs/onboard/
title: Onboarding to Cyber Insurance Hub \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:03:24.677802+00:00
---

# Onboarding to Cyber Insurance Hub  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/risk-manager/docs/onboard/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Cyber Insurance Hub ](https://docs.cloud.google.com/risk-manager/docs)
  * [ Guides ](https://docs.cloud.google.com/risk-manager/docs/quickstarts)



Send feedback 

#  Onboarding to Cyber Insurance Hub Stay organized with collections  Save and categorize content based on your preferences. 

**Preview**

This product is subject to the "Pre-GA Offerings Terms" in the General Service Terms section of the [Service Specific Terms](https://docs.cloud.google.com/terms/service-terms#1). Pre-GA products are available "as is" and might have limited support. For more information, see the [launch stage descriptions](https://cloud.google.com/products/#product-launch-stages). 

This document describes the process for onboarding to Cyber Insurance Hub.

## Overview

Onboarding to Cyber Insurance Hub requires engagement from your IT organization. The Cyber Insurance Hub tool is deployed as a Google Cloud service and lets you apply for cyber insurance using the [Risk Protection Program](https://cloud.google.com/security/products/risk-protection-program). If you have questions about the following processes or the Risk Protection Program, contact your Google Cloud sales representative. If you don't have a sales representative, [contact the Risk Protection Program team](https://forms.gle/97HcNd5H9oRJdvby9).

## Onboarding steps

The following steps describe the process for onboarding to Cyber Insurance Hub. In order to complete these steps, you must have the [Organization Administrator](https://docs.cloud.google.com/iam/docs/roles-permissions/resourcemanager#resourcemanager.organizationAdmin) role. For more information about Identity and Access Management (IAM) roles, see [Roles and permissions](https://docs.cloud.google.com/iam/docs/roles-overview).

  1. In the Google Cloud console, select the organization to onboard onto Cyber Insurance Hub. Cyber Insurance Hub is only supported for Google Cloud [organizations](https://docs.cloud.google.com/resource-manager/docs/cloud-platform-resource-hierarchy).

  2. [Set up Security Command Center](https://docs.cloud.google.com/security-command-center/docs/set-up). This step is required for Cyber Insurance Hub reports to be generated.

The following table describes the [Security Command Center pricing tiers](https://cloud.google.com/security-command-center/pricing#tier-pricing) and the Cyber Insurance Hub functionality that they enable.

Security Command Center tier | Cyber Insurance Hub functionality | Security Command Center enablement  
---|---|---  
Standard |  You can see CIS Benchmarks through aggregated reports. However, links to specific findings in Security Command Center are not available.  |  To enable the Standard tier, see [ Activate Security Command Center Standard tier for an organization](https://docs.cloud.google.com/security-command-center/docs/activate-standard-tier).   
Premium | Full |  To enable the Premium tier, see [ Activate Security Command Center Premium tier for an organization](https://docs.cloud.google.com/security-command-center/docs/activate-premium-tier).   
Enterprise | Full |  To enable the Enterprise tier, see [ Activate the Security Command Center Enterprise tier](https://docs.cloud.google.com/security-command-center/docs/activate-enterprise-tier).   
  3. Ensure that the Security Health Analytics service is enabled in Security Command Center. This step is required for Cyber Insurance Hub reports to be generated.

For more information, see [Configure Security Command Center services](https://docs.cloud.google.com/security-command-center/docs/how-to-configure-security-command-center) and follow the instructions to [enable](https://docs.cloud.google.com/security-command-center/docs/how-to-configure-security-command-center#enable-service) Security Health Analytics. You can also go to the Security Command Center **Settings** page to ensure that the Security Health Analytics service is set to **Enabled by default**.

[Go to Security Command Center Settings](https://console.cloud.google.com/security/command-center/config/services)




## What's next?

  * Learn how to [configure Cyber Insurance Hub](https://docs.cloud.google.com/risk-manager/docs/configuring-risk-manager).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
