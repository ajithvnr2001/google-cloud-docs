---
url: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ArtifactRegistry.V1Beta2/latest/Google.Cloud.ArtifactRegistry.V1Beta2
title: Artifact Registry v1beta2 API - Namespace Google.Cloud.ArtifactRegistry.V1Beta2 (2.0.0-beta06) \u00a0|\u00a0 .NET client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T17:18:17.215193+00:00
---

# Artifact Registry v1beta2 API - Namespace Google.Cloud.ArtifactRegistry.V1Beta2 (2.0.0-beta06)  |  .NET client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ArtifactRegistry.V1Beta2/latest/Google.Cloud.ArtifactRegistry.V1Beta2

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ .NET ](https://docs.cloud.google.com/dotnet/docs)
  * [ Client libraries ](https://docs.cloud.google.com/dotnet/docs/reference)



Send feedback 

#  Artifact Registry v1beta2 API - Namespace Google.Cloud.ArtifactRegistry.V1Beta2 (2.0.0-beta06) Stay organized with collections  Save and categorize content based on your preferences. 

Version latestkeyboard_arrow_down

  * [ 2.0.0-beta06 (latest) ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ArtifactRegistry.V1Beta2/latest/Google.Cloud.ArtifactRegistry.V1Beta2)
  * [ 2.0.0-beta05 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ArtifactRegistry.V1Beta2/2.0.0-beta05/Google.Cloud.ArtifactRegistry.V1Beta2)
  * [ 1.0.0-beta06 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ArtifactRegistry.V1Beta2/1.0.0-beta06/Google.Cloud.ArtifactRegistry.V1Beta2)



## Classes 

### [AptArtifact](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ArtifactRegistry.V1Beta2/latest/Google.Cloud.ArtifactRegistry.V1Beta2.AptArtifact)

A detailed representation of an Apt artifact. Information in the record is derived from the archive's control file. See <https://www.debian.org/doc/debian-policy/ch-controlfields.html>

### [AptArtifact.Types](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ArtifactRegistry.V1Beta2/latest/Google.Cloud.ArtifactRegistry.V1Beta2.AptArtifact.Types)

Container for nested types declared in the AptArtifact message type.

### [AptArtifactName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ArtifactRegistry.V1Beta2/latest/Google.Cloud.ArtifactRegistry.V1Beta2.AptArtifactName)

Resource name for the `AptArtifact` resource.

### [ArtifactRegistry](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ArtifactRegistry.V1Beta2/latest/Google.Cloud.ArtifactRegistry.V1Beta2.ArtifactRegistry)

The Artifact Registry API service.

Artifact Registry is an artifact management system for storing artifacts from different package management systems.

The resources managed by this API are:

  * Repositories, which group packages and their data.
  * Packages, which group versions and their tags.
  * Versions, which are specific forms of a package.
  * Tags, which represent alternative names for versions.
  * Files, which contain content and are optionally associated with a Package or Version.



### [ArtifactRegistry.ArtifactRegistryBase](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ArtifactRegistry.V1Beta2/latest/Google.Cloud.ArtifactRegistry.V1Beta2.ArtifactRegistry.ArtifactRegistryBase)

Base class for server-side implementations of ArtifactRegistry

### [ArtifactRegistry.ArtifactRegistryClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ArtifactRegistry.V1Beta2/latest/Google.Cloud.ArtifactRegistry.V1Beta2.ArtifactRegistry.ArtifactRegistryClient)

Client for ArtifactRegistry

### [ArtifactRegistryClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ArtifactRegistry.V1Beta2/latest/Google.Cloud.ArtifactRegistry.V1Beta2.ArtifactRegistryClient)

ArtifactRegistry client wrapper, for convenient use.

### [ArtifactRegistryClientBuilder](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ArtifactRegistry.V1Beta2/latest/Google.Cloud.ArtifactRegistry.V1Beta2.ArtifactRegistryClientBuilder)

Builder class for [ArtifactRegistryClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ArtifactRegistry.V1Beta2/latest/Google.Cloud.ArtifactRegistry.V1Beta2.ArtifactRegistryClient) to provide simple configuration of credentials, endpoint etc.

### [ArtifactRegistryClientImpl](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ArtifactRegistry.V1Beta2/latest/Google.Cloud.ArtifactRegistry.V1Beta2.ArtifactRegistryClientImpl)

ArtifactRegistry client wrapper implementation, for convenient use.

### [ArtifactRegistrySettings](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ArtifactRegistry.V1Beta2/latest/Google.Cloud.ArtifactRegistry.V1Beta2.ArtifactRegistrySettings)

Settings for [ArtifactRegistryClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ArtifactRegistry.V1Beta2/latest/Google.Cloud.ArtifactRegistry.V1Beta2.ArtifactRegistryClient) instances.

### [CreateRepositoryRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ArtifactRegistry.V1Beta2/latest/Google.Cloud.ArtifactRegistry.V1Beta2.CreateRepositoryRequest)

The request to create a new repository.

### [CreateTagRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ArtifactRegistry.V1Beta2/latest/Google.Cloud.ArtifactRegistry.V1Beta2.CreateTagRequest)

The request to create a new tag.

### [DeletePackageRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ArtifactRegistry.V1Beta2/latest/Google.Cloud.ArtifactRegistry.V1Beta2.DeletePackageRequest)

The request to delete a package.

### [DeleteRepositoryRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ArtifactRegistry.V1Beta2/latest/Google.Cloud.ArtifactRegistry.V1Beta2.DeleteRepositoryRequest)

The request to delete a repository.

### [DeleteTagRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ArtifactRegistry.V1Beta2/latest/Google.Cloud.ArtifactRegistry.V1Beta2.DeleteTagRequest)

The request to delete a tag.

### [DeleteVersionRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ArtifactRegistry.V1Beta2/latest/Google.Cloud.ArtifactRegistry.V1Beta2.DeleteVersionRequest)

The request to delete a version.

### [File](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ArtifactRegistry.V1Beta2/latest/Google.Cloud.ArtifactRegistry.V1Beta2.File)

Files store content that is potentially associated with Packages or Versions.

### [FileName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ArtifactRegistry.V1Beta2/latest/Google.Cloud.ArtifactRegistry.V1Beta2.FileName)

Resource name for the `File` resource.

### [GetFileRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ArtifactRegistry.V1Beta2/latest/Google.Cloud.ArtifactRegistry.V1Beta2.GetFileRequest)

The request to retrieve a file.

### [GetPackageRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ArtifactRegistry.V1Beta2/latest/Google.Cloud.ArtifactRegistry.V1Beta2.GetPackageRequest)

The request to retrieve a package.

### [GetProjectSettingsRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ArtifactRegistry.V1Beta2/latest/Google.Cloud.ArtifactRegistry.V1Beta2.GetProjectSettingsRequest)

Gets the redirection status for a project.

### [GetRepositoryRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ArtifactRegistry.V1Beta2/latest/Google.Cloud.ArtifactRegistry.V1Beta2.GetRepositoryRequest)

The request to retrieve a repository.

### [GetTagRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ArtifactRegistry.V1Beta2/latest/Google.Cloud.ArtifactRegistry.V1Beta2.GetTagRequest)

The request to retrieve a tag.

### [GetVersionRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ArtifactRegistry.V1Beta2/latest/Google.Cloud.ArtifactRegistry.V1Beta2.GetVersionRequest)

The request to retrieve a version.

### [Hash](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ArtifactRegistry.V1Beta2/latest/Google.Cloud.ArtifactRegistry.V1Beta2.Hash)

A hash of file content.

### [Hash.Types](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ArtifactRegistry.V1Beta2/latest/Google.Cloud.ArtifactRegistry.V1Beta2.Hash.Types)

Container for nested types declared in the Hash message type.

### [ImportAptArtifactsErrorInfo](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ArtifactRegistry.V1Beta2/latest/Google.Cloud.ArtifactRegistry.V1Beta2.ImportAptArtifactsErrorInfo)

Error information explaining why a package was not imported.

### [ImportAptArtifactsGcsSource](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ArtifactRegistry.V1Beta2/latest/Google.Cloud.ArtifactRegistry.V1Beta2.ImportAptArtifactsGcsSource)

Google Cloud Storage location where the artifacts currently reside.

### [ImportAptArtifactsMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ArtifactRegistry.V1Beta2/latest/Google.Cloud.ArtifactRegistry.V1Beta2.ImportAptArtifactsMetadata)

The operation metadata for importing artifacts.

### [ImportAptArtifactsRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ArtifactRegistry.V1Beta2/latest/Google.Cloud.ArtifactRegistry.V1Beta2.ImportAptArtifactsRequest)

The request to import new apt artifacts.

### [ImportAptArtifactsResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ArtifactRegistry.V1Beta2/latest/Google.Cloud.ArtifactRegistry.V1Beta2.ImportAptArtifactsResponse)

The response message from importing APT artifacts.

### [ImportYumArtifactsErrorInfo](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ArtifactRegistry.V1Beta2/latest/Google.Cloud.ArtifactRegistry.V1Beta2.ImportYumArtifactsErrorInfo)

Error information explaining why a package was not imported.

### [ImportYumArtifactsGcsSource](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ArtifactRegistry.V1Beta2/latest/Google.Cloud.ArtifactRegistry.V1Beta2.ImportYumArtifactsGcsSource)

Google Cloud Storage location where the artifacts currently reside.

### [ImportYumArtifactsMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ArtifactRegistry.V1Beta2/latest/Google.Cloud.ArtifactRegistry.V1Beta2.ImportYumArtifactsMetadata)

The operation metadata for importing artifacts.

### [ImportYumArtifactsRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ArtifactRegistry.V1Beta2/latest/Google.Cloud.ArtifactRegistry.V1Beta2.ImportYumArtifactsRequest)

The request to import new yum artifacts.

### [ImportYumArtifactsResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ArtifactRegistry.V1Beta2/latest/Google.Cloud.ArtifactRegistry.V1Beta2.ImportYumArtifactsResponse)

The response message from importing YUM artifacts.

### [ListFilesRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ArtifactRegistry.V1Beta2/latest/Google.Cloud.ArtifactRegistry.V1Beta2.ListFilesRequest)

The request to list files.

### [ListFilesResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ArtifactRegistry.V1Beta2/latest/Google.Cloud.ArtifactRegistry.V1Beta2.ListFilesResponse)

The response from listing files.

### [ListPackagesRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ArtifactRegistry.V1Beta2/latest/Google.Cloud.ArtifactRegistry.V1Beta2.ListPackagesRequest)

The request to list packages.

### [ListPackagesResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ArtifactRegistry.V1Beta2/latest/Google.Cloud.ArtifactRegistry.V1Beta2.ListPackagesResponse)

The response from listing packages.

### [ListRepositoriesRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ArtifactRegistry.V1Beta2/latest/Google.Cloud.ArtifactRegistry.V1Beta2.ListRepositoriesRequest)

The request to list repositories.

### [ListRepositoriesResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ArtifactRegistry.V1Beta2/latest/Google.Cloud.ArtifactRegistry.V1Beta2.ListRepositoriesResponse)

The response from listing repositories.

### [ListTagsRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ArtifactRegistry.V1Beta2/latest/Google.Cloud.ArtifactRegistry.V1Beta2.ListTagsRequest)

The request to list tags.

### [ListTagsResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ArtifactRegistry.V1Beta2/latest/Google.Cloud.ArtifactRegistry.V1Beta2.ListTagsResponse)

The response from listing tags.

### [ListVersionsRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ArtifactRegistry.V1Beta2/latest/Google.Cloud.ArtifactRegistry.V1Beta2.ListVersionsRequest)

The request to list versions.

### [ListVersionsResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ArtifactRegistry.V1Beta2/latest/Google.Cloud.ArtifactRegistry.V1Beta2.ListVersionsResponse)

The response from listing versions.

### [OperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ArtifactRegistry.V1Beta2/latest/Google.Cloud.ArtifactRegistry.V1Beta2.OperationMetadata)

Metadata type for longrunning-operations, currently empty.

### [Package](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ArtifactRegistry.V1Beta2/latest/Google.Cloud.ArtifactRegistry.V1Beta2.Package)

Packages are named collections of versions.

### [ProjectSettings](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ArtifactRegistry.V1Beta2/latest/Google.Cloud.ArtifactRegistry.V1Beta2.ProjectSettings)

The Artifact Registry settings that apply to a Project.

### [ProjectSettings.Types](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ArtifactRegistry.V1Beta2/latest/Google.Cloud.ArtifactRegistry.V1Beta2.ProjectSettings.Types)

Container for nested types declared in the ProjectSettings message type.

### [ProjectSettingsName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ArtifactRegistry.V1Beta2/latest/Google.Cloud.ArtifactRegistry.V1Beta2.ProjectSettingsName)

Resource name for the `ProjectSettings` resource.

### [Repository](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ArtifactRegistry.V1Beta2/latest/Google.Cloud.ArtifactRegistry.V1Beta2.Repository)

A Repository for storing artifacts with a specific format.

### [Repository.Types](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ArtifactRegistry.V1Beta2/latest/Google.Cloud.ArtifactRegistry.V1Beta2.Repository.Types)

Container for nested types declared in the Repository message type.

### [Repository.Types.MavenRepositoryConfig](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ArtifactRegistry.V1Beta2/latest/Google.Cloud.ArtifactRegistry.V1Beta2.Repository.Types.MavenRepositoryConfig)

MavenRepositoryConfig is maven related repository details. Provides additional configuration details for repositories of the maven format type.

### [Repository.Types.MavenRepositoryConfig.Types](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ArtifactRegistry.V1Beta2/latest/Google.Cloud.ArtifactRegistry.V1Beta2.Repository.Types.MavenRepositoryConfig.Types)

Container for nested types declared in the MavenRepositoryConfig message type.

### [RepositoryName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ArtifactRegistry.V1Beta2/latest/Google.Cloud.ArtifactRegistry.V1Beta2.RepositoryName)

Resource name for the `Repository` resource.

### [Tag](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ArtifactRegistry.V1Beta2/latest/Google.Cloud.ArtifactRegistry.V1Beta2.Tag)

Tags point to a version and represent an alternative name that can be used to access the version.

### [TagName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ArtifactRegistry.V1Beta2/latest/Google.Cloud.ArtifactRegistry.V1Beta2.TagName)

Resource name for the `Tag` resource.

### [UpdateProjectSettingsRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ArtifactRegistry.V1Beta2/latest/Google.Cloud.ArtifactRegistry.V1Beta2.UpdateProjectSettingsRequest)

Sets the settings of the project.

### [UpdateRepositoryRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ArtifactRegistry.V1Beta2/latest/Google.Cloud.ArtifactRegistry.V1Beta2.UpdateRepositoryRequest)

The request to update a repository.

### [UpdateTagRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ArtifactRegistry.V1Beta2/latest/Google.Cloud.ArtifactRegistry.V1Beta2.UpdateTagRequest)

The request to create or update a tag.

### [Version](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ArtifactRegistry.V1Beta2/latest/Google.Cloud.ArtifactRegistry.V1Beta2.Version)

The body of a version resource. A version resource represents a collection of components, such as files and other data. This may correspond to a version in many package management schemes.

### [VersionName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ArtifactRegistry.V1Beta2/latest/Google.Cloud.ArtifactRegistry.V1Beta2.VersionName)

Resource name for the `Version` resource.

### [YumArtifact](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ArtifactRegistry.V1Beta2/latest/Google.Cloud.ArtifactRegistry.V1Beta2.YumArtifact)

A detailed representation of a Yum artifact.

### [YumArtifact.Types](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ArtifactRegistry.V1Beta2/latest/Google.Cloud.ArtifactRegistry.V1Beta2.YumArtifact.Types)

Container for nested types declared in the YumArtifact message type.

### [YumArtifactName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ArtifactRegistry.V1Beta2/latest/Google.Cloud.ArtifactRegistry.V1Beta2.YumArtifactName)

Resource name for the `YumArtifact` resource.

## Enums 

### [AptArtifact.Types.PackageType](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ArtifactRegistry.V1Beta2/latest/Google.Cloud.ArtifactRegistry.V1Beta2.AptArtifact.Types.PackageType)

Package type is either binary or source.

### [AptArtifactName.ResourceNameType](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ArtifactRegistry.V1Beta2/latest/Google.Cloud.ArtifactRegistry.V1Beta2.AptArtifactName.ResourceNameType)

The possible contents of [AptArtifactName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ArtifactRegistry.V1Beta2/latest/Google.Cloud.ArtifactRegistry.V1Beta2.AptArtifactName).

### [FileName.ResourceNameType](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ArtifactRegistry.V1Beta2/latest/Google.Cloud.ArtifactRegistry.V1Beta2.FileName.ResourceNameType)

The possible contents of [FileName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ArtifactRegistry.V1Beta2/latest/Google.Cloud.ArtifactRegistry.V1Beta2.FileName).

### [Hash.Types.HashType](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ArtifactRegistry.V1Beta2/latest/Google.Cloud.ArtifactRegistry.V1Beta2.Hash.Types.HashType)

The algorithm used to compute the hash.

### [ImportAptArtifactsErrorInfo.SourceOneofCase](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ArtifactRegistry.V1Beta2/latest/Google.Cloud.ArtifactRegistry.V1Beta2.ImportAptArtifactsErrorInfo.SourceOneofCase)

Enum of possible cases for the "source" oneof.

### [ImportAptArtifactsRequest.SourceOneofCase](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ArtifactRegistry.V1Beta2/latest/Google.Cloud.ArtifactRegistry.V1Beta2.ImportAptArtifactsRequest.SourceOneofCase)

Enum of possible cases for the "source" oneof.

### [ImportYumArtifactsErrorInfo.SourceOneofCase](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ArtifactRegistry.V1Beta2/latest/Google.Cloud.ArtifactRegistry.V1Beta2.ImportYumArtifactsErrorInfo.SourceOneofCase)

Enum of possible cases for the "source" oneof.

### [ImportYumArtifactsRequest.SourceOneofCase](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ArtifactRegistry.V1Beta2/latest/Google.Cloud.ArtifactRegistry.V1Beta2.ImportYumArtifactsRequest.SourceOneofCase)

Enum of possible cases for the "source" oneof.

### [ProjectSettings.Types.RedirectionState](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ArtifactRegistry.V1Beta2/latest/Google.Cloud.ArtifactRegistry.V1Beta2.ProjectSettings.Types.RedirectionState)

The possible redirection states for legacy repositories.

### [ProjectSettingsName.ResourceNameType](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ArtifactRegistry.V1Beta2/latest/Google.Cloud.ArtifactRegistry.V1Beta2.ProjectSettingsName.ResourceNameType)

The possible contents of [ProjectSettingsName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ArtifactRegistry.V1Beta2/latest/Google.Cloud.ArtifactRegistry.V1Beta2.ProjectSettingsName).

### [Repository.FormatConfigOneofCase](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ArtifactRegistry.V1Beta2/latest/Google.Cloud.ArtifactRegistry.V1Beta2.Repository.FormatConfigOneofCase)

Enum of possible cases for the "format_config" oneof.

### [Repository.Types.Format](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ArtifactRegistry.V1Beta2/latest/Google.Cloud.ArtifactRegistry.V1Beta2.Repository.Types.Format)

A package format.

### [Repository.Types.MavenRepositoryConfig.Types.VersionPolicy](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ArtifactRegistry.V1Beta2/latest/Google.Cloud.ArtifactRegistry.V1Beta2.Repository.Types.MavenRepositoryConfig.Types.VersionPolicy)

VersionPolicy is the version policy for the repository.

### [RepositoryName.ResourceNameType](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ArtifactRegistry.V1Beta2/latest/Google.Cloud.ArtifactRegistry.V1Beta2.RepositoryName.ResourceNameType)

The possible contents of [RepositoryName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ArtifactRegistry.V1Beta2/latest/Google.Cloud.ArtifactRegistry.V1Beta2.RepositoryName).

### [TagName.ResourceNameType](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ArtifactRegistry.V1Beta2/latest/Google.Cloud.ArtifactRegistry.V1Beta2.TagName.ResourceNameType)

The possible contents of [TagName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ArtifactRegistry.V1Beta2/latest/Google.Cloud.ArtifactRegistry.V1Beta2.TagName).

### [VersionName.ResourceNameType](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ArtifactRegistry.V1Beta2/latest/Google.Cloud.ArtifactRegistry.V1Beta2.VersionName.ResourceNameType)

The possible contents of [VersionName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ArtifactRegistry.V1Beta2/latest/Google.Cloud.ArtifactRegistry.V1Beta2.VersionName).

### [VersionView](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ArtifactRegistry.V1Beta2/latest/Google.Cloud.ArtifactRegistry.V1Beta2.VersionView)

The view, which determines what version information is returned in a response.

### [YumArtifact.Types.PackageType](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ArtifactRegistry.V1Beta2/latest/Google.Cloud.ArtifactRegistry.V1Beta2.YumArtifact.Types.PackageType)

Package type is either binary or source.

### [YumArtifactName.ResourceNameType](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ArtifactRegistry.V1Beta2/latest/Google.Cloud.ArtifactRegistry.V1Beta2.YumArtifactName.ResourceNameType)

The possible contents of [YumArtifactName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ArtifactRegistry.V1Beta2/latest/Google.Cloud.ArtifactRegistry.V1Beta2.YumArtifactName).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-03-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-03-09 UTC."],[],[]] 
