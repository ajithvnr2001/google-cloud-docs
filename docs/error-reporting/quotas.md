---
url: https://docs.cloud.google.com/error-reporting/quotas/
title: Quotas and limits \u00a0|\u00a0 Error Reporting \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T13:11:57.098954+00:00
---

# Quotas and limits  |  Error Reporting  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/error-reporting/quotas/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Observability ](https://docs.cloud.google.com/docs/observability)
  * [ Error Reporting ](https://docs.cloud.google.com/error-reporting/docs)
  * [ Resources ](https://docs.cloud.google.com/error-reporting/quotas)



Send feedback 

#  Quotas and limits Stay organized with collections  Save and categorize content based on your preferences. 

Error Reporting enforces API activity rate quotas, deployment tracking limits, and a 30-day data retention period to help manage resource usage in your Google Cloud project. _Quotas_ have default values that you can request to adjust, whereas _system limits_ are fixed values that can't be changed. For general information about how quotas work in Google Cloud, see the [Cloud Quotas overview](https://docs.cloud.google.com/docs/quotas/overview).

## API activity limits

Quota name | Limit  
---|---  
Error event data requests per minute per user | 60  
Error group metadata requests per minute per user | 60  
Error reports per minute | 6,000  
  
You can also use the [API dashboard](https://console.cloud.google.com/apis/dashboard) to view your API activity and quotas. To view limits, select an API and then select **Quotas**.

### Request changes to Error Reporting API quotas

To determine whether you can request a higher or lower Error Reporting API limit for quota by using the Google Cloud console, go to the **Quotas & System Limits** page and search for the quota of interest.

  * If the quota is listed, then you can use that page to request a change to the limit. For information about those steps, see [View and manage quotas](https://docs.cloud.google.com/docs/quotas/view-manage).


  * If the quota isn't listed or if you request a quota update and get the error `Edit is not allowed for this quota`, then [contact Cloud Customer Care](https://cloud.google.com/support) and request a change to the quota. Billing must be enabled on the Google Cloud project to edit quotas in the Google Cloud console.



## Deployment limits

There is a limit of 10,000 deployment-error group pairs, where a deployment is a combination of [`service`](https://docs.cloud.google.com/error-reporting/reference/rest/v1beta1/ServiceContext) and [`version`](https://docs.cloud.google.com/error-reporting/reference/rest/v1beta1/ServiceContext). After you reach this limit, Error Reporting discards the oldest (or less-recently modified) deployments and their associated error data.

## Data retention periods

Information in Error Reporting is retained for 30 days.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-21 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-21 UTC."],[],[]] 
