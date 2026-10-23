---
url: https://docs.cloud.google.com/talent-solution/quotas/
title: Quotas and limits \u00a0|\u00a0 Cloud Talent Solution \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T08:37:50.780615+00:00
---

# Quotas and limits  |  Cloud Talent Solution  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/talent-solution/quotas/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Industry solutions ](https://docs.cloud.google.com/docs/industry)
  * [ Cloud Talent Solution ](https://docs.cloud.google.com/talent-solution/docs)
  * [ Resources ](https://docs.cloud.google.com/talent-solution/docs/resources)



Send feedback 

#  Quotas and limits Stay organized with collections  Save and categorize content based on your preferences. 

**Note:** For all Cloud Talent Solution APIs, the size of each request cannot exceed 10MB.

## Quotas and limits as of January 5, 2021

### Request Limits

The API usage limits for Cloud Talent Solution - Job Search will be as follows (subject to change):

Type of Limit | Usage limit  
---|---  
Requests per 60 seconds for UserfacingGroup QPS (search, histogram and GET API calls) | 3,000*   
Requests per 60 seconds for PeriodicTaskGroup QPS (searchForAlerts API call) | 4,000*   
Requests per 60 seconds for defaultGroup QPS (indexing and List API calls) | 300*   
Maximum number of jobs at any time* | 3,000,000*  
Maximum number of companies at any time* | 1,000,000*  
  
* Quotas are projected up to the specified caps. It doesn't guarantee the availability of the quotas displayed above.

### Increasing Limits

To increase quota limits associated with Job Search job/company create, updates, and deletes, or stored jobs/companies, submit quota increase requests from the [Google Cloud console Quotas](https://console.cloud.google.com/iam-admin/quotas) page. Requests are granted up to the limits defined below, subject to availability and the validation of Cloud Talent Solution integration.

Cloud Talent Solution is committed to responding to quota increase requests within 5 business days.

**Monthly Spend Tiers** |  | **CUD Queries per 60 seconds limit**  
---|---|---  
$ - | $ 1,000 | 300  
$ 1,001 - | $ 10,000 | 1,200  
$ 10,001 - | $ 50,000 | 6,000  
$ 50,001+ |  | 12,000  
  
## Field Limits

The Cloud Talent Solution has many types of fields and thus has variations in the number of characters that can be included in each field. Fields typically support between 160-10,000 characters, depending on the field. See more information in the description of each field in the [reference documentation](https://docs.cloud.google.com/talent-solution/job-search/docs/reference/rest).

## Expired jobs

Cloud Talent Solution stores a number of expired jobs in the system. By default, the retention period of these expired jobs is 90 days.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
