---
url: https://docs.cloud.google.com/artifact-registry/docs/reference/rpc/
title: Artifact Registry API \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T17:10:35.500390+00:00
---

# Artifact Registry API  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/artifact-registry/docs/reference/rpc/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Artifact Registry ](https://docs.cloud.google.com/artifact-registry/docs)
  * [ Reference ](https://docs.cloud.google.com/artifact-registry/docs/apis)



Send feedback 

#  Artifact Registry API Stay organized with collections  Save and categorize content based on your preferences. 

Store and manage build artifacts in a scalable and integrated service built on Google infrastructure.

## Service: artifactregistry.googleapis.com

The Service name `artifactregistry.googleapis.com` is needed to create RPC client stubs.

## `[google.cloud.location.Locations](https://docs.cloud.google.com/artifact-registry/docs/reference/rpc/google.cloud.location#google.cloud.location.Locations)`

Methods  
---  
``[GetLocation](https://docs.cloud.google.com/artifact-registry/docs/reference/rpc/google.cloud.location#google.cloud.location.Locations.GetLocation)`` |  Gets information about a location.  
``[ListLocations](https://docs.cloud.google.com/artifact-registry/docs/reference/rpc/google.cloud.location#google.cloud.location.Locations.ListLocations)`` |  Lists information about the supported locations for this service.  
  
## `[google.devtools.artifactregistry.v1.ArtifactRegistry](https://docs.cloud.google.com/artifact-registry/docs/reference/rpc/google.devtools.artifactregistry.v1#google.devtools.artifactregistry.v1.ArtifactRegistry)`

Methods  
---  
``[BatchDeleteVersions](https://docs.cloud.google.com/artifact-registry/docs/reference/rpc/google.devtools.artifactregistry.v1#google.devtools.artifactregistry.v1.ArtifactRegistry.BatchDeleteVersions)`` |  Deletes multiple versions across a repository.  
``[CreateAttachment](https://docs.cloud.google.com/artifact-registry/docs/reference/rpc/google.devtools.artifactregistry.v1#google.devtools.artifactregistry.v1.ArtifactRegistry.CreateAttachment)`` |  Creates an attachment.  
``[CreateRepository](https://docs.cloud.google.com/artifact-registry/docs/reference/rpc/google.devtools.artifactregistry.v1#google.devtools.artifactregistry.v1.ArtifactRegistry.CreateRepository)`` |  Creates a repository.  
``[CreateRule](https://docs.cloud.google.com/artifact-registry/docs/reference/rpc/google.devtools.artifactregistry.v1#google.devtools.artifactregistry.v1.ArtifactRegistry.CreateRule)`` |  Creates a rule.  
``[CreateTag](https://docs.cloud.google.com/artifact-registry/docs/reference/rpc/google.devtools.artifactregistry.v1#google.devtools.artifactregistry.v1.ArtifactRegistry.CreateTag)`` |  Creates a tag.  
``[DeleteAttachment](https://docs.cloud.google.com/artifact-registry/docs/reference/rpc/google.devtools.artifactregistry.v1#google.devtools.artifactregistry.v1.ArtifactRegistry.DeleteAttachment)`` |  Deletes an attachment.  
``[DeleteFile](https://docs.cloud.google.com/artifact-registry/docs/reference/rpc/google.devtools.artifactregistry.v1#google.devtools.artifactregistry.v1.ArtifactRegistry.DeleteFile)`` |  Deletes a file and all of its content.  
``[DeletePackage](https://docs.cloud.google.com/artifact-registry/docs/reference/rpc/google.devtools.artifactregistry.v1#google.devtools.artifactregistry.v1.ArtifactRegistry.DeletePackage)`` |  Deletes a package and all of its versions and tags.  
``[DeleteRepository](https://docs.cloud.google.com/artifact-registry/docs/reference/rpc/google.devtools.artifactregistry.v1#google.devtools.artifactregistry.v1.ArtifactRegistry.DeleteRepository)`` |  Deletes a repository and all of its contents.  
``[DeleteRule](https://docs.cloud.google.com/artifact-registry/docs/reference/rpc/google.devtools.artifactregistry.v1#google.devtools.artifactregistry.v1.ArtifactRegistry.DeleteRule)`` |  Deletes a rule.  
``[DeleteTag](https://docs.cloud.google.com/artifact-registry/docs/reference/rpc/google.devtools.artifactregistry.v1#google.devtools.artifactregistry.v1.ArtifactRegistry.DeleteTag)`` |  Deletes a tag.  
``[DeleteVersion](https://docs.cloud.google.com/artifact-registry/docs/reference/rpc/google.devtools.artifactregistry.v1#google.devtools.artifactregistry.v1.ArtifactRegistry.DeleteVersion)`` |  Deletes a version and all of its content.  
``[ExportArtifact](https://docs.cloud.google.com/artifact-registry/docs/reference/rpc/google.devtools.artifactregistry.v1#google.devtools.artifactregistry.v1.ArtifactRegistry.ExportArtifact)`` |  Exports an artifact to a Cloud Storage bucket.  
``[GetAttachment](https://docs.cloud.google.com/artifact-registry/docs/reference/rpc/google.devtools.artifactregistry.v1#google.devtools.artifactregistry.v1.ArtifactRegistry.GetAttachment)`` |  Gets an attachment.  
``[GetDockerImage](https://docs.cloud.google.com/artifact-registry/docs/reference/rpc/google.devtools.artifactregistry.v1#google.devtools.artifactregistry.v1.ArtifactRegistry.GetDockerImage)`` |  Gets a docker image.  
``[GetFile](https://docs.cloud.google.com/artifact-registry/docs/reference/rpc/google.devtools.artifactregistry.v1#google.devtools.artifactregistry.v1.ArtifactRegistry.GetFile)`` |  Gets a file.  
``[GetIamPolicy](https://docs.cloud.google.com/artifact-registry/docs/reference/rpc/google.devtools.artifactregistry.v1#google.devtools.artifactregistry.v1.ArtifactRegistry.GetIamPolicy)`` |  Gets the IAM policy for a given resource.  
``[GetMavenArtifact](https://docs.cloud.google.com/artifact-registry/docs/reference/rpc/google.devtools.artifactregistry.v1#google.devtools.artifactregistry.v1.ArtifactRegistry.GetMavenArtifact)`` |  Gets a maven artifact.  
``[GetNpmPackage](https://docs.cloud.google.com/artifact-registry/docs/reference/rpc/google.devtools.artifactregistry.v1#google.devtools.artifactregistry.v1.ArtifactRegistry.GetNpmPackage)`` |  Gets a npm package.  
``[GetPackage](https://docs.cloud.google.com/artifact-registry/docs/reference/rpc/google.devtools.artifactregistry.v1#google.devtools.artifactregistry.v1.ArtifactRegistry.GetPackage)`` |  Gets a package.  
``[GetProjectSettings](https://docs.cloud.google.com/artifact-registry/docs/reference/rpc/google.devtools.artifactregistry.v1#google.devtools.artifactregistry.v1.ArtifactRegistry.GetProjectSettings)`` |  Retrieves the Settings for the Project.  
``[GetPythonPackage](https://docs.cloud.google.com/artifact-registry/docs/reference/rpc/google.devtools.artifactregistry.v1#google.devtools.artifactregistry.v1.ArtifactRegistry.GetPythonPackage)`` |  Gets a python package.  
``[GetRepository](https://docs.cloud.google.com/artifact-registry/docs/reference/rpc/google.devtools.artifactregistry.v1#google.devtools.artifactregistry.v1.ArtifactRegistry.GetRepository)`` |  Gets a repository.  
``[GetRule](https://docs.cloud.google.com/artifact-registry/docs/reference/rpc/google.devtools.artifactregistry.v1#google.devtools.artifactregistry.v1.ArtifactRegistry.GetRule)`` |  Gets a rule.  
``[GetTag](https://docs.cloud.google.com/artifact-registry/docs/reference/rpc/google.devtools.artifactregistry.v1#google.devtools.artifactregistry.v1.ArtifactRegistry.GetTag)`` |  Gets a tag.  
``[GetVPCSCConfig](https://docs.cloud.google.com/artifact-registry/docs/reference/rpc/google.devtools.artifactregistry.v1#google.devtools.artifactregistry.v1.ArtifactRegistry.GetVPCSCConfig)`` |  Retrieves the VPCSC Config for the Project.  
``[GetVersion](https://docs.cloud.google.com/artifact-registry/docs/reference/rpc/google.devtools.artifactregistry.v1#google.devtools.artifactregistry.v1.ArtifactRegistry.GetVersion)`` |  Gets a version  
``[ImportAptArtifacts](https://docs.cloud.google.com/artifact-registry/docs/reference/rpc/google.devtools.artifactregistry.v1#google.devtools.artifactregistry.v1.ArtifactRegistry.ImportAptArtifacts)`` |  Imports Apt artifacts.  
``[ImportGoogetArtifacts](https://docs.cloud.google.com/artifact-registry/docs/reference/rpc/google.devtools.artifactregistry.v1#google.devtools.artifactregistry.v1.ArtifactRegistry.ImportGoogetArtifacts)`` |  Imports GooGet artifacts.  
``[ImportYumArtifacts](https://docs.cloud.google.com/artifact-registry/docs/reference/rpc/google.devtools.artifactregistry.v1#google.devtools.artifactregistry.v1.ArtifactRegistry.ImportYumArtifacts)`` |  Imports Yum (RPM) artifacts.  
``[ListAttachments](https://docs.cloud.google.com/artifact-registry/docs/reference/rpc/google.devtools.artifactregistry.v1#google.devtools.artifactregistry.v1.ArtifactRegistry.ListAttachments)`` |  Lists attachments.  
``[ListDockerImages](https://docs.cloud.google.com/artifact-registry/docs/reference/rpc/google.devtools.artifactregistry.v1#google.devtools.artifactregistry.v1.ArtifactRegistry.ListDockerImages)`` |  Lists docker images.  
``[ListFiles](https://docs.cloud.google.com/artifact-registry/docs/reference/rpc/google.devtools.artifactregistry.v1#google.devtools.artifactregistry.v1.ArtifactRegistry.ListFiles)`` |  Lists files.  
``[ListMavenArtifacts](https://docs.cloud.google.com/artifact-registry/docs/reference/rpc/google.devtools.artifactregistry.v1#google.devtools.artifactregistry.v1.ArtifactRegistry.ListMavenArtifacts)`` |  Lists maven artifacts.  
``[ListNpmPackages](https://docs.cloud.google.com/artifact-registry/docs/reference/rpc/google.devtools.artifactregistry.v1#google.devtools.artifactregistry.v1.ArtifactRegistry.ListNpmPackages)`` |  Lists npm packages.  
``[ListPackages](https://docs.cloud.google.com/artifact-registry/docs/reference/rpc/google.devtools.artifactregistry.v1#google.devtools.artifactregistry.v1.ArtifactRegistry.ListPackages)`` |  Lists packages.  
``[ListPythonPackages](https://docs.cloud.google.com/artifact-registry/docs/reference/rpc/google.devtools.artifactregistry.v1#google.devtools.artifactregistry.v1.ArtifactRegistry.ListPythonPackages)`` |  Lists python packages.  
``[ListRepositories](https://docs.cloud.google.com/artifact-registry/docs/reference/rpc/google.devtools.artifactregistry.v1#google.devtools.artifactregistry.v1.ArtifactRegistry.ListRepositories)`` |  Lists repositories.  
``[ListRules](https://docs.cloud.google.com/artifact-registry/docs/reference/rpc/google.devtools.artifactregistry.v1#google.devtools.artifactregistry.v1.ArtifactRegistry.ListRules)`` |  Lists rules.  
``[ListTags](https://docs.cloud.google.com/artifact-registry/docs/reference/rpc/google.devtools.artifactregistry.v1#google.devtools.artifactregistry.v1.ArtifactRegistry.ListTags)`` |  Lists tags.  
``[ListVersions](https://docs.cloud.google.com/artifact-registry/docs/reference/rpc/google.devtools.artifactregistry.v1#google.devtools.artifactregistry.v1.ArtifactRegistry.ListVersions)`` |  Lists versions.  
``[SetIamPolicy](https://docs.cloud.google.com/artifact-registry/docs/reference/rpc/google.devtools.artifactregistry.v1#google.devtools.artifactregistry.v1.ArtifactRegistry.SetIamPolicy)`` |  Updates the IAM policy for a given resource.  
``[TestIamPermissions](https://docs.cloud.google.com/artifact-registry/docs/reference/rpc/google.devtools.artifactregistry.v1#google.devtools.artifactregistry.v1.ArtifactRegistry.TestIamPermissions)`` |  Tests if the caller has a list of permissions on a resource.  
``[UpdateFile](https://docs.cloud.google.com/artifact-registry/docs/reference/rpc/google.devtools.artifactregistry.v1#google.devtools.artifactregistry.v1.ArtifactRegistry.UpdateFile)`` |  Updates a file.  
``[UpdatePackage](https://docs.cloud.google.com/artifact-registry/docs/reference/rpc/google.devtools.artifactregistry.v1#google.devtools.artifactregistry.v1.ArtifactRegistry.UpdatePackage)`` |  Updates a package.  
``[UpdateProjectSettings](https://docs.cloud.google.com/artifact-registry/docs/reference/rpc/google.devtools.artifactregistry.v1#google.devtools.artifactregistry.v1.ArtifactRegistry.UpdateProjectSettings)`` |  Updates the Settings for the Project.  
``[UpdateRepository](https://docs.cloud.google.com/artifact-registry/docs/reference/rpc/google.devtools.artifactregistry.v1#google.devtools.artifactregistry.v1.ArtifactRegistry.UpdateRepository)`` |  Updates a repository.  
``[UpdateRule](https://docs.cloud.google.com/artifact-registry/docs/reference/rpc/google.devtools.artifactregistry.v1#google.devtools.artifactregistry.v1.ArtifactRegistry.UpdateRule)`` |  Updates a rule.  
``[UpdateTag](https://docs.cloud.google.com/artifact-registry/docs/reference/rpc/google.devtools.artifactregistry.v1#google.devtools.artifactregistry.v1.ArtifactRegistry.UpdateTag)`` |  Updates a tag.  
``[UpdateVPCSCConfig](https://docs.cloud.google.com/artifact-registry/docs/reference/rpc/google.devtools.artifactregistry.v1#google.devtools.artifactregistry.v1.ArtifactRegistry.UpdateVPCSCConfig)`` |  Updates the VPCSC Config for the Project.  
``[UpdateVersion](https://docs.cloud.google.com/artifact-registry/docs/reference/rpc/google.devtools.artifactregistry.v1#google.devtools.artifactregistry.v1.ArtifactRegistry.UpdateVersion)`` |  Updates a version.  
  
## `[google.longrunning.Operations](https://docs.cloud.google.com/artifact-registry/docs/reference/rpc/google.longrunning#google.longrunning.Operations)`

Methods  
---  
``[GetOperation](https://docs.cloud.google.com/artifact-registry/docs/reference/rpc/google.longrunning#google.longrunning.Operations.GetOperation)`` |  Gets the latest state of a long-running operation.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2025-11-14 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2025-11-14 UTC."],[],[]] 
