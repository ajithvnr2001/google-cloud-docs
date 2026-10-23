---
url: https://docs.cloud.google.com/chronicle/docs/event-processing/request-log-type/
title: Request prebuilt and create custom log types \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T13:20:35.275386+00:00
---

# Request prebuilt and create custom log types  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/event-processing/request-log-type/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)
  * [ Guides ](https://docs.cloud.google.com/chronicle/docs/secops/secops-overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Request prebuilt and create custom log types

Supported in:

Google SecOps  [ SIEM ](https://docs.cloud.google.com/chronicle/docs/secops/google-secops-siem-toc)

This document describes options to help you process log data that isn't processed by existing Google Security Operations parsers. In such cases, Google SecOps supports the creation of log types to enable parsing and ingestion.

You can choose between the following log types:

## Prebuilt log types

This path is for formats you want to contribute as a platform standard, making them available to all Google SecOps customers.

If the log type is meant for internal use in your tenant, we recommend using a custom log type (even if the product is commercial).

If needed, you can send a request to Google SecOps to have a prebuilt log type added to the platform:

Action item | Process and timeline  
---|---  
Request a new log type | Contact your Google account manager or support representative to submit the request. Once approved, the new prebuilt log type is available to all Google SecOps customers.  
Request a new prebuilt parser | Google manages a new, prebuilt parser request as a new **Feature Request** , which is part of the product backlog.  
**Note:** Because the parser request isn't picked up immediately, we strongly advise you to configure your own custom parser for the new log type to enable immediate ingestion and use.

## Custom log types

This path is recommended for proprietary or tenant-specific logs where speed and privacy are key.

  * **Recommendation** : Use a custom log type if the format is intended only for internal use within your tenant, even if the source product is commercial.

  * **Ownership** : Created and fully managed by your organization.

  * **Parser requirement** : You must configure the corresponding custom parsers in-house.

  * **Availability** : The custom log types and parsers become available only to your organization approximately 10 minutes after creation.




For information about corresponding **prebuilt parsers** and **custom parsers** , see [Manage prebuilt and custom parsers](https://docs.cloud.google.com/chronicle/docs/event-processing/manage-parser-updates).

## Create a custom log type

To create a custom log type, do the following:

  1. Go to **SIEM settings > Available Log Types**. You can view available log types using the **Search** feature.

  2. Click **Create Custom Log Type**.

  3. Under the **Create a custom log type on your own** , enter details for your log type.

For example, to create a custom log type for _Azure Key Vault logging_ , complete the following:

     * In the **Vendor/Product** field, enter `Azure Key Vault logging`.

     * In the **Log Type** field, enter `AZURE_KEYVAULT_LOGGING`.

  4. Click **Create Log Type**. Note that the `_CUSTOM`suffix is added to the log type. 

  5. Wait 10 minutes to ensure that the new log type is available in all components before creating feeds with it. 




The custom log type limitations are:

  * Total: 400

  * Daily: 25

  * Hourly: 8




**Need more help?** [Get answers from Community members and Google SecOps professionals.](https://security.googlecloudcommunity.com/)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
