---
url: https://docs.cloud.google.com/apigee/docs/api-monitoring/
title: Overview of API Monitoring \u00a0|\u00a0 Apigee \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T09:44:16.937675+00:00
---

# Overview of API Monitoring  |  Apigee  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/apigee/docs/api-monitoring/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Apigee ](https://docs.cloud.google.com/apigee/docs)
  * [ Guides ](https://docs.cloud.google.com/apigee/docs/api-platform/get-started/what-apigee)



Send feedback 

#  Overview of API Monitoring Stay organized with collections  Save and categorize content based on your preferences. 

_This page applies to**Apigee** and **Apigee hybrid**._

_View[ Apigee Edge](https://docs.apigee.com/api-platform/get-started/what-apigee-edge) documentation._ ![](https://fonts.gstatic.com/s/i/googlematerialicons/help/v13/gm_grey-24dp/1x/gm_help_gm_grey_24dp.png)

After you build and launch your APIs on Apigee, you need to ensure that they are available and performing as expected in order to maintain uninterrupted service. Apigee's API Monitoring enables you to track your APIs to make sure they are up and running correctly. API Monitoring provides near real-time insights into API traffic and performance, to help you quickly diagnose and solve issues as they arise.

API Monitoring enables you to:

  * Create alerts to notify you of changes in API traffic so you can take appropriate action before customers are affected.
  * Increase API availability and reduce the mean-time-to-diagnosis (MTTD) by quickly investigating issues with your APIs.
  * Leverage fault codes to speed diagnosis. 
  * Isolate problem areas quickly to diagnose errors, performance, and latency issues and their source.



As an Apigee customer, you can also use [Cloud Monitoring](https://cloud.google.com/monitoring/docs) tools to support API Monitoring.

**About data retention** : API Monitoring logs capture query parameter and user agent data. Since this data may contain personally identifiable information (PII), it is retained for **6 weeks** , then deleted per the [ Google Privacy Policy](https://www.google.com/policies/privacy). For more details, see [ Data retention](https://cloud.google.com/monitoring/quotas#data_retention_policy). **Apigee hybrid users** : Do not disable metrics in your hybrid configuration if you intend to view API Monitoring data. [Metrics](https://docs.cloud.google.com/apigee/docs/hybrid/latest/metrics-enable) must be enabled in your hybrid configuration for API Monitoring data to show up. Metrics is enabled for hybrid by default.

## API Monitoring roles

To access API Monitoring, you need to be assigned the following roles:

  * `roles/apigee.readOnlyAdmin`
  * `roles/monitoring.viewer`



See [Apigee roles](https://cloud.google.com/iam/docs/roles-permissions/apigee) for more information about what roles are appropriate for using API Monitoring.

## Accessing API Monitoring

You can access API Monitoring through the Apigee UI by doing the following steps:

In the Google Cloud console, go to the **Apigee > Proxy Development > API monitoring** page.

[Go to API monitoring](https://console.cloud.google.com/apigee/apimonitoring)

This displays the main API Monitoring view. In the **View** menu, you can select one of the following views:

  * **Timeline** : Displays timelines of recent API traffic data. 
  * **Investigate** : Displays tables of API traffic data, such as fault code by region.
  * **Recent** : Displays treemaps of data in which each proxy is represented by a rectangle, whose size is proportional to the amount of API traffic for the proxy, and whose color denotes the relative size of related metrics.

The following sections describe these views in detail: 
  * [Timeline](https://docs.cloud.google.com/apigee/docs/api-monitoring/timeline)
  * [Investigate](https://docs.cloud.google.com/apigee/docs/api-monitoring/investigate)
  * [Recent](https://docs.cloud.google.com/apigee/docs/api-monitoring/recent)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
