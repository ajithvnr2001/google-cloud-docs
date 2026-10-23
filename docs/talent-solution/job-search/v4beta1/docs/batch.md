---
url: https://docs.cloud.google.com/talent-solution/job-search/v4beta1/docs/batch/
title: Batch operations (v4beta1) \u00a0|\u00a0 Cloud Talent Solution - Job Search v4beta1 \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T09:34:22.672300+00:00
---

# Batch operations (v4beta1)  |  Cloud Talent Solution - Job Search v4beta1  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/talent-solution/job-search/v4beta1/docs/batch/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Industry solutions ](https://docs.cloud.google.com/docs/industry)
  * [ Cloud Talent Solution ](https://docs.cloud.google.com/talent-solution/docs)
  * [ Job Search ](https://docs.cloud.google.com/talent-solution/job-search/docs)
  * [ Job Search v4beta1 (deprecated) ](https://docs.cloud.google.com/talent-solution/job-search/v4beta1/docs)



Send feedback 

#  Batch operations (v4beta1) Stay organized with collections  Save and categorize content based on your preferences. 

Cloud Talent Solution supports asynchronous batch operations, which allows you to put multiple API calls into a single HTTP request. The returned response type is `google.longrunning.operation`. The detailed status of the batch operation can be retrieved by calling the `GetOperation` method using the [`name`](https://docs.cloud.google.com/talent-solution/matching-engine/docs/reference/rpc/google.longrunning#getoperationrequest) field in `google.longrunning.operation`.

Using batching yields decreased latency in the API response time and higher throughput. Note that successfully receiving a batch API response indicates only that the batch request has been created. Actual data processing is done asynchronously. Batch operations created more than 30 days ago will be no longer accessible by the `GetOperation` method.

**Each batch is limited to 200 requests**.

## Batch operation progress indicator

The `google.longrunning.operation` created by calling the batch create or update method falls under one of the following states:

  * STATE_UNSPECIFIED (the default value)
  * INITIALIZING
  * PROCESSING
  * SUCCEEDED
  * FAILED



In state INITIALIZING, `success_count`, `failure_count`, and `total_count` fields are set to 0. If the operation is in state PROCESSING the `success_count` and `failure_count` may increase. In state SUCCEEDED, `success_count` \+ `failure_count` is always equal to `total_count`, and `success_count` > 0\. In state FAILED, `success_count` is always 0.

**Note:** Only the `GetOperation` method is currently only supported on the `google.longrunning.operation` resource.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
