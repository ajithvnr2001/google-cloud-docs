---
url: https://docs.cloud.google.com/python/docs/reference/apigeeregistry/latest/google.cloud.apigee_registry_v1.types
title: Package types (0.10.0) \u00a0|\u00a0 Python client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T19:24:07.897311+00:00
---

# Package types (0.10.0)  |  Python client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/python/docs/reference/apigeeregistry/latest/google.cloud.apigee_registry_v1.types

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Python ](https://docs.cloud.google.com/python/docs)
  * [ Client libraries ](https://docs.cloud.google.com/python/docs/reference)



Send feedback 

#  Package types (0.10.0) Stay organized with collections  Save and categorize content based on your preferences. 

0.10.0 (latest)  0.9.0  0.8.0  0.7.0  0.6.18  0.5.1  0.4.0  0.3.2  0.2.1  0.1.2 

API documentation for `apigee_registry_v1.types` package.

## Classes 

### [Api](https://docs.cloud.google.com/python/docs/reference/apigeeregistry/latest/google.cloud.apigee_registry_v1.types.Api)

A top-level description of an API. Produced by producers and are commitments to provide services.

### [ApiDeployment](https://docs.cloud.google.com/python/docs/reference/apigeeregistry/latest/google.cloud.apigee_registry_v1.types.ApiDeployment)

Describes a service running at particular address that provides a particular version of an API. ApiDeployments have revisions which correspond to different configurations of a single deployment in time. Revision identifiers should be updated whenever the served API spec or endpoint address changes.

### [ApiSpec](https://docs.cloud.google.com/python/docs/reference/apigeeregistry/latest/google.cloud.apigee_registry_v1.types.ApiSpec)

Describes a version of an API in a structured way. ApiSpecs provide formal descriptions that consumers can use to use a version. ApiSpec resources are intended to be fully-resolved descriptions of an ApiVersion. When specs consist of multiple files, these should be bundled together (e.g., in a zip archive) and stored as a unit. Multiple specs can exist to provide representations in different API description formats. Synchronization of these representations would be provided by tooling and background services.

### [ApiVersion](https://docs.cloud.google.com/python/docs/reference/apigeeregistry/latest/google.cloud.apigee_registry_v1.types.ApiVersion)

Describes a particular version of an API. ApiVersions are what consumers actually use.

### [Artifact](https://docs.cloud.google.com/python/docs/reference/apigeeregistry/latest/google.cloud.apigee_registry_v1.types.Artifact)

Artifacts of resources. Artifacts are unique (single-value) per resource and are used to store metadata that is too large or numerous to be stored directly on the resource. Since artifacts are stored separately from parent resources, they should generally be used for metadata that is needed infrequently, i.e., not for display in primary views of the resource but perhaps displayed or downloaded upon request. The `ListArtifacts` method allows artifacts to be quickly enumerated and checked for presence without downloading their (potentially-large) contents.

### [CreateApiDeploymentRequest](https://docs.cloud.google.com/python/docs/reference/apigeeregistry/latest/google.cloud.apigee_registry_v1.types.CreateApiDeploymentRequest)

Request message for CreateApiDeployment.

### [CreateApiRequest](https://docs.cloud.google.com/python/docs/reference/apigeeregistry/latest/google.cloud.apigee_registry_v1.types.CreateApiRequest)

Request message for CreateApi.

### [CreateApiSpecRequest](https://docs.cloud.google.com/python/docs/reference/apigeeregistry/latest/google.cloud.apigee_registry_v1.types.CreateApiSpecRequest)

Request message for CreateApiSpec.

### [CreateApiVersionRequest](https://docs.cloud.google.com/python/docs/reference/apigeeregistry/latest/google.cloud.apigee_registry_v1.types.CreateApiVersionRequest)

Request message for CreateApiVersion.

### [CreateArtifactRequest](https://docs.cloud.google.com/python/docs/reference/apigeeregistry/latest/google.cloud.apigee_registry_v1.types.CreateArtifactRequest)

Request message for CreateArtifact.

### [CreateInstanceRequest](https://docs.cloud.google.com/python/docs/reference/apigeeregistry/latest/google.cloud.apigee_registry_v1.types.CreateInstanceRequest)

Request message for CreateInstance.

### [DeleteApiDeploymentRequest](https://docs.cloud.google.com/python/docs/reference/apigeeregistry/latest/google.cloud.apigee_registry_v1.types.DeleteApiDeploymentRequest)

Request message for DeleteApiDeployment.

### [DeleteApiDeploymentRevisionRequest](https://docs.cloud.google.com/python/docs/reference/apigeeregistry/latest/google.cloud.apigee_registry_v1.types.DeleteApiDeploymentRevisionRequest)

Request message for DeleteApiDeploymentRevision.

### [DeleteApiRequest](https://docs.cloud.google.com/python/docs/reference/apigeeregistry/latest/google.cloud.apigee_registry_v1.types.DeleteApiRequest)

Request message for DeleteApi.

### [DeleteApiSpecRequest](https://docs.cloud.google.com/python/docs/reference/apigeeregistry/latest/google.cloud.apigee_registry_v1.types.DeleteApiSpecRequest)

Request message for DeleteApiSpec.

### [DeleteApiSpecRevisionRequest](https://docs.cloud.google.com/python/docs/reference/apigeeregistry/latest/google.cloud.apigee_registry_v1.types.DeleteApiSpecRevisionRequest)

Request message for DeleteApiSpecRevision.

### [DeleteApiVersionRequest](https://docs.cloud.google.com/python/docs/reference/apigeeregistry/latest/google.cloud.apigee_registry_v1.types.DeleteApiVersionRequest)

Request message for DeleteApiVersion.

### [DeleteArtifactRequest](https://docs.cloud.google.com/python/docs/reference/apigeeregistry/latest/google.cloud.apigee_registry_v1.types.DeleteArtifactRequest)

Request message for DeleteArtifact.

### [DeleteInstanceRequest](https://docs.cloud.google.com/python/docs/reference/apigeeregistry/latest/google.cloud.apigee_registry_v1.types.DeleteInstanceRequest)

Request message for DeleteInstance.

### [GetApiDeploymentRequest](https://docs.cloud.google.com/python/docs/reference/apigeeregistry/latest/google.cloud.apigee_registry_v1.types.GetApiDeploymentRequest)

Request message for GetApiDeployment.

### [GetApiRequest](https://docs.cloud.google.com/python/docs/reference/apigeeregistry/latest/google.cloud.apigee_registry_v1.types.GetApiRequest)

Request message for GetApi.

### [GetApiSpecContentsRequest](https://docs.cloud.google.com/python/docs/reference/apigeeregistry/latest/google.cloud.apigee_registry_v1.types.GetApiSpecContentsRequest)

Request message for GetApiSpecContents.

### [GetApiSpecRequest](https://docs.cloud.google.com/python/docs/reference/apigeeregistry/latest/google.cloud.apigee_registry_v1.types.GetApiSpecRequest)

Request message for GetApiSpec.

### [GetApiVersionRequest](https://docs.cloud.google.com/python/docs/reference/apigeeregistry/latest/google.cloud.apigee_registry_v1.types.GetApiVersionRequest)

Request message for GetApiVersion.

### [GetArtifactContentsRequest](https://docs.cloud.google.com/python/docs/reference/apigeeregistry/latest/google.cloud.apigee_registry_v1.types.GetArtifactContentsRequest)

Request message for GetArtifactContents.

### [GetArtifactRequest](https://docs.cloud.google.com/python/docs/reference/apigeeregistry/latest/google.cloud.apigee_registry_v1.types.GetArtifactRequest)

Request message for GetArtifact.

### [GetInstanceRequest](https://docs.cloud.google.com/python/docs/reference/apigeeregistry/latest/google.cloud.apigee_registry_v1.types.GetInstanceRequest)

Request message for GetInstance.

### [Instance](https://docs.cloud.google.com/python/docs/reference/apigeeregistry/latest/google.cloud.apigee_registry_v1.types.Instance)

An Instance represents the instance resources of the Registry. Currently, only one instance is allowed for each project.

### [ListApiDeploymentRevisionsRequest](https://docs.cloud.google.com/python/docs/reference/apigeeregistry/latest/google.cloud.apigee_registry_v1.types.ListApiDeploymentRevisionsRequest)

Request message for ListApiDeploymentRevisions.

### [ListApiDeploymentRevisionsResponse](https://docs.cloud.google.com/python/docs/reference/apigeeregistry/latest/google.cloud.apigee_registry_v1.types.ListApiDeploymentRevisionsResponse)

Response message for ListApiDeploymentRevisionsResponse.

### [ListApiDeploymentsRequest](https://docs.cloud.google.com/python/docs/reference/apigeeregistry/latest/google.cloud.apigee_registry_v1.types.ListApiDeploymentsRequest)

Request message for ListApiDeployments.

### [ListApiDeploymentsResponse](https://docs.cloud.google.com/python/docs/reference/apigeeregistry/latest/google.cloud.apigee_registry_v1.types.ListApiDeploymentsResponse)

Response message for ListApiDeployments.

### [ListApiSpecRevisionsRequest](https://docs.cloud.google.com/python/docs/reference/apigeeregistry/latest/google.cloud.apigee_registry_v1.types.ListApiSpecRevisionsRequest)

Request message for ListApiSpecRevisions.

### [ListApiSpecRevisionsResponse](https://docs.cloud.google.com/python/docs/reference/apigeeregistry/latest/google.cloud.apigee_registry_v1.types.ListApiSpecRevisionsResponse)

Response message for ListApiSpecRevisionsResponse.

### [ListApiSpecsRequest](https://docs.cloud.google.com/python/docs/reference/apigeeregistry/latest/google.cloud.apigee_registry_v1.types.ListApiSpecsRequest)

Request message for ListApiSpecs.

### [ListApiSpecsResponse](https://docs.cloud.google.com/python/docs/reference/apigeeregistry/latest/google.cloud.apigee_registry_v1.types.ListApiSpecsResponse)

Response message for ListApiSpecs.

### [ListApiVersionsRequest](https://docs.cloud.google.com/python/docs/reference/apigeeregistry/latest/google.cloud.apigee_registry_v1.types.ListApiVersionsRequest)

Request message for ListApiVersions.

### [ListApiVersionsResponse](https://docs.cloud.google.com/python/docs/reference/apigeeregistry/latest/google.cloud.apigee_registry_v1.types.ListApiVersionsResponse)

Response message for ListApiVersions.

### [ListApisRequest](https://docs.cloud.google.com/python/docs/reference/apigeeregistry/latest/google.cloud.apigee_registry_v1.types.ListApisRequest)

Request message for ListApis.

### [ListApisResponse](https://docs.cloud.google.com/python/docs/reference/apigeeregistry/latest/google.cloud.apigee_registry_v1.types.ListApisResponse)

Response message for ListApis.

### [ListArtifactsRequest](https://docs.cloud.google.com/python/docs/reference/apigeeregistry/latest/google.cloud.apigee_registry_v1.types.ListArtifactsRequest)

Request message for ListArtifacts.

### [ListArtifactsResponse](https://docs.cloud.google.com/python/docs/reference/apigeeregistry/latest/google.cloud.apigee_registry_v1.types.ListArtifactsResponse)

Response message for ListArtifacts.

### [OperationMetadata](https://docs.cloud.google.com/python/docs/reference/apigeeregistry/latest/google.cloud.apigee_registry_v1.types.OperationMetadata)

Represents the metadata of the long-running operation.

### [ReplaceArtifactRequest](https://docs.cloud.google.com/python/docs/reference/apigeeregistry/latest/google.cloud.apigee_registry_v1.types.ReplaceArtifactRequest)

Request message for ReplaceArtifact.

### [RollbackApiDeploymentRequest](https://docs.cloud.google.com/python/docs/reference/apigeeregistry/latest/google.cloud.apigee_registry_v1.types.RollbackApiDeploymentRequest)

Request message for RollbackApiDeployment.

### [RollbackApiSpecRequest](https://docs.cloud.google.com/python/docs/reference/apigeeregistry/latest/google.cloud.apigee_registry_v1.types.RollbackApiSpecRequest)

Request message for RollbackApiSpec.

### [TagApiDeploymentRevisionRequest](https://docs.cloud.google.com/python/docs/reference/apigeeregistry/latest/google.cloud.apigee_registry_v1.types.TagApiDeploymentRevisionRequest)

Request message for TagApiDeploymentRevision.

### [TagApiSpecRevisionRequest](https://docs.cloud.google.com/python/docs/reference/apigeeregistry/latest/google.cloud.apigee_registry_v1.types.TagApiSpecRevisionRequest)

Request message for TagApiSpecRevision.

### [UpdateApiDeploymentRequest](https://docs.cloud.google.com/python/docs/reference/apigeeregistry/latest/google.cloud.apigee_registry_v1.types.UpdateApiDeploymentRequest)

Request message for UpdateApiDeployment.

### [UpdateApiRequest](https://docs.cloud.google.com/python/docs/reference/apigeeregistry/latest/google.cloud.apigee_registry_v1.types.UpdateApiRequest)

Request message for UpdateApi.

### [UpdateApiSpecRequest](https://docs.cloud.google.com/python/docs/reference/apigeeregistry/latest/google.cloud.apigee_registry_v1.types.UpdateApiSpecRequest)

Request message for UpdateApiSpec.

### [UpdateApiVersionRequest](https://docs.cloud.google.com/python/docs/reference/apigeeregistry/latest/google.cloud.apigee_registry_v1.types.UpdateApiVersionRequest)

Request message for UpdateApiVersion.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-06-02 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-06-02 UTC."],[],[]] 
