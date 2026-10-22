---
url: https://docs.cloud.google.com/artifact-registry/docs/artifact-registry-regulatory-compliance/
title: Regulatory support in Artifact Registry \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T12:30:22.515917+00:00
---

# Regulatory support in Artifact Registry  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/artifact-registry/docs/artifact-registry-regulatory-compliance/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Artifact Registry ](https://docs.cloud.google.com/artifact-registry/docs)
  * [ Resources ](https://docs.cloud.google.com/artifact-registry/docs/resources)



Send feedback 

#  Regulatory support in Artifact Registry Stay organized with collections  Save and categorize content based on your preferences. 

This document describes the features, configurations and APIs in Artifact Registry that align with the controls for supported control packages. This document assumes that you're using [Assured Workloads](https://docs.cloud.google.com/assured-workloads/docs/overview).

Show AllAustralia Data Boundary and SupportData Boundary for ITAR  
  
---  
  
## Australia Data Boundary and Support

### Supported services

The following table lists the Artifact Registry APIs and versions that meet the requirements of Australia Data Boundary and Support. | Service | Version | Status  
---|---|---  
artifactregistry.googleapis.com | v1 |  SUPPORTED   
artifactregistry.googleapis.com | v1beta1 |  SUPPORTED   
artifactregistry.googleapis.com | v1beta2 |  SUPPORTED   
  
### Compliance supported regions

Artifact Registry is available for Australia Data Boundary and Support in the following Google Cloud regions:

  * australia-southeast1
  * australia-southeast2



### Fields not intended for Sensitive data

The following table provides an illustrative list of field categories and specific fields that aren't suitable for sensitive information. To maintain compliance, avoid placing protected data in these fields. For a complete list, contact your Google Cloud representative.

Category | Fields  
---|---  
Attachment details | 

  * `attachment.annotations.key`
  * `attachment.annotations.value`
  * `attachment.attachmentNamespace`
  * `attachment.files`
  * `attachment.target`
  * `attachment.type`

  
Blob/File identifiers | 

  * `blob.filename`
  * `blob.objectId.bucketName`
  * `blob.objectId.objectName`
  * `blob.path`
  * `blob.token`

  
Blob/File metadata | 

  * `blob.contentType`
  * `blob.contentTypeInfo.bestGuess`
  * `blob.contentTypeInfo.fromBytes`
  * `blob.contentTypeInfo.fromFileName`
  * `blob.contentTypeInfo.fromFusionId`
  * `blob.contentTypeInfo.fromUrlPath`

  
Filtering and ordering | 

  * `filter`
  * `orderBy`

  
Pagination control | 

  * `pageToken`

  
Parent/Scope identification | 

  * `parent`
  * `projectConfig.name`
  * `projectSettings.name`

  
Repository configuration | 

  * `repository.description`
  * `repository.kmsKeyName`
  * `repository.name`
  * `repository.networkConfig.alternativeHostname`
  * `repository.networkConfig.prefix`
  * `repository.remoteRepositoryConfig.commonRepository.uri`

  
Resource identification | 

  * `attachmentId`
  * `fileId`
  * `name`
  * `repositoryId`
  * `ruleId`
  * `tagId`

  
Update mask | 

  * `updateMask.paths`

  
Version and checksum information | 

  * `blob.diffChecksumsResponse.checksumsLocation.objectId.bucketName`
  * `blob.diffChecksumsResponse.checksumsLocation.objectId.objectName`
  * `blob.diffChecksumsResponse.checksumsLocation.path`
  * `blob.diffChecksumsResponse.objectVersion`
  * `blob.diffVersionResponse.objectVersion`

  
  
  
  
## Data Boundary for ITAR

### Supported services

The following table lists the Artifact Registry APIs and versions that meet the requirements of Data Boundary for ITAR. | Service | Version | Status  
---|---|---  
artifactregistry.googleapis.com | v1 |  SUPPORTED   
artifactregistry.googleapis.com | v1beta1 |  SUPPORTED   
artifactregistry.googleapis.com | v1beta2 |  SUPPORTED   
  
### Compliance supported regions

Artifact Registry is available for Data Boundary for ITAR in the following Google Cloud regions:

  * us-central1
  * us-central2
  * us-east1
  * us-east4
  * us-east5
  * us-south1
  * us-west1
  * us-west2
  * us-west3
  * us-west4



### Fields not intended for Sensitive data

The following table provides an illustrative list of field categories and specific fields that aren't suitable for sensitive information. To maintain compliance, avoid placing protected data in these fields. For a complete list, contact your Google Cloud representative.

Category | Fields  
---|---  
Attachment and file details | 

  * `attachment.annotations.value`
  * `attachment.attachmentNamespace`
  * `attachment.files`
  * `attachment.target`
  * `attachment.type`
  * `file.name`

  
Blob identification and location | 

  * `blob.diffDownloadResponse.objectLocation.blobstore2Info.blobId`
  * `blob.diffDownloadResponse.objectLocation.objectId.bucketName`
  * `blob.diffDownloadResponse.objectLocation.objectId.objectName`
  * `blob.diffDownloadResponse.objectLocation.path`
  * `blob.objectId.bucketName`
  * `blob.objectId.objectName`

  
Blob metadata and content | 

  * `blob.contentType`
  * `blob.contentTypeInfo.bestGuess`
  * `blob.contentTypeInfo.fromBytes`
  * `blob.contentTypeInfo.fromFileName`
  * `blob.contentTypeInfo.fromFusionId`
  * `blob.contentTypeInfo.fromHeader`

  
Blob upload/download details | 

  * `blob.diffChecksumsResponse.checksumsLocation.blobstore2Info.readToken`
  * `blob.diffChecksumsResponse.objectVersion`
  * `blob.diffUploadRequest.checksumsInfo.blobstore2Info.blobId`
  * `blob.diffUploadRequest.checksumsInfo.path`
  * `blob.diffUploadRequest.objectVersion`
  * `blob.diffUploadResponse.originalObject.path`

  
Filtering and sorting | 

  * `filter`
  * `orderBy`

  
Media request information | 

  * `mediaRequestInfo.customData`
  * `mediaRequestInfo.diffObjectVersion`
  * `mediaRequestInfo.requestId`

  
Paging and navigation | 

  * `pageToken`

  
Parent resource specification | 

  * `parent`

  
Repository configuration | 

  * `repository.description`
  * `repository.kmsKeyName`
  * `repository.labels.value`
  * `repository.name`
  * `repository.networkConfig.alternativeHostname`
  * `repository.remoteRepositoryConfig.commonRepository.uri`

  
Resource identification | 

  * `attachmentId`
  * `fileId`
  * `name`
  * `repositoryId`
  * `ruleId`
  * `tagId`

  
  
  
  
## What's next

  * Learn more about [compliance in Google Cloud](https://cloud.google.com/compliance).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
