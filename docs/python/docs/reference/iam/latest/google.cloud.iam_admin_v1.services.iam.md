---
url: https://docs.cloud.google.com/python/docs/reference/iam/latest/google.cloud.iam_admin_v1.services.iam
title: Package iam (2.26.0) \u00a0|\u00a0 Python client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T17:45:25.272651+00:00
---

# Package iam (2.26.0)  |  Python client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/python/docs/reference/iam/latest/google.cloud.iam_admin_v1.services.iam

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Python ](https://docs.cloud.google.com/python/docs)
  * [ Client libraries ](https://docs.cloud.google.com/python/docs/reference)



Send feedback 

#  Package iam (2.26.0) Stay organized with collections  Save and categorize content based on your preferences. 

2.26.0 (latest)  2.25.0  2.24.1  2.23.0  2.22.0  2.21.0  2.20.0  2.19.1  2.18.3  2.17.0  2.16.1  2.15.2  2.14.3  2.13.0  2.12.1  2.11.2  2.10.0  2.9.0  2.8.2  2.7.0  2.6.2  2.5.1  2.4.0  2.3.2  2.2.0  2.1.0  2.0.0  1.0.3  0.3.2  0.2.0 

API documentation for `iam_admin_v1.services.iam` package.

## Classes 

### [IAMAsyncClient](https://docs.cloud.google.com/python/docs/reference/iam/latest/google.cloud.iam_admin_v1.services.iam.IAMAsyncClient)

Creates and manages Identity and Access Management (IAM) resources.

You can use this service to work with all of the following resources:

  * **Service accounts** , which identify an application or a virtual machine (VM) instance rather than a person
  * **Service account keys** , which service accounts use to authenticate with Google APIs
  * **IAM policies for service accounts** , which specify the roles that a principal has for the service account
  * **IAM custom roles** , which help you limit the number of permissions that you grant to principals



In addition, you can use this service to complete the following tasks, among others:

  * Test whether a service account can use specific permissions
  * Check which roles you can grant for a specific resource
  * Lint, or validate, condition expressions in an IAM policy



When you read data from the IAM API, each read is eventually consistent. In other words, if you write data with the IAM API, then immediately read that data, the read operation might return an older version of the data. To deal with this behavior, your application can retry the request with truncated exponential backoff.

In contrast, writing data to the IAM API is sequentially consistent. In other words, write operations are always processed in the order in which they were received.

### [IAMClient](https://docs.cloud.google.com/python/docs/reference/iam/latest/google.cloud.iam_admin_v1.services.iam.IAMClient)

Creates and manages Identity and Access Management (IAM) resources.

You can use this service to work with all of the following resources:

  * **Service accounts** , which identify an application or a virtual machine (VM) instance rather than a person
  * **Service account keys** , which service accounts use to authenticate with Google APIs
  * **IAM policies for service accounts** , which specify the roles that a principal has for the service account
  * **IAM custom roles** , which help you limit the number of permissions that you grant to principals



In addition, you can use this service to complete the following tasks, among others:

  * Test whether a service account can use specific permissions
  * Check which roles you can grant for a specific resource
  * Lint, or validate, condition expressions in an IAM policy



When you read data from the IAM API, each read is eventually consistent. In other words, if you write data with the IAM API, then immediately read that data, the read operation might return an older version of the data. To deal with this behavior, your application can retry the request with truncated exponential backoff.

In contrast, writing data to the IAM API is sequentially consistent. In other words, write operations are always processed in the order in which they were received.

## Modules 

### [pagers](https://docs.cloud.google.com/python/docs/reference/iam/latest/google.cloud.iam_admin_v1.services.iam.pagers)

API documentation for `iam_admin_v1.services.iam.pagers` module.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-03 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-03 UTC."],[],[]] 
