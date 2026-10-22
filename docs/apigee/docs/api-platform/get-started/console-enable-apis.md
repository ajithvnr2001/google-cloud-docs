---
url: https://docs.cloud.google.com/apigee/docs/api-platform/get-started/console-enable-apis/
title: Step 1: Enable required APIs \u00a0|\u00a0 Apigee \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T09:48:50.433833+00:00
---

# Step 1: Enable required APIs  |  Apigee  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/apigee/docs/api-platform/get-started/console-enable-apis/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Apigee ](https://docs.cloud.google.com/apigee/docs)
  * [ Guides ](https://docs.cloud.google.com/apigee/docs/api-platform/get-started/what-apigee)



Send feedback 

#  Step 1: Enable required APIs Stay organized with collections  Save and categorize content based on your preferences. 

_This page applies to**Apigee** , but not to **Apigee hybrid**._

_View[ Apigee Edge](https://docs.apigee.com/api-platform/get-started/what-apigee-edge) documentation._ ![](https://fonts.gstatic.com/s/i/googlematerialicons/help/v13/gm_grey-24dp/1x/gm_help_gm_grey_24dp.png)

![](https://docs.cloud.google.com/static/apigee/docs/api-platform/images/ng-saas/chevrons-1-setup.png)

## What you're doing in this step

To provision and use an Apigee instance, you must enable the following APIs for your Cloud project:

API Name | Location | Description  
---|---|---  
[Apigee](https://console.cloud.google.com/apis/library/apigee.googleapis.com) | `apigee.googleapis.com` | Provides communications between your project and other services and Cloud APIs.  
[API hub](https://console.cloud.google.com/apis/library/apihub.googleapis.com) | `apihub.googleapis.com` | Used to manage your API hub instance.  
[Service Networking](https://console.cloud.google.com/apis/library/servicenetworking.googleapis.com) | `servicenetworking.googleapis.com` | Enables your managed services on internal IP addresses to connect to service consumers.  
[Compute Engine](https://console.cloud.google.com/apis/library/compute.googleapis.com) | `compute.googleapis.com` | Used for managing your Apigee runtime.  
[Cloud Key Management Service (KMS)](https://console.cloud.google.com/apis/library/cloudkms.googleapis.com) | `cloudkms.googleapis.com` | Manages keys and performs cryptographic operations for direct use by other Cloud resources.  
  
## Perform the step

#### Permissions required for this task

You can give the Apigee provisioner a predefined role that includes the permissions needed to complete this task, or give more fine-grained permissions to provide the least privilege necessary. See [Predefined roles](https://docs.cloud.google.com/apigee/docs/api-platform/get-started/permissions#predefined-roles) and [API enablement permissions](https://docs.cloud.google.com/apigee/docs/api-platform/get-started/permissions#api-enablement-permissions). 

In Step 1, the console displays a list of the APIs that must be enabled to provision and use Apigee. A green check mark appears next to an APIs already enabled in your project. 

To enable any APIs not previously enabled in your project, click **Enable APIs**. It may take a few moments for the step to complete. Upon success, a blue check mark displays next to the **Enable required APIs** step.

**Tip:** You can see all of the APIs enabled for your project in the [Google Cloud Platform APIs & Services Dashboard](https://console.cloud.google.com/apis/dashboard). The list includes all of the APIs enabled for your project, including the ones you just enabled for Apigee.

Go to the next step, [Step 2: Set up networking](https://docs.cloud.google.com/apigee/docs/api-platform/get-started/console-configure-networking).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
