---
url: https://docs.cloud.google.com/apigee/docs/hybrid/v1.14/precog-overview/
title: Overview \u00a0|\u00a0 Apigee \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T19:02:23.482047+00:00
---

# Overview  |  Apigee  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/apigee/docs/hybrid/v1.14/precog-overview/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Apigee ](https://docs.cloud.google.com/apigee/docs)
  * [ Guides ](https://docs.cloud.google.com/apigee/docs/api-platform/get-started/what-apigee)



Send feedback 

#  Overview Stay organized with collections  Save and categorize content based on your preferences. 

You are currently viewing version 1.14 of the Apigee hybrid documentation. For more information, see [Supported versions](https://docs.cloud.google.com/apigee/docs/hybrid/supported-platforms#supported-versions).

Version 1.14 keyboard_arrow_down

Supported versions:

  * [ v1.17 (latest) ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.17/precog-overview.html)
  * [ v1.16 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.16/precog-overview.html)
  * [ v1.15 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.15/precog-overview.html)
  * [ v1.14 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.14/precog-overview.html)
  * [ List of supported versions ](https://docs.cloud.google.com/apigee/docs/hybrid/supported-platforms#supported-versions)

Unsupported versions:

  * [ v1.13 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.13/precog-overview.html)
  * [ v1.12 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.12/precog-overview.html)
  * [ v1.11 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.11/precog-overview.html)
  * [ v1.10 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.10/precog-overview.html)
  * [ v1.9 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.9/precog-overview.html)
  * [ v1.8 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.8/precog-overview.html)
  * [ v1.7 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.7/precog-overview.html)
  * [ v1.6 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.6/precog-overview.html)
  * [ v1.5 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.5/precog-overview.html)
  * [ v1.4 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.4/precog-overview.html)
  * [ v1.3 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.3/precog-overview.html)
  * [ v1.2 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.2/precog-overview.html)
  * [ v1.1 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.1/precog-overview.html)



In this part, you perform the following tasks:

Task | Description |  [Prerequisites](https://docs.cloud.google.com/apigee/docs/hybrid/v1.14/prerequisites) |  You need a Google Cloud project, a billing account, and the `gcloud` CLI.  If your installation will use [Data residency](https://docs.cloud.google.com/apigee/docs/api-platform/get-started/drz-concepts), Your project must have a [Subscription](https://docs.cloud.google.com/apigee/docs/api-platform/reference/subscription-entitlements) billing type and you must know in advance the regions where you plan to locate your control plane and user data.   
---|---  
[Step 1: Enable APIs](https://docs.cloud.google.com/apigee/docs/hybrid/v1.14/precog-enableapi) |  Enable the APIs for Google Cloud services used by Apigee hybrid.   
[Step 2: Create an Apigee organization](https://docs.cloud.google.com/apigee/docs/hybrid/v1.14/precog-provision) |  Your [Apigee organization](https://docs.cloud.google.com/apigee/docs/api-platform/get-started/basic-concepts#organization) contains everything you create using Apigee, including API proxies and services, along with the resources needed to support them. Note that an Apigee organization is _not_ the same as a Google Cloud organization.   
[Step 3: Create an environment and environment group](https://docs.cloud.google.com/apigee/docs/hybrid/v1.14/precog-add-environment) |  An [environment](https://docs.cloud.google.com/apigee/docs/api-platform/get-started/basic-concepts#environment) is an isolated software environment in which you can use Apigee's software tools to create and deploy API proxies. You can create multiple environments in an organization. An [environment group](https://docs.cloud.google.com/apigee/docs/api-platform/get-started/basic-concepts#environment-group) is used to group one or more Apigee environments under a single hostname that can be used to call API proxies deployed to any environment in the environment group.   
**Note:** If you plan to enable Google Cloud [ Virtual Private Cloud (VPC) Service Controls](https://cloud.google.com/vpc-service-controls) with your Apigee hybrid installation, see [Using VPC Service Controls with Apigee and Apigee hybrid](https://docs.cloud.google.com/apigee/docs/api-platform/security/vpc-sc) for instructions before you proceed.

##  Next step 

Go to Step 1: [Enable APIs](https://docs.cloud.google.com/apigee/docs/hybrid/v1.14/precog-enableapi). 

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
