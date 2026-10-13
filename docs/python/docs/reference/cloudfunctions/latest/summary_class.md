---
url: https://docs.cloud.google.com/python/docs/reference/cloudfunctions/latest/summary_class/
title: Package Classes (1.25.0) \u00a0|\u00a0 Python client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T12:31:09.877180+00:00
---

# Package Classes (1.25.0)  |  Python client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/python/docs/reference/cloudfunctions/latest/summary_class/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Python ](https://docs.cloud.google.com/python/docs)
  * [ Client libraries ](https://docs.cloud.google.com/python/docs/reference)



Send feedback 

#  Package Classes (1.25.0) Stay organized with collections  Save and categorize content based on your preferences. 

1.25.0 (latest)  1.24.0  1.23.0  1.22.0  1.21.0  1.20.4  1.19.0  1.18.1  1.16.5  1.15.0  1.14.0  1.13.2  1.12.0  1.11.0  1.10.1  1.9.0  1.8.3  1.7.0  1.6.0  1.5.2  1.4.0  1.3.1  1.2.0  1.1.1  1.0.4  0.7.2  0.6.1  0.5.1  0.4.0  0.1.0 

Summary of entries of Classes for cloudfunctions.

## Classes 

### [CloudFunctionsServiceAsyncClient](https://docs.cloud.google.com/python/docs/reference/cloudfunctions/latest/google.cloud.functions_v1.services.cloud_functions_service.CloudFunctionsServiceAsyncClient)

A service that application uses to manipulate triggers and functions.

### [CloudFunctionsServiceClient](https://docs.cloud.google.com/python/docs/reference/cloudfunctions/latest/google.cloud.functions_v1.services.cloud_functions_service.CloudFunctionsServiceClient)

A service that application uses to manipulate triggers and functions.

### [ListFunctionsAsyncPager](https://docs.cloud.google.com/python/docs/reference/cloudfunctions/latest/google.cloud.functions_v1.services.cloud_functions_service.pagers.ListFunctionsAsyncPager)

A pager for iterating through `list_functions` requests.

This class thinly wraps an initial [ListFunctionsResponse](https://docs.cloud.google.com/python/docs/reference/cloudfunctions/latest/google.cloud.functions_v1.types.ListFunctionsResponse) object, and provides an `__aiter__` method to iterate through its `functions` field.

If there are more pages, the `__aiter__` method will make additional `ListFunctions` requests and continue to iterate through the `functions` field on the corresponding responses.

All the usual [ListFunctionsResponse](https://docs.cloud.google.com/python/docs/reference/cloudfunctions/latest/google.cloud.functions_v1.types.ListFunctionsResponse) attributes are available on the pager. If multiple requests are made, only the most recent response is retained, and thus used for attribute lookup.

### [ListFunctionsPager](https://docs.cloud.google.com/python/docs/reference/cloudfunctions/latest/google.cloud.functions_v1.services.cloud_functions_service.pagers.ListFunctionsPager)

A pager for iterating through `list_functions` requests.

This class thinly wraps an initial [ListFunctionsResponse](https://docs.cloud.google.com/python/docs/reference/cloudfunctions/latest/google.cloud.functions_v1.types.ListFunctionsResponse) object, and provides an `__iter__` method to iterate through its `functions` field.

If there are more pages, the `__iter__` method will make additional `ListFunctions` requests and continue to iterate through the `functions` field on the corresponding responses.

All the usual [ListFunctionsResponse](https://docs.cloud.google.com/python/docs/reference/cloudfunctions/latest/google.cloud.functions_v1.types.ListFunctionsResponse) attributes are available on the pager. If multiple requests are made, only the most recent response is retained, and thus used for attribute lookup.

### [CallFunctionRequest](https://docs.cloud.google.com/python/docs/reference/cloudfunctions/latest/google.cloud.functions_v1.types.CallFunctionRequest)

Request for the `CallFunction` method.

### [CallFunctionResponse](https://docs.cloud.google.com/python/docs/reference/cloudfunctions/latest/google.cloud.functions_v1.types.CallFunctionResponse)

Response of `CallFunction` method.

### [CloudFunction](https://docs.cloud.google.com/python/docs/reference/cloudfunctions/latest/google.cloud.functions_v1.types.CloudFunction)

Describes a Cloud Function that contains user computation executed in response to an event. It encapsulate function and triggers configurations.

This message has `oneof`_ fields (mutually exclusive fields). For each oneof, at most one member field can be set at the same time. Setting any member of the oneof automatically clears all other members.

.. _oneof: <https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields>

### [AutomaticUpdatePolicy](https://docs.cloud.google.com/python/docs/reference/cloudfunctions/latest/google.cloud.functions_v1.types.CloudFunction.AutomaticUpdatePolicy)

Security patches are applied automatically to the runtime without requiring the function to be redeployed.

### [BuildEnvironmentVariablesEntry](https://docs.cloud.google.com/python/docs/reference/cloudfunctions/latest/google.cloud.functions_v1.types.CloudFunction.BuildEnvironmentVariablesEntry)

The abstract base class for a message.

### [DockerRegistry](https://docs.cloud.google.com/python/docs/reference/cloudfunctions/latest/google.cloud.functions_v1.types.CloudFunction.DockerRegistry)

Docker Registry to use for storing function Docker images.

### [EnvironmentVariablesEntry](https://docs.cloud.google.com/python/docs/reference/cloudfunctions/latest/google.cloud.functions_v1.types.CloudFunction.EnvironmentVariablesEntry)

The abstract base class for a message.

### [IngressSettings](https://docs.cloud.google.com/python/docs/reference/cloudfunctions/latest/google.cloud.functions_v1.types.CloudFunction.IngressSettings)

Available ingress settings.

This controls what traffic can reach the function.

If unspecified, ALLOW_ALL will be used.

### [LabelsEntry](https://docs.cloud.google.com/python/docs/reference/cloudfunctions/latest/google.cloud.functions_v1.types.CloudFunction.LabelsEntry)

The abstract base class for a message.

### [OnDeployUpdatePolicy](https://docs.cloud.google.com/python/docs/reference/cloudfunctions/latest/google.cloud.functions_v1.types.CloudFunction.OnDeployUpdatePolicy)

Security patches are only applied when a function is redeployed.

### [VpcConnectorEgressSettings](https://docs.cloud.google.com/python/docs/reference/cloudfunctions/latest/google.cloud.functions_v1.types.CloudFunction.VpcConnectorEgressSettings)

Available egress settings.

This controls what traffic is diverted through the VPC Access Connector resource. By default PRIVATE_RANGES_ONLY will be used.

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

### [Retry](https://docs.cloud.google.com/python/docs/reference/cloudfunctions/latest/google.cloud.functions_v1.types.FailurePolicy.Retry)

Describes the retry policy in case of function's execution failure. A function execution will be retried on any failure. A failed execution will be retried up to 7 days with an exponential backoff (capped at 10 seconds). Retried execution is charged as any other execution.

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

### [SecurityLevel](https://docs.cloud.google.com/python/docs/reference/cloudfunctions/latest/google.cloud.functions_v1.types.HttpsTrigger.SecurityLevel)

Available security level settings.

This controls the methods to enforce security (HTTPS) on a URL.

If unspecified, SECURE_OPTIONAL will be used.

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

### [SecretVersion](https://docs.cloud.google.com/python/docs/reference/cloudfunctions/latest/google.cloud.functions_v1.types.SecretVolume.SecretVersion)

Configuration for a single version.

### [SourceRepository](https://docs.cloud.google.com/python/docs/reference/cloudfunctions/latest/google.cloud.functions_v1.types.SourceRepository)

Describes SourceRepository, used to represent parameters related to source repository where a function is hosted.

### [UpdateFunctionRequest](https://docs.cloud.google.com/python/docs/reference/cloudfunctions/latest/google.cloud.functions_v1.types.UpdateFunctionRequest)

Request for the `UpdateFunction` method.

### [FunctionServiceAsyncClient](https://docs.cloud.google.com/python/docs/reference/cloudfunctions/latest/google.cloud.functions_v2.services.function_service.FunctionServiceAsyncClient)

Google Cloud Functions is used to deploy functions that are executed by Google in response to various events. Data connected with that event is passed to a function as the input data.

A **function** is a resource which describes a function that should be executed and how it is triggered.

### [FunctionServiceClient](https://docs.cloud.google.com/python/docs/reference/cloudfunctions/latest/google.cloud.functions_v2.services.function_service.FunctionServiceClient)

Google Cloud Functions is used to deploy functions that are executed by Google in response to various events. Data connected with that event is passed to a function as the input data.

A **function** is a resource which describes a function that should be executed and how it is triggered.

### [ListFunctionsAsyncPager](https://docs.cloud.google.com/python/docs/reference/cloudfunctions/latest/google.cloud.functions_v2.services.function_service.pagers.ListFunctionsAsyncPager)

A pager for iterating through `list_functions` requests.

This class thinly wraps an initial [ListFunctionsResponse](https://docs.cloud.google.com/python/docs/reference/cloudfunctions/latest/google.cloud.functions_v2.types.ListFunctionsResponse) object, and provides an `__aiter__` method to iterate through its `functions` field.

If there are more pages, the `__aiter__` method will make additional `ListFunctions` requests and continue to iterate through the `functions` field on the corresponding responses.

All the usual [ListFunctionsResponse](https://docs.cloud.google.com/python/docs/reference/cloudfunctions/latest/google.cloud.functions_v2.types.ListFunctionsResponse) attributes are available on the pager. If multiple requests are made, only the most recent response is retained, and thus used for attribute lookup.

### [ListFunctionsPager](https://docs.cloud.google.com/python/docs/reference/cloudfunctions/latest/google.cloud.functions_v2.services.function_service.pagers.ListFunctionsPager)

A pager for iterating through `list_functions` requests.

This class thinly wraps an initial [ListFunctionsResponse](https://docs.cloud.google.com/python/docs/reference/cloudfunctions/latest/google.cloud.functions_v2.types.ListFunctionsResponse) object, and provides an `__iter__` method to iterate through its `functions` field.

If there are more pages, the `__iter__` method will make additional `ListFunctions` requests and continue to iterate through the `functions` field on the corresponding responses.

All the usual [ListFunctionsResponse](https://docs.cloud.google.com/python/docs/reference/cloudfunctions/latest/google.cloud.functions_v2.types.ListFunctionsResponse) attributes are available on the pager. If multiple requests are made, only the most recent response is retained, and thus used for attribute lookup.

### [AutomaticUpdatePolicy](https://docs.cloud.google.com/python/docs/reference/cloudfunctions/latest/google.cloud.functions_v2.types.AutomaticUpdatePolicy)

Security patches are applied automatically to the runtime without requiring the function to be redeployed.

### [BuildConfig](https://docs.cloud.google.com/python/docs/reference/cloudfunctions/latest/google.cloud.functions_v2.types.BuildConfig)

Describes the Build step of the function that builds a container from the given source.

This message has `oneof`_ fields (mutually exclusive fields). For each oneof, at most one member field can be set at the same time. Setting any member of the oneof automatically clears all other members.

.. _oneof: <https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields>

### [DockerRegistry](https://docs.cloud.google.com/python/docs/reference/cloudfunctions/latest/google.cloud.functions_v2.types.BuildConfig.DockerRegistry)

Docker Registry to use for storing function Docker images.

### [EnvironmentVariablesEntry](https://docs.cloud.google.com/python/docs/reference/cloudfunctions/latest/google.cloud.functions_v2.types.BuildConfig.EnvironmentVariablesEntry)

The abstract base class for a message.

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

### [RetryPolicy](https://docs.cloud.google.com/python/docs/reference/cloudfunctions/latest/google.cloud.functions_v2.types.EventTrigger.RetryPolicy)

Describes the retry policy in case of function's execution failure. Retried execution is charged as any other execution.

### [Function](https://docs.cloud.google.com/python/docs/reference/cloudfunctions/latest/google.cloud.functions_v2.types.Function)

Describes a Cloud Function that contains user computation executed in response to an event. It encapsulates function and trigger configurations.

### [LabelsEntry](https://docs.cloud.google.com/python/docs/reference/cloudfunctions/latest/google.cloud.functions_v2.types.Function.LabelsEntry)

The abstract base class for a message.

### [State](https://docs.cloud.google.com/python/docs/reference/cloudfunctions/latest/google.cloud.functions_v2.types.Function.State)

Describes the current state of the function.

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

### [Runtime](https://docs.cloud.google.com/python/docs/reference/cloudfunctions/latest/google.cloud.functions_v2.types.ListRuntimesResponse.Runtime)

Describes a runtime and any special information (e.g., deprecation status) related to it.

### [RuntimeStage](https://docs.cloud.google.com/python/docs/reference/cloudfunctions/latest/google.cloud.functions_v2.types.ListRuntimesResponse.RuntimeStage)

The various stages that a runtime can be in.

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

### [SecretVersion](https://docs.cloud.google.com/python/docs/reference/cloudfunctions/latest/google.cloud.functions_v2.types.SecretVolume.SecretVersion)

Configuration for a single version.

### [ServiceConfig](https://docs.cloud.google.com/python/docs/reference/cloudfunctions/latest/google.cloud.functions_v2.types.ServiceConfig)

Describes the Service being deployed. Currently Supported : Cloud Run (fully managed).

### [EnvironmentVariablesEntry](https://docs.cloud.google.com/python/docs/reference/cloudfunctions/latest/google.cloud.functions_v2.types.ServiceConfig.EnvironmentVariablesEntry)

The abstract base class for a message.

### [IngressSettings](https://docs.cloud.google.com/python/docs/reference/cloudfunctions/latest/google.cloud.functions_v2.types.ServiceConfig.IngressSettings)

Available ingress settings.

This controls what traffic can reach the function.

If unspecified, ALLOW_ALL will be used.

### [SecurityLevel](https://docs.cloud.google.com/python/docs/reference/cloudfunctions/latest/google.cloud.functions_v2.types.ServiceConfig.SecurityLevel)

Available security level settings.

This enforces security protocol on function URL.

Security level is only configurable for 1st Gen functions, If unspecified, SECURE_OPTIONAL will be used. 2nd Gen functions are SECURE_ALWAYS ONLY.

### [VpcConnectorEgressSettings](https://docs.cloud.google.com/python/docs/reference/cloudfunctions/latest/google.cloud.functions_v2.types.ServiceConfig.VpcConnectorEgressSettings)

Available egress settings.

This controls what traffic is diverted through the VPC Access Connector resource. By default PRIVATE_RANGES_ONLY will be used.

### [Source](https://docs.cloud.google.com/python/docs/reference/cloudfunctions/latest/google.cloud.functions_v2.types.Source)

The location of the function source code.

This message has `oneof`_ fields (mutually exclusive fields). For each oneof, at most one member field can be set at the same time. Setting any member of the oneof automatically clears all other members.

.. _oneof: <https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields>

### [SourceProvenance](https://docs.cloud.google.com/python/docs/reference/cloudfunctions/latest/google.cloud.functions_v2.types.SourceProvenance)

Provenance of the source. Ways to find the original source, or verify that some source was used for this build.

### [Stage](https://docs.cloud.google.com/python/docs/reference/cloudfunctions/latest/google.cloud.functions_v2.types.Stage)

Each Stage of the deployment process

### [Name](https://docs.cloud.google.com/python/docs/reference/cloudfunctions/latest/google.cloud.functions_v2.types.Stage.Name)

Possible names for a Stage

### [State](https://docs.cloud.google.com/python/docs/reference/cloudfunctions/latest/google.cloud.functions_v2.types.Stage.State)

Possible states for a Stage

### [StateMessage](https://docs.cloud.google.com/python/docs/reference/cloudfunctions/latest/google.cloud.functions_v2.types.StateMessage)

Informational messages about the state of the Cloud Function or Operation.

### [Severity](https://docs.cloud.google.com/python/docs/reference/cloudfunctions/latest/google.cloud.functions_v2.types.StateMessage.Severity)

Severity of the state message.

### [StorageSource](https://docs.cloud.google.com/python/docs/reference/cloudfunctions/latest/google.cloud.functions_v2.types.StorageSource)

Location of the source in an archive file in Google Cloud Storage.

### [UpdateFunctionRequest](https://docs.cloud.google.com/python/docs/reference/cloudfunctions/latest/google.cloud.functions_v2.types.UpdateFunctionRequest)

Request for the `UpdateFunction` method.

## Modules 

### [pagers](https://docs.cloud.google.com/python/docs/reference/cloudfunctions/latest/google.cloud.functions_v1.services.cloud_functions_service.pagers)

API documentation for `functions_v1.services.cloud_functions_service.pagers` module.

### [pagers](https://docs.cloud.google.com/python/docs/reference/cloudfunctions/latest/google.cloud.functions_v2.services.function_service.pagers)

API documentation for `functions_v2.services.function_service.pagers` module.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-04 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-04 UTC."],[],[]] 
