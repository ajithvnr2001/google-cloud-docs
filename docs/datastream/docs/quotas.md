---
url: https://docs.cloud.google.com/datastream/docs/quotas/
title: Quotas and limits \u00a0|\u00a0 Datastream \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T05:41:30.288438+00:00
---

# Quotas and limits  |  Datastream  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/datastream/docs/quotas/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Datastream ](https://docs.cloud.google.com/datastream/docs)
  * [ Resources ](https://docs.cloud.google.com/datastream/docs/quotas)



Send feedback 

#  Quotas and limits Stay organized with collections  Save and categorize content based on your preferences. 

Datastream limits the maximum rates of incoming requests and enforces appropriate quotas on a per-project basis. Specific policies vary depending on resource availability, user profile, service usage history, and other factors, and are subject to change without notice.

Datastream has the following quota limits:

  * Each Google Cloud project can have a maximum of 200 stream resources per region.
  * Each Google Cloud project can have a maximum of 5 private connectivity configurations.
  * Each user can make up to 1,200 API calls per minute.



## Salesforce API quotas

Salesforce defines a limit for the total number of inbound API requests during a 24-hour period for an org. We recommend carefully considering your polling interval values and the number of objects that you want to replicate.

To find out what limits there are in place for your org, use the Salesforce [Limits API](https://developer.salesforce.com/docs/atlas.en-us.api_rest.meta/api_rest/resources_limits.htm).

**Note:** Limits are imposed on an org-basis, meaning that they affect the entire Salesforce org. If the API usage reaches 90% of the quota, Datastream throttles your stream, and the stream temporarily enters a `FAILED` state. After a short while, Datastream checks if the usage is under 90% and if so, the stream resumes.

## Salesforce Marketing Cloud API quotas

**Preview**

This feature is subject to the "Pre-GA Offerings Terms" in the General Service Terms section of the [Service Specific Terms](https://docs.cloud.google.com/terms/service-terms#1). Pre-GA features are available "as is" and might have limited support. For more information, see the [launch stage descriptions](https://cloud.google.com/products/#product-launch-stages). 

Salesforce Marketing Cloud has specific API rate limits. For most APIs, the limit is 250 requests per minute per account. For more information, refer to the [Salesforce Marketing Cloud API Rate Limiting documentation](https://developer.salesforce.com/docs/marketing/marketing-cloud/guide/rate-limiting.html).

## Write to BigQuery and Cloud Storage

When writing data into BigQuery and Cloud Storage, the quotas and limits for [BigQuery](https://docs.cloud.google.com/bigquery/quotas) and [Cloud Storage](https://docs.cloud.google.com/storage/quotas) apply.

## Cloud Logging

Datastream saves logs in [Cloud Logging](https://docs.cloud.google.com/logging). The Logging quota applies to your Datastream resources.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
