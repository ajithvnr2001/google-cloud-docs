---
url: https://docs.cloud.google.com/python/docs/reference/iam/latest/google.cloud.iam_admin_v1.types.ServiceAccount
title: Class ServiceAccount (2.26.0) \u00a0|\u00a0 Python client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T17:45:36.017240+00:00
---

# Class ServiceAccount (2.26.0)  |  Python client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/python/docs/reference/iam/latest/google.cloud.iam_admin_v1.types.ServiceAccount

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Python ](https://docs.cloud.google.com/python/docs)
  * [ Client libraries ](https://docs.cloud.google.com/python/docs/reference)



Send feedback 

#  Class ServiceAccount (2.26.0) Stay organized with collections  Save and categorize content based on your preferences. 

2.26.0 (latest)  2.25.0  2.24.1  2.23.0  2.22.0  2.21.0  2.20.0  2.19.1  2.18.3  2.17.0  2.16.1  2.15.2  2.14.3  2.13.0  2.12.1  2.11.2  2.10.0  2.9.0  2.8.2  2.7.0  2.6.2  2.5.1  2.4.0  2.3.2  2.2.0  2.1.0  2.0.0  1.0.3  0.3.2  0.2.0 
    
    
    ServiceAccount(mapping=None, *, ignore_unknown_fields=False, **kwargs)

An IAM service account.

A service account is an account for an application or a virtual machine (VM) instance, not a person. You can use a service account to call Google APIs. To learn more, read the `overview of service accounts <https://cloud.google.com/iam/help/service-accounts/overview>`__.

When you create a service account, you specify the project ID that owns the service account, as well as a name that must be unique within the project. IAM uses these values to create an email address that identifies the service account.

## Attributes  
  
---  
**Name** | **Description**  
`name` |  `str`   
The resource name of the service account. Use one of the following formats: \- `projects/{PROJECT_ID}/serviceAccounts/{EMAIL_ADDRESS}` \- `projects/{PROJECT_ID}/serviceAccounts/{UNIQUE_ID}` As an alternative, you can use the `-` wildcard character instead of the project ID: \- `projects/-/serviceAccounts/{EMAIL_ADDRESS}` \- `projects/-/serviceAccounts/{UNIQUE_ID}` When possible, avoid using the `-` wildcard character, because it can cause response messages to contain misleading error codes. For example, if you try to get the service account `projects/-/serviceAccounts/fake@example.com`, which does not exist, the response contains an HTTP `403 Forbidden` error instead of a `404 Not Found` error.   
`project_id` |  `str`   
Output only. The ID of the project that owns the service account.   
`unique_id` |  `str`   
Output only. The unique, stable numeric ID for the service account. Each service account retains its unique ID even if you delete the service account. For example, if you delete a service account, then create a new service account with the same name, the new service account has a different unique ID than the deleted service account.   
`email` |  `str`   
Output only. The email address of the service account.   
`display_name` |  `str`   
Optional. A user-specified, human-readable name for the service account. The maximum length is 100 UTF-8 bytes.   
`etag` |  `bytes`   
Deprecated. Do not use.   
`description` |  `str`   
Optional. A user-specified, human-readable description of the service account. The maximum length is 256 UTF-8 bytes.   
`oauth2_client_id` |  `str`   
Output only. The OAuth 2.0 client ID for the service account.   
`disabled` |  `bool`   
Output only. Whether the service account is disabled.   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-03 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-03 UTC."],[],[]] 
