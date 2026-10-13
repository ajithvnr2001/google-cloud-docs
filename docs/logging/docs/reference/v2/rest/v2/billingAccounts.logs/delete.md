---
url: https://docs.cloud.google.com/logging/docs/reference/v2/rest/v2/billingAccounts.logs/delete/
title: Method: billingAccounts.logs.delete \u00a0|\u00a0 Cloud Logging \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T12:42:46.661927+00:00
---

# Method: billingAccounts.logs.delete  |  Cloud Logging  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/logging/docs/reference/v2/rest/v2/billingAccounts.logs/delete/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Observability ](https://docs.cloud.google.com/docs/observability)
  * [ Cloud Logging ](https://docs.cloud.google.com/logging/docs)
  * [ Reference ](https://docs.cloud.google.com/logging/docs/apis)



Send feedback 

#  Method: billingAccounts.logs.delete Stay organized with collections  Save and categorize content based on your preferences. 

  * HTTP request
  * Path parameters
  * Request body
  * Response body
  * Authorization scopes
  * Try it!



Deletes all the log entries in a log for the global _Default Log Bucket. The log reappears if it receives new entries. Log entries written shortly before the delete operation might not be deleted. Entries received after the delete operation with a timestamp before the operation will be deleted.

### HTTP request

Choose an endpoint:

globalafrica-south1asia-east1asia-east2asia-northeast1asia-northeast2asia-northeast3asia-south1asia-south2asia-southeast1asia-southeast2asia-southeast3australia-southeast1australia-southeast2europe-central2europe-north1europe-north2europe-north3europe-southwest1europe-west1europe-west10europe-west12europe-west2europe-west3europe-west4europe-west6europe-west8europe-west9me-central1me-central2me-west1northamerica-northeast1northamerica-northeast2northamerica-south1southamerica-east1southamerica-west1us-central1us-east1us-east4us-east5us-south1us-west1us-west2us-west3us-west4cacheuinsaus

  
`DELETE https://logging.googleapis.com/v2/{logName=billingAccounts/*/logs/*}`

The URLs use [gRPC Transcoding](https://google.aip.dev/127) syntax.

### Path parameters

Parameters  
---  
`logName` |  `string` Required. The resource name of the log to delete:

  * `projects/[PROJECT_ID]/logs/[LOG_ID]`
  * `organizations/[ORGANIZATION_ID]/logs/[LOG_ID]`
  * `billingAccounts/[BILLING_ACCOUNT_ID]/logs/[LOG_ID]`
  * `folders/[FOLDER_ID]/logs/[LOG_ID]`

`[LOG_ID]` must be URL-encoded. For example, `"projects/my-project-id/logs/syslog"`, `"organizations/123/logs/cloudaudit.googleapis.com%2Factivity"`.For more information about log names, see `[LogEntry](https://docs.cloud.google.com/logging/docs/reference/v2/rest/v2/LogEntry)`. Authorization requires the following [IAM](https://cloud.google.com/iam/docs/) permission on the specified resource `logName`:

  * `logging.logs.delete`

  
  
### Request body

The request body must be empty.

### Response body

If successful, the response body is an empty JSON object.

### Authorization scopes

Requires one of the following OAuth scopes:

  * `https://www.googleapis.com/auth/logging.admin`
  * ` https://www.googleapis.com/auth/cloud-platform`



For more information, see the [Authentication Overview](https://docs.cloud.google.com/docs/authentication#authorization-gcp).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-09-17 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-09-17 UTC."],[],[]] 
