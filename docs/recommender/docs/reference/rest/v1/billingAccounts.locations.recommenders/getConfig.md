---
url: https://docs.cloud.google.com/recommender/docs/reference/rest/v1/billingAccounts.locations.recommenders/getConfig/
title: Method: billingAccounts.locations.recommenders.getConfig \u00a0|\u00a0 Recommender \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T16:29:27.382675+00:00
---

# Method: billingAccounts.locations.recommenders.getConfig  |  Recommender  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/recommender/docs/reference/rest/v1/billingAccounts.locations.recommenders/getConfig/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Access and resource management ](https://docs.cloud.google.com/docs/access-resources)
  * [ Recommender ](https://docs.cloud.google.com/recommender/docs)
  * [ Reference ](https://docs.cloud.google.com/recommender/docs/apis)



Send feedback 

#  Method: billingAccounts.locations.recommenders.getConfig Stay organized with collections  Save and categorize content based on your preferences. 

  * HTTP request
  * Path parameters
  * Request body
  * Response body
  * Authorization scopes



Gets the requested Recommender Config. There is only one instance of the config for each Recommender.

### HTTP request

`GET https://recommender.googleapis.com/v1/{name=billingAccounts/*/locations/*/recommenders/*/config}`

The URL uses [gRPC Transcoding](https://google.aip.dev/127) syntax.

### Path parameters

Parameters  
---  
`name` |  `string` Required. Name of the Recommendation Config to get.Acceptable formats:

  * `projects/[PROJECT_NUMBER]/locations/[LOCATION]/recommenders/[RECOMMENDER_ID]/config`
  * `projects/[PROJECT_ID]/locations/[LOCATION]/recommenders/[RECOMMENDER_ID]/config`
  * `organizations/[ORGANIZATION_ID]/locations/[LOCATION]/recommenders/[RECOMMENDER_ID]/config`
  * `billingAccounts/[BILLING_ACCOUNT_ID]/locations/[LOCATION]/recommenders/[RECOMMENDER_ID]/config`

  
  
### Request body

The request body must be empty.

### Response body

If successful, the response body contains an instance of `[RecommenderConfig](https://docs.cloud.google.com/recommender/docs/reference/rest/v1/RecommenderConfig)`.

### Authorization scopes

Requires the following OAuth scope:

  * `https://www.googleapis.com/auth/cloud-platform`



For more information, see the [Authentication Overview](https://cloud.google.com/docs/authentication/).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2025-05-14 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2025-05-14 UTC."],[],[]] 
