---
url: https://docs.cloud.google.com/apigee/docs/apihub/configure-api-insights/
title: Configure API insights \u00a0|\u00a0 Apigee \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-15T15:19:40.673111+00:00
---

# Configure API insights  |  Apigee  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/apigee/docs/apihub/configure-api-insights/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Apigee ](https://docs.cloud.google.com/apigee/docs)
  * [ Guides ](https://docs.cloud.google.com/apigee/docs/api-platform/get-started/what-apigee)



Send feedback 

#  Configure API insights Stay organized with collections  Save and categorize content based on your preferences. 

_This page applies to**Apigee** and **Apigee hybrid**._

This page describes how to configure API insights in API hub to view and analyze API data from your attached gateways. Depending on the type of gateway you want to monitor, you can configure API insights in API hub by either attaching a runtime project or by creating a plugin instance. 

**Note:** When you provision API hub as part of Apigee provisioning, it automatically identifies and attaches any associated Apigee runtime projects. API traffic for such attached projects is collected and analyzed automatically. 

## Before you begin

  * Grant the required IAM roles and permissions to your principal account. See [IAM roles and permissions](https://docs.cloud.google.com/apigee/docs/apihub/api-insights-overview#iam-roles) for more details.
  * Ensure that your Apigee organization doesn't have Data Residency (DRZ) enabled. API insights doesn't support creating a plugin instance if Data Residency is enabled for your Apigee organization. 



##  Configure API insights for Apigee and Apigee hybrid 

**Note:** API insights is supported only for Apigee hybrid versions **1.14.0** and later. 

To configure API insights to ingest API data from [Apigee](https://docs.cloud.google.com/apigee/docs/api-platform/get-started/what-apigee) and [Apigee hybrid](https://docs.cloud.google.com/apigee/docs/hybrid/v1.15/what-is-hybrid) gateways, attach a runtime project to API hub. For more information, see [attach a runtime project](https://docs.cloud.google.com/apigee/docs/apihub/auto-register-apigee-proxies#attach-a-runtime-project). 

If you have an existing runtime project attached, but are unable to see any API data in API insights, then you may need to edit the project settings to import the necessary API assets into API hub. For more information, see [Edit project association settings](https://docs.cloud.google.com/apigee/docs/apihub/auto-register-apigee-proxies#edit-project-association-settings). 

##  Configure API insights for Apigee Edge Public Cloud 

To configure API insights to ingest API data from [Apigee Edge Public Cloud](https://docs.apigee.com/api-platform/get-started/get-started) gateway, perform the following steps: 

  1. Create a plugin instance for your Apigee Edge Public Cloud gateway. For more information, see [create a plugin instance](https://docs.cloud.google.com/apigee/docs/apihub/create-plugin-instances). 
  2. Set up the Apigee Edge API hub connector for your Apigee Edge organization. For more information, see [Apigee Edge API hub connector setup](https://docs.apigee.com/api-platform/integrations/apigee-edge-uapim-prerequisites#apigee-edge-api-hub-connector-setup-opt-in-for-an-organization). 



##  Configure API insights for Apigee Edge Private Cloud (OPDK) 

**Note:** API insights is supported only for OPDK versions **4.52.02.xx** and **4.53.00.xx**. 

To configure API insights to ingest API data from [Apigee Edge Private Cloud (OPDK)](https://docs.apigee.com/private-cloud/versions) gateway, perform the following steps: 

  1. Create a plugin instance for your Apigee Edge Private Cloud (OPDK) gateway. For more information, see [create a plugin instance](https://docs.cloud.google.com/apigee/docs/apihub/create-plugin-instances). 
  2. Install the Apigee API hub for private cloud connector RPM package on your Apigee OPDK environment. For more information, see [Install Apigee API Hub for Private Cloud connector](https://docs.apigee.com/private-cloud/v4.52.02/privatecloud-install-uapim-connector). 
  3. Configure the network, authentication, and organization-specific settings for the Apigee API hub for private cloud connector. For more information, see [Configure Apigee API Hub for Private Cloud connector](https://docs.apigee.com/private-cloud/v4.52.02/privatecloud-configure-uapim-connector). 
  4. Configure the message processor (MP) configuration for the Apigee API hub for private cloud connector. For more information, see [Configure runtime](https://docs.apigee.com/private-cloud/v4.52.02/privatecloud-uapim-configure-runtime). 



## Considerations

  * Plugin instances recreated using the same plugin instance ID as a previously deleted plugin instance will inherit the insights of the previous plugin instance. 
  * Creating plugin instances with a [custom curation logic](https://cloud.google.com/apigee/docs/apihub/curations#curation-types) might result in runtime data sync issues. It is recommended to use the default curation logic while creating a plugin instance. 
  * It is recommended to use unique display names for your APIs. API insights uses the display name of an API to identify the API in the API inventory. 
  * API insights presents empty API data values as `Not set`. 



## What's next

  * Learn about [API insights dashboards](https://docs.cloud.google.com/apigee/docs/apihub/api-insights-dashboard).
  * Learn about [attaching a runtime project](https://docs.cloud.google.com/apigee/docs/apihub/auto-register-apigee-proxies#attach-a-runtime-project) or [creating a plugin instance](https://docs.cloud.google.com/apigee/docs/apihub/create-plugin-instances) in API hub.



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
