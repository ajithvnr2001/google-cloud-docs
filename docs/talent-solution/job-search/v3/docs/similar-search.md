---
url: https://docs.cloud.google.com/talent-solution/job-search/v3/docs/similar-search/
title: Retrieve Similar Job Recommendations (v3) \u00a0|\u00a0 Cloud Talent Solution - Job Search v3 \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T03:53:40.953396+00:00
---

# Retrieve Similar Job Recommendations (v3)  |  Cloud Talent Solution - Job Search v3  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/talent-solution/job-search/v3/docs/similar-search/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Industry solutions ](https://docs.cloud.google.com/docs/industry)
  * [ Cloud Talent Solution ](https://docs.cloud.google.com/talent-solution/docs)
  * [ Job Search ](https://docs.cloud.google.com/talent-solution/job-search/docs)
  * [ Job Search v3 (deprecated) ](https://docs.cloud.google.com/talent-solution/job-search/v3/docs)



Send feedback 

#  Retrieve Similar Job Recommendations (v3) Stay organized with collections  Save and categorize content based on your preferences. 

**Beta**  
This is a Beta release of Cloud Talent Solution. This release is not covered by any SLA or deprecation policy and is not intended for real-time use in critical applications. This is an alpha release of Cloud Job Discovery Similar Job Recommendations. This an experimental feature that is not covered by SLAs, and the API and its behavior may change without notice.

Similar Job Recommendations allows the customer to return a set of jobs that are similar to a job of interest to a job seeker.

## API Overview

A caller passes a `Job` entity X, and an optional `resultSize` number N, to the [jobs.recommend](https://docs.cloud.google.com/job-discovery/docs/reference/rest/v2beta1/jobs/recommend) API. The Cloud Job Discovery service returns up to N similar recommended jobs.

The results are based on:

  * User behavior: API returns jobs viewed or applied for by other users who also viewed or applied for the passed-in job X
  * Job metadata: API returns jobs with a similar classification to the passed-in job X as determined by the service's job classification machine learning model



The list of returned jobs is sorted by relevance (job N has higher relevance than job N+1).

**De-Duplication** : The service removes jobs from the results that are possible duplicates of the passed-in job X. De-duplication logic is based on the passed-in job's associated `companyName` and `jobTitle`.

## Usage Requirements

The following steps are necessary or recommended when using this feature:

  * For each Search and Histogram request, the `sessionId` and `userId` in the [requestHeader](https://docs.cloud.google.com/job-search/v3/docs/reference/rest/v2beta1/RequestHeader)/[requestMetadata](https://docs.cloud.google.com/talent-solution/job-search/v3/docs/reference/rpc/google.cloud.talent.v3#requestmetadata) must be populated
  * For each Search request, User Behavior Event reporting (via [Pub/Sub](https://docs.cloud.google.com/pubsub/docs)) must be implemented, and, if applicable, the implementation must send at least the following [events](https://docs.cloud.google.com/talent-solution/job-search/v3/docs/client-event#client-event.EventType) for each search request: 
    * `VIEW`
    * and one of 
      * `APPLY_START`
      * `APPLY_REDIRECT`
      * `APPLY_COMPANY_SUBMIT`
  * For best results, greater than 20,000 unique user queries per month and a large number of jobs per company are recommended



## Limitations

Recommended jobs are only returned for the company associated with the passed-in job (jobs associated with the passed-in Job's `companyName`).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
