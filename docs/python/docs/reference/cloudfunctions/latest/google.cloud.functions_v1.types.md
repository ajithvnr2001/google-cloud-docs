---
url: https://docs.cloud.google.com/python/docs/reference/cloudfunctions/latest/google.cloud.functions_v1.types
title: Package types (1.25.0) \u00a0|\u00a0 Python client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T19:39:59.850592+00:00
---

# Package types (1.25.0)  |  Python client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/python/docs/reference/cloudfunctions/latest/google.cloud.functions_v1.types

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Python ](https://docs.cloud.google.com/python/docs)
  * [ Client libraries ](https://docs.cloud.google.com/python/docs/reference)



Send feedback 

#  Package types (1.25.0) Stay organized with collections  Save and categorize content based on your preferences. 

1.25.0 (latest)  1.24.0  1.23.0  1.22.0  1.21.0  1.20.4  1.19.0  1.18.1  1.16.5  1.15.0  1.14.0  1.13.2  1.12.0  1.11.0  1.10.1  1.9.0  1.8.3  1.7.0  1.6.0  1.5.2  1.4.0  1.3.1  1.2.0  1.1.1  1.0.4  0.7.2  0.6.1  0.5.1  0.4.0  0.1.0 

API documentation for `functions_v1.types` package.

## Classes 

### [CallFunctionRequest](https://docs.cloud.google.com/python/docs/reference/cloudfunctions/latest/google.cloud.functions_v1.types.CallFunctionRequest)

Request for the `CallFunction` method.

### [CallFunctionResponse](https://docs.cloud.google.com/python/docs/reference/cloudfunctions/latest/google.cloud.functions_v1.types.CallFunctionResponse)

Response of `CallFunction` method.

### [CloudFunction](https://docs.cloud.google.com/python/docs/reference/cloudfunctions/latest/google.cloud.functions_v1.types.CloudFunction)

Describes a Cloud Function that contains user computation executed in response to an event. It encapsulate function and triggers configurations.

This message has `oneof`_ fields (mutually exclusive fields). For each oneof, at most one member field can be set at the same time. Setting any member of the oneof automatically clears all other members.

.. _oneof: <https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields>

### [CloudFunctionStatus](https://docs.cloud.google.com/python/docs/reference/cloudfunctions/latest/google.cloud.functions_v1.types.CloudFunctionStatus)

Describes the current stage of a deployment.

### [CreateFunctionRequest](https://docs.cloud.google.com/python/docs/reference/cloudfunctions/latest/google.cloud.functions_v1.types.CreateFunctionRequest)

Request for the `CreateFunction` method.

### [DeleteFunctionRequest](https://docs.cloud.google.com/python/docs/reference/cloudfunctions/latest/google.cloud.functions_v1.types.DeleteFunctionRequest)

Request for the `DeleteFunction` method.

### [EventTrigger](https://docs.cloud.google.com/python/docs/reference/cloudfunctions/latest/google.cloud.functions_v1.types.EventTrigger)

Describes EventTrigger, used to request events be sent from another service.

### [FailurePolicy](https://docs.cloud.google.com/python/docs/reference/cloudfunctions/latest/google.cloud.functions_v1.types.FailurePolicy)

Describes the policy in case of function's execution failure. If empty, then defaults to ignoring failures (i.e. not retrying them).

.. _oneof: <https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields>

### [GenerateDownloadUrlRequest](https://docs.cloud.google.com/python/docs/reference/cloudfunctions/latest/google.cloud.functions_v1.types.GenerateDownloadUrlRequest)

Request of `GenerateDownloadUrl` method.

### [GenerateDownloadUrlResponse](https://docs.cloud.google.com/python/docs/reference/cloudfunctions/latest/google.cloud.functions_v1.types.GenerateDownloadUrlResponse)

Response of `GenerateDownloadUrl` method.

### [GenerateUploadUrlRequest](https://docs.cloud.google.com/python/docs/reference/cloudfunctions/latest/google.cloud.functions_v1.types.GenerateUploadUrlRequest)

Request of `GenerateSourceUploadUrl` method.

### [GenerateUploadUrlResponse](https://docs.cloud.google.com/python/docs/reference/cloudfunctions/latest/google.cloud.functions_v1.types.GenerateUploadUrlResponse)

Response of `GenerateSourceUploadUrl` method.

### [GetFunctionRequest](https://docs.cloud.google.com/python/docs/reference/cloudfunctions/latest/google.cloud.functions_v1.types.GetFunctionRequest)

Request for the `GetFunction` method.

### [HttpsTrigger](https://docs.cloud.google.com/python/docs/reference/cloudfunctions/latest/google.cloud.functions_v1.types.HttpsTrigger)

Describes HttpsTrigger, could be used to connect web hooks to function.

### [ListFunctionsRequest](https://docs.cloud.google.com/python/docs/reference/cloudfunctions/latest/google.cloud.functions_v1.types.ListFunctionsRequest)

Request for the `ListFunctions` method.

### [ListFunctionsResponse](https://docs.cloud.google.com/python/docs/reference/cloudfunctions/latest/google.cloud.functions_v1.types.ListFunctionsResponse)

Response for the `ListFunctions` method.

### [OperationMetadataV1](https://docs.cloud.google.com/python/docs/reference/cloudfunctions/latest/google.cloud.functions_v1.types.OperationMetadataV1)

Metadata describing an `Operation][google.longrunning.Operation]`

### [OperationType](https://docs.cloud.google.com/python/docs/reference/cloudfunctions/latest/google.cloud.functions_v1.types.OperationType)

A type of an operation.

### [SecretEnvVar](https://docs.cloud.google.com/python/docs/reference/cloudfunctions/latest/google.cloud.functions_v1.types.SecretEnvVar)

Configuration for a secret environment variable. It has the information necessary to fetch the secret value from secret manager and expose it as an environment variable.

### [SecretVolume](https://docs.cloud.google.com/python/docs/reference/cloudfunctions/latest/google.cloud.functions_v1.types.SecretVolume)

Configuration for a secret volume. It has the information necessary to fetch the secret value from secret manager and make it available as files mounted at the requested paths within the application container. Secret value is not a part of the configuration. Every filesystem read operation performs a lookup in secret manager to retrieve the secret value.

### [SourceRepository](https://docs.cloud.google.com/python/docs/reference/cloudfunctions/latest/google.cloud.functions_v1.types.SourceRepository)

Describes SourceRepository, used to represent parameters related to source repository where a function is hosted.

### [UpdateFunctionRequest](https://docs.cloud.google.com/python/docs/reference/cloudfunctions/latest/google.cloud.functions_v1.types.UpdateFunctionRequest)

Request for the `UpdateFunction` method.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-04 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-04 UTC."],[],[]] 
