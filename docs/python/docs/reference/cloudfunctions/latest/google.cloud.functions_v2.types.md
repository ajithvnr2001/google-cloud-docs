---
url: https://docs.cloud.google.com/python/docs/reference/cloudfunctions/latest/google.cloud.functions_v2.types
title: Package types (1.25.0) \u00a0|\u00a0 Python client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T19:40:04.534707+00:00
---

# Package types (1.25.0)  |  Python client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/python/docs/reference/cloudfunctions/latest/google.cloud.functions_v2.types

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Python ](https://docs.cloud.google.com/python/docs)
  * [ Client libraries ](https://docs.cloud.google.com/python/docs/reference)



Send feedback 

#  Package types (1.25.0) Stay organized with collections  Save and categorize content based on your preferences. 

1.25.0 (latest)  1.24.0  1.23.0  1.22.0  1.21.0  1.20.4  1.19.0  1.18.1  1.16.5  1.15.0  1.14.0  1.13.2  1.12.0  1.11.0  1.10.1  1.9.0  1.8.3  1.7.0  1.6.0  1.5.2  1.4.0  1.3.1  1.2.0  1.1.1  1.0.4  0.7.2  0.6.1  0.5.1  0.4.0  0.1.0 

API documentation for `functions_v2.types` package.

## Classes 

### [AutomaticUpdatePolicy](https://docs.cloud.google.com/python/docs/reference/cloudfunctions/latest/google.cloud.functions_v2.types.AutomaticUpdatePolicy)

Security patches are applied automatically to the runtime without requiring the function to be redeployed.

### [BuildConfig](https://docs.cloud.google.com/python/docs/reference/cloudfunctions/latest/google.cloud.functions_v2.types.BuildConfig)

Describes the Build step of the function that builds a container from the given source.

This message has `oneof`_ fields (mutually exclusive fields). For each oneof, at most one member field can be set at the same time. Setting any member of the oneof automatically clears all other members.

.. _oneof: <https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields>

### [CreateFunctionRequest](https://docs.cloud.google.com/python/docs/reference/cloudfunctions/latest/google.cloud.functions_v2.types.CreateFunctionRequest)

Request for the `CreateFunction` method.

### [DeleteFunctionRequest](https://docs.cloud.google.com/python/docs/reference/cloudfunctions/latest/google.cloud.functions_v2.types.DeleteFunctionRequest)

Request for the `DeleteFunction` method.

### [Environment](https://docs.cloud.google.com/python/docs/reference/cloudfunctions/latest/google.cloud.functions_v2.types.Environment)

The environment the function is hosted on.

### [EventFilter](https://docs.cloud.google.com/python/docs/reference/cloudfunctions/latest/google.cloud.functions_v2.types.EventFilter)

Filters events based on exact matches on the CloudEvents attributes.

### [EventTrigger](https://docs.cloud.google.com/python/docs/reference/cloudfunctions/latest/google.cloud.functions_v2.types.EventTrigger)

Describes EventTrigger, used to request events to be sent from another service.

### [Function](https://docs.cloud.google.com/python/docs/reference/cloudfunctions/latest/google.cloud.functions_v2.types.Function)

Describes a Cloud Function that contains user computation executed in response to an event. It encapsulates function and trigger configurations.

### [GenerateDownloadUrlRequest](https://docs.cloud.google.com/python/docs/reference/cloudfunctions/latest/google.cloud.functions_v2.types.GenerateDownloadUrlRequest)

Request of `GenerateDownloadUrl` method.

### [GenerateDownloadUrlResponse](https://docs.cloud.google.com/python/docs/reference/cloudfunctions/latest/google.cloud.functions_v2.types.GenerateDownloadUrlResponse)

Response of `GenerateDownloadUrl` method.

### [GenerateUploadUrlRequest](https://docs.cloud.google.com/python/docs/reference/cloudfunctions/latest/google.cloud.functions_v2.types.GenerateUploadUrlRequest)

Request of `GenerateSourceUploadUrl` method.

### [GenerateUploadUrlResponse](https://docs.cloud.google.com/python/docs/reference/cloudfunctions/latest/google.cloud.functions_v2.types.GenerateUploadUrlResponse)

Response of `GenerateSourceUploadUrl` method.

### [GetFunctionRequest](https://docs.cloud.google.com/python/docs/reference/cloudfunctions/latest/google.cloud.functions_v2.types.GetFunctionRequest)

Request for the `GetFunction` method.

### [ListFunctionsRequest](https://docs.cloud.google.com/python/docs/reference/cloudfunctions/latest/google.cloud.functions_v2.types.ListFunctionsRequest)

Request for the `ListFunctions` method.

### [ListFunctionsResponse](https://docs.cloud.google.com/python/docs/reference/cloudfunctions/latest/google.cloud.functions_v2.types.ListFunctionsResponse)

Response for the `ListFunctions` method.

### [ListRuntimesRequest](https://docs.cloud.google.com/python/docs/reference/cloudfunctions/latest/google.cloud.functions_v2.types.ListRuntimesRequest)

Request for the `ListRuntimes` method.

### [ListRuntimesResponse](https://docs.cloud.google.com/python/docs/reference/cloudfunctions/latest/google.cloud.functions_v2.types.ListRuntimesResponse)

Response for the `ListRuntimes` method.

### [LocationMetadata](https://docs.cloud.google.com/python/docs/reference/cloudfunctions/latest/google.cloud.functions_v2.types.LocationMetadata)

Extra GCF specific location information.

### [OnDeployUpdatePolicy](https://docs.cloud.google.com/python/docs/reference/cloudfunctions/latest/google.cloud.functions_v2.types.OnDeployUpdatePolicy)

Security patches are only applied when a function is redeployed.

### [OperationMetadata](https://docs.cloud.google.com/python/docs/reference/cloudfunctions/latest/google.cloud.functions_v2.types.OperationMetadata)

Represents the metadata of the long-running operation.

### [OperationType](https://docs.cloud.google.com/python/docs/reference/cloudfunctions/latest/google.cloud.functions_v2.types.OperationType)

The type of the long running operation.

### [RepoSource](https://docs.cloud.google.com/python/docs/reference/cloudfunctions/latest/google.cloud.functions_v2.types.RepoSource)

Location of the source in a Google Cloud Source Repository.

This message has `oneof`_ fields (mutually exclusive fields). For each oneof, at most one member field can be set at the same time. Setting any member of the oneof automatically clears all other members.

.. _oneof: <https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields>

### [SecretEnvVar](https://docs.cloud.google.com/python/docs/reference/cloudfunctions/latest/google.cloud.functions_v2.types.SecretEnvVar)

Configuration for a secret environment variable. It has the information necessary to fetch the secret value from secret manager and expose it as an environment variable.

### [SecretVolume](https://docs.cloud.google.com/python/docs/reference/cloudfunctions/latest/google.cloud.functions_v2.types.SecretVolume)

Configuration for a secret volume. It has the information necessary to fetch the secret value from secret manager and make it available as files mounted at the requested paths within the application container.

### [ServiceConfig](https://docs.cloud.google.com/python/docs/reference/cloudfunctions/latest/google.cloud.functions_v2.types.ServiceConfig)

Describes the Service being deployed. Currently Supported : Cloud Run (fully managed).

### [Source](https://docs.cloud.google.com/python/docs/reference/cloudfunctions/latest/google.cloud.functions_v2.types.Source)

The location of the function source code.

This message has `oneof`_ fields (mutually exclusive fields). For each oneof, at most one member field can be set at the same time. Setting any member of the oneof automatically clears all other members.

.. _oneof: <https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields>

### [SourceProvenance](https://docs.cloud.google.com/python/docs/reference/cloudfunctions/latest/google.cloud.functions_v2.types.SourceProvenance)

Provenance of the source. Ways to find the original source, or verify that some source was used for this build.

### [Stage](https://docs.cloud.google.com/python/docs/reference/cloudfunctions/latest/google.cloud.functions_v2.types.Stage)

Each Stage of the deployment process

### [StateMessage](https://docs.cloud.google.com/python/docs/reference/cloudfunctions/latest/google.cloud.functions_v2.types.StateMessage)

Informational messages about the state of the Cloud Function or Operation.

### [StorageSource](https://docs.cloud.google.com/python/docs/reference/cloudfunctions/latest/google.cloud.functions_v2.types.StorageSource)

Location of the source in an archive file in Google Cloud Storage.

### [UpdateFunctionRequest](https://docs.cloud.google.com/python/docs/reference/cloudfunctions/latest/google.cloud.functions_v2.types.UpdateFunctionRequest)

Request for the `UpdateFunction` method.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-04 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-04 UTC."],[],[]] 
